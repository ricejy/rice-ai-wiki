---
title: Google
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [companies, ai-labs]
sources: [google-turboquant, agent-payments-protocol, telegram-impt-ai-news-digest]
---

# Google

## Overview

Major AI research lab and cloud provider. Develops the Gemini model family and publishes foundational research across ML infrastructure, optimization, and model architecture.

## Key contributions (in wiki)

**Inference optimization:**
- **TurboQuant** (ICLR 2026) — training-free [[KV Cache]] [[Quantization]] achieving 6x compression with zero accuracy loss
- **PolarQuant** (AISTATS 2026) — polar coordinate-based vector quantization, a component of TurboQuant

**Models:**
- **Gemma 4 E2B** — on-device model running at ~40 tokens/sec on iPhone 17 Pro via [[MLX]]. Built from same research as Gemini 3. Image understanding + reasoning capable.
- **Gemini Nano** — on-device model shipped inside Chrome via the Prompt API (controversial — opposed by Mozilla, WebKit, W3C TAG, Microsoft)

**Agent protocols:**
- **[[A2A Protocol]]** (Agent-to-Agent) — open protocol for agent discovery and collaboration
- **AP2** (Agent Payments Protocol) — open protocol for [[Agent Commerce]], extends A2A. Donated to FIDO Alliance
- **ADK** (Agent Development Kit) — agent framework

## See also
- [[Anthropic]]
- [[Agent Commerce]]
- [[Agent Interoperability]]
- [[Local LLM Inference]]
- [[Quantization]]
- [[KV Cache]]
