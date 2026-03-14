# Security Program Overview

## Purpose

This document describes the security program used for software developed and operated by a solo developer across the `nkllon` organization and the `louspringer` GitHub account. The program is intentionally lightweight, but it is structured to provide clear ownership, repeatable security practices, and defensible controls for applications and integrations adjacent to financial-data workflows.

## Governance model

- Security ownership rests with the repository owner and maintainer.
- Changes are managed primarily through GitHub repositories, pull requests, and repository-level controls.
- Public repositories rely on transparency, issue tracking, CI validation, and dependency monitoring as core control mechanisms.
- Private repositories are used when integrations require deployment details, environment configuration, or operational secrets that must not be exposed publicly.

## Security objectives

- Prevent exposure of credentials, access tokens, and secret material.
- Minimize storage and retention of sensitive data.
- Use trusted cloud-provider controls where cloud deployment is required.
- Detect vulnerable dependencies and insecure code changes early through CI and repository tooling.
- Maintain a documented response process for incidents, vulnerabilities, and reported security issues.

## Observed control baseline

- GitHub Actions CI is present in multiple active repositories.
- Some repositories use dependency update automation and security scanning.
- Deployment patterns favor runtime secret injection through environment variables or managed secret stores.
- Reviewed repositories commonly exclude `.env`, key files, local settings, and logs from version control.
- Public repositories did not show committed production secrets during this review.

## Control limitations

- Controls are not yet standardized across the entire repository portfolio.
- Repository-level enforcement varies by project.
- Some documented controls are architectural intent or implementation guidance rather than universally enforced controls.

## Core mandatory controls

- Multi-factor authentication is required for GitHub accounts with administrative or write access.
- Production secrets must be stored only in managed secret stores or equivalent approved secure tooling.
- Public repositories must not contain live customer credentials, Plaid credentials, access tokens, or personal financial data.
- High-risk repositories must use pull requests, branch protection, and CI validation prior to merge.
- Policies in this package must be reviewed at least annually, after material architecture changes, and after security incidents.

## Solo developer operating model

- The maintainer operates a single-operator model in which development, review, deployment, and incident response remain centralized, with compensating controls coming from strong identity controls, source transparency, branch protection where enabled, CI checks, dependency monitoring, and managed cloud security features.

## Review cadence

- Security-relevant repositories must be reviewed at least quarterly for dependency posture, exposed secrets, branch protections, and deployment configuration.
- High-risk integration repositories must be reviewed before material release, infrastructure change, or onboarding of a new external integration such as Plaid, Microsoft Graph, Snowflake, or similar third-party APIs.
