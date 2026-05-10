---
title: "MemPalace"
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [memory, retrieval, local, tools]
source-type: screenshot
---

# MemPalace

## Summary

An open-source memory layer for LLMs that stores full conversations locally and retrieves them using a structured "palace" hierarchy rather than summaries. Addresses the problem that past chats, decisions, and debugging steps disappear after each session.

## Key insight: structure over summaries

MemPalace rejects context summarization — the approach where past interactions are condensed into shorter text, losing fine-grained information. Instead, it stores **full conversations** and organizes them into a navigable structure, using semantic search only after narrowing scope via the hierarchy.

This directly addresses the failure mode documented in the attention optimization primer: context summarization deleting important instructions, causing agents to do things they were told not to do.

## Architecture

**Palace structure:**
- **Wings** — projects (top-level organizational unit)
- **Rooms** — topics within a project
- **Halls** — types of content within a topic

Search flow: narrow by structure first (wing → room), then run semantic search within that scope. This avoids the noise of searching the entire memory space.

**Local stack:**
- SQLite + ChromaDB
- No API key required
- AAAK compression: ~30x smaller context, still readable by any LLM
- Knowledge graph tracks facts and flags contradictions

## Performance

| Benchmark | Mode | Score | API Calls |
|-----------|------|-------|-----------|
| LongMemEval R@5 | Raw (ChromaDB only) | 96.6% | Zero |
| LongMemEval R@5 | Hybrid + Haiku rerank | 100% (500/500) | ~500 |
| LoCoMo R@10 | Raw, session level | 60.3% | Zero |
| Personal palace R@10 | Heuristic bench | 85% | Zero |
| Palace structure impact | Wing+room filtering | +34% R@10 | Zero |

The +34% improvement from structure filtering is the key result — it validates the "narrow by structure, then search" approach over flat semantic search.

## Usage

```
pip install mempalace
mempalace init
mempalace mine <dir>        # ingest chats or code
mempalace search "query"    # query memory
```

Connects to agents via MCP or by injecting results into prompts manually.

## Relevance

MemPalace represents a different approach to the [[Agent Memory]] problem than [[KV Cache]] optimization. KV cache techniques address within-session memory (keeping more context in the active window). MemPalace addresses across-session memory (persisting and retrieving knowledge between conversations). Both are needed for truly continuous [[Agentic Systems]].

The palace structure (wings → rooms → halls) is conceptually similar to this wiki's own structure (sources → concepts → entities). Both use hierarchical organization to make retrieval tractable at scale.

## See also
- [[Agent Memory]]
- [[Agentic Systems]]
- [[Local LLM Inference]]
- [[Model Context Protocol]]
