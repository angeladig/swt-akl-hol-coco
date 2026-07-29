# How I Start My Day with Snowflake CoWork

**Snowflake World Tour Auckland 2026 — Hands-on Lab**

| Duration | Audience | Level | Prerequisites |
|----------|----------|-------|---------------|
| 45–60 minutes | Business analysts, knowledge workers, decision-makers | L100 (Introductory) | A Snowflake account with CoWork enabled; no SQL or coding knowledge required |

---

## The Problem

Every morning, business leaders face the same friction: dashboards are stale, the analyst queue is days long, and decisions can't wait. You know the data exists — revenue by category, customer trends, supplier performance — but getting answers means filing a ticket, waiting for a query, and hoping the result matches your question.

**What if you could just ask?**

Snowflake CoWork is an AI-powered conversational agent that connects directly to your governed enterprise data. No SQL. No dashboards to build. No waiting. Just ask a question in plain language and get trusted, visualized answers — with the full governance and security your enterprise requires.

---

## Story Arc

| Beat | This Lab |
|------|----------|
| **Problem** | Business users are stuck between stale dashboards and multi-day analyst queues |
| **Traditional Failure** | Dashboards can't answer new questions; every ad-hoc request bottlenecks on a data team |
| **Why Snowflake** | One agent with full business context, automatic data understanding, day-one usefulness |
| **Platform Principles** | Governance travels with data · AI lives next to governed data · One agent, full context |
| **Hands-on** | Start a workday with CoWork — ask questions, visualize, research, act |
| **Operationalization** | Built-in RBAC, masking, and attribution — no parallel security stack to maintain |
| **Extension** | User Skills, MCP connectors (Slack/email), mobile access |
| **Takeaway** | You can independently get answers, generate reports, and act on insights — without code |

---

## Platform Principles

These are the enduring ideas you should carry forward:

- **Governance travels with the data, not the application.** CoWork inherits every row-access policy, column mask, and RBAC grant your admin already configured. There is no parallel security stack.
- **AI lives next to governed data.** Your questions are answered by an agent that queries your Snowflake tables directly — data never leaves the governed boundary.
- **One agent, full business context.** CoWork combines structured tables, unstructured documents, and external context in a single conversational experience. No tool-switching.

---

## Your Scenario

You are **Jordan Chen**, a **Regional Category Manager** at **Mosaic Retail**, a mid-to-large omnichannel retailer based in Auckland. You oversee the Home & Kitchen product category across ANZ.

It's Monday morning. You have a buyer meeting at 2pm, and you need to:
- Check how your category performed last week
- Understand why a key product line is underperforming
- Prepare a brief with supporting data for your buyer meeting
- Share your findings with your merchandise planning team

You're going to do all of this with CoWork — before your first coffee gets cold.

---

## Modules

| # | Module | What You'll Do | Time |
|---|--------|---------------|------|
| 01 | [Welcome & Getting Started](01_Welcome_And_Setup/README.md) | Log in, explore the CoWork interface, understand your data | ~10 min |
| 02 | [Ask Questions & Get Insights](02_Ask_Questions_Get_Insights/README.md) | Ask natural-language questions, get visualizations, explore Verified Answers | ~15 min |
| 03 | [Go Deeper with Deep Research](03_Deep_Research/README.md) | Run a multi-agent investigation, review a cited report, save artifacts | ~15 min |
| 04 | [Take Action & Extend](04_Take_Action/README.md) | Share insights via Slack/email, create a User Skill, explore mobile (bonus) | ~15 min |

**Total hands-on time: ~55 minutes**

---

## Key Capabilities Covered

| Capability | Where |
|------------|-------|
| Natural language Q&A over structured data | Module 02 |
| Dynamic visualizations (charts, tables) | Module 02 |
| Verified Answers (green shield trust signal) | Module 02 |
| Deep Research (multi-agent cited report) | Module 03 |
| Artifacts (save & revisit analyses) | Module 03 |
| MCP Connectors (Slack, email) | Module 04 |
| User Skills (reusable multi-step workflows) | Module 04 |
| CoWork Mobile (iOS) | Module 04 (bonus) |
| Built-in Governance (RBAC, masking, attribution) | Throughout |

---

## What You Will NOT Do

This lab is designed for business users. You will **not**:
- Write any SQL or code
- Set up data pipelines or semantic models
- Configure admin settings or security policies
- Install any software

Everything is pre-provisioned. You just need a browser and your login credentials.

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Snowflake account | Provided by your lab instructor (or use your own account with CoWork enabled) |
| Browser | Chrome, Edge, or Safari (latest version) |
| CoWork access | Your role must have access to at least one Cortex Agent |
| Data | Pre-provisioned retail dataset (Mosaic Retail) — or your organization's own data |

> **Lab instructor note:** If running this lab in a workshop setting, pre-provision accounts with CoWork access, a configured Cortex Agent connected to a retail semantic view, and ensure participants' roles have appropriate data access.

---

## Key Messaging

> "Two years of AI demos. Now for the hard part."
>
> The gap between AI that demos well and AI that deploys at enterprise scale is real. Snowflake CoWork closes that gap — one agent, full business context, day-one usefulness, built for how work actually happens, inheriting governance rather than rebuilding it.

**Customer proof:** Fanatics Betting & Gaming — 80% of their CX organization using CoWork weekly, saving 3+ hours per person per week, with 3 agents in production.

---

## File Structure

```
cowork-hol-auckland/
├── README.md                          ← You are here
├── 01_Welcome_And_Setup/README.md
├── 02_Ask_Questions_Get_Insights/README.md
├── 03_Deep_Research/README.md
├── 04_Take_Action/README.md
├── images/
└── assets/
```

---

## After the Lab

You've just experienced a new way of working with data. The tools you used today are available right now in your Snowflake account:

1. **Ask your admin** to enable CoWork and configure a Cortex Agent for your team's data
2. **Start with one question** — the one you'd normally email an analyst about
3. **Save what works** — pin useful conversations, create User Skills for repeated workflows
4. **Share with your team** — CoWork respects your existing RBAC, so everyone sees only what they should

---

*Built for Snowflake World Tour Auckland 2026*
