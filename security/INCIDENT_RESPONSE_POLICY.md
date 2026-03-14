# Incident Response Policy

## Purpose

This policy defines the minimum incident response process for a solo developer operating open source and integration-focused software.

## Incident types

- Suspected credential exposure
- Suspected or confirmed Plaid secret or token exposure
- Unauthorized repository or infrastructure access
- Exposure of sensitive data
- Vulnerability exploitation
- Malicious dependency or supply chain event
- Material service outage affecting security controls

## Response roles

- Incident commander: repository owner / maintainer
- Communications owner: repository owner / maintainer
- Technical investigator: repository owner / maintainer, with external maintainers or providers engaged as needed

## Response process

## Severity classification

- Critical: confirmed compromise of production credentials, access tokens, secret stores, or regulated or sensitive financial data.
- High: likely compromise, active exploitation, or security failure affecting a production integration or protected branch.
- Medium: validated vulnerability or exposure with limited scope and no evidence of active compromise.
- Low: security hygiene issue, policy gap, or non-exploited weakness.

### 1. Detection

- Detect incidents through GitHub alerts, CI failures, cloud-provider alerts, issue reports, user reports, or manual review.

### 2. Containment

- Disable or rotate affected credentials.
- Restrict repository, deployment, or cloud access as needed.
- Pause affected integrations or deployments when active compromise is suspected.
- On confirmed compromise of Plaid or equivalent financial-integration credentials, affected secrets must be rotated immediately, active tokens must be revoked where supported, and affected integrations must be suspended until the environment is validated.

### 3. Investigation

- Review commit history, workflow runs, logs, issue reports, and provider audit data where available.
- Determine scope, affected systems, exposed secrets, and whether sensitive data was accessed or exfiltrated.

### 4. Remediation

- Remove exposed material from active use.
- Patch vulnerable code or dependencies.
- Rebuild and redeploy affected services from known-good source.
- Tighten controls if the incident exposed a process gap.

### 5. Disclosure

- Notify affected partners, users, or platform providers when disclosure is appropriate.
- Public repositories must document material security issues through advisories, issue updates, or other suitable channels after containment.
- Critical incidents affecting third-party integrations, customer data, or security credentials must be evaluated for partner notification immediately after initial containment.

## Timing expectations

- Critical credential exposure: begin containment immediately.
- High-severity confirmed incident: investigate and remediate as soon as practical, targeting same-day triage.
- Lower-severity events: address in the next normal maintenance cycle unless exploitation risk is elevated.
- Exposed Plaid or equivalent production secrets must be rotated immediately upon confirmation or strong suspicion of compromise.

## Evidence retention

- Preserve relevant commits, logs, workflow outputs, and screenshots as needed to support investigation and post-incident review.

## Post-incident review

- Record root cause, impact, actions taken, and follow-up improvements.
- Corrective actions must be tracked to completion.
- Policy, CI, branch protections, deployment controls, and secret handling practices must be updated if the incident reveals control gaps.
