---
title: LangChain Deep Agents
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [agents, architecture, langchain]
author: LangChain
url: https://www.langchain.com/blog/deep-agents
published: 2026
---

# LangChain Deep Agents

## Summary

LangChain's analysis of what makes "deep agents" — systems like [[Claude Code]], OpenAI Deep Research, and Manus — qualitatively different from standard agent loops. The core algorithm (LLM iterating with tool calls) is the same; the differentiation is architectural.

## Four architectural pillars

### 1. Detailed system prompts
Deep agents use extensive system instructions with few-shot examples and tool usage guidance. [[Claude Code]]'s system prompt is notably long with behavioral examples. The prompting sophistication is a primary driver of agent depth.

### 2. Planning tools
Planning mechanisms implemented as no-operation tools. Claude Code's todo list "doesn't do anything — it's basically a no-op" but serves as a context engineering strategy to maintain focus during complex multi-step tasks. The plan exists in-context, not in code.

### 3. Sub-agents
Task decomposition through spawning dedicated agents for individual components. Provides context management and prompt shortcuts — each sub-agent gets a focused prompt rather than inheriting the full parent context.

### 4. File system access
Persistent storage for notes, intermediate results, and shared workspace. Addresses accumulated context management during extended operations. The file system becomes an external memory layer.

## Key insight

The difference between shallow and deep agents isn't the loop — it's the scaffolding. Planning tools, sub-agents, and file access are all forms of **context engineering**: managing what the LLM sees and remembers across long task horizons.

## Implementation

LangChain released `deepagents`, an open-source package implementing these patterns on LangGraph. Customizable components for system prompts, planning tools, sub-agent spawning, and a virtual file system.

## Relevance to wiki

Extends [[Agent Design Patterns]] beyond the 7-level complexity ladder. Deep agents aren't a new level — they're a set of architectural investments that make level-7 autonomous agents actually work in practice. The four pillars map directly to known challenges: context window limits (file system), task tracking (planning tools), prompt complexity (detailed system prompts), and scope management (sub-agents).

## See also
- [[Agent Design Patterns]]
- [[Claude Code]]
- [[Agentic Systems]]
- [[Agent Memory]]
