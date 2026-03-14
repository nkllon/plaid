# Access Control Policy

## Purpose

This policy defines access control expectations for source code, deployment systems, secrets, and administrative functions.

## Identity and authentication

- GitHub is the system of record for source repository access.
- Each user must authenticate with an individual GitHub account. Shared accounts are not permitted.
- Administrative and write access should be limited to the maintainer and explicitly authorized collaborators only.

Based on typical practices for the environment observed, the following control is assumed:

- Multi-factor authentication is required on GitHub accounts with administrative or write access.

## Repository permission model

- Public repositories are readable by anyone and are treated as non-secret by design.
- Private repositories are used for operational details, deployment configurations, or integrations that should not be publicly exposed.
- Access to private repositories is granted on least-privilege principles.
- Administrative privileges should be limited to the repository owner and only to accounts necessary to maintain the repository.

## Pull requests and branch protection

Observed examples:

- `nkllon/gorgonaut` has branch protection on `main`, administrator enforcement enabled, force pushes disabled, deletions disabled, and linear history required.
- `louspringer/chatbot-llm` has branch protection on `develop`, strict status checks enabled, and force pushes and deletions disabled.
- `louspringer/chatbot-llm` includes a stored branch protection definition requiring one approving review and stale review dismissal.
- `nkllon/composable-ai-advisors` contains a branch-protection proposal that recommends at least one review and required CI checks.

Policy expectations:

- Changes to default branches should occur through pull requests whenever practical.
- Protected branches should disable force pushes and deletions.
- At least one review should be required for higher-risk repositories where GitHub plan features permit it.
- Required status checks should be enabled for CI workflows that materially validate build, test, and security posture.

## Administrative access

- Repository administration must be restricted to the owner or designated maintainer accounts.
- Administrative actions include branch protection changes, repository visibility changes, secret management, and deployment configuration changes.
- Administrative access should be reviewed during periodic security review.

## Service and deployment access

- Cloud deployment credentials must not be embedded in code.
- Service accounts or cloud identities should be used for deployment automation where supported.
- Access to cloud consoles, secret stores, and deployment tooling should be restricted to the maintainer and only enabled where operationally required.
