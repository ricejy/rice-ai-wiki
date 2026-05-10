---
title: Agent Design Patterns
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agents, architecture, patterns]
sources: [building-effective-agents, langchain-deep-agents]
---

# Agent Design Patterns

## Definition

A hierarchy of composable patterns for building [[Agentic Systems]], ordered by increasing complexity. The core principle: use the simplest pattern that solves the problem. Only escalate when simpler approaches fall short.

## The complexity ladder

| Level | Pattern | Type | When to use |
|-------|---------|------|-------------|
| 1 | Augmented LLM | Foundation | Single-turn tasks with retrieval/tools |
| 2 | Prompt chaining | Workflow | Fixed sequential subtasks |
| 3 | Routing | Workflow | Input-dependent specialization |
| 4 | Parallelization | Workflow | Independent subtasks or voting |
| 5 | Orchestrator-workers | Workflow | Dynamic task decomposition |
| 6 | Evaluator-optimizer | Workflow | Iterative refinement with clear criteria |
| 7 | Autonomous agent | Agent | Open-ended, unpredictable step count |

## Key insight: workflows vs. agents

Most "agent" use cases are actually workflows — predefined code paths where the LLM handles subtasks. True agents (level 7) dynamically direct their own processes. The distinction matters because workflows are more predictable, debuggable, and cheaper. Agents are only justified when the task structure genuinely can't be predetermined.

## Pattern interactions

- **Routing + parallelization** — classify then fan out to specialized parallel workers
- **Orchestrator-workers + evaluator-optimizer** — dynamic decomposition with quality feedback loops
- **Any pattern + [[Model-Based Guardrail]]** — safety layer gatekeeping actions at any level of the hierarchy
- **Prompt chaining + [[Deny-and-Continue]]** — failed steps get retried with alternative approaches

## Deep agents: making level 7 work

LangChain's "deep agents" analysis identifies four architectural investments that differentiate production autonomous agents (like [[Claude Code]], OpenAI Deep Research, Manus) from naive agent loops:

1. **Detailed system prompts** — extensive behavioral examples and tool usage guidance
2. **Planning tools** — no-op tools that force the LLM to maintain task plans in-context
3. **Sub-agents** — task decomposition through spawned specialist agents
4. **File system access** — persistent storage as external memory

These aren't new levels on the complexity ladder — they're the scaffolding that makes level-7 agents effective over long task horizons. All four are forms of **context engineering**: managing what the LLM sees and remembers.

## Framework vs. raw API

[[Anthropic]]'s recommendation: start with direct API calls. Frameworks (including [[Claude Agent SDK]]) add useful abstraction but can obscure the underlying logic and complicate debugging. Reach for frameworks once the patterns are proven and the application warrants the abstraction.

## See also
- [[Agentic Systems]]
- [[Agent-Computer Interface]]
- [[Model-Based Guardrail]]
- [[Claude Code]]
