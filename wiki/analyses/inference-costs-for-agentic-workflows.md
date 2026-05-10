---
title: Inference Costs for Agentic Workflows
type: analysis
created: 2026-05-10
updated: 2026-05-10
tags: [agents, inference, kv-cache, optimization, cost]
sources: [attention-optimization-primer, google-turboquant, claude-code-auto-mode, building-effective-agents]
---

# Inference Costs for Agentic Workflows

An analysis of why [[Agentic Systems]] are disproportionately affected by inference costs, and which optimization techniques best address each bottleneck.

## Why agents are expensive

Single-turn LLM calls have a fixed context window. Agents are different — they accumulate context across an entire workflow:

| Agent workload | Context characteristics |
|---------------|----------------------|
| Code repository analysis | Massive prefill (thousands of files), moderate decode |
| Multi-day conversation | Continuously growing KV cache, periodic summarization |
| Multi-file editing | Repeated tool calls, each adding to context |
| Web browsing + research | Unpredictable context growth from fetched content |

The costs compound at two levels:
1. **Quadratic attention** — each new token attends to all previous tokens. A 100K-token agent context costs 100x more attention compute than a 10K-token single query.
2. **Linear KV cache** — the [[KV Cache]] grows with every token. At agent scale (hours of operation, entire repositories), it exhausts GPU memory.

## The agent memory wall

When the KV cache exceeds available memory, the system must either:
- **Offload to CPU/disk** — adds latency, defeats the purpose of fast inference
- **Truncate context** — loses information the agent may need later
- **Crash** — breaks the workflow entirely

This is why the attention optimization primer calls long-context KV cache "the" bottleneck for continuous agentic interaction.

## Optimization techniques mapped to agent needs

### For prefill-heavy workloads (code analysis, document processing)

The bottleneck is time-to-first-token (TTFT). The agent ingests a massive context before it can start working.

| Technique | Impact | Tradeoff |
|-----------|--------|----------|
| KV cache compression (KVTC) | Up to 8x TTFT improvement | Compression compute overhead |
| [[Sparse Attention]] (DSA) | ~Constant memory regardless of context | May miss isolated details |
| [[Quantization]] (TurboQuant) | 6x memory reduction | Minimal — zero measured accuracy loss |

**Best approach:** TurboQuant for memory + KVTC for TTFT speed. Sparse attention if needle-in-a-haystack retrieval isn't critical.

### For decode-heavy workloads (long conversations, iterative editing)

The bottleneck is tokens-per-second during generation. The KV cache grows continuously as the agent works.

| Technique | Impact | Tradeoff |
|-----------|--------|----------|
| KV cache compression | Keeps cache in fast memory longer | Ongoing compression cost |
| Sliding window | Fixed memory, fast decode | Amnesia — forgets early instructions |
| Context summarization | Compacts history | Loses fine-grained details |

**Best approach:** KV cache compression to extend how long the agent can run before hitting the memory wall. Avoid sliding window for agents — losing early instructions is catastrophic (documented failure: agent started doing things it was told not to do).

### For retrieval-heavy workloads (searching repositories, fact-checking)

The bottleneck is accuracy on specific lookups within massive context.

| Technique | Impact | Tradeoff |
|-----------|--------|----------|
| KV cache compression | Preserves full trace, good retrieval | Memory savings less dramatic than sparse |
| Full attention | Maximum retrieval accuracy | Quadratic cost |
| [[Sparse Attention]] | Good for reasoning, weaker on needles | May miss isolated facts |

**Best approach:** KV cache compression (TurboQuant, KVTC). Sparse attention's weakness on needle-in-a-haystack makes it risky for retrieval-critical agent tasks.

## Cost implications for agent architecture

The choice of attention optimization affects which [[Agent Design Patterns]] are feasible:

| Pattern | Context profile | Recommended optimization |
|---------|----------------|------------------------|
| Prompt chaining | Short, reset between steps | None needed |
| Orchestrator-workers | Moderate per-worker, short-lived | Standard attention fine |
| Evaluator-optimizer | Growing loop context | KV cache compression |
| Autonomous agent | Long, continuously growing | KV cache compression + sparse attention |

The higher up the [[Agent Design Patterns]] complexity ladder, the more critical attention optimization becomes. Autonomous agents (level 7) are impractical for long-running tasks without some form of KV cache management.

## The guardrail cost multiplier

[[Model-Based Guardrail]] systems add a second model evaluation for each action. In [[Claude Code]] auto mode, the transcript classifier runs on [[Sonnet 4.6]] — a separate inference call per gated action. This effectively doubles the inference cost for tier-3 actions. Two-stage classification (fast filter → slow reasoning) mitigates this by keeping most evaluations cheap.

For budget-constrained deployments, the guardrail cost is a real factor in deciding between auto mode and manual approval.

## Open questions

- Can KV cache compression and sparse attention be composed? (Use sparse attention for the reasoning pass, but compress the full cache for retrieval fallback)
- What's the cost crossover point where agent memory optimizations pay for themselves vs. just using a shorter context?
- How do [[Local LLM Inference]] constraints differ from cloud constraints? (Unified memory on Apple Silicon changes the calculus — no CPU/GPU transfer overhead)
- Could agents learn to manage their own context — requesting summarization or cache eviction strategically?

## See also
- [[Agentic Systems]]
- [[KV Cache]]
- [[Sparse Attention]]
- [[Quantization]]
- [[Agent Design Patterns]]
- [[Model-Based Guardrail]]
- [[Local LLM Inference]]
- [[Guardrail Layer Design]]
