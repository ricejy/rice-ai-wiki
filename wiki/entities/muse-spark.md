---
title: Muse Spark
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [models, meta, frontier]
sources: [telegram-impt-ai-news-digest]
---

# Muse Spark

## Overview

First model from MSL (led by Alexandr Wang, formerly Scale AI). Powers Meta AI. Released 2026-04-09. A genuine frontier entrant — strong across multimodal, reasoning, and agentic benchmarks, though not category-leading across the board.

## Benchmarks

| Category | Benchmark | Muse Spark | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 | Grok 4.2 |
|----------|-----------|------------|----------|----------------|---------|----------|
| Multimodal | MMMU Pro | 80.4 | 77.4 | 83.9 | 81.2 | 75.2 |
| Reasoning | HLE (no tools) | 42.8 | 40.0 | 45.4 | 43.9 | 31.6 |
| Reasoning | GPQA Diamond | 89.5 | 92.7 | 94.3 | 92.8 | 88.5 |
| Reasoning | ARC AGI 2 | 42.5 | 63.3 | 76.5 | 76.1 | 53.3 |
| Agentic | SWE-Bench Verified | 77.4 | 80.8 | 80.6 | — | 76.7 |
| Agentic | SWE-Bench Pro | 52.4 | 53.4 | 54.2 | 57.7 | 51.8 |
| Agentic | Terminal-Bench 2.0 | 59.0 | 65.4 | 68.5 | 75.1 | 47.1 |

Artificial Analysis Intelligence Index: 52 (#4 overall).

## What stood out

- **Token efficiency** — 58M output tokens to run the Artificial Analysis index vs. 120M for GPT-5.4 and 157M for Claude Opus 4.6. Roughly 2-3x more efficient.
- **Training efficiency** — rebuilt pretraining stack reaches equivalent capability with >10x less compute than Llama 4 Maverick
- **Thought compression** — model becomes more token-efficient under response-length pressure (test-time scaling insight)
- **Parallel multi-agent inference** — Meta highlighted this as a way to improve performance at similar latency
- **Visual grounding** — unusually good at image-to-code and one-shot game generation

## Weaknesses

Weaker on longer-horizon agentic work than the very top proprietary coding/agent models (Terminal-Bench, SWE-Bench Pro gaps).

## See also
- [[Anthropic]]
- [[Google]]
- [[DeepSeek]]
