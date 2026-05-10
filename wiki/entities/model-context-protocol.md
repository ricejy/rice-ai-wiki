---
title: Model Context Protocol
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [anthropic, protocols, tooling]
sources: [building-effective-agents, agent-payments-protocol, agents-for-financial-services]
---

# Model Context Protocol

## Overview

An open protocol by [[Anthropic]] for connecting LLMs to external tools, data sources, and services. Mentioned in "Building Effective Agents" as one implementation approach for the augmented LLM building block — the foundation of all [[Agent Design Patterns]].

Provides a standardized way for models to discover and use tools, rather than each integration requiring custom code.

## Role in the agent stack

MCP is the **tool layer** of the [[Agent Interoperability]] stack:
- MCP — tools and data access
- [[A2A Protocol]] — agent-to-agent collaboration
- AP2 — agent payments (extends both A2A and MCP)

AP2 works as an MCP extension, meaning payment capabilities can be added to any MCP-equipped agent.

## MCP apps

Beyond simple connectors, **MCP apps** embed provider-specific tools and interactive UI directly inside the agent. Example: **Moody's MCP app** brings proprietary credit ratings and data on 600M+ public and private entities into Claude for compliance, credit analysis, and business development.

## See also
- [[Anthropic]]
- [[Agent Interoperability]]
- [[A2A Protocol]]
- [[Agent-Computer Interface]]
- [[Agent Design Patterns]]
