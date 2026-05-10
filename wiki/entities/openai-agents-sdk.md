---
title: OpenAI Agents SDK
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [openai, agents, sdk, frameworks]
sources: [telegram-impt-ai-news-digest]
---

# OpenAI Agents SDK

## Overview

OpenAI's SDK for building production-grade agents. Major update in April 2026 introduced a model-native harness — running agents in a way that matches how models naturally use tools and context.

## Architecture

**Agent loop:** Receive request → Route to model → Call tools → Update context → Generate response

**Built-in tools:**
- File system (read, write, edit across project directories)
- Shell (commands inside sandbox)
- [[Model Context Protocol]] (structured tool use for external APIs)
- Code interpreter
- Skills (gradual tool exposure rather than full access at once)
- Remote MCP
- Web search, file search

**Key components (handled by SDK):**
- Message handling
- Model interface
- Tool manager
- Context management

## Notable features

- **AGENTS.md** — persistent instructions guiding agent behavior (analogous to CLAUDE.md in [[Claude Code]])
- **Sandbox execution** — safe code/file access with credential isolation
- **Manifest system** — describes inputs, outputs, and directory structure per run
- **Cloud storage** — supports S3, GCS
- **Provider-agnostic deployment** — Cloudflare, Vercel, or custom environments

## Comparison to Anthropic's approach

| Feature | OpenAI Agents SDK | [[Claude Agent SDK]] |
|---------|------------------|---------------------|
| Agent instructions | AGENTS.md | CLAUDE.md |
| Tool protocol | MCP + built-in | MCP |
| Sandbox | Built-in | Platform-dependent |
| Philosophy | SDK-first, structured harness | "Start with raw API calls" |

## See also
- [[Claude Agent SDK]]
- [[Agent Design Patterns]]
- [[Model Context Protocol]]
- [[Agentic Systems]]
