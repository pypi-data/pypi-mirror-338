# Security Policy

## Supported Versions

We currently provide security updates for the following versions of llamamlx-embeddings:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within llamamlx-embeddings, please send an email to security@example.com. All security vulnerabilities will be promptly addressed.

Please include the following information in your report:

- Type of vulnerability
- Path of the file with the issue
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue

This project follows good practices of responsible disclosure, so please allow time for the issue to be addressed before disclosing it publicly.

## Security Update Process

When we receive a security bug report, we will:

1. Confirm the problem and determine the affected versions
2. Audit code to find any similar potential problems
3. Prepare fixes for all supported versions
4. Release new security patch versions

## Best Practices for Users

To ensure your use of llamamlx-embeddings is secure:

1. Keep the library updated to the latest version
2. Use dependency scanning tools (like Dependabot) to monitor for vulnerabilities
3. Follow our security advisories through GitHub's security advisory feature
4. Consider using API authentication when serving embeddings via our FastAPI server
5. Be careful with model files from untrusted sources

Thank you for helping keep llamamlx-embeddings and its community safe! 