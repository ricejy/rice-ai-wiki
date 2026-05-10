---
title: Agentic Systems
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agents, autonomy, tooling]
sources: [claude-code-auto-mode, building-effective-agents, attention-optimization-primer]
---

# Agentic Systems

## Definition

AI systems where an LLM operates in a loop — reading context, reasoning, taking actions (tool calls, code execution, API requests), observing results, and iterating. Distinguished from single-turn chat by the ability to take real-world actions autonomously.

Important distinction from [[Anthropic]]'s "Building Effective Agents": most "agentic" use cases are actually **workflows** (predefined code paths where the LLM handles subtasks), not true **agents** (where the LLM dynamically directs its own process). The distinction matters — workflows are more predictable, debuggable, and cheaper. See [[Agent Design Patterns]] for the full complexity ladder.

## Key challenges

**Permission and safety.** Every action an agent takes is a potential blast radius. The tension between autonomy (letting the agent work without interruption) and safety (preventing unintended consequences) is the central design problem. [[Model-Based Guardrail]] systems address this by using a classifier to gate actions.

**Approval fatigue.** When humans must approve every action, they stop reading carefully — 93% approval rate observed in [[Claude Code]]. This degrades the safety mechanism it's supposed to provide.

**Automation friction.** Overly conservative safety systems break the flow of autonomous work. The [[Deny-and-Continue]] pattern (letting the agent find alternative approaches after a block) reduces this friction.

**Inference cost.** Agents handle increasingly long contexts — entire code repositories, multi-day conversation histories, multi-file workflows. The [[KV Cache]] grows linearly with context length, and attention compute grows quadratically. At agent scale, the KV cache can exhaust GPU memory entirely, breaking the workflow. [[Sparse Attention]] and KV cache compression ([[Quantization]]) are the primary mitigations. See [[Inference Costs for Agentic Workflows]] for detailed analysis.

## Patterns

- **Guardrail layers** — classifier models gating agent actions ([[Model-Based Guardrail]])
- **Tiered permissions** — allowlisting safe actions, classifying risky ones
- **Multi-agent architectures** — delegation with security boundaries at handoff points
- **[[Deny-and-Continue]]** — blocked actions produce feedback, not termination

## See also
- [[Agent Design Patterns]]
- [[Agent-Computer Interface]]
- [[KV Cache]]
- [[Model-Based Guardrail]]
- [[Prompt Injection]]
- [[Claude Code]]
