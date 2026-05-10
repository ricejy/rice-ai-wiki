---
title: Claude Code
type: entity
created: 2026-05-10
updated: 2026-05-10
tags: [anthropic, tools, agents, cli]
sources: [claude-code-auto-mode, building-effective-agents, telegram-impt-ai-news-digest]
---

# Claude Code

## Overview

[[Anthropic]]'s agentic coding tool — a CLI (and IDE extension) where Claude operates as an autonomous software engineering agent. It reads files, writes code, runs commands, searches the web, and manages git workflows.

## Auto mode

Introduced March 2026. Replaces the manual permission prompt system with a [[Model-Based Guardrail]] — two model-based classifiers that auto-approve low-risk actions and block dangerous ones. Key stats:
- 93% of permission prompts were being approved → approval fatigue
- 0.4% false positive rate on real traffic after two-stage classification
- 17% false negative rate on real overeager actions (acknowledged openly)

Three permission tiers: safe-tool allowlist → in-project edits → transcript classifier.

Uses a deny-and-continue strategy: blocked actions produce feedback, not session termination.

## /autofix-pr

New feature (April 2026): after finishing a PR, run `/autofix-pr` to send the session to the cloud. The PR autofixer monitors CI failures and review comments, investigates issues, and pushes fixes directly to the PR branch — all with full context from the original session.

## Design philosophy

Embodies [[Anthropic]]'s "Building Effective Agents" principles: composable tool calls over complex planning architectures, transparency in reasoning steps, and strong [[Agent-Computer Interface]] design (e.g., absolute filepaths, content-based edits). Sits at level 7 (autonomous agent) on the [[Agent Design Patterns]] complexity ladder but internally uses simpler patterns like prompt chaining and routing.

## See also
- [[Anthropic]]
- [[Agent Design Patterns]]
- [[Agent-Computer Interface]]
- [[Model-Based Guardrail]]
- [[Agentic Systems]]
