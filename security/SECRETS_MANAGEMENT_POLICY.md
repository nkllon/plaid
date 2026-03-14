# Secrets Management Policy

## Purpose

This policy defines how secrets are created, stored, accessed, rotated, and removed.

## Approved secret handling methods

- GitHub repository or environment secrets for CI and deployment variables.
- Cloud secret stores such as GCP Secret Manager and Azure Key Vault.
- Local secure secret tooling such as 1Password for development workflows.
- Runtime environment variables populated from an approved secret store.

## Prohibited practices

- Committing plaintext secrets, access tokens, private keys, or production credentials to version control.
- Embedding secrets in container images.
- Sharing credentials through chat, issue comments, or documentation intended for public distribution.

## Observed implementation signals

- `nkllon/sharepoint-mcp` deploys Cloud Run with secrets populated from GCP Secret Manager.
- `louspringer/chatbot-llm` contains Azure Key Vault integration code and templates for moving bot, Snowflake, Cosmos DB, and encryption secrets into Key Vault.
- `louspringer/chatbot-llm` local testing guidance explicitly states that `.env` files must not be committed and that 1Password should be used for secrets.
- Reviewed repositories commonly ignore `.env`, `local.settings.json`, key material, and logs in `.gitignore`.

## Secret lifecycle requirements

- Secrets must be created with sufficient entropy and unique values per environment.
- Secrets must be stored only in approved secret stores or secure local developer tooling.
- Secrets should be rotated after suspected exposure, personnel change, or major integration change.
- Long-lived credentials should be replaced with managed identity or short-lived credentials where supported.

## Rotation expectations

- High-risk integration secrets should be rotated at least annually, and sooner when supported by the provider or incident response requirements.
- Emergency rotation must be initiated immediately upon suspected exposure.

Based on typical practices for the environment observed, the following control is assumed:

- GitHub Actions workflows that require secrets use repository or environment secrets rather than storing sensitive values in workflow files.

## Validation

- Secret values should be tested in non-production environments before production rollout when practical.
- Repository scanning, manual review, and GitHub secret scanning features should be used to reduce accidental secret exposure.
