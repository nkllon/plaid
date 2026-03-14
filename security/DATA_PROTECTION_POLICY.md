# Data Protection Policy

## Purpose

This policy defines how application, integration, and operational data should be protected across development and deployment environments.

## Data classification

- Public: open source code, public documentation, test fixtures without secrets, and non-sensitive metadata.
- Internal: architecture notes, deployment details, issue discussions, and operational metadata not intended for broad public distribution.
- Confidential: API credentials, tokens, cloud secrets, service account material, private keys, and non-public operational data.
- Restricted: any real customer data, financial account data, authentication secrets, or regulated data introduced by external integrations.

## Observed data handling posture

- Reviewed public repositories did not show committed production financial credentials or personal financial data.
- `louspringer/chatbot-llm` references sample financial datasets and connected-service credentials for development and deployment.
- `nkllon/sharepoint-mcp` processes authenticated SharePoint and Microsoft Graph requests and therefore handles access tokens and application credentials in runtime environments.

## Data minimization

- Repositories should store code, configuration templates, and documentation only.
- Sensitive values must be provided at runtime through secret stores or environment injection rather than committed to source control.
- Development and test environments should use synthetic, sample, or non-production data whenever possible.

## Encryption in transit

- External API communication is expected to occur over HTTPS or provider-managed TLS endpoints.
- Reviewed integrations with GitHub, Microsoft Graph, SharePoint, Google Cloud Run, Azure Key Vault, and cloud control planes inherently rely on TLS-enabled endpoints.

## Encryption at rest

- Source code is stored in GitHub-managed storage.
- Cloud secret stores such as GCP Secret Manager and Azure Key Vault should be used for sensitive values, relying on provider-managed encryption at rest.

Based on typical practices for the environment observed, the following control is assumed:

- Where production data or logs are retained in cloud platforms, encryption at rest is provided by the underlying managed service.

## Environment separation

- Development, testing, and production values should be separated by distinct environment variables, secret entries, and cloud resources.
- Local development must not reuse production secrets unless there is a documented emergency requirement.
- Production deployment artifacts must be built without embedding secrets in the image or repository.

## Retention and deletion

- Secrets and tokens should be deleted or rotated when no longer required.
- Logs should avoid storing secrets and should be retained only as long as operationally necessary.
- Any real customer or financial data introduced into a connected system should be retained only for the minimum period required by application function or legal obligation.
