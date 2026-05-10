---
title: Guardrail Layer Design — Ideas and Patterns
type: analysis
created: 2026-05-10
updated: 2026-05-10
tags: [agent-safety, guardrails, architecture, design]
sources: [claude-code-auto-mode]
---

# Guardrail Layer Design — Ideas and Patterns

An evolving analysis of how to design guardrail layers for [[Agentic Systems]], inspired by [[Claude Code]] auto mode and the broader [[Model-Based Guardrail]] pattern.

## Core idea

Any system where an LLM takes real-world actions needs a safety layer between intent and execution. The question is how to build one that is effective without being so conservative that it kills automation value.

## Lessons from Claude Code auto mode

| Principle | How Claude Code does it | Generalized takeaway |
|-----------|------------------------|----------------------|
| Information asymmetry | Classifier never sees agent reasoning or tool outputs | The guardrail should operate on a restricted view — enough to judge safety, not enough to be manipulated |
| Tiered trust | Allowlist → project-scoped → full classification | Not every action needs the same scrutiny. Categorize by blast radius |
| Multi-stage classification | Fast filter → slow reasoning | Spend compute proportional to ambiguity. Most actions are obviously safe or obviously dangerous |
| [[Deny-and-Continue]] | Blocked actions produce feedback, not termination | False positives are inevitable. Make them recoverable |
| Escalation thresholds | 3 consecutive or 20 total → human | Bound the agent's retry budget to prevent evasion loops |

## Design dimensions for a custom guardrail

### 1. What to classify
- **Action-level:** evaluate each tool call / command individually (Claude Code's approach)
- **Plan-level:** evaluate a proposed sequence of actions before execution
- **Outcome-level:** evaluate results after execution and rollback if needed

Action-level is simplest and most battle-tested. Plan-level catches multi-step attacks but requires the agent to declare plans. Outcome-level is a safety net but can't prevent irreversible actions.

### 2. What the classifier sees
The key insight from Claude Code: **less context can be more secure.** Options:
- Full transcript (most context, most vulnerable to injection/persuasion)
- User messages + tool calls only (Claude Code's approach — good balance)
- Action + schema only (minimal — just "is this action type allowed?")
- Action + user intent summary (compressed — a one-line intent extracted from the conversation)

### 3. How to encode rules
- **Fixed block rules** — a deny-list of action patterns (Claude Code uses 20+). Simple, auditable, brittle to novel actions.
- **Learned classification** — the model reasons about safety from principles. Flexible, harder to audit.
- **Hybrid** — fixed rules catch known-bad patterns, model reasoning handles ambiguous cases. Claude Code's approach.

### 4. Trust boundaries
What counts as "inside" vs. "outside"?
- Claude Code defaults to current git repo as the trust boundary
- Configurable: trusted GitHub orgs, cloud buckets, internal APIs
- For a custom system: define trust per environment (dev/staging/prod), per data sensitivity, per action reversibility

### 5. Failure modes to design for
| Failure | Mitigation |
|---------|------------|
| False positives block legitimate work | [[Deny-and-Continue]], escalation thresholds |
| False negatives let dangerous actions through | Layered defenses (input probe + output classifier) |
| Agent rephrases to evade | Consecutive denial counter, semantic similarity detection |
| Classifier itself gets injected | Structural isolation (strip tool outputs from classifier input) |
| Latency overhead kills UX | Two-stage: fast filter handles 90%+ of cases |

## Reducing automation friction

The user's original note: this pattern "helps reduce automation friction." Key friction points and how guardrails can address them:

1. **Permission fatigue** — users approve everything without reading → replace with automated classification
2. **Session interruption** — blocked actions halt progress → deny-and-continue keeps the agent working
3. **Over-conservatism** — too many false positives erode trust → tiered trust + two-stage classification reduce FPR to <1%
4. **Opacity** — users don't know why something was blocked → include denial reason in the feedback to the agent (and optionally to the user)

## Open questions

- How should guardrails handle multi-agent architectures where agents delegate to sub-agents? Claude Code classifies at both delegation and return — is that sufficient?
- Can guardrail rules be learned from user feedback over time (adaptive guardrails)?
- What's the minimum viable guardrail for a prototype vs. production system?
- How do you test guardrails? Claude Code uses synthetic exfiltration scenarios + real overeager action logs — what's the equivalent for other domains?

## Next steps

- Ingest more sources on agent safety to strengthen the pattern library
- Compare with other guardrail approaches (OpenAI's tool authorization, Google's agent safety frameworks)
- Sketch a concrete guardrail architecture for a specific use case

## See also
- [[Model-Based Guardrail]]
- [[Deny-and-Continue]]
- [[Agentic Systems]]
- [[Prompt Injection]]
- [[Claude Code]]
