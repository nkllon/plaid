# Incident Response Policy

## Purpose

This policy defines the minimum incident response process for a solo developer operating open source and integration-focused software.

## Incident types

- Suspected credential exposure
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

### 1. Detection

- Detect incidents through GitHub alerts, CI failures, cloud-provider alerts, issue reports, user reports, or manual review.

### 2. Containment

- Disable or rotate affected credentials.
- Restrict repository, deployment, or cloud access as needed.
- Pause affected integrations or deployments when active compromise is suspected.

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
- Public repositories should document material security issues through advisories, issue updates, or other suitable channels after containment.

## Timing expectations

- Critical credential exposure: begin containment immediately.
- High-severity confirmed incident: investigate and remediate as soon as practical, targeting same-day triage.
- Lower-severity events: address in the next normal maintenance cycle unless exploitation risk is elevated.

## Evidence retention

- Preserve relevant commits, logs, workflow outputs, and screenshots as needed to support investigation and post-incident review.

## Post-incident review

- Record root cause, impact, actions taken, and follow-up improvements.
- Update policy, CI, branch protections, or secret handling practices if the incident reveals control gaps.
