---
title: "Claude Code Auto Mode: A Safer Way to Skip Permissions"
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [agent-safety, guardrails, claude-code, prompt-injection, permissions]
author: John Hughes
published: 2026-03-25
url: https://www.anthropic.com/engineering/claude-code-auto-mode
---

# Claude Code Auto Mode: A Safer Way to Skip Permissions

## Summary

Anthropic introduced auto mode for [[Claude Code]] to address approval fatigue — users approve 93% of permission prompts, meaning the safety mechanism degrades into rubber-stamping. Auto mode replaces manual approval with a [[Model-Based Guardrail]] system: two model-based classifiers that automatically approve low-risk actions while blocking dangerous ones.

## Architecture

Two defensive layers:

**Input layer — Prompt Injection Probe**
A server-side classifier scans tool outputs before they enter the agent's context. When hostile content is detected, a warning is injected telling the agent to treat the content as suspect.

**Output layer — Transcript Classifier**
Runs on [[Sonnet 4.6]]. Evaluates each proposed action in two stages:
- **Stage 1:** Fast single-token yes/no filter. Conservative — 8.5% false positive rate, but catches most dangerous actions.
- **Stage 2:** Chain-of-thought reasoning, triggered only when stage 1 flags. Reduces false positives to 0.4%.

Critical design choice: the classifier sees only user messages and tool call commands. Claude's own messages and tool outputs are stripped. This prevents self-persuasion (the agent talking the classifier into approving) and blocks [[Prompt Injection]] via tool results in a single architectural decision.

## Permission tiers

| Tier | Scope | Review |
|------|-------|--------|
| 1 | Safe-tool allowlist (reads, search, navigation) | Auto-approved |
| 2 | File edits within project directory | Auto-approved (git-reviewable) |
| 3 | Shell commands, web fetches, external tools, out-of-project filesystem | Transcript classifier |

## Threat model

Four categories of risky behavior:
1. **Overeager behavior** — agent understands goals but takes unauthorized initiative (e.g., accessing found credentials, deleting perceived obstacles)
2. **Honest mistakes** — agent misunderstands scope (e.g., treating shared resources as test-scoped)
3. **[[Prompt Injection]]** — malicious instructions in files or web content redirect the agent
4. **Model misalignment** — agent pursues own goals (not observed in practice)

## Real-world blocks

- User says "clean up old branches" → agent tries to batch-delete remote branches → blocked
- Agent hits auth error → systematically searches env vars for API tokens → blocked
- Agent creates a GitHub Gist to share a debugging script without consent → blocked
- Deploy fails pre-check → agent retries with `--skip-verification` → blocked

## Deny-and-continue

When blocked, the agent receives the denial as a tool result with instructions to find a safer approach. Sessions accumulating 3 consecutive denials or 20 total escalate to human review (or terminate in headless mode). This makes false positives survivable without killing sessions.

## Performance

| Dataset | Final FPR | Final FNR |
|---------|-----------|-----------|
| Real traffic (n=10,000) | 0.4% | — |
| Real overeager actions (n=52) | — | 17% |
| Synthetic exfiltration (n=1,000) | — | 5.7% |

The 17% FNR on overeager actions is acknowledged openly — these are cases where the classifier identifies danger but misjudges whether user consent covers the blast radius.

## Design insights

- Stripping assistant text from the classifier's input is a dual-purpose defense: prevents self-persuasion *and* prompt injection.
- Two-stage classification breaks the efficiency/accuracy tradeoff. Stage 2 shares cache with stage 1, keeping costs low.
- The prompt injection probe and transcript classifier require attacks to evade both layers independently — compounding difficulty.
- For multi-agent setups, the classifier operates at both delegation and return boundaries.

## Relevance

The [[Model-Based Guardrail]] pattern — using a classifier model to gate another model's actions — is a general technique applicable beyond CLI tools. The deny-and-continue strategy is particularly notable for reducing automation friction in [[Agentic Systems]].

## See also
- [[Model-Based Guardrail]]
- [[Prompt Injection]]
- [[Agentic Systems]]
- [[Claude Code]]
- [[Anthropic]]
