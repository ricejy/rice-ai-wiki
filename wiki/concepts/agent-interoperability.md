---
title: Agent Interoperability
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agents, protocols, standards]
sources: [agent-payments-protocol, agents-for-financial-services]
---

# Agent Interoperability

## Definition

The set of open protocols and standards enabling AI agents from different providers to discover each other, communicate, share tools, and transact. Without interoperability, the agent ecosystem fragments into proprietary silos.

## The protocol stack

| Layer | Protocol | Purpose |
|-------|----------|---------|
| Tools | [[Model Context Protocol]] (MCP) | Connect agents to external tools and data sources |
| Communication | [[A2A Protocol]] (Agent-to-Agent) | Agents discover and collaborate with other agents |
| Commerce | AP2 (Agent Payments Protocol) | Agents make payments on behalf of users |
| Trust | FIDO Alliance standards | Cryptographic verification of agent identity and intent |

These layers are composable: an agent built with any framework can use MCP for tools, A2A for collaboration, and AP2 for payments.

## Data connectors

Beyond protocols, agents need governed access to real-world data. [[Anthropic]]'s financial services ecosystem connects to dozens of providers (FactSet, S&P, Moody's, etc.). **MCP apps** go further than connectors by embedding provider tools directly inside the agent — e.g., Moody's MCP app brings credit ratings and data on 600M+ entities.

## Standardization trend

AP2 donated to FIDO Alliance. MCP is open-source. A2A is open. The trajectory is toward open standards rather than proprietary integrations — similar to how the web standardized on HTTP/HTML rather than proprietary networks.

## See also
- [[Model Context Protocol]]
- [[A2A Protocol]]
- [[Agent Commerce]]
- [[Agentic Systems]]
