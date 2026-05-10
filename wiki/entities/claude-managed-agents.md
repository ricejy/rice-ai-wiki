---
title: Claude Managed Agents
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [anthropic, agents, enterprise, platform]
sources: [agents-for-financial-services]
---

# Claude Managed Agents

## Overview

[[Anthropic]]'s platform for running autonomous agents on the Claude Platform, as distinct from interactive plugin-based agents in Claude Cowork/Code. Designed for work that spans hours or runs on schedules (e.g., nightly deal close, batch processing a book of deals).

## Key features

- **Long-running sessions** — multi-hour tasks (e.g., deal closes)
- **Per-tool permissions** — granular control over what each agent can access
- **Managed credential vaults** — secure credential storage
- **Full audit log** — every tool call and decision inspectable by compliance and engineering
- **Cookbooks** — reference architectures that package skills, connectors, and subagents

## Relevance

Managed Agents are the enterprise-grade deployment mode for the [[Agent Design Patterns]] orchestrator-workers pattern. The audit logging and per-tool permissions serve the same trust function as [[Model-Based Guardrail]] systems but at the platform level rather than the model level.

The "human in the loop" remains — users review, iterate, and approve before output goes to clients or gets filed. This is [[Deny-and-Continue]] at the workflow level.

## See also
- [[Anthropic]]
- [[Agent Design Patterns]]
- [[Agent Commerce]]
- [[Model-Based Guardrail]]
