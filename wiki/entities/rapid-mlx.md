---
title: Rapid-MLX
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [inference, apple-silicon, local]
sources: [telegram-impt-ai-news-digest]
---

# Rapid-MLX

## Overview

Open-source local inference engine for Apple Silicon, claiming 4.2x faster performance than Ollama. Built on Apple's [[MLX]] framework with native Metal compute kernels. Drop-in replacement for OpenAI's API.

## Performance

- 160 tokens/sec on lightweight models, 31+ tokens/sec on frontier-scale models
- Cached time-to-first-token as low as 0.08s via prompt caching
- Continuous batching for concurrent requests

## Key features

- **Tool calling** — 17 tool-call parsers with automatic recovery for malformed output from quantized models. 100% tool calling accuracy on supported model families.
- **Reasoning separation** — isolates chain-of-thought from responses
- **Multimodal** — vision, audio, and video understanding
- **Smart cloud routing** — offloads to cloud when local inference would be slow
- **OpenAI-compatible API** — works with Cursor, [[Claude Code]], PydanticAI, LangChain, Aider, Anthropic SDK

## Why it matters

Demonstrates that [[Local LLM Inference]] on Apple Silicon is reaching practical performance levels for agentic workflows — tool calling, multimodal, and continuous batching were previously cloud-only capabilities.

## See also
- [[MLX]]
- [[Local LLM Inference]]
- [[Quantization]]
