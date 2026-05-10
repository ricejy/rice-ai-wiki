---
title: Local LLM Inference
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [inference, local, hardware, apple-silicon]
sources: [google-turboquant, attention-optimization-primer, telegram-impt-ai-news-digest]
---

# Local LLM Inference

## Definition

Running LLM inference on consumer hardware (laptops, desktops, single GPUs) rather than cloud infrastructure. Enabled by [[Quantization]] techniques that compress models to fit in limited memory.

## Why it matters

- **Privacy** — data never leaves the device
- **Cost** — no API fees, no per-token charges
- **Latency** — no network round-trip
- **Availability** — works offline
- **Experimentation** — iterate freely without usage concerns

## Key constraints

| Resource | Constraint | Mitigation |
|----------|-----------|------------|
| Memory | Model + KV cache must fit in RAM/VRAM | Weight [[Quantization]], [[KV Cache]] compression |
| Compute | Consumer GPUs/CPUs are slower than data center hardware | Smaller models, speculative decoding |
| Context length | Long contexts inflate [[KV Cache]] | KV cache quantization (TurboQuant), [[Sparse Attention]] |

## Apple Silicon as a platform

Apple Silicon (M-series) has become a popular platform for local inference due to unified memory (CPU and GPU share RAM). Key tooling:
- **[[MLX]]** — Apple's ML framework optimized for Metal
- **[[Rapid-MLX]]** — inference engine on MLX, 4.2x faster than Ollama. 160 tok/s on light models, tool calling, multimodal, OpenAI-compatible API.
- **llama.cpp** — cross-platform inference engine with Metal support

TurboQuant on Apple Silicon: community ports enable Qwen2.5-32B on a 16GB MacBook Air by compressing both weights (Q4_K_M) and KV cache (3-bit TurboQuant). This was previously impossible — the KV cache alone would exceed memory on long contexts.

## See also
- [[Quantization]]
- [[KV Cache]]
- [[Sparse Attention]]
