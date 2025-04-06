"""
BERT model implementation for MLX.
"""

import math
from dataclasses import dataclass
from typing import Dict, Optional

import mlx.core as mx
import mlx.nn as nn

from .base import register_model


@dataclass
class ModelArgs:
    """Arguments for the BERT model."""

    hidden_size: int
    num_hidden_layers: int
    num_attention_heads: int
    intermediate_size: int
    hidden_dropout_prob: float = 0.1
    attention_probs_dropout_prob: float = 0.1
    max_position_embeddings: int = 512
    vocab_size: int = 30522
    type_vocab_size: int = 2
    layer_norm_eps: float = 1e-12
    use_mean_pooling: bool = True

    def __init__(self, **kwargs):
        """Initialize from kwargs."""
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)


class BertEmbeddings(nn.Module):
    """
    BERT embeddings module.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.word_embeddings = nn.Embedding(args.vocab_size, args.hidden_size)
        self.position_embeddings = nn.Embedding(args.max_position_embeddings, args.hidden_size)
        self.token_type_embeddings = nn.Embedding(args.type_vocab_size, args.hidden_size)

        self.layer_norm = nn.LayerNorm(args.hidden_size, eps=args.layer_norm_eps)
        self.dropout = nn.Dropout(p=args.hidden_dropout_prob)

        # Position IDs (for position embeddings)
        self.position_ids = mx.arange(args.max_position_embeddings).reshape(1, -1)

    def __call__(
        self,
        input_ids: mx.array,
        token_type_ids: Optional[mx.array] = None,
        position_ids: Optional[mx.array] = None,
    ):
        input_shape = input_ids.shape
        seq_length = input_shape[1]

        # If position_ids not provided, use defaults
        if position_ids is None:
            position_ids = self.position_ids[:, :seq_length]

        # If token_type_ids not provided, use zeros
        if token_type_ids is None:
            token_type_ids = mx.zeros(input_shape, dtype=mx.int32)

        # Get embeddings for words, positions, and token types
        word_embeds = self.word_embeddings(input_ids)
        position_embeds = self.position_embeddings(position_ids)
        token_type_embeds = self.token_type_embeddings(token_type_ids)

        # Sum the embeddings
        embeddings = word_embeds + position_embeds + token_type_embeds

        # Apply layer norm and dropout
        embeddings = self.layer_norm(embeddings)
        embeddings = self.dropout(embeddings)

        return embeddings


class BertSelfAttention(nn.Module):
    """
    BERT self-attention mechanism.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()

        self.num_attention_heads = args.num_attention_heads
        self.attention_head_size = args.hidden_size // args.num_attention_heads
        self.all_head_size = self.num_attention_heads * self.attention_head_size

        # Query, key, and value projections
        self.query = nn.Linear(args.hidden_size, self.all_head_size)
        self.key = nn.Linear(args.hidden_size, self.all_head_size)
        self.value = nn.Linear(args.hidden_size, self.all_head_size)

        # Output projection
        self.dropout = nn.Dropout(p=args.attention_probs_dropout_prob)

    def transpose_for_scores(self, x: mx.array) -> mx.array:
        """Reshape for multi-head attention."""
        batch_size, seq_len = x.shape[0], x.shape[1]

        # Reshape to [batch_size, seq_len, num_heads, head_dim]
        x = x.reshape(batch_size, seq_len, self.num_attention_heads, self.attention_head_size)

        # Transpose to [batch_size, num_heads, seq_len, head_dim]
        return x.transpose(0, 2, 1, 3)

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
    ):
        batch_size, seq_len = hidden_states.shape[0], hidden_states.shape[1]

        # Project to query, key, value
        query = self.query(hidden_states)
        key = self.key(hidden_states)
        value = self.value(hidden_states)

        # Reshape for multi-head attention
        query = self.transpose_for_scores(query)
        key = self.transpose_for_scores(key)
        value = self.transpose_for_scores(value)

        # Compute attention scores: [batch_size, num_heads, seq_len, seq_len]
        attention_scores = mx.matmul(query, key.transpose(0, 1, 3, 2))
        attention_scores = attention_scores / math.sqrt(self.attention_head_size)

        # Apply attention mask if provided
        if attention_mask is not None:
            # Add a large negative value to masked positions
            mask = attention_mask.reshape(batch_size, 1, 1, seq_len)
            mask = (1.0 - mask) * -10000.0
            attention_scores = attention_scores + mask

        # Apply softmax to get attention probabilities
        attention_probs = mx.softmax(attention_scores, axis=-1)
        attention_probs = self.dropout(attention_probs)

        # Apply attention to values
        context = mx.matmul(attention_probs, value)

        # Reshape back to [batch_size, seq_len, hidden_size]
        context = context.transpose(0, 2, 1, 3)
        context = context.reshape(batch_size, seq_len, self.all_head_size)

        return context


