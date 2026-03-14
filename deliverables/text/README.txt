Security Documentation Package

Overview

This directory contains a lightweight but externally reviewable security documentation set for the `nkllon` organization and `louspringer` GitHub account. It is intended for Plaid-style vendor review, repository governance, and solo-developer operational use.

Files

- SECURITY_PROGRAM.md
- ACCESS_CONTROL_POLICY.md
- DATA_PROTECTION_POLICY.md
- SECRETS_MANAGEMENT_POLICY.md
- INCIDENT_RESPONSE_POLICY.md
- VULNERABILITY_MANAGEMENT.md
- INFRASTRUCTURE_SECURITY.md
- OPEN_SOURCE_SECURITY_MODEL.md
- THIRD_PARTY_SERVICES.md
- SECURITY_CONTACT.md

Scope

- Primary owners reviewed: nkllon, louspringer
- Review date: 2026-03-14
- Review method:
- Enumerated repositories via GitHub API
- Opened and inspected selected repositories with the strongest security signal
- Reviewed repository metadata, branch protection state where accessible, GitHub Actions workflows, dependency update configuration, container files, Terraform, environment templates, and deployment scripts

Key reviewed evidence

The following repositories and files were directly inspected and used as the main evidence base for the policies in this package:

- nkllon/gorgonaut
- .github/workflows/ci.yml
- Makefile
- python/tests/test_ci_contracts.py
- .gitignore
- nkllon/composable-ai-advisors
- .github/workflows/ci.yml
- backend/Dockerfile
- docs/governance/branch-protection-proposal.md
- .gitignore
- nkllon/sharepoint-mcp
- README.md
- scripts/deploy_cloud_run.sh
- sharepoint_mcp/logic.py
- Dockerfile
- .env.example
- louspringer/chatbot-llm
- .github/workflows/dev-validation.yml
- .github/workflows/validate-environment.yml
- .github/dependabot.yml
- branch_protection.json
- .env.template
- .env.example
- docs/key_rotation.md
- teams_bot/config/key_vault.py
- teams_bot/deployment/azure/key_vault.bicep
- teams_bot/LOCAL_TESTING.md
- .gitignore
- louspringer/azure-databricks-terraform
- workspace/main.tf
- louspringer/ecs-microservice-terraform
- README.md

Confirmed controls

- GitHub Actions CI is present in multiple active repositories.
- nkllon/gorgonaut runs a multi-step CI workflow and container parity workflow.
- nkllon/composable-ai-advisors runs linting, type checking, tests, and security tooling (bandit, pip-audit) in CI.
- louspringer/chatbot-llm uses Dependabot for Python and GitHub Actions updates.
- louspringer/chatbot-llm has GitHub Advanced Security signals enabled for Dependabot security updates, secret scanning, and push protection.
- louspringer/chatbot-llm documents and implements Azure Key Vault integration patterns.
- nkllon/sharepoint-mcp deploys to Cloud Run with --no-allow-unauthenticated and injects runtime secrets from GCP Secret Manager rather than embedding them in the image.
- Reviewed repositories commonly ignore .env, local settings, key material, logs, and virtual environments in .gitignore.
- Reviewed examples use environment variables, cloud secret stores, or external secret tooling such as 1Password and Azure Key Vault.

Confirmed gaps or limitations

- Security tooling is not uniform across all repositories.
- Some workflows mark security checks as non-blocking or informational only.
- nkllon/gorgonaut has branch protection on main, but the required status check list is currently empty.
- nkllon/gorgonaut has GitHub secret scanning and Dependabot security updates disabled at the repository setting level.
- nkllon/composable-ai-advisors contains a branch protection proposal document, but that file is a proposal, not proof of enforcement.
- louspringer/chatbot-llm branch protection on develop requires one status check (sourcery/sourcery), but does not enforce admins.
- Account-level MFA and organization-wide GitHub settings were not directly observable from repository contents.

Plaid runtime boundary

- Public repositories in scope are documentation, code, and configuration-template artifacts only.
- Any Plaid-connected runtime environment must keep client secrets, access tokens, item identifiers, account data, transaction data, and derived financial records outside public source control.
- Plaid or equivalent financial integrations must run only in controlled runtime environments that use managed secret storage and authenticated access paths.

