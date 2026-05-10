---
title: Model-Based Guardrail
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agent-safety, guardrails, classifiers]
sources: [claude-code-auto-mode]
---

# Model-Based Guardrail

## Definition

A pattern where a separate model (the guardrail) classifies and gates the actions of a primary agent model before execution. The guardrail model evaluates proposed actions against safety criteria and either approves, blocks, or escalates to a human.

## Key design principles

**Information asymmetry as defense.** The guardrail should see less context than the primary agent — specifically, it should not see the agent's own reasoning or raw tool outputs. This prevents two attack vectors simultaneously: the agent persuading the guardrail, and prompt injections in tool outputs reaching the guardrail. Demonstrated in [[Claude Code]] auto mode.

**Multi-stage classification.** A fast, conservative first stage catches most issues cheaply. A slower, reasoning-heavy second stage handles ambiguous cases. This breaks the efficiency/accuracy tradeoff — the first stage's cache can be shared with the second stage to reduce cost.

**[[Deny-and-Continue]].** When the guardrail blocks an action, the agent should receive the denial as feedback with instructions to find an alternative, rather than having the session terminated. This makes false positives survivable and reduces automation friction. Escalation thresholds (e.g., 3 consecutive or 20 total denials) catch persistent issues.

**Tiered trust.** Not all actions need classifier review. Read-only operations can be allowlisted. In-project edits may be auto-approved if they're reviewable via version control. Only actions with real-world side effects or cross-boundary implications go through the full classifier.

## Open questions

- How well does this pattern scale to more autonomous, longer-running agents where the context window grows very large?
- What's the right balance between block rules (fixed) and learned classification?
- Can guardrail models be made adversarially robust, or will prompt injection always require layered defenses?

## See also
- [[Deny-and-Continue]]
- [[Prompt Injection]]
- [[Agentic Systems]]
- [[Claude Code]]