class BertSelfOutput(nn.Module):
    """
    BERT self-output module.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.hidden_size, args.hidden_size)
        self.layer_norm = nn.LayerNorm(args.hidden_size, eps=args.layer_norm_eps)
        self.dropout = nn.Dropout(p=args.hidden_dropout_prob)

    def __call__(self, hidden_states: mx.array, input_tensor: mx.array):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states)
        hidden_states = self.layer_norm(hidden_states + input_tensor)
        return hidden_states


class BertAttention(nn.Module):
    """
    BERT attention module (self-attention + output).
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.self_attention = BertSelfAttention(args)
        self.output = BertSelfOutput(args)

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
    ):
        self_outputs = self.self_attention(hidden_states, attention_mask)
        attention_output = self.output(self_outputs, hidden_states)
        return attention_output


class BertIntermediate(nn.Module):
    """
    BERT intermediate (FFN) module.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.hidden_size, args.intermediate_size)

    def __call__(self, hidden_states: mx.array):
        hidden_states = self.dense(hidden_states)
        hidden_states = mx.gelu(hidden_states)
        return hidden_states


class BertOutput(nn.Module):
    """
    BERT output module.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.intermediate_size, args.hidden_size)
        self.layer_norm = nn.LayerNorm(args.hidden_size, eps=args.layer_norm_eps)
        self.dropout = nn.Dropout(p=args.hidden_dropout_prob)

    def __call__(self, hidden_states: mx.array, input_tensor: mx.array):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states)
        hidden_states = self.layer_norm(hidden_states + input_tensor)
        return hidden_states


class BertLayer(nn.Module):
    """
    BERT transformer layer.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.attention = BertAttention(args)
        self.intermediate = BertIntermediate(args)
        self.output = BertOutput(args)

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
    ):
        attention_output = self.attention(hidden_states, attention_mask)
        intermediate_output = self.intermediate(attention_output)
        layer_output = self.output(intermediate_output, attention_output)
        return layer_output


class BertEncoder(nn.Module):
    """
    BERT encoder (stack of transformer layers).
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.layers = [BertLayer(args) for _ in range(args.num_hidden_layers)]

    def __call__(
        self,
        hidden_states: mx.array,
        attention_mask: Optional[mx.array] = None,
    ):
        for layer in self.layers:
            hidden_states = layer(hidden_states, attention_mask)
        return hidden_states


class BertPooler(nn.Module):
    """
    BERT pooler for sentence embeddings.
    """

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.dense = nn.Linear(args.hidden_size, args.hidden_size)
        self.activation = mx.tanh
        self.use_mean_pooling = args.use_mean_pooling

    def __call__(self, hidden_states: mx.array, attention_mask: Optional[mx.array] = None):
        if self.use_mean_pooling and attention_mask is not None:
            # Use mean pooling
            mask = attention_mask.reshape(attention_mask.shape[0], attention_mask.shape[1], 1)
            hidden_states = hidden_states * mask
            sum_embeddings = mx.sum(hidden_states, axis=1)
            sum_mask = mx.sum(mask, axis=1)
            sum_mask = mx.maximum(sum_mask, mx.ones_like(sum_mask))  # Avoid division by zero
            pooled_output = sum_embeddings / sum_mask
        else:
            # Use [CLS] token
            pooled_output = hidden_states[:, 0]
            pooled_output = self.dense(pooled_output)
            pooled_output = self.activation(pooled_output)

        return pooled_output


