"""
BERT model implementation for MLX.
"""

import math
from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import mlx.core as mx
import mlx.nn as nn


@dataclass
class ModelArgs:
    """Arguments for BERT models."""

    vocab_size: int = 30522
    hidden_size: int = 768
    num_hidden_layers: int = 12
    num_attention_heads: int = 12
    intermediate_size: int = 3072
    hidden_act: str = "gelu"
    hidden_dropout_prob: float = 0.1
    attention_probs_dropout_prob: float = 0.1
    max_position_embeddings: int = 512
    type_vocab_size: int = 2
    initializer_range: float = 0.02
    layer_norm_eps: float = 1e-12
    pad_token_id: int = 0
    position_embedding_type: str = "absolute"
    use_cache: bool = True
    classifier_dropout: Optional[float] = None
    model_type: str = "bert"

    def __post_init__(self):
        # Validate arguments
        if self.hidden_size % self.num_attention_heads != 0:
            raise ValueError(
                f"Hidden size ({self.hidden_size}) must be divisible by number of attention heads ({self.num_attention_heads})"
            )


class BertEmbeddings(nn.Module):
    """Embeddings for BERT models."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.word_embeddings = nn.Embedding(args.vocab_size, args.hidden_size)
        self.position_embeddings = nn.Embedding(args.max_position_embeddings, args.hidden_size)
        self.token_type_embeddings = nn.Embedding(args.type_vocab_size, args.hidden_size)

        self.layer_norm = nn.LayerNorm(args.hidden_size, eps=args.layer_norm_eps)
        self.dropout = nn.Dropout(args.hidden_dropout_prob)

        self.position_embedding_type = args.position_embedding_type
        self.max_position_embeddings = args.max_position_embeddings

    def __call__(
        self,
        input_ids: mx.array,
        token_type_ids: Optional[mx.array] = None,
        position_ids: Optional[mx.array] = None,
        training: bool = False,
    ) -> mx.array:
        input_shape = input_ids.shape
        seq_length = input_shape[1]

        # Create position IDs if not provided
        if position_ids is None:
            position_ids = mx.arange(seq_length).reshape(1, -1)

        # Create token type IDs if not provided
        if token_type_ids is None:
            token_type_ids = mx.zeros(input_shape, dtype=mx.int32)

        # Get embeddings for inputs
        word_embeds = self.word_embeddings(input_ids)
        token_type_embeds = self.token_type_embeddings(token_type_ids)

        # Add position embeddings
        embeddings = word_embeds + token_type_embeds

        if self.position_embedding_type == "absolute":
            position_embeds = self.position_embeddings(position_ids)
            embeddings = embeddings + position_embeds

        # Apply layer normalization and dropout
        embeddings = self.layer_norm(embeddings)
        embeddings = self.dropout(embeddings, training)

        return embeddings


class BertSelfAttention(nn.Module):
    """Self-attention layer for BERT models."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.num_attention_heads = args.num_attention_heads
        self.attention_head_size = args.hidden_size // args.num_attention_heads
        self.all_head_size = self.num_attention_heads * self.attention_head_size

        # Query, key, and value projections
        self.query = nn.Linear(args.hidden_size, self.all_head_size)
        self.key = nn.Linear(args.hidden_size, self.all_head_size)
        self.value = nn.Linear(args.hidden_size, self.all_head_size)

        # Regularization
        self.dropout = nn.Dropout(args.attention_probs_dropout_prob)

    def reshape_for_attention(self, x: mx.array, batch_size: int, seq_length: int) -> mx.array:
        """Reshape input for multi-head attention."""
        # Reshape: [batch, seq, all_head_size] -> [batch, seq, num_heads, head_size]
        x = x.reshape(batch_size, seq_length, self.num_attention_heads, self.attention_head_size)
        # Permute: [batch, seq, num_heads, head_size] -> [batch, num_heads, seq, head_size]
        return x.transpose(0, 2, 1, 3)

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
        training: bool = False,
    ) -> Tuple[mx.array, Optional[mx.array]]:
        batch_size, seq_length = hidden_states.shape[0], hidden_states.shape[1]

        # Project inputs to queries, keys, and values
        query = self.query(hidden_states)
        key = self.key(hidden_states)
        value = self.value(hidden_states)

        # Reshape for multi-head attention
        query = self.reshape_for_attention(query, batch_size, seq_length)
        key = self.reshape_for_attention(key, batch_size, seq_length)
        value = self.reshape_for_attention(value, batch_size, seq_length)

        # Compute attention scores: batch_size x num_heads x seq_length x seq_length
        # Matmul and scale
        scale = math.sqrt(self.attention_head_size)
        attention_scores = mx.matmul(query, key.transpose(0, 1, 3, 2)) / scale

        # Apply attention mask if provided
        if attention_mask is not None:
            # Add large negative value to masked positions
            attention_scores = attention_scores + attention_mask

        # Apply softmax to get attention probabilities
        attention_probs = mx.softmax(attention_scores, axis=-1)

        # Apply dropout to attention probabilities
        attention_probs = self.dropout(attention_probs, training)

        # Apply attention to values
        context = mx.matmul(attention_probs, value)

        # Reshape context back: [batch, num_heads, seq, head_size] -> [batch, seq, all_head_size]
        context = context.transpose(0, 2, 1, 3)
        context = context.reshape(batch_size, seq_length, self.all_head_size)

        return context, attention_probs


