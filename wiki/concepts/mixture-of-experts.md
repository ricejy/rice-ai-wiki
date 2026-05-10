---
title: Mixture of Experts
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [architecture, efficiency, inference]
sources: [telegram-impt-ai-news-digest]
---

# Mixture of Experts

## Definition

A model architecture where only a subset of parameters ("experts") are activated for each token, selected by a learned routing mechanism. Total parameter count remains large (for capacity) but active parameter count per token is small (for efficiency).

## Why it matters

MoE breaks the scaling dilemma: larger models are more capable but more expensive. With MoE, you get the capacity of a large model at the inference cost of a small one.

## Example: Qwen 3.6-35B-A3B

Alibaba's Qwen 3.6-35B-A3B (April 2026): 35B total parameters but only 3B active per token. Results:
- SWE-bench Verified: 73.4 (competitive with much larger dense models)
- Terminal-Bench 2.0: 51.5
- QwenClawBench: 52.6

The key idea: instead of using all parameters every time, the model selects a few relevant "experts" for each step. This keeps compute low while maintaining performance.

## Relevance to local inference

MoE is particularly relevant for [[Local LLM Inference]] — a 35B MoE model with 3B active fits similar compute budgets as a 3B dense model, but with much higher capability. The tradeoff: total memory footprint is still 35B (all experts must be in memory), but compute per token is dramatically lower.

Combined with [[KV Cache]] compression and [[Quantization]], MoE makes frontier-class models increasingly feasible on consumer hardware.

## See also
- [[Local LLM Inference]]
- [[Quantization]]
- [[Sparse Attention]]
