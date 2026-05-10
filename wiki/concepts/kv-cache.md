---
title: KV Cache
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [inference, memory, architecture]
sources: [google-turboquant, attention-optimization-primer]
---

# KV Cache

## Definition

The key-value cache stores precomputed attention keys and values from previous tokens during autoregressive LLM inference. Instead of recomputing attention over the entire sequence at each step, the model caches K and V tensors and only computes the new token's contribution. This is essential for efficient inference but creates a memory bottleneck.

## Why it matters

KV cache size grows linearly with sequence length and batch size. For long-context models (100K+ tokens), the KV cache can consume more memory than the model weights themselves. This is the primary constraint on:
- Maximum context length in practice
- Batch size (throughput)
- Running large models on consumer hardware ([[Local LLM Inference]])

## Impact on inference stages

The KV cache bottleneck manifests differently in the two stages of LLM inference:

- **Prefill** — ingesting the prompt. Large prompts require enormous immediate compute and memory, increasing time-to-first-token (TTFT).
- **Decode** — generating tokens. KV cache size constrains memory bandwidth, capping tokens-per-second.

For [[Agentic Systems]] handling entire repositories or multi-day conversations, the KV cache can exhaust GPU memory entirely, breaking the workflow.

## Compression approaches

**[[Quantization]]** — reduce precision of cached values:
- KIVI (ICML 2024): ~2.6x compression, asymmetric per-channel/per-token
- TurboQuant ([[Google]], ICLR 2026): 6x compression, 3 bits per value, training-free, zero accuracy loss

**Transform coding** — apply mathematical compression (PCA, dimensionality reduction):
- KVTC ([[Nvidia]]): up to 20x memory reduction, 8x TTFT improvement. PCA-based, analogous to JPEG compression. Model-agnostic, no retraining.

**Eviction / [[Sparse Attention]]** — selectively discard or skip less important cache entries:
- StreamingLLM, H2O — eviction heuristics
- Dynamic Memory Sparsification ([[Nvidia]]) — delayed eviction with graceful aging

**Architectural** — reduce KV cache size by design:
- Multi-Query Attention (MQA): share K and V heads across query heads
- Grouped-Query Attention (GQA): compromise between MHA and MQA

## Choosing an approach

| Workload | Best approach | Why |
|----------|--------------|-----|
| Short context | No optimization needed | Full attention is fine |
| Long-context reasoning | [[Sparse Attention]] | Constant memory, good general recall |
| Massive-context retrieval | KV cache compression (TurboQuant, KVTC) | Preserves complete attention trace |

## Practical tip

From TurboQuant community testing: compressing K and V asymmetrically works better than uniform compression. Specifically, q8_0 for keys + 3-bit TurboQuant for values outperforms compressing both equally. Keys appear more sensitive to quantization than values.

## See also
- [[Sparse Attention]]
- [[Quantization]]
- [[Local LLM Inference]]
- [[Agentic Systems]]