@register_model("bert")
class Model(nn.Module):
    """
    BERT model with pooling for sentence embeddings.
    """

    # Reference to the model args class
    ModelArgs = ModelArgs

    def __init__(self, args: ModelArgs):
        super().__init__()
        self.embeddings = BertEmbeddings(args)
        self.encoder = BertEncoder(args)
        self.pooler = BertPooler(args)

    def __call__(
        self,
        input_ids: mx.array,
        attention_mask: Optional[mx.array] = None,
        token_type_ids: Optional[mx.array] = None,
        position_ids: Optional[mx.array] = None,
    ):
        # Create default attention mask if not provided
        if attention_mask is None:
            attention_mask = mx.ones_like(input_ids)

        # Get embeddings
        embedding_output = self.embeddings(
            input_ids=input_ids,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
        )

        # Pass through encoder
        sequence_output = self.encoder(
            hidden_states=embedding_output,
            attention_mask=attention_mask,
        )

        # Apply pooling
        pooled_output = self.pooler(sequence_output, attention_mask)

        return {
            "last_hidden_state": sequence_output,
            "pooler_output": pooled_output,
        }

    def load_weights(self, weights: Dict[str, mx.array]):
        """
        Load weights into the model.

        Args:
            weights: Dictionary of parameter name -> array
        """
        params = dict(self.parameters())

        # Map HuggingFace BERT parameters to our model
        mapping = {
            "bert.embeddings.word_embeddings.weight": "embeddings.word_embeddings.weight",
            "bert.embeddings.position_embeddings.weight": "embeddings.position_embeddings.weight",
            "bert.embeddings.token_type_embeddings.weight": "embeddings.token_type_embeddings.weight",
            "bert.embeddings.LayerNorm.weight": "embeddings.layer_norm.weight",
            "bert.embeddings.LayerNorm.bias": "embeddings.layer_norm.bias",
        }

        # Add mappings for each layer
        for i in range(len(self.encoder.layers)):
            layer_prefix = f"bert.encoder.layer.{i}."
            our_prefix = f"encoder.layers.{i}."

            mapping.update(
                {
                    f"{layer_prefix}attention.self.query.weight": f"{our_prefix}attention.self_attention.query.weight",
                    f"{layer_prefix}attention.self.query.bias": f"{our_prefix}attention.self_attention.query.bias",
                    f"{layer_prefix}attention.self.key.weight": f"{our_prefix}attention.self_attention.key.weight",
                    f"{layer_prefix}attention.self.key.bias": f"{our_prefix}attention.self_attention.key.bias",
                    f"{layer_prefix}attention.self.value.weight": f"{our_prefix}attention.self_attention.value.weight",
                    f"{layer_prefix}attention.self.value.bias": f"{our_prefix}attention.self_attention.value.bias",
                    f"{layer_prefix}attention.output.dense.weight": f"{our_prefix}attention.output.dense.weight",
                    f"{layer_prefix}attention.output.dense.bias": f"{our_prefix}attention.output.dense.bias",
                    f"{layer_prefix}attention.output.LayerNorm.weight": f"{our_prefix}attention.output.layer_norm.weight",
                    f"{layer_prefix}attention.output.LayerNorm.bias": f"{our_prefix}attention.output.layer_norm.bias",
                    f"{layer_prefix}intermediate.dense.weight": f"{our_prefix}intermediate.dense.weight",
                    f"{layer_prefix}intermediate.dense.bias": f"{our_prefix}intermediate.dense.bias",
                    f"{layer_prefix}output.dense.weight": f"{our_prefix}output.dense.weight",
                    f"{layer_prefix}output.dense.bias": f"{our_prefix}output.dense.bias",
                    f"{layer_prefix}output.LayerNorm.weight": f"{our_prefix}output.layer_norm.weight",
                    f"{layer_prefix}output.LayerNorm.bias": f"{our_prefix}output.layer_norm.bias",
                }
            )

        # Add pooler mappings
        mapping.update(
            {
                "bert.pooler.dense.weight": "pooler.dense.weight",
                "bert.pooler.dense.bias": "pooler.dense.bias",
            }
        )

        # Also try common sentence-transformers keys
        mapping.update(
            {
                "0.auto_model.bert.embeddings.word_embeddings.weight": "embeddings.word_embeddings.weight",
                "0.auto_model.bert.embeddings.position_embeddings.weight": "embeddings.position_embeddings.weight",
                "0.auto_model.bert.embeddings.token_type_embeddings.weight": "embeddings.token_type_embeddings.weight",
                "0.auto_model.bert.embeddings.LayerNorm.weight": "embeddings.layer_norm.weight",
                "0.auto_model.bert.embeddings.LayerNorm.bias": "embeddings.layer_norm.bias",
            }
        )

        # Try to load weights using the mapping
        remaining_weights = {}
        for name, array in weights.items():
            if name in mapping and mapping[name] in params:
                # If shapes match, load directly
                if params[mapping[name]].shape == array.shape:
                    params[mapping[name]] = array
                else:
                    print(f"Shape mismatch: {name} {array.shape} vs {params[mapping[name]].shape}")
            else:
                # Keep track of weights we couldn't map
                remaining_weights[name] = array

        # Try to load remaining weights directly
        for name, array in remaining_weights.items():
            if name in params:
                if params[name].shape == array.shape:
                    params[name] = array

        # Update the model parameters
        self.update_parameters(params)
