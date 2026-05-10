---
title: Quantization
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [inference, compression, optimization]
sources: [google-turboquant, attention-optimization-primer]
---

# Quantization

## Definition

Reducing the numerical precision of model parameters or intermediate computations (e.g., from 16-bit floats to 4-bit integers) to decrease memory usage and increase inference speed. A fundamental technique for making LLMs practical on limited hardware.

## Types

**Weight quantization** — compress model parameters for storage and loading. Common formats: Q4_K_M, Q5_K_S, GPTQ, AWQ. Widely supported in llama.cpp, vLLM, and other inference engines.

**Activation quantization** — compress intermediate computations during inference. Harder than weight quantization because activations have more dynamic range.

**[[KV Cache]] quantization** — compress the attention key-value cache specifically. A distinct problem from weight quantization because KV cache grows with sequence length. TurboQuant (ICLR 2026) achieves 3-bit KV cache with zero accuracy loss.

## Key tradeoff

Lower bit-width = less memory + faster inference, but potential accuracy degradation. The goal is to find the sweet spot where compression is aggressive but quality is preserved. TurboQuant's contribution is pushing this frontier significantly for KV cache — 6x compression with no measurable quality loss.

## Relevance to local inference

Quantization is what makes [[Local LLM Inference]] possible. A 32B parameter model at FP16 requires ~64GB; at Q4_K_M it fits in ~20GB. Combined with KV cache quantization (TurboQuant), even long-context inference becomes feasible on consumer hardware.

## Relationship to sparse attention

[[Quantization]] and [[Sparse Attention]] are complementary approaches to the same underlying problem — making long-context inference feasible. Quantization preserves the full attention trace but compresses the data; sparse attention reduces which tokens are attended to. The choice depends on workload: sparse attention for general long-context reasoning, compression for retrieval-heavy tasks where every token might matter. They can be combined.

## See also
- [[KV Cache]]
- [[Sparse Attention]]
- [[Local LLM Inference]]
