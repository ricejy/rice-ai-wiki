---
title: "AP2 — Agent Payments Protocol"
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [agents, payments, commerce, protocols, google]
author: Google
published: 2026-05-10
url: https://ap2-protocol.org/
---

# AP2 — Agent Payments Protocol

## Summary

[[Google]]'s open protocol for enabling AI agents to make payments on behalf of users. Addresses a fundamental gap: today's payment systems assume a human clicks "buy." When an autonomous agent initiates a payment, this assumption breaks, creating unanswered questions about authorization, authenticity, and accountability.

AP2 extends the [[A2A Protocol]] and [[Model Context Protocol]] — it's part of the broader [[Agent Interoperability]] stack.

## The trust problem

When agents transact autonomously, three questions arise that current payment systems can't answer:

| Question | Problem |
|----------|---------|
| **Authorization** | How to verify the user gave the agent authority for this specific purchase? |
| **Authenticity** | How can a merchant be sure the request reflects the user's true intent, not a hallucination? |
| **Accountability** | If something goes wrong, who is responsible — user, developer, merchant, issuer, PSP? |

Without a protocol, the risk is a fragmented ecosystem of proprietary payment solutions — confusing for users, expensive for merchants, unmanageable for financial institutions.

## Core design: Verifiable Digital Credentials (VDCs)

AP2 engineers trust using cryptographically signed digital objects called VDCs. Two types, each with two stages:

**Checkout Mandate** (shared with merchant):
- *Open* — captures user's constraints and goals before a specific cart is finalized
- *Closed* — captures authorization for a specific, finalized checkout

**Payment Mandate** (shared with credential provider / networks / payment processor):
- *Open* — captures payment constraints (budget, allowed instruments)
- *Closed* — captures authorization for a specific amount bound to a finalized checkout

VDCs are chained to provide a complete, verifiable audit trail for both human-present and human-not-present transactions. This is **verifiable intent, not inferred action** — trust is anchored to deterministic, non-repudiable proof.

## Design principles

- **Open and interoperable** — non-proprietary, works with A2A and MCP
- **User control and privacy** — role-based architecture protects payment details
- **Verifiable intent** — cryptographic proof, not inferred action
- **Clear accountability** — non-repudiable audit trail for every transaction
- **Global and future-proof** — starts with card payments, roadmap includes e-wallets, real-time bank transfers (UPI, PIX), digital currencies

## Protocol stack

AP2 fits into a layered agent infrastructure:
- **Build agents** with ADK (or any framework)
- **Equip with tools** via [[Model Context Protocol]] (or any tool protocol)
- **Agent-to-agent collaboration** via [[A2A Protocol]]
- **Secure payments** via AP2

Donated to the **FIDO Alliance** for standardization — the same body that standardized WebAuthn/passkeys.

## Relevance

AP2 is the first serious attempt at solving [[Agent Commerce]] — agents transacting autonomously in the real economy. It connects to [[Agentic Systems]] at the commerce layer: if agents can browse, research, and decide, they also need to pay. The VDC approach is conceptually similar to [[Model-Based Guardrail]] thinking — engineering trust constraints into the system rather than relying on the agent to behave correctly.

## See also
- [[Agent Commerce]]
- [[Agent Interoperability]]
- [[A2A Protocol]]
- [[Model Context Protocol]]
- [[Google]]
- [[Agentic Systems]]
