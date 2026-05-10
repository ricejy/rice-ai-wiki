---
title: PageIndex
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [rag, retrieval, search]
sources: [telegram-impt-ai-news-digest]
---

# PageIndex

## Overview

Open-source retrieval system that replaces vector databases with hierarchical tree indexes navigated by LLM reasoning. Built by VectifyAI. Powers Mafin 2.5 (98.7% accuracy on FinanceBench).

## Architecture

Two-phase approach:

1. **Indexing** — documents are transformed into semantic tree structures resembling tables of contents, preserving natural section hierarchy instead of fragmenting into artificial chunks
2. **Retrieval** — LLMs traverse the tree through reasoned queries, selecting relevant sections based on context rather than similarity scores

## Key differentiators from vector RAG

| Dimension | Vector RAG | PageIndex |
|-----------|-----------|-----------|
| Index type | Embedding vectors | Semantic tree |
| Retrieval | Cosine similarity | LLM reasoning |
| Document structure | Destroyed (chunked) | Preserved (hierarchical) |
| Interpretability | Opaque similarity scores | Logical section references |
| Context-adaptive | No (static embeddings) | Yes (conversation history informs search) |

## Best for

Professional documents with strong structure: financial reports, regulatory filings, academic papers, legal documents, technical manuals. Less suited for unstructured content where hierarchy isn't natural.

## See also
- [[Agent Memory]]
- [[Agentic Systems]]
