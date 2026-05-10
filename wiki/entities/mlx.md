---
title: MLX
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [apple-silicon, frameworks, inference]
sources: [google-turboquant, telegram-impt-ai-news-digest]
---

# MLX

## Overview

Apple's machine learning framework optimized for Apple Silicon (M-series chips). Designed for on-device inference and training, leveraging Metal for GPU acceleration and unified memory architecture.

A key enabler of [[Local LLM Inference]] on Mac hardware. Community ports of techniques like TurboQuant ([[Google]]) to MLX have enabled running models like Qwen2.5-32B on a 16GB MacBook Air — compressing both weights and [[KV Cache]] natively in the framework.

## Ecosystem

- **[[Rapid-MLX]]** — inference engine built on MLX, claiming 4.2x faster than Ollama. Supports tool calling, multimodal, continuous batching, and OpenAI-compatible API.
- **Gemma 4 E2B** — [[Google]]'s on-device model running at ~40 tokens/sec on iPhone 17 Pro via MLX

## See also
- [[Local LLM Inference]]
- [[KV Cache]]
- [[Quantization]]
- [[Rapid-MLX]]
