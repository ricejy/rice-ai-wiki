---
title: Agent Commerce
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agents, payments, commerce, economy]
sources: [agent-payments-protocol, agents-for-financial-services, telegram-impt-ai-news-digest]
---

# Agent Commerce

## Definition

The emerging domain of AI agents transacting autonomously in the real economy — browsing, negotiating, purchasing, and paying on behalf of users. Extends [[Agentic Systems]] from tool use and content generation into financial transactions with real-world consequences.

## The trust gap

Current payment infrastructure assumes human presence at the point of transaction. When agents act autonomously, three trust problems emerge:

1. **Authorization** — proving the user granted specific authority for this purchase
2. **Authenticity** — verifying the request reflects true user intent, not hallucination
3. **Accountability** — determining liability when transactions go wrong

These parallel the safety challenges in [[Model-Based Guardrail]] design — how do you let an agent act autonomously while maintaining trust constraints?

## Approaches

**Protocol-level trust ([[A2A Protocol]] + AP2):** [[Google]]'s approach. Verifiable Digital Credentials provide cryptographic proof of user intent. Non-repudiable audit trail. Donated to FIDO Alliance for standardization. Trust is engineered into the protocol, not inferred from agent behavior.

**Platform-level trust ([[Claude Managed Agents]]):** [[Anthropic]]'s approach for financial services. Per-tool permissions, managed credential vaults, full audit logs. Compliance teams inspect every tool call. Trust enforced by the platform, with humans reviewing before actions are finalized.

Both approaches share a core principle: **verifiable intent over inferred action** — the system should prove what the user authorized, not guess from agent behavior.

## Consumer-facing agents

Beyond B2B agent deployment, consumer fintech is adopting agent interfaces:
- **Revolut AIR** (April 2026) — in-app AI financial assistant. Manages finances, controls cards, tracks investments, manages subscriptions via conversation. Rolling out to UK first.
- **Alibaba Qoderwake** — "digital employee" product for engineering, operations, and sales roles
- **[[Sierra AI]]** — enterprise Agent OS platform for customer experience. Deploys agents across chat, SMS, WhatsApp, email, voice. Outcome-based pricing. Customers include Rocket Mortgage, SoFi, Wayfair.

## Infrastructure stack

The agent commerce stack is layering up:
- **Agent frameworks** — ADK, [[Claude Agent SDK]], etc.
- **Tool protocols** — [[Model Context Protocol]]
- **Agent collaboration** — [[A2A Protocol]]
- **Payments** — AP2
- **Data connectors** — FactSet, S&P, Moody's, etc.

## See also
- [[Agentic Systems]]
- [[A2A Protocol]]
- [[Agent Interoperability]]
- [[Model-Based Guardrail]]
- [[Claude Managed Agents]]