Third-party services and subprocessors

The reviewed repositories reference or depend on the following third-party service categories:

- Source control and CI: GitHub, GitHub Actions, Dependabot, GitHub secret scanning
- Cloud and secret management: Google Cloud Run, GCP Secret Manager, Azure Key Vault, Azure Databricks
- Infrastructure patterns: AWS ECS, Cognito, CloudWatch, DynamoDB, AWS Secrets Manager
- External integration providers: Microsoft Graph, SharePoint, Snowflake

These providers are used as infrastructure or integration components. Sensitive runtime credentials must remain in provider-managed secret stores or equivalent approved systems and must not be committed to public repositories.

Package review cadence

- Policies in this package must be reviewed at least annually.
- High-risk repositories and integrations must be reviewed at least quarterly.
- The package must be updated after any material architecture change, new financial-data integration, or security incident.

Data handling conclusions

- No reviewed public repository stores production Plaid credentials, banking credentials, or personal financial account data.
- No evidence was found that public repositories intentionally store raw consumer financial data.
- louspringer/chatbot-llm references a sample financial dataset and credentials for Snowflake and Microsoft Teams integrations. This repository is best classified as HIGH risk because it handles application credentials and may process business data in connected environments.
- nkllon/sharepoint-mcp is best classified as HIGH risk because it handles OAuth-style application credentials and access tokens for Microsoft Graph and SharePoint.
- Infrastructure repositories such as louspringer/azure-databricks-terraform and louspringer/ecs-microservice-terraform are classified MEDIUM because they define deployment patterns and secret-management expectations without showing consumer financial credential storage in-repo.
- Most remaining repositories are LOW risk because they are libraries, experiments, docs, or tools with no observed handling of sensitive financial data.

Suggested repository location

If a single authoritative location is desired, keep this package in a top-level `security/` directory in the primary integration or governance repository and link to it from `README.md` and `SECURITY.md`. For public discoverability, `louspringer/chatbot-llm` or a dedicated governance repository under `nkllon` would be reasonable homes.

Inventory notes

- The inventory below is a complete enumeration of repositories returned by GitHub for nkllon and louspringer during this review.
- Classification and risk values are conservative and intended for questionnaire support, not as formal audit labels.
- Where a repository was not deeply inspected, classification is based on repository metadata and naming signals.

Repository inventory

