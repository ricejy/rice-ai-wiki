---
title: "Agents for Financial Services"
type: source
created: 2026-05-10
updated: 2026-05-10
tags: [agents, enterprise, finance, anthropic]
author: Anthropic
published: 2026-05-05
url: https://www.anthropic.com/news/finance-agents
---

# Agents for Financial Services

## Summary

[[Anthropic]] released ten ready-to-run agent templates for financial services, alongside Microsoft 365 integrations and an expanded data connector ecosystem. This is a significant enterprise push — moving from "build your own agent" to "deploy a pre-built agent on real financial work in days."

## Agent templates

Each template packages three things:
- **Skills** — instructions and domain knowledge for the task
- **Connectors** — governed access to data sources
- **Subagents** — additional Claude models for specific subtasks (e.g., comparables selection, methodology checks)

This is the [[Agent Design Patterns]] orchestrator-workers pattern (level 5) shipped as a product.

### Research and client coverage
- **Pitch builder** — target lists, comps, pitchbook drafts
- **Meeting preparer** — client and counterparty briefs
- **Earnings reviewer** — transcript/filing analysis, model updates, thesis-relevant flags
- **Model builder** — financial models from filings and data feeds
- **Market researcher** — sector tracking, news/filing synthesis, credit/risk flagging

### Finance and operations
- **Valuation reviewer** — checks against comps, methodology, firm standards
- **General ledger reconciler** — GL reconciliation, NAV calculations
- **Month-end closer** — close checklist, journal entries, close reports
- **Statement auditor** — consistency, completeness, audit-readiness
- **KYC screener** — entity files, source document review, compliance escalation

## Two deployment modes

**Plugin (Claude Cowork / Claude Code)** — runs alongside the analyst, interactive. Uses desktop software (Excel, PowerPoint, Outlook). Human stays in the loop.

**[[Claude Managed Agents]]** — runs autonomously on the Claude Platform. For batch work (whole book of deals, nightly schedules). Features: long-running sessions (multi-hour), per-tool permissions, managed credential vaults, full audit log. Compliance teams can inspect every tool call and decision.

Both modes keep humans in the loop for review and approval before output goes to clients or gets filed.

## Microsoft 365 integration

Claude add-ins for Excel, PowerPoint, Word, and Outlook (coming soon). Key capability: **context carries between applications** — work started in Excel doesn't need re-explanation when moving to PowerPoint. In Cowork, [[Dispatch]] lets users assign tasks by text or voice from anywhere.

## Data ecosystem

Connectors to: FactSet, S&P Capital IQ, MSCI, PitchBook, Morningstar, Chronograph, LSEG, Daloopa, plus firms' own data warehouses and CRMs.

New connectors: Dun & Bradstreet, Fiscal AI, Financial Modeling Prep, Guidepoint, IBISWorld, SS&C Intralinks, Third Bridge, Verisk.

**Moody's MCP app** — [[Model Context Protocol]] integration bringing proprietary credit ratings and data on 600M+ entities directly into Claude. MCP apps go beyond connectors by embedding the provider's own tools inside Claude.

## Performance

Claude Opus 4.7 leads the Vals AI Finance Agent benchmark at 64.37%.

## Relevance

This is [[Anthropic]]'s most concrete enterprise agent deployment. The template architecture (skills + connectors + subagents) is a productized version of the orchestrator-workers pattern from [[Agent Design Patterns]]. The managed agents platform with audit logging addresses the trust and compliance requirements that [[Model-Based Guardrail]] systems handle at the technical level.

## See also
- [[Agentic Systems]]
- [[Agent Design Patterns]]
- [[Model Context Protocol]]
- [[Anthropic]]
- [[Claude Managed Agents]]