class BertSelfOutput(nn.Module):
    """Output projection and residual connection for self-attention."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.hidden_size, args.hidden_size)
        self.layer_norm = nn.LayerNorm(args.hidden_size, eps=args.layer_norm_eps)
        self.dropout = nn.Dropout(args.hidden_dropout_prob)

    def __call__(
        self, hidden_states: mx.array, input_tensor: mx.array, training: bool = False
    ) -> mx.array:
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states, training)
        hidden_states = self.layer_norm(hidden_states + input_tensor)
        return hidden_states


class BertAttention(nn.Module):
    """Combined self-attention and output projection."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.self_attention = BertSelfAttention(args)
        self.output = BertSelfOutput(args)

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
        training: bool = False,
    ) -> Tuple[mx.array, Optional[mx.array]]:
        self_outputs, attention_probs = self.self_attention(
            hidden_states, attention_mask, training=training
        )
        attention_output = self.output(self_outputs, hidden_states, training=training)
        return attention_output, attention_probs


class BertIntermediate(nn.Module):
    """Intermediate dense layer with activation."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.hidden_size, args.intermediate_size)
        self.activation = nn.GELU()

    def __call__(self, hidden_states: mx.array) -> mx.array:
        hidden_states = self.dense(hidden_states)
        hidden_states = self.activation(hidden_states)
        return hidden_states


class BertOutput(nn.Module):
    """Output projection with residual connection and layer normalization."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.intermediate_size, args.hidden_size)
        self.layer_norm = nn.LayerNorm(args.hidden_size, eps=args.layer_norm_eps)
        self.dropout = nn.Dropout(args.hidden_dropout_prob)

    def __call__(
        self, hidden_states: mx.array, input_tensor: mx.array, training: bool = False
    ) -> mx.array:
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states, training)
        hidden_states = self.layer_norm(hidden_states + input_tensor)
        return hidden_states


class BertLayer(nn.Module):
    """BERT layer with attention, intermediate, and output sublayers."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.attention = BertAttention(args)
        self.intermediate = BertIntermediate(args)
        self.output = BertOutput(args)

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
        training: bool = False,
    ) -> Tuple[mx.array, Optional[mx.array]]:
        # Self-attention
        attention_output, attention_probs = self.attention(
            hidden_states, attention_mask, training=training
        )

        # Intermediate
        intermediate_output = self.intermediate(attention_output)

        # Output
        layer_output = self.output(intermediate_output, attention_output, training=training)

        return layer_output, attention_probs


class BertEncoder(nn.Module):
    """Stack of BERT layers."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.layers = [BertLayer(args) for _ in range(args.num_hidden_layers)]

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
        training: bool = False,
    ) -> Tuple[mx.array, Optional[Dict[str, mx.array]]]:
        all_attention_probs = {}

        for i, layer in enumerate(self.layers):
            hidden_states, attention_probs = layer(hidden_states, attention_mask, training=training)
            all_attention_probs[f"layer_{i}"] = attention_probs

        return hidden_states, all_attention_probs


class BertPooler(nn.Module):
    """Pooler for the BERT model (typically for sentence embeddings)."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.hidden_size, args.hidden_size)
        self.activation = nn.Tanh()

    def __call__(self, hidden_states: mx.array) -> mx.array:
        # Pool from the first token (CLS token)
        first_token_tensor = hidden_states[:, 0]
        pooled_output = self.dense(first_token_tensor)
        pooled_output = self.activation(pooled_output)
        return pooled_output


class Model(nn.Module):
    """BERT model implementation for MLX."""

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.config = args

        # Core BERT modules
        self.embeddings = BertEmbeddings(args)
        self.encoder = BertEncoder(args)
        self.pooler = BertPooler(args)

    def __call__(
        self,
        input_ids: mx.array,
        attention_mask: Optional[mx.array] = None,
        token_type_ids: Optional[mx.array] = None,
        position_ids: Optional[mx.array] = None,
        training: bool = False,
    ) -> Dict[str, Any]:
        # Prepare attention mask
        if attention_mask is not None:
            # Expand mask to attention shape: [batch, 1, 1, seq_length]
            attention_mask = attention_mask[:, None, None, :]
            # Convert 0s to large negative values for masked positions
            attention_mask = (1.0 - attention_mask) * -10000.0

        # Forward pass through embeddings
        embedding_output = self.embeddings(
            input_ids, token_type_ids, position_ids, training=training
        )

        # Forward pass through encoder
        sequence_output, all_attention_probs = self.encoder(
            embedding_output, attention_mask, training=training
        )

        # Forward pass through pooler
        pooled_output = self.pooler(sequence_output)

        # Return outputs as a dictionary
        return {
            "last_hidden_state": sequence_output,
            "pooler_output": pooled_output,
            "attention_probs": all_attention_probs,
        }
