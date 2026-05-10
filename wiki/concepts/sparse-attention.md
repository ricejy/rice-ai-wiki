---
title: Sparse Attention
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [attention, inference, optimization]
sources: [attention-optimization-primer]
---

# Sparse Attention

## Definition

An attention mechanism that dynamically selects which tokens to attend to, rather than computing attention over the entire context. Sits between full attention (accurate but O(n²)) and sliding window (cheap but forgetful). The model learns or computes which parts of the context are most relevant to the current generation step.

## Why it matters

Standard attention is quadratic — doubling context length quadruples compute. Sliding window attention is linear but causes amnesia. Sparse attention offers approximately constant memory and compute as context grows, while retaining the ability to attend to any position in the context.

## Implementations

### DeepSeek Sparse Attention (DSA)
Used in [[DeepSeek]] V3.2+. Two-stage pipeline:
1. **Lightning indexer** — lightweight scan to identify the most relevant tokens
2. **Targeted attention** — full attention computed only on the selected subset

Result: attention cost stays roughly constant regardless of context length.

### IndexCache (Z.ai)
Upgrade to DSA that reuses indexed tokens across adjacent transformer layers. Reduces indexer compute by 75%, delivers 1.82x faster inference with negligible quality loss.

### Dynamic Memory Sparsification (DMS)
[[Nvidia]]'s approach. Can be retrofitted to existing models (no architecture change). Key innovation: **delayed eviction** — instead of dropping tokens immediately, tokens age out gracefully like garbage collection. The model extracts remaining value before purging. Up to 8x reasoning cost reduction on some models.

## Limitations

**Needle-in-a-haystack retrieval.** Sparse attention's primary weakness is tasks requiring retrieval of highly specific, isolated information from deep within the context. The indexer may not flag a single critical token buried among thousands of irrelevant ones. For these workloads, [[KV Cache]] compression (which preserves the full attention trace) is preferable.

## Comparison to KV cache compression

| Dimension | Sparse Attention | KV Cache Compression |
|-----------|-----------------|---------------------|
| Approach | Attend to fewer tokens | Attend to all tokens, compress storage |
| Memory scaling | ~Constant | Linear but compressed |
| Retrieval accuracy | Weaker on needles | Preserves full trace |
| Model modification | May require architecture changes (DSA) or retrofitting (DMS) | Typically model-agnostic (TurboQuant, KVTC) |
| Best for | Long-context reasoning | Massive-context retrieval |

These approaches are complementary — sparse attention can be combined with KV cache compression.

## See also
- [[KV Cache]]
- [[Quantization]]
- [[Agentic Systems]]
- [[DeepSeek]]
- [[Nvidia]]
