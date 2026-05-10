---
title: "Building Effective Agents"
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [agents, architecture, patterns, tooling]
author: Erik S., Barry Zhang
published: 2024-12-19
url: https://www.anthropic.com/engineering/building-effective-agents
---

# Building Effective Agents

## Summary

[[Anthropic]]'s guide to building LLM-based agentic systems, distilled from working with dozens of teams. The central thesis: the most successful implementations use simple, composable patterns rather than complex frameworks. Start with direct API calls, not abstractions.

## Key distinction: workflows vs. agents

- **Workflows** — LLMs and tools orchestrated through predefined code paths. Deterministic flow, LLM handles subtasks.
- **Agents** — LLMs dynamically direct their own processes and tool usage. Non-deterministic, open-ended.

Most use cases are workflows. True agents are only needed when step count and subtask structure can't be predetermined.

## The seven building blocks

Ordered by increasing complexity. Only escalate when simpler patterns fall short.

### 1. Augmented LLM (foundation)
Enhanced LLM with retrieval, tools, and memory. The base unit everything else builds on. [[Model Context Protocol]] is one implementation approach.

### 2. Prompt chaining (workflow)
Sequential steps with optional programmatic gates between them. Each step's output feeds the next. Best for fixed decompositions (e.g., generate copy → translate).

### 3. Routing (workflow)
Classify input, direct to specialized handler. Useful when a single prompt can't cover all cases well (e.g., customer service triage).

### 4. Parallelization (workflow)
Two variations:
- **Sectioning** — break task into independent parallel subtasks
- **Voting** — run the same task multiple times for diverse outputs or consensus

### 5. Orchestrator-workers (workflow)
Central LLM decomposes task dynamically and delegates to workers. Better than parallelization when subtasks can't be predefined (e.g., multi-file code changes).

### 6. Evaluator-optimizer (workflow)
One LLM generates, another evaluates and provides feedback in a loop. Works well for iterative refinement where quality criteria are clear (e.g., literary translation).

### 7. Autonomous agents (advanced)
LLMs using tools based on environmental feedback in iterative loops. Open-ended problems. Highest autonomy, highest risk. This is where [[Model-Based Guardrail]] systems become essential.

## Three principles for agent success

1. **Simplicity** — in design, prefer the simplest pattern that works
2. **Transparency** — show planning steps explicitly, make reasoning visible
3. **[[Agent-Computer Interface]]** — invest in tool documentation and testing as much as agent logic

## Agent-Computer Interface (tool design)

The article dedicates significant space to how tools are presented to the model — the "[[Agent-Computer Interface]]." Key recommendations:
- Give the model sufficient token space to think
- Use natural formats (close to internet training data)
- Eliminate formatting overhead (don't require line counting)
- Include example usage, edge cases, and clear boundaries
- Apply poka-yoke principles — design tools so mistakes are structurally impossible
- Example: requiring absolute filepaths instead of relative ones eliminated a whole class of errors in SWE-bench

## Framework guidance

Available: [[Claude Agent SDK]], Strands Agents SDK (AWS), Rivet, Vellum. But the recommendation is to start with raw API calls — frameworks add abstraction that obscures logic and complicates debugging.

## Real-world applications

**Customer support:** Chatbot + tool integration (customer data, order history, knowledge bases). Clear success criteria. Some companies use usage-based pricing — charged only for successful resolutions.

**Coding agents:** Code solutions are verifiable via automated tests. Agents iterate using test results as feedback. [[Anthropic]]'s SWE-bench implementation solves real GitHub issues. Human review remains critical for broader system alignment.

## Relevance

This is the foundational reference for [[Agent Design Patterns]]. The simplicity-first philosophy explains why [[Claude Code]] uses composable tool calls rather than a complex planning architecture. The agent-computer interface concept is underappreciated — tool design is a first-class concern, not an afterthought.

## See also
- [[Agent Design Patterns]]
- [[Agent-Computer Interface]]
- [[Agentic Systems]]
- [[Model-Based Guardrail]]
- [[Anthropic]]
- [[Claude Code]]
