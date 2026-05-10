---
title: Agent Memory
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agents, memory, retrieval, context]
sources: [mempalace, attention-optimization-primer, telegram-impt-ai-news-digest, langchain-deep-agents]
---

# Agent Memory

## Definition

How [[Agentic Systems]] persist and retrieve knowledge — both within a single session (working memory) and across sessions (long-term memory). A fundamental challenge: agents that forget between sessions can't compound knowledge, and agents that lose context within sessions make errors.

## Two distinct problems

### Within-session memory (working memory)

The [[KV Cache]] holds attention state for the current session. As context grows, the cache exhausts memory. Mitigations:
- [[Quantization]] — compress cache data (TurboQuant: 6x reduction)
- [[Sparse Attention]] — attend selectively (DeepSeek DSA, Nvidia DMS)
- Context summarization — condense past interactions (lossy — documented failure mode where summarization deletes critical instructions)
- Sliding window — drop oldest tokens (causes amnesia)

See [[Inference Costs for Agentic Workflows]] for detailed analysis.

### Across-session memory (long-term memory)

Knowledge from past conversations must be stored and retrieved for future sessions. Approaches:

**Flat retrieval (RAG):** Embed past interactions, retrieve by similarity. Simple but noisy — no structure to guide search. [[PageIndex]] takes a different approach: vectorless RAG using hierarchical tree indexes navigated by LLM reasoning instead of embedding similarity.

**Structured memory (MemPalace):** Organize memories hierarchically (wings → rooms → halls), search within structure. +34% retrieval improvement from structure filtering alone. Stores full conversations, not summaries. Local stack (SQLite + ChromaDB), 100% on LongMemEval.

**Wiki/knowledge base (this project):** Incrementally build structured, interlinked pages from sources. The LLM synthesizes and cross-references — knowledge is compiled once and kept current, not re-derived per query.

### Memory consolidation (emerging idea)

Most agent memory systems freeze the base model entirely — memory is always retrieved, never internalized. A paper argues this caps performance: at some point, patterns from long-term memory should become cheap, internalized capabilities via periodic, low-frequency fine-tuning from accumulated agent memory. This requires continual-learning safeguards to avoid catastrophic forgetting. Most teams are not doing this today, but it's the logical next step: retrieval for rare knowledge, internalization for frequent patterns.

### File system as external memory

The [[LangChain Deep Agents]] analysis identifies file system access as one of four architectural pillars of production autonomous agents. Agents write notes, intermediate results, and plans to persistent storage — offloading context that doesn't fit in the working window. This is a pragmatic middle ground between in-context memory and structured retrieval: cheaper than retrieval, more durable than context.

## Key tradeoff: summaries vs. full storage

Context summarization is tempting because it's cheap, but it's lossy. Documented failure: summarization deleted important instructions, causing the agent to perform forbidden actions. Full storage preserves information but requires better retrieval to remain tractable.

MemPalace and wiki-based approaches both avoid summarization loss by preserving complete information and using structure (hierarchy or wikilinks) to make retrieval efficient.

## See also
- [[KV Cache]]
- [[Agentic Systems]]
- [[Sparse Attention]]
- [[Local LLM Inference]]
- [[PageIndex]]
