# How I Start My Day with Snowflake CoWork

**Snowflake World Tour Auckland 2026 — Hands-on Lab**

> **Context:** Part of the **Mosaic Retail CoWork Lab (L100)** — A business user's first morning with conversational AI on governed enterprise data.
> **Goal:** Go from "revenue is down" to a cited report, two decisions, and a shared meeting brief — without writing SQL or filing a ticket.
> **Estimated Completion Time:** 45-60 minutes

| Duration | Audience | Level | Prerequisites |
|----------|----------|-------|---------------|
| 45-60 minutes | Business analysts, knowledge workers, decision-makers | L100 (Introductory) | A Snowflake account with CoWork enabled; no SQL or coding knowledge required |

---

## Story Arc

| Beat | This Lab |
|------|----------|
| **Problem** | Business users are stuck between stale dashboards and multi-day analyst queues |
| **Traditional Failure** | Dashboards can't answer new questions; every ad-hoc request bottlenecks on a data team |
| **Why Snowflake** | One agent with full business context, automatic data understanding, day-one usefulness — all within the governed boundary |
| **Platform Principles** | Governance travels with data · AI lives next to governed data · One agent, full context |
| **Hands-on** | Start a workday with CoWork — ask questions, visualize, research, act |
| **Operationalization** | Built-in RBAC, row access policies, attribution — no parallel security stack to maintain |
| **Extension** | User Skills, MCP connectors (Slack/email), mobile access |
| **Customer Takeaway** | You can independently get answers, generate reports, and act on insights — without code, without waiting, without leaving the governed boundary |

---

## The Problem

> **Business Context:** Every Monday morning, business leaders face the same friction: dashboards are stale, the analyst queue is days long, and decisions can't wait. You know the data exists — revenue by category, supplier performance, product trends — but getting answers means filing a ticket, waiting for a query, and hoping the result matches your question.

