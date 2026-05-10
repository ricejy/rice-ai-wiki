---
title: Prompt Injection
type: concept
created: 2026-05-10
updated: 2026-05-10
tags: [agent-safety, adversarial, attacks]
sources: [claude-code-auto-mode]
---

# Prompt Injection

## Definition

An attack where malicious instructions are embedded in content that an LLM processes (files, web pages, tool outputs), causing the model to deviate from its intended behavior. Analogous to SQL injection — untrusted data is interpreted as instructions.

## Relevance to agentic systems

Prompt injection is especially dangerous in [[Agentic Systems]] where models take real-world actions (executing code, making API calls, modifying files). A successful injection can redirect the agent to exfiltrate data, modify code maliciously, or bypass security controls.

## Defenses

**Structural isolation.** Separate the classifier/guardrail from the content channel. In [[Claude Code]] auto mode, the transcript classifier never sees tool outputs — the primary vector for injected content. This is a design-level defense rather than a content-filtering one.

**Input-layer probing.** A dedicated classifier scans tool outputs before they enter the agent's context, flagging hostile content with warnings. This catches injections at the agent level even if the guardrail layer uses structural isolation.

**Layered defense.** Requiring an attack to evade multiple independent layers (e.g., both an input probe and a structurally isolated classifier) compounds the difficulty multiplicatively.

## Open questions

- Can models reliably distinguish instructions from data in adversarial settings, or is structural isolation the only robust defense?
- How do multi-turn prompt injections (gradual context poisoning) interact with guardrail systems?

## See also
- [[Model-Based Guardrail]]
- [[Agentic Systems]]