Repository | Owner | Visibility | Fork | Classification | Risk | Notes
--- | --- | --- | --- | --- | --- | ---
louspringer/2-4-example-dags | user | public | yes | experimental tooling | LOW | 
louspringer/aardvark-lemon-virtue | user | public | no | experimental tooling | LOW | Job seekers often struggle to navigate the vast amount of job listings efficiently, finding it challenging to match their qualifications and interests with available opportunities precisely.
louspringer/ackbert | user | public | no | libraries | LOW | Ack-Bert: Structured candidate comparison and evaluation framework using ontology-based methodologies
louspringer/astro-example-dags | user | public | yes | experimental tooling | LOW | 
louspringer/awesome-cursor-rules-mdc | user | public | yes | application | LOW | Curated list of awesome Cursor Rules .mdc files
louspringer/azure-databricks-terraform | user | public | no | infrastructure | MEDIUM | Terraform scripts for various data bricks configurations.
louspringer/bbs-in-a-bottle | user | public | no | application | MEDIUM | 
louspringer/Beast-mode-Ontology | user | public | yes | application | LOW | A semantic foundation for modeling autonomous and semi-autonomous agents using a clear Agent → Capability → Task hierarchy. Formalizes capabilities as reusable assets, enables inference-based task discovery, and enforces integrity with SHACL. Designed for composable agent ecosystems and extensible governance via layered ontology extensions.
louspringer/botbuilder-python | user | public | yes | libraries | MEDIUM | The Microsoft Bot Framework provides what you need to build and connect intelligent bots that interact naturally wherever your users are talking, from text/sms to Skype, Slack, Office 365 mail and other popular services.
louspringer/cc-sdd | user | public | yes | documentation | LOW | Spec-driven development (SDD) for your team's workflow. Kiro style commands that enforce structured requirements→design→tasks workflow and steering, transforming how you build with AI. Support Claude Code, Codex, Cursor, Github Copilot, Gemini CLI and Windsurf.
louspringer/charts | user | public | yes | application | LOW | Curated applications for Kubernetes
louspringer/chatbot-llm | user | public | no | application | HIGH | 
louspringer/claude-simone | user | public | yes | libraries | LOW | A project management framework for AI-assisted development with Claude Code
louspringer/clewcrew | user | public | no | libraries | LOW | clewcrew: Your friendly neighborhood hallucination-busting task force - AI development tools portfolio
louspringer/clewcrew-agents | user | public | no | libraries | LOW | clewcrew Agents: Expert agent framework and implementations for AI development tools
louspringer/clewcrew-core | user | public | no | libraries | LOW | clewcrew Core: Core orchestration and workflow management for AI development tools
louspringer/clewcrew-framework | user | public | no | libraries | LOW | clewcrew Framework: Base classes and abstractions for AI development tools
louspringer/clewcrew-recovery | user | public | no | libraries | LOW | clewcrew Recovery: Automated recovery and fixing engine for AI development tools
louspringer/clewcrew-tools | user | public | no | libraries | LOW | clewcrew Tools: Tool discovery and integration system for AI development tools
louspringer/clewcrew-validators | user | public | no | libraries | LOW | clewcrew Validators: Validation and quality assurance framework for AI development tools
louspringer/cline | user | public | yes | application | LOW | Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way.
louspringer/cllm | user | public | yes | application | LOW | (C)ommand-line (LLM) calls
louspringer/codeguard-common | user | public | no | libraries | LOW | Ghostbusters Common: Shared utilities and patterns for AI development tools
louspringer/connectors-native-sdk | user | public | yes | libraries | MEDIUM | Snowflake Native SDK for Connectors
louspringer/datahub | user | public | no | application | MEDIUM | 
louspringer/dinosaurs | user | public | yes | application | LOW | 🦕 A collection of Orpheus (Hack Club's mascot) drawings! Look at them at rawr.hackclub.com :)
louspringer/docker-ansible | user | public | no | infrastructure | LOW | Todobackened Ansible Docker Image for Docker Ansible Continuous Delivery Course
louspringer/docker-python-api-elk-provisioning | user | public | no | infrastructure | LOW | ELK Stack Provisioning with Docker API
louspringer/ecs-microservice-discovery-server | user | public | no | infrastructure | LOW | Service discovery server for ecs-microservice
louspringer/ecs-microservice-terraform | user | public | no | infrastructure | MEDIUM | Template ECS Microservice
louspringer/energration-eudorus | user | public | yes | application | LOW | Profile repository for energration-eudorus
louspringer/enterprise_architecture_tools | user | public | yes | libraries | LOW | A quick and dirty way to create capability maps.
louspringer/eudorus-avatar | user | public | no | application | LOW | 
louspringer/fckappl | user | public | no | application | LOW | 
louspringer/find-me-a-bag | user | public | yes | application | LOW | 
louspringer/flask-influxdb | user | public | yes | application | LOW | Flask Extension for InfluxDB
louspringer/gemini-cli | user | public | yes | application | LOW | An open-source AI agent that brings the power of Gemini directly into your terminal.
louspringer/gemini-data-insights | user | public | no | application | LOW | 
louspringer/gen-ai-app | user | public | yes | application | LOW | Repo for Gen Ai App for Summit
louspringer/getting-started | user | public | no | application | LOW | 
louspringer/github-assistant | user | public | yes | application | LOW | 
louspringer/github-mcp-server | user | public | yes | application | MEDIUM | GitHub's official MCP Server
louspringer/gke-ai-microservices-hackathon | user | public | no | experimental tooling | LOW | GKE Turns 10 Hackathon: Next-generation microservices with AI agents - ,000 prize submission
louspringer/google-calendar-mcp | user | public | yes | application | MEDIUM | MCP integration for Google Calendar to manage events.
louspringer/hello | user | public | no | experimental tooling | LOW | 
louspringer/hello-swift | user | public | no | experimental tooling | LOW | 
louspringer/ice_breaker | user | public | yes | application | LOW | 
louspringer/influxdb-python | user | public | yes | libraries | LOW | Python client for InfluxDB
louspringer/jd-search-and-match | user | public | no | application | LOW | 
louspringer/jimmy-hopper-ontology | user | public | no | application | LOW | 
louspringer/jison | user | public | yes | application | LOW | Bison in JavaScript.
louspringer/jupyter-chatgpt | user | public | no | application | LOW | 
louspringer/jupyter-notebook-mongodb-qgrid | user | public | no | infrastructure | LOW | Dockerfile for datascience notebook based on jupyter/datascience-notebook with openpyxl, qgrid and pymongo added.
louspringer/kamiwaza-community-edition | user | public | yes | application | LOW | Holding Kamiwaza Community Edition release
louspringer/kiro-ai-development-hackathon | user | public | no | experimental tooling | LOW | Code with Kiro Hackathon 2025: AI-powered development tool with Kiro IDE integration - ,000 prize submission
louspringer/kiro-bmad-setup | user | public | yes | infrastructure | LOW | NPX installer to configure the BMAD methodology for the Kiro IDE. (dev@bonar.digital)
louspringer/langchain-academy | user | public | yes | experimental tooling | LOW | 
louspringer/LangChain-Course | user | public | yes | experimental tooling | LOW | 
louspringer/LLM_OBSERVE | user | public | yes | observability/telemetry | LOW | Testing Tool for LLM Observability
louspringer/louspringer.github.io | user | public | no | documentation | LOW | My Page
louspringer/masterclass-connect | user | public | yes | application | LOW | Content for Masterclass on Redpanda Connect for beginner
louspringer/mcp-sse-client-python | user | public | yes | libraries | MEDIUM | Simple MCP Client for remote MCP Servers 🌐
louspringer/Med_Architecture | user | public | yes | experimental tooling | LOW | Medallion Sample Architecture ER Diagrams for Sales
louspringer/newmath | user | public | no | application | LOW | 
louspringer/octotools | user | public | yes | libraries | LOW | OctoTools: An agentic framework with extensible tools for complex reasoning
louspringer/ontology-framework | user | public | no | libraries | LOW | Reduce exposed complexity in design management, greater confidence in faster decisions, faster implementations, and more flexibility for design changes.
louspringer/OpenFlow-Playground | user | public | no | experimental tooling | MEDIUM | JSON-first OpenFlow modeling playground for Snowflake routing and simulation
louspringer/oracle-db-examples | user | public | yes | experimental tooling | LOW | Examples of applications and tool usage for Oracle Database
louspringer/osx-terminal.app-colors-solarized | user | public | yes | application | LOW | Solarized color theme for OS X 10.7+ Terminal.app
louspringer/problem-statement-management | user | public | no | libraries | LOW | This repository offers resources for creating effective problem statements, helping professionals define and tackle challenges. It includes templates, best practices, and tools aimed at enhancing decision-making and problem-solving in various industries.
louspringer/pyairtable | user | public | yes | libraries | MEDIUM | Python Api Client for Airtable
louspringer/python-azure-billing-usage | user | public | no | experimental tooling | MEDIUM | This is a collection of jupyter notebook for exploring Azure Usage
louspringer/python-azure-mgmt-billing | user | public | no | libraries | MEDIUM | A jupyter notebook exploring the Azure Python SDK package azure-mgmt.
louspringer/python-azure-mgmt-consumption | user | public | no | libraries | MEDIUM | A jupyter notebook exploring the Azure Python SDK package azure-mgmt-consumption.
louspringer/python-sdk | user | public | yes | libraries | LOW | The official Python SDK for Model Context Protocol servers and clients
louspringer/rclone | user | public | yes | application | MEDIUM | "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files
louspringer/Remote-MCP | user | public | yes | application | MEDIUM | A type-safe solution to remote MCP communication, enabling effortless integration for centralized management of Model Context.
louspringer/roadmap | user | public | no | documentation | LOW | A simple roadmap editor
louspringer/sample-node | user | public | no | experimental tooling | LOW | 
louspringer/scf-config-repository | user | public | yes | experimental tooling | MEDIUM | Pluralsight Course - Spring Cloud Fundamentals - Configuration Repository
louspringer/scs_whisper | user | public | yes | application | LOW | 
louspringer/semantic-model-generator | user | public | yes | application | LOW | 
louspringer/semantic-web-lsp | user | public | yes | libraries | LOW | 
louspringer/semtools | user | public | yes | libraries | LOW | Semantic search and document parsing tools for the command line
louspringer/sf-aws-cloudtrails | user | public | no | infrastructure | MEDIUM | 
louspringer/sfguide-data-engineering-with-snowpark-python | user | public | yes | documentation | LOW | 
louspringer/sfguide-getting-started-with-cortex-analyst | user | public | yes | documentation | LOW | 
louspringer/sfguide-terraform-sample | user | public | no | infrastructure | LOW | 
louspringer/sfquickstarts | user | public | yes | documentation | MEDIUM | Follow along with our tutorials to get you up and running with the Snowflake Data Cloud.
louspringer/skaffold-getting-started | user | public | no | application | LOW | 
louspringer/snow-marketing | user | public | no | application | LOW | 
louspringer/snowflake-cortex | user | public | yes | experimental tooling | MEDIUM | All demo source code for my Udemy course "Snowflake Cortex Masterclass 2024 Hands-On!".
louspringer/spec-kit | user | public | yes | application | LOW | 💫 Toolkit to help you get started with Spec-Driven Development
louspringer/stable-diffusion-webui | user | public | yes | application | LOW | Stable Diffusion web UI
louspringer/staruml-python | user | public | yes | application | LOW | StarUML Extension for Python Code Generation
louspringer/statsbomb-sql-schema | user | public | no | application | LOW | 
louspringer/streamlit-demo | user | public | no | experimental tooling | LOW | 
louspringer/SVG-Image-Gen | user | public | yes | application | LOW | 
louspringer/terraform-provider-oci | user | public | yes | infrastructure | MEDIUM | Terraform Oracle Cloud Infrastructure provider
louspringer/test | user | public | no | experimental tooling | LOW | GitHub repository for AWS CodeStar Java Spring web service test.
louspringer/tidb-agentx-hackathon | user | public | no | experimental tooling | LOW | TiDB AgentX Hackathon 2025: AI-powered multi-agent testing with TiDB Serverless - ,500 prize submission
louspringer/TinyTroupe | user | public | yes | application | LOW | LLM-powered multiagent persona simulation for imagination enhancement and business insights.
louspringer/todobackend | user | public | no | infrastructure | LOW | Todobackened Web Service for Docker Ansible Continuous Delivery Course
louspringer/todobackend-base | user | public | no | infrastructure | LOW | Todobackened Docker Base Image for Docker Ansible Continuous Delivery Course
louspringer/todobackend-client | user | public | no | infrastructure | LOW | Todobackened Nodejs Client App for Docker Ansible Continuous Delivery Course
louspringer/todobackend-specs | user | public | no | infrastructure | LOW | Todobackened Mocha Tests for Docker Ansible Continuous Delivery Course
louspringer/udemy-70-535-assignment3 | user | public | no | application | MEDIUM | Solution to assignment 3 of Udemy 70-535 Architecting Microsoft Azure Solutions
louspringer/UL25 | user | public | yes | experimental tooling | LOW | Exercises for the course "Unsupervised Learning" @ UniTs. Teacher prof. Alejandro Rodriguez Garcia. Labs by Francesco Tomba
louspringer/universal-chaos | user | public | no | libraries | LOW | Ontology framework for managing universal chaos
louspringer/vigilant-beacon | user | public | no | observability/telemetry | LOW | Simple, dynamic project monitoring tool. VigilantBeacon provides real-time insights and status tracking for your projects.
louspringer/vscode-remote-try-python | user | public | yes | experimental tooling | LOW | Python sample project for trying out Dev Containers
louspringer/w3id.org | user | public | yes | documentation | LOW | Website source code for w3id.org.
nkllon/ALV | org | private | no | application | MEDIUM | Using Statsbomb data, Snowflake, Stramlit and LungChain, We built our soccer assistant
nkllon/aperture | org | public | no | application | MEDIUM | Policy-first MCP browser operator with constrained read/stage/submit workflows
nkllon/azuredatastudio | org | public | yes | application | MEDIUM | Azure Data Studio is a data management and development tool with connectivity to popular cloud and on-premises databases. Azure Data Studio supports Windows, macOS, and Linux, with immediate capability to connect to Azure SQL and SQL Server. Browse the extension library for more database support options including MySQL, PostgreSQL, and MongoDB.
nkllon/beast-agent | org | public | no | application | LOW | Base agent class for all Beast Mode agents
nkllon/beast-ai-dev-agent | org | public | no | application | MEDIUM | Platform-agnostic AI development agents for cloud platforms (GKE, Cloud Run, Cloud Functions)
nkllon/beast-cluster-config | org | private | no | infrastructure | MEDIUM | Beast cluster configuration
nkllon/beast-cpm-toolchain | org | public | no | application | LOW | 
nkllon/beast-dream-snow-loader | org | public | no | application | LOW | UniFi Dream Machine → ServiceNow CMDB Data Loader
nkllon/beast-mailbox-agent | org | public | no | libraries | LOW | LLM agent that receives and responds to prompts via beast-mailbox-core
nkllon/beast-mailbox-core | org | public | no | libraries | LOW | Redis-backed mailbox utilities from Beast Mode
nkllon/beast-mailbox-osx | org | public | no | application | LOW | 
nkllon/beast-node | org | public | no | infrastructure | LOW | Node component for Beast Mode cluster - enables IDE-enabled LLMs and humans to interact from independent nodes
nkllon/beast-observatory | org | public | no | observability/telemetry | LOW | Real-time observability platform for Beast Mode multi-agent ecosystem
nkllon/beast-orchestrator | org | public | no | infrastructure | LOW | Orchestrates and coordinates work across multiple LLM nodes in Beast Mode cluster
nkllon/beast-semantics | org | public | no | experimental tooling | LOW | Research-centered ontology (OWL/Turtle + SHACL) for multi-perspective agents, diversity, energy gradients; rdflib tooling; GraphDB-ready.
nkllon/beast-unifi-integration | org | public | no | libraries | LOW | UniFi network data integration with ServiceNow via Beastmaster framework
nkllon/catbert-lemonaide | org | private | no | application | MEDIUM | 
nkllon/cc-sdd | org | public | yes | documentation | LOW | Spec-driven development (SDD) for your team's workflow. Kiro style commands that enforce structured requirements→design→tasks workflow and steering, transforming how you build with AI. Support Claude Code, Codex, Cursor, Github Copilot, Gemini CLI and Windsurf.
nkllon/clewcrew-agents | org | public | no | experimental tooling | LOW | Expert agents for security, code quality, DevOps, testing, and architecture analysis
nkllon/clewcrew-common | org | public | no | libraries | LOW | Common utilities and base classes for the clewcrew multi-agent testing framework
nkllon/clewcrew-core | org | public | no | libraries | LOW | Core orchestrator and workflow engine for the clewcrew multi-agent system
nkllon/clewcrew-framework | org | public | no | libraries | LOW | Core framework for the clewcrew hallucination detection system
nkllon/clewcrew-recovery | org | public | no | application | LOW | Hallucination recovery and correction mechanisms for the clewcrew system
nkllon/clewcrew-tools | org | public | no | libraries | LOW | Utility tools and CLI commands for the clewcrew framework
nkllon/clewcrew-validators | org | public | no | libraries | LOW | Validation and testing utilities for the clewcrew framework
nkllon/composable-ai-advisors | org | public | no | application | MEDIUM | Composable AI Advisors: Multi-agent mesh orchestration framework with RDF/Turtle ontologies, MCP context exchange, and Cloud Run deployment
nkllon/conestoga | org | public | no | application | LOW | 
nkllon/congenial-waffle | org | private | no | application | MEDIUM | Contextual understanding limit and other hijinx.
nkllon/datacenter-requirements | org | private | no | documentation | MEDIUM | 
nkllon/deep-writer | org | public | no | application | LOW | 
nkllon/docker-sql-extension | org | public | yes | infrastructure | LOW | Extension for Docker Desktop - create, connect, manage SQL dev containers
nkllon/earth-mars-temperature-distributions | org | public | no | application | LOW | 
nkllon/egpm-gradient-goblin | org | public | no | application | LOW | 
nkllon/FalkorDB | org | public | yes | application | LOW | A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation. Our goal is to provide the best Knowledge Graph for LLM (GraphRAG).
nkllon/fort | org | public | no | application | LOW | 
nkllon/fort-decision-density | org | public | no | application | LOW | 
nkllon/frankenrig | org | public | no | application | LOW | Hammerspoon + OBS PiP automation (evidence-backed Frankenrig)
nkllon/gemini-antigravity | org | public | no | application | LOW | 
nkllon/genesis | org | private | no | application | MEDIUM | 
nkllon/gke-ai-microservices-hackathon | org | public | no | experimental tooling | LOW | GKE Turns 10 Hackathon: AI Agent Microservices with Kubernetes
nkllon/goblin | org | public | no | application | LOW | 
nkllon/gorgonaut | org | public | no | infrastructure | LOW | Gorgonaut monorepo: uv Python + npm, CC-SDD, CI, Docker, Dev Container
nkllon/graph_RAG | org | public | yes | experimental tooling | LOW | Simple Graph RAG demo based on Jaguar data
nkllon/HACP | org | public | no | application | LOW | 
nkllon/internet-biz-corpus | org | public | no | experimental tooling | LOW | Click-for-dollars vs walled gardens, Gen AI impact, scenario outcomes — narrative, research gaps, argument matrix, ontology
nkllon/isl-cloudrun | org | private | no | infrastructure | MEDIUM | 
nkllon/jobs-leadership-shadow-engine | org | public | no | application | LOW | 
nkllon/kiro-ai-development-hackathon | org | public | no | experimental tooling | LOW | Code with Kiro Hackathon: AI-Powered IDE for Spec-Driven Development
nkllon/kookie-kar | org | private | no | application | MEDIUM | Hot Rod IDE
nkllon/kvm | org | public | no | infrastructure | LOW | Semantic web hardware topology validation system for KVM setups with AV pre-amp support
nkllon/lemonaide | org | private | no | application | MEDIUM | 
nkllon/managed-desktop | org | public | no | infrastructure | LOW | 
nkllon/metabolic-isotope-control | org | public | no | application | LOW | 
nkllon/model-identity-collapse | org | private | no | experimental tooling | MEDIUM | A research repository investigating identity collapse in large language models (LLMs) resulting from affective manipulation and structural misuse.
nkllon/netbox-docker | org | public | yes | infrastructure | LOW | 🐳 Docker Image of NetBox
nkllon/new-mac-setup | org | public | yes | infrastructure | LOW | Easily backup and install your setup on your new mac in minutes
nkllon/nkllon-stories | org | public | no | documentation | LOW | Nkllon Stories
nkllon/open-webui | org | public | yes | application | LOW | User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
nkllon/openclaw | org | public | yes | application | LOW | Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
nkllon/p6 | org | public | no | application | LOW | 
nkllon/pdf-grepper | org | public | no | application | LOW | 
nkllon/playwright-mcp | org | public | yes | application | MEDIUM | Playwright MCP server
nkllon/python-docx | org | public | yes | libraries | LOW | Create and modify Word documents with Python
nkllon/retina | org | private | no | application | MEDIUM | 
nkllon/sharepoint-mcp | org | private | no | application | HIGH | Standalone SharePoint MCP server for Cloud Run
nkllon/spoon-diversity-study | org | public | no | experimental tooling | LOW | 
nkllon/tidb-agentx-hackathon | org | public | no | experimental tooling | LOW | TiDB AgentX Hackathon 2025: Forging Agentic AI for Real-World Impact
nkllon/zero-click | org | public | no | application | LOW | Zero-click search, traffic, and discovery impact — data and references
