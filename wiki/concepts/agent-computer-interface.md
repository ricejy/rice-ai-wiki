---
title: Agent-Computer Interface
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [tooling, agents, design]
sources: [building-effective-agents]
---

# Agent-Computer Interface

## Definition

The design of tools and APIs as they are presented to an LLM agent. Analogous to UI/UX design for humans — the interface between the agent and the systems it operates on. A term from [[Anthropic]]'s "Building Effective Agents" article.

## Why it matters

Tool design is a first-class concern in [[Agentic Systems]], not an afterthought. Poor tool interfaces cause agent failures that no amount of prompt engineering can fix. Teams underinvest here relative to the impact it has.

## Design principles

**Natural formats.** Use formats close to what the model saw in training data. Don't invent custom schemas when JSON, markdown, or plain text work.

**Eliminate formatting overhead.** Don't require the model to count lines, track indices, or maintain state across calls. If the tool can handle that, it should.

**Poka-yoke (mistake-proofing).** Design tools so entire classes of errors are structurally impossible. Example from SWE-bench: requiring absolute filepaths instead of relative ones eliminated path resolution mistakes entirely.

**Sufficient thinking space.** Give the model enough token budget to reason before committing to a tool call.

**Clear boundaries.** Document what the tool does, what it doesn't do, edge cases, and example usage. The model's tool documentation is its "manual" — it needs to be good.

## Examples

| Problem | Bad design | Good design |
|---------|-----------|-------------|
| File paths | Relative paths after `cd` | Absolute paths always |
| Code edits | Line-number-based replacement | Content-based search-and-replace |
| Output format | Custom DSL | Standard markdown/JSON |
| Error handling | Silent failure | Descriptive error messages |

## See also
- [[Agent Design Patterns]]
- [[Agentic Systems]]
- [[Claude Code]]
- [[Scrapling]]