In the old world, a category manager's Monday morning looks like this:
- Check a static dashboard (limited view, can't answer new questions)
- Email the analytics team with follow-up questions (2-3 days wait)
- Schedule a meeting to clarify what you actually wanted
- Wait for the revised analysis
- Scramble to prep for your buyer meeting

**What if you could just ask?**

Snowflake CoWork is an AI-powered conversational agent that connects directly to your governed enterprise data. No SQL. No dashboards to build. No waiting. Just ask a question in plain language and get trusted, visualized answers — with the full governance and security your enterprise requires.

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

## Getting Started (~5 min)

> **Business Context:** In the traditional workflow, before Jordan can even ask a question, they need to log in to a BI tool, find the right dashboard, check if data is refreshed, and hope it answers their specific question. With CoWork, setup is: open browser, ask question.

### Step 1: Log In

1. Open your browser and navigate to the Snowflake URL provided by your lab instructor
2. Sign in with the credentials provided (or your existing Snowflake credentials)
3. From the left navigation panel, click **CoWork**

You should see the CoWork chat interface — a clean conversational window ready for your questions.

### Step 2: Orient Yourself

| Element | What It Does |
|---------|-------------|
| **Chat input bar** | Where you type natural-language questions |
| **+ button** | Access Deep Research, file uploads, and other modes |
| **Thread history** (left panel) | Previous conversations and saved Artifacts |
| **Your role** (top right) | Shows which Snowflake role you're using — this controls what data you can see |

### Step 3: Select the Agent

In the chat, select the **Mosaic Retail** agent. This agent is connected to your retail dataset and understands your business vocabulary — categories, subcategories, suppliers, stores, and channels.

### Step 4: Warm Up

Type your first question:

```
What data do I have access to?
```

CoWork responds with a summary of available data: sales transactions, product catalog, supplier info, and store details. This confirms everything is working.

---

## Platform Principles

Before we begin, these are the enduring ideas you should carry forward:

- **Governance travels with the data, not the application.** CoWork inherits every row-access policy, column mask, and RBAC grant your admin already configured. There is no parallel security stack to build or maintain.
- **AI lives next to governed data.** Your questions are answered by an agent that queries your Snowflake tables directly — data never leaves the governed boundary. No data movement, no shadow copies, no ungoverned exports.
- **One agent, full business context.** CoWork combines structured tables, unstructured documents, and external context in a single conversational experience. No tool-switching, no context loss between systems.
- **Cost is observable.** Every CoWork interaction consumes Cortex AI credits. Your admin can monitor usage via `SNOWFLAKE.ACCOUNT_USAGE` views — no surprise bills, full attribution by user and role.

> These principles apply to every Snowflake AI capability, not just CoWork. They are the architectural foundation that makes enterprise AI deployable at scale.

---

## Act 1: Let Me Check the Numbers (~5 min)

> **Business Context:** Jordan's buyer meeting is at 2pm. First instinct: how did my category do last week? In the old world, this means opening a dashboard and hoping the filters are right. With CoWork, it's a question.

---

### Q1

```
How did Home & Kitchen perform last week?
```

**What to expect:** A total revenue number for the most recent week (Aug 25-31). This sets the baseline — Jordan sees a number but doesn't yet know if it's good or bad.

> **Verified Answers:** Look for the green shield icon next to the response. This indicates a **Verified Answer** — a metric backed by a curated, data-team-approved definition.
>
> | Signal | Meaning |
> |--------|---------|
> | Green shield | This metric uses a curated, data-team-approved definition and calculation |
> | No shield | CoWork reasoned from the data schema — still accurate, but not pre-validated by your data team |
>
> When your CFO asks "where did that number come from?", the green shield means it uses the exact calculation your organisation agreed on.

---

### Q2

```
How does that compare to the week before?
```

**What to expect:** A week-over-week comparison — something like "-8% vs prior week." The problem is now visible. Notice how CoWork maintains context from Q1 without you needing to re-specify "Home & Kitchen."

---

### Q3

```
Which subcategory drove the decline?
```

**What to expect:** A breakdown showing Kitchen Appliances as the clear underperformer while other subcategories (Cookware, Home Decor, etc.) are flat or slightly up. Jordan's attention is now focused.

---

### Q4

```
Show me Kitchen Appliances revenue by week for the past 8 weeks as a line chart
```

**What to expect:** A line chart with weeks of steady/growing revenue, then a visible drop. This is the visual "something broke" moment.

> *Instructor: "Notice the shape — steady growth, then a break. Something happened recently. Let's find out what."*

> **Auto-visualization:** CoWork generates charts automatically based on your question. Trends get line charts, comparisons get bar charts, distributions get pie charts. You can also request a specific chart type — like "as a line chart" above. See [CoWork visualizations documentation](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#visualizations).

---

### Save Your First Artifact

Click the **Save as Artifact** button on the chart. Name it:

```
KA Weekly Trend
```

The chart is now saved to your Artifacts panel (left sidebar) for quick reference later.

> **What are Artifacts?** Any chart, table, or report CoWork generates can be saved as an Artifact. They persist in your workspace, are shareable with colleagues (within their access permissions), and are revisitable without regenerating the analysis. See [Artifacts documentation](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#artifacts).

---

## Act 2: The Detective Work (~10 min)

> **Business Context:** The numbers say "something broke." But "sales are down" isn't a negotiating position for a buyer meeting. Jordan needs the root cause: which products, which supplier, how much revenue is at risk. In the old world, this is three separate analyst tickets across 2-3 days. With CoWork, it's three follow-up questions.

---

### Q5

```
Which products in Kitchen Appliances declined the most last week? Show as a bar chart sorted by decline
```

**What to expect:** A bar chart ranking products by revenue decline. The top 3-4 decliners are all Apex Kitchen Co products (BrewMaster 360, SmartToast Pro, QuickBoil Kettle). ProBlend 9000 and non-Apex products are absent from the decline list.

> **Chart customization:** Adding "show as a bar chart sorted by decline" gives you control over the visualization. You can always ask CoWork to change chart types, add labels, sort differently, or switch to a table format — all in natural language.

---

### Q6

```
What supplier are those products from?
```

**What to expect:** "Apex Kitchen Co" — all the declining products come from a single supplier. The pattern clicks. Notice the conversational context: CoWork knows "those products" refers to the decliners from Q5.

---

### Q7

```
Does Apex Kitchen Co have any delivery delays?
```

**What to expect:** "Yes — 9 days delayed, starting August 25, expected resolution September 8." The root cause is confirmed. The dates align perfectly with the revenue dip.

> *Instructor: "Three questions to go from 'revenue is down' to 'here's the exact supplier, the exact start date, and the expected fix date.' This is what used to be a 3-day analyst request."*

---

### Q8

```
How much revenue did we lose from Apex products last week vs their 4-week average?
```

**What to expect:** A specific dollar figure — the revenue gap. This is the number Jordan puts on the meeting slide. It quantifies the problem for the buyer negotiation.

---

## Act 3: But What's Working? (~5 min)

> **Business Context:** Good category managers don't just bring problems to buyer meetings — they bring opportunities. Jordan needs a growth story to pair with the supply disruption. "We're losing money here, but here's where we should invest" is a complete narrative.

---

### Q9

```
Despite this, are any Kitchen Appliances products still growing?
```

**What to expect:** ProBlend 9000 surfaces at or near the top. The framing "despite this" keeps the conversation in context. Jordan pivots from problem to opportunity.

---

### Q10

```
Show me ProBlend 9000 weekly revenue since launch as a line chart
```

**What to expect:** A line chart showing 13 weeks of consistent growth since the June 2 launch. Steady, organic growth curve — the opposite shape to the Kitchen Appliances dip from Q4.

---

### Q10b: Iterate on the Chart

```
Add ProBlend 5000 to that chart for comparison
```

**What to expect:** A multi-series line chart with two lines: PB9000 ramping up, PB5000 gently declining. The crossover point tells the cannibalization story visually.

> *Instructor: "You can iterate on charts — add series, change time ranges, switch chart types — all in natural language."*

---

### Save Your Second Artifact

Click **Save as Artifact** on the comparison chart. Name it:

```
ProBlend 9000 vs 5000 Trend
```

You now have two saved artifacts: the KA decline story and the PB9000 growth story — the two pillars of your meeting brief.

---

### Q11

```
What percentage of ProBlend 9000 sales are online vs in-store? Show as a pie chart
```

**What to expect:** A pie/donut chart showing ~62% Online, ~28% In-Store, ~10% Click-and-Collect. This reinforces why PB9000 is winning — it dominates the fastest-growing channel.

---

### Q12

```
Is ProBlend 9000 cannibalizing ProBlend 5000?
```

**What to expect:** "ProBlend 5000 has declined ~2-3% per month since June." The upgrade path is real, but the total blender category is still growing because the 9000 more than compensates.

> *Instructor: "You now have two complete stories for your 2pm meeting: a fire to address (Apex) and an opportunity to propose (increase the ProBlend 9000 buy). All from one conversation, no SQL, no analyst ticket."*

---

## Deep Research (~10 min)

> **Business Context:** Jordan has the "what" — now they need the "why" at a depth suitable for a formal recommendation. "Sales are down" isn't a negotiating position. "Sales are down because of a 9-day supply disruption at our third-largest supplier, with $X at risk if it slips, and here's the evidence for activating backup sourcing" — that's a negotiating position. Deep Research produces that level of insight in minutes, not days.

### When to Use Deep Research

| Use Deep Research when... | Use standard chat when... |
|--------------------------|--------------------------|
| You need to understand *why* | You need a quick *what* |
| The answer spans multiple data domains | The answer comes from one table/metric |
| You want a shareable report with citations | You want a quick number or chart |
| You'd normally ask an analyst for this | You'd normally check a dashboard |

See [Deep Research documentation](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#deep-research).

---

### Q13

Click the **+ button** in the message bar, then select **Deep Research**. Type:

```
Investigate the Apex Kitchen Co supply disruption's impact on Kitchen Appliances. Quantify the total revenue loss, identify which products and stores were most affected, and recommend whether we should activate a backup supplier or wait for resolution on September 8.
```

**What to expect:** Deep Research decomposes your question into 3-5 sub-investigations and runs them in parallel. You'll see progress updates as it works. This takes 3-5 minutes.

The final report includes:
- Total revenue loss quantified (~$X over the disruption period)
- Products ranked by impact
- Stores most affected
- A "wait vs. diversify" recommendation backed by data
- Revenue-at-risk calculation if the Sep 8 resolution slips

Every finding is cited — click any reference number to see the underlying data query.

> *Instructor (while Deep Research runs): "Watch the progress indicator — you can see CoWork decomposing the question into sub-investigations and running them in parallel. This is the kind of analysis that normally takes a business analyst 2-3 days. Every number in the final report traces back to a query you can audit."*

---

### Save and Pin the Report

1. Click **Save as Artifact** on the completed report. Name it:

```
Apex Kitchen Co Impact Analysis — Aug 2026
```

2. Open the Artifacts panel (left sidebar). Find the report and click **Pin**. Pinned artifacts are discoverable by other CoWork users in your organisation.

> *Instructor: "This saves the full document — not just the summary, but every chart and citation. Pinning makes it findable by your team without you needing to forward it."*

---

### Q13b (Optional)

```
From that research, show me a bar chart of revenue loss by product
```

**What to expect:** A clean bar chart extracted from the research findings, showing per-product revenue impact. Demonstrates that you can pull specific visuals from a completed Deep Research report.

---

## Take Action (~10 min)

> **Business Context:** Analysis without action is just trivia. Jordan's buyer meeting is in 2 hours. They need to share the decline analysis with their merchandise planning team and prepare a structured brief — all without leaving CoWork.

---

### Q14

```
Summarise my key findings for the buyer meeting in two sections: first, the Apex supply disruption and its impact; second, the ProBlend 9000 growth case and my recommendation to increase the Q4 buy.
```

**What to expect:** A clean, structured brief:

> **1. Apex Kitchen Co — Supply Disruption**
> - Revenue impact: -$X last week (-8% WoW in Kitchen Appliances)
> - Root cause: 9-day delivery delay from Aug 25, affecting 4 products
> - Expected resolution: Sep 8. Revenue-at-risk if it slips: $Y/week
> - Recommendation: Monitor through Sep 8; if unresolved, activate backup sourcing
>
> **2. ProBlend 9000 — Growth Opportunity**
> - +100% revenue growth since June launch, consistent weekly ramp
> - 62% online channel (our fastest-growing channel)
> - Mild cannibalization of ProBlend 5000 (-2-3% MoM) but net category positive
> - Recommendation: Increase Q4 buy by 40%

---

### Q15

```
Share the Apex impact analysis to the #merch-planning Slack channel with the note: "Prep for 2pm — Apex supply impact attached. Two decisions needed: (1) backup supplier activation, (2) ProBlend Q4 allocation increase."
```

**What to expect:** CoWork uses the MCP Slack connector to compose a message, shows you a preview, and asks for confirmation before sending. Your team arrives at 2pm having already read the brief.

> **MCP Connectors:** CoWork connects to external tools via the [Model Context Protocol](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#mcp-connectors). Your admin configures which connectors are available:
>
> | Connector | Actions |
> |-----------|---------|
> | **Slack** | Send messages, post to channels, share artifacts |
> | **Gmail** | Compose and send emails with data summaries |
> | **Jira** | Create tickets, update issues |
> | **Salesforce** | Log activities, update records |
>
> You don't need to switch apps. The action happens from within your data conversation.

---

## Bonus: Create a User Skill

You do this kind of Monday morning analysis every week. Instead of repeating the same questions, capture the workflow as a **User Skill** — a personal, reusable multi-step command.

```
Create a skill called "Monday Category Review" that does the following:
1. Pull this week's revenue for Home & Kitchen by subcategory
2. Compare to last week and flag any subcategory that declined more than 10%
3. For any flagged subcategory, identify the top 3 products driving the decline
4. Summarize findings in bullet points ready for my team standup
```

Next Monday, you simply say:

```
Run my Monday Category Review skill
```

And get the same multi-step analysis in seconds.

> **User Skills** are personal, reusable workflows saved to your workspace. They run with your data access and can be triggered by name in any conversation. See [User Skills documentation](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#user-skills).

---

## Bonus: Governance Demo

> *This is an instructor-led demonstration. Participants watch on the projector.*

The instructor asks the same question using two different roles:

```
What is total revenue across all departments this year?
```

| Role | Result |
|------|--------|
| HOL_ATTENDEE_ROLE | Returns only Home & Kitchen |
| COMMERCIAL_DIRECTOR_ROLE | Returns all four departments (Home & Kitchen, Electronics, Outdoor & Garden, Sports & Fitness) |

> *"Same agent, same question, same data. The only difference is the role. Jordan sees their world. The Commercial Director sees everything. No one configured this per-agent — it's inherited from the row access policy your admin already set up."*

This is what "governance travels with the data" means in practice. CoWork doesn't rebuild security — it inherits it. See [Row Access Policies documentation](https://docs.snowflake.com/en/user-guide/security-row-intro).

---

## Cost and Monitoring

> **For admins and SE conversations:** CoWork interactions consume Cortex AI credits. Usage is fully observable:

```sql
-- Monitor CoWork usage by user (admin query — not part of this lab)
SELECT USER_NAME, COUNT(*) AS INTERACTIONS, SUM(CREDITS) AS TOTAL_CREDITS
FROM SNOWFLAKE.ACCOUNT_USAGE.CORTEX_AI_FUNCTIONS_USAGE_HISTORY
WHERE FUNCTION_NAME = 'AGENT'
GROUP BY USER_NAME
ORDER BY TOTAL_CREDITS DESC;
```

Key points for customer conversations:
- Every interaction is metered and attributable to a specific user and role
- Admins can set budgets and alerts using Snowflake's standard cost governance
- Deep Research consumes more credits than standard Q&A (multiple sub-queries)
- No opaque per-seat licensing — you pay for what you use

---

## Why This Matters

You just experienced Snowflake CoWork. But that is not the real lesson.

The real lesson is this: **enterprise AI that actually deploys requires governance, trust, and action — not just a chat interface.** Every answer Jordan received today was governed by their role, every metric was attributable to a curated definition, every action respected the same security boundary that protects the underlying data.

Jordan walks away able to **independently get answers, generate cited reports, and act on insights — without code, without waiting, without leaving the governed boundary of their enterprise data.**

The Platform Principles you experienced today:
- **Governance travels with the data** — Jordan's row access policy limited results automatically. No one configured this per-agent.
- **AI lives next to governed data** — Every question was answered by querying Snowflake tables directly. No data left the governed boundary.
- **One agent, full business context** — From revenue trends to supplier delays to channel mix — one conversation, no tool-switching.
- **Cost is observable** — Every interaction is metered, attributed, and governable through standard Snowflake cost controls.

CoWork is one component. The Snowflake AI Data Cloud is the competitive advantage.

---

## Business Outcome Validation

Without running any queries, can you answer these four questions?

1. **What is the business problem this lab addresses?**
   Business users are stuck between stale dashboards and multi-day analyst queues, unable to self-serve on time-sensitive questions.

2. **Why does the Snowflake AI Data Cloud solve it better than alternatives?**
   One agent with full business context, automatic data understanding, day-one usefulness — all within the governed boundary, with no parallel security stack to build.

3. **What would break if a customer tried to build this outside of Snowflake?**
   They'd need to rebuild governance (RBAC, masking, row access) in a separate system, build semantic layers from scratch, manage AI infrastructure, handle data movement, and maintain sync between the analytics layer and the security layer.

4. **How would you explain the production operations story to a VP?**
   "It inherits everything — roles, policies, access controls — automatically. No new security stack to manage. Data never leaves Snowflake. Every answer is attributable. Every credit is observable. And it's available today."

If you can answer all four, the lab has done its job.

---

## Lab Complete

### What You Accomplished

| Time | What You Did | Traditional Equivalent |
|------|-------------|----------------------|
| 5 min | Logged in, oriented, asked first question | Check a dashboard (limited) |
| 5 min | Identified the decline and visualized it | Email analyst, wait 1-2 days |
| 10 min | Root cause investigation across products/suppliers | Analyst project (2-3 days) |
| 5 min | Found the growth opportunity, compared products | Second analyst request |
| 10 min | Deep Research cited report | Analyst + Business Analyst (3-5 days) |
| 10 min | Meeting brief, shared via Slack, created a skill | Manual email/Slack + repeat effort weekly |
| **~45 min** | **Full Monday morning workflow** | **1-2 weeks of analyst time** |

### CoWork Features Covered

| Feature | Where |
|---------|-------|
| Natural language Q&A | Q1-Q12 |
| Verified Answers (green shield) | Q1 |
| Conversational context (follow-ups) | Q2, Q3, Q6, Q10b |
| Auto-visualization (line chart) | Q4, Q10, Q10b |
| Auto-visualization (bar chart) | Q5, Q13b |
| Auto-visualization (pie/donut) | Q11 |
| Chart customization | Q5 (sort), Q11 (type), Q10b (add series) |
| Artifacts (save) | After Q4, Q10b, Q13 |
| Artifacts (pin to homepage) | After Q13 |
| Deep Research | Q13 |
| Summary/synthesis | Q14 |
| MCP Connector (Slack) | Q15 |
| User Skills (automation) | Bonus |
| Row-Level Security | Governance demo |
| Cost observability | Cost section (admin reference) |

### Customer Proof

> **Fanatics Betting & Gaming:** 80% of their customer experience organisation uses CoWork weekly. They save 3+ hours per person per week, with 3 agents in production.

---

## What to Do Next

1. **Try with your own data.** Ask your data team to enable CoWork and connect it to your business data.
2. **Start with the question you ask most.** What do you email your analyst about every week?
3. **Create your first User Skill.** Automate the workflow you dread every Monday.
4. **Share with a colleague.** CoWork respects your existing RBAC, so everyone sees only what they should.

---

## Resources

**Official documentation:**
- [Snowflake CoWork Overview](https://docs.snowflake.com/en/user-guide/snowflake-cowork/about-cowork)
- [Using CoWork](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork)
- [Cortex Agents](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents)
- [Semantic Views](https://docs.snowflake.com/en/sql-reference/sql/create-semantic-view)
- [Row Access Policies](https://docs.snowflake.com/en/user-guide/security-row-intro)

**Cost and monitoring:**
- [Cortex AI Usage History](https://docs.snowflake.com/en/sql-reference/account-usage/cortex_ai_functions_usage_history)
- [Budgets and Cost Controls](https://docs.snowflake.com/en/user-guide/budgets)

---

## Pacing Notes for Instructors

- **Getting Started:** Keep tight. Participants should be typing Q1 within 3-4 minutes of sitting down.
- **Act 1 (Q1-Q4):** Fast. Each question answers in <10 seconds. Let the speed speak for itself. Don't over-explain.
- **Act 2 (Q5-Q8):** Detective pace. Slightly slower — let attendees read the product names and notice the Apex pattern across multiple products.
- **Act 3 (Q9-Q12):** Mood shift from problem to opportunity. The growth chart is the "smile" moment.
- **Deep Research (Q13):** Takes 3-5 minutes. Use the wait time to explain multi-agent decomposition. Don't fill awkward silence — let them watch the progress indicator.
- **Take Action (Q14-Q15):** Fast wrap. "Meeting prep done. Before lunch. Without writing SQL or filing a ticket."
- **Governance Demo:** Instructor-led. Have both roles ready. The role switch should be dramatic — same question, visibly different results.

---

> *"Two years of AI demos. Now for the hard part."*
>
> The hard part is deployment at enterprise scale — governance, trust, adoption, action. CoWork is built for the hard part.

---

*Built for Snowflake World Tour Auckland 2026*
