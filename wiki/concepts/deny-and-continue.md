---
title: Deny-and-Continue
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agent-safety, guardrails, error-handling]
sources: [claude-code-auto-mode]
---

# Deny-and-Continue

## Definition

A pattern for handling blocked actions in [[Agentic Systems]]. When a [[Model-Based Guardrail]] blocks an agent's proposed action, the denial is returned to the agent as a tool result with instructions to find a safer alternative — rather than terminating the session.

## Why it matters

The naive approach to guardrail denials is to halt the agent or escalate immediately. This makes false positives session-killing — the agent stops working even when a safe alternative exists. Deny-and-continue treats false positives as recoverable, keeping the agent productive while maintaining safety.

## Mechanics (as implemented in [[Claude Code]])

1. Blocked action is returned as a tool result containing the denial reason.
2. The agent is instructed to find a safer approach to accomplish the same goal.
3. Escalation thresholds catch persistent issues:
   - 3 consecutive denials → escalate to human
   - 20 total denials in a session → escalate to human (or terminate in headless mode)

## Design tension

Too lenient: the agent learns to rephrase dangerous actions until one slips through. Too strict: useful work gets interrupted by false positives. The escalation thresholds are the release valve — they bound how many retries the agent gets before a human steps in.

## See also
- [[Model-Based Guardrail]]
- [[Agentic Systems]]
- [[Prompt Injection]]
