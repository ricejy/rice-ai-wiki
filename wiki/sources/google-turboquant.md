---
title: "TurboQuant: Redefining AI Efficiency with Extreme Compression"
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [quantization, inference, kv-cache, local-llm, apple-silicon]
author: Amir Zandieh, Vahab Mirrokni
published: 2026-03-24
url: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
paper: https://arxiv.org/abs/2504.19874
venue: ICLR 2026
---

# TurboQuant: Redefining AI Efficiency with Extreme Compression

## Summary

[[Google]] Research introduced TurboQuant, a training-free, data-oblivious vector quantization algorithm that compresses the [[KV Cache]] of LLMs to 3 bits per value — achieving 6x memory reduction and up to 8x attention speedup with zero accuracy loss. Presented at ICLR 2026.

This is not weight quantization — it specifically targets the KV cache, which grows linearly with sequence length and is a major bottleneck for long-context inference.

## How it works

Two-stage pipeline:

### Stage 1 — PolarQuant
- Applies random vector rotation to the cache vectors
- Converts Cartesian coordinates to polar coordinates (radius = strength, angle = meaning)
- Quantizes each part individually on a fixed circular grid
- Eliminates traditional normalization overhead
- Presented separately at AISTATS 2026

### Stage 2 — QJL (Quantized Johnson-Lindenstrauss)
- 1-bit residual compression on the quantization error from stage 1
- Reduces each residual number to a sign bit (+1 or −1)
- Preserves essential distances and relationships between data points
- Near-zero memory overhead for this correction step

Key property: the entire pipeline is **training-free and data-oblivious** — no calibration data, no fine-tuning, works out of the box on any model.

## Performance

| Metric | Result |
|--------|--------|
| KV cache compression | 3 bits per value |
| Memory reduction | ≥6x |
| Attention speedup (H100) | Up to 8x vs. 32-bit |
| Accuracy loss | Zero (on tested benchmarks) |

Benchmarks: LongBench, Needle In A Haystack, ZeroSCROLLS, RULER, L-Eval
Models tested: Gemma, Mistral

Compared to prior art (KIVI, ICML 2024): KIVI achieved ~2.6x compression with asymmetric per-channel/per-token quantization. TurboQuant more than doubles this.

## Local LLM impact

The Reddit/community discussion highlights the practical impact for [[Local LLM Inference]]:

- Community ports to [[MLX]] on Apple Silicon enable running Qwen2.5-32B on a **16GB MacBook Air** — both model weights and KV cache fit in memory
- Validated on Metal (Apple Silicon): 3.125 bits/val, 5.12x compression, identical perplexity
- Practical configuration tip: **q8_0 for keys + TurboQuant 3-bit for values** outperforms symmetric compression (compressing both K and V equally)
- Multiple open-source implementations: llama.cpp integration (discussion #20969), MLX ports, Triton kernels + vLLM integration

## Also applicable to vector search

Beyond LLM inference, TurboQuant achieves superior recall on vector search benchmarks (GloVe dataset) vs. Product Quantization and RabbitQ baselines. Relevant for embedding-based retrieval systems.

## Related papers

1. TurboQuant — arxiv.org/abs/2504.19874 (ICLR 2026)
2. PolarQuant — arxiv.org/abs/2502.02617 (AISTATS 2026)
3. QJL — dl.acm.org/doi/10.1609/aaai.v39i24.34773

## See also
- [[Attention Optimization Primer]] — broader context on KV cache compression vs. sparse attention
- [[KV Cache]]
- [[Quantization]]
- [[Local LLM Inference]]
- [[MLX]]
- [[Google]]
