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

---

## Platform Principles

Before we begin, these are the enduring ideas you should carry forward:

- **Governance travels with the data, not the application.** CoWork inherits every row-access policy, column mask, and RBAC grant your admin already configured. There is no parallel security stack to build or maintain.
- **AI lives next to governed data.** Your questions are answered by an agent that queries your Snowflake tables directly — data never leaves the governed boundary. No data movement, no shadow copies, no ungoverned exports.
- **One agent, full business context.** CoWork combines structured tables, unstructured documents, and external context in a single conversational experience. No tool-switching, no context loss between systems.
- **Cost is observable.** Every CoWork interaction consumes Cortex AI credits. Your admin can monitor usage via `SNOWFLAKE.ACCOUNT_USAGE` views — no surprise bills, full attribution by user and role.

---

## Act 1: Spot the Problem (~10 min)

> **Business Context:** Jordan's buyer meeting is at 2pm. First instinct: how did my category do last week? In the old world, this means opening a dashboard, checking filters, then filing a ticket for any follow-up. With CoWork, it's a conversation.

Each question in this section introduces a different CoWork capability. Pay attention to the feature callout after each one.

---

### Q1 — Natural Language Q&A + Verified Answers

```
How did Home & Kitchen perform last week?
```

**What to expect:** A total revenue number for Aug 25-31, with a comparison to the prior period.

**New feature — Verified Answers:** Look for the green shield icon next to the response. This indicates a metric backed by a curated, data-team-approved definition — not just AI reasoning, but an organisation-agreed calculation.

| Signal | Meaning |
|--------|---------|
| Green shield | Uses a curated, data-team-approved definition |
| No shield | CoWork reasoned from the data schema — accurate, but not pre-validated |

> *Instructor: "The green shield is what lets you put this number in a board deck with confidence."*

---

### Q2 — Conversational Context (Follow-ups)

```
Which subcategory drove the decline?
```

**What to expect:** A breakdown showing Kitchen Appliances as the underperformer. Other subcategories are flat or slightly up.

**New feature — Conversational context:** Notice you didn't re-specify "Home & Kitchen" or "last week." CoWork maintains the thread context — each question builds on the prior answer, just like talking to a colleague.

---

### Q3 — Auto-Visualization (Trend Line Chart)

```
Show me Kitchen Appliances revenue by week for the past 8 weeks
```

**What to expect:** A line chart showing steady/growing revenue, then a visible drop in recent weeks. The visual "something broke" moment.

**New feature — Auto-visualization:** CoWork generates the chart automatically — you didn't specify "line chart." The agent infers that a time-series question should produce a trend visualization. (Comparisons get bar charts, distributions get pie charts.)

> *Instructor: "Notice the shape — steady growth, then a break. Something happened. Let's find out what."*

**Save as Artifact:** Click the **Save as Artifact** button on this chart. Name it `KA Weekly Trend`. You'll use it in your meeting brief later.

> **What are Artifacts?** Any chart, table, or report can be saved to your Artifacts panel (left sidebar). They persist, are shareable, and are revisitable without regenerating.

---

### Q4 — Chart Customization + Cross-Table Reasoning

```
Which products in Kitchen Appliances declined the most? Show as a horizontal bar chart sorted by revenue decline
```

**What to expect:** A horizontal bar chart ranking products by decline. The top decliners are all Apex Kitchen Co products (BrewMaster 360, SmartToast Pro, QuickBoil Kettle).

**New feature — Chart customization:** You specified the chart type ("horizontal bar") and the sort order ("sorted by revenue decline"). CoWork respects your visualization preferences. You can always override the auto-generated format.

**New feature — Cross-table reasoning:** This answer required joining daily_sales with products to get product names and grouping by revenue change. CoWork navigated multiple tables without you needing to know the schema.

---

### Q5 — Multi-Table Joins + Root Cause

```
What supplier are those products from, and do they have any delivery delays recorded?
```

**What to expect:** "Apex Kitchen Co — 9 days delayed, starting August 25, expected resolution September 8." Root cause confirmed in one question.

**New feature — Multi-table joins in a single question:** This answer required linking products → suppliers → delivery status. CoWork traversed three tables and returned a synthesized answer. In the old world, this is three separate queries and a manual cross-reference.

> *Instructor: "Four questions to go from 'revenue is down' to 'here's the exact supplier, the exact start date, and the expected fix date.' This is what used to be a 3-day analyst request."*

---

## Act 2: Find the Opportunity (~10 min)

> **Business Context:** Good category managers don't just bring problems to buyer meetings — they bring opportunities. Jordan needs a growth story to pair with the supply disruption. "We're losing money here, but here's where we should invest" is a complete narrative.

---

### Q6 — Multi-Series Comparison Chart

```
Compare ProBlend 9000 and ProBlend 5000 weekly revenue since June as a line chart
```

**What to expect:** A multi-series line chart with two lines: PB9000 ramping up, PB5000 gently declining. The crossover point tells the story visually.

**New feature — Multi-series comparison:** By naming two products in one question, you get them overlaid on the same chart. You can compare any dimensions this way — products, stores, channels, time periods.

> *Instructor: "You can iterate further — 'add ProBlend 3000 to that' or 'change to monthly' — all in natural language."*

---

### Q7 — Pie Chart + Channel Analysis

```
What's the channel split for ProBlend 9000? Show as a pie chart
```

**What to expect:** A pie/donut chart: ~62% Online, ~28% In-Store, ~10% Click-and-Collect. ProBlend 9000 is winning in the fastest-growing channel.

**New feature — Explicit chart type request:** You asked for a pie chart and got one. CoWork wouldn't auto-generate a pie chart for this question (it would likely default to a table), but respects your explicit preference.

---

### Q8 — Analytical Reasoning

```
Is ProBlend 9000 cannibalizing ProBlend 5000, or is the total blender category growing?
```

**What to expect:** A nuanced answer: "ProBlend 5000 has declined ~2-3% per month since June, but ProBlend 9000 more than compensates — the total blender category is growing." This requires the agent to reason about net impact, not just pull a single metric.

**New feature — Analytical reasoning:** This isn't a metric lookup — it's a judgment question that requires comparing two trends and drawing a conclusion. CoWork can reason across data, not just retrieve it.

> *Instructor: "You now have two stories for your meeting: a fire to address (Apex) and an opportunity to propose (increase the ProBlend 9000 buy). All from one conversation."*

---

## Deep Research (~10 min)

> **Business Context:** Jordan has the "what" — now they need a formal recommendation at a depth suitable for a buyer meeting. Deep Research produces multi-page cited reports in minutes, not days.

### When to Use Deep Research vs Standard Chat

| Use Deep Research when... | Use standard chat when... |
|--------------------------|--------------------------|
| You need to understand *why* | You need a quick *what* |
| The answer spans multiple data domains | The answer comes from one table/metric |
| You want a shareable report with citations | You want a quick number or chart |
| You'd normally ask an analyst for this | You'd normally check a dashboard |

See [Deep Research documentation](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#deep-research).

---

### Q9 — Deep Research (Multi-Agent Investigation)

Click the **+ button** in the message bar, then select **Deep Research**. Type:

```
Investigate the Apex Kitchen Co supply disruption's impact on Kitchen Appliances. Quantify the total revenue loss, identify which products and stores were most affected, and recommend whether we should activate a backup supplier or wait for resolution on September 8.
```

**What to expect:** Deep Research decomposes your question into 3-5 sub-investigations and runs them in parallel. This takes 3-5 minutes.

The final report includes:
- Total revenue loss quantified
- Products ranked by impact
- Stores most affected
- A "wait vs. diversify" recommendation backed by data
- Revenue-at-risk calculation if Sep 8 slips

**New feature — Deep Research:** Unlike standard chat (single query → single answer), Deep Research runs a multi-agent investigation: it decomposes the question, executes parallel sub-queries, synthesizes findings, and produces a cited report. Every claim has a reference you can click to see the underlying query.

> *Instructor (while it runs): "Watch the progress indicator — you can see sub-investigations running in parallel. This is the kind of analysis that normally takes a business analyst 2-3 days."*

---

### Save, Pin, and Refine

1. **Save:** Click **Save as Artifact** on the report → name it `Apex Kitchen Co Impact Analysis — Aug 2026`

2. **Pin:** Open the Artifacts panel → click **Pin** on the report. Pinned artifacts are discoverable by other CoWork users in your org.

3. **Refine (Q9b):**

```
From that research, show me a bar chart of revenue loss by product
```

**New feature — Extract visuals from research:** You can pull specific charts out of a Deep Research report by asking for them. The full report context is maintained.

---

## Take Action (~10 min)

> **Business Context:** Analysis without action is just trivia. Jordan's buyer meeting is in 2 hours. It's time to package findings and share with the team.

---

### Q10 — Synthesis (Meeting Brief Generation)

```
Summarise my key findings for the buyer meeting in two sections: first, the Apex supply disruption and its impact; second, the ProBlend 9000 growth case and my recommendation to increase the Q4 buy.
```

**What to expect:** A structured brief with two clear sections, each with bullet points and a recommendation. CoWork synthesizes everything from the conversation — Q1 through Q9 — into a presentation-ready format.

**New feature — Synthesis from full conversation:** CoWork uses the entire thread context to generate a summary. You didn't need to re-state any facts — it pulled from all prior answers, including the Deep Research report.

---

### Q11 — MCP Connector (Share to Slack)

```
Share the Apex impact analysis to the #merch-planning Slack channel with the note: "Prep for 2pm — Apex supply impact attached. Two decisions needed: (1) backup supplier activation, (2) ProBlend Q4 allocation increase."
```

**What to expect:** CoWork composes a Slack message, shows you a preview, and asks for confirmation before sending. Your team arrives at 2pm having already read the brief.

**New feature — MCP Connectors:** CoWork connects to external tools via the [Model Context Protocol](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#mcp-connectors). Actions happen from within your data conversation — no app-switching.

| Connector | Actions |
|-----------|---------|
| **Slack** | Send messages, post to channels, share artifacts |
| **Gmail** | Compose and send emails with data summaries |
| **Jira** | Create tickets, update issues |
| **Salesforce** | Log activities, update records |

---

## Bonus: User Skills (Automation)

You do this kind of Monday morning analysis every week. Instead of repeating the same questions, capture the workflow as a **User Skill** — a personal, reusable multi-step command.

```
Create a skill called "Monday Category Review" that does the following:
1. Pull this week's revenue for Home & Kitchen by subcategory
2. Compare to last week and flag any subcategory that declined more than 10%
3. For any flagged subcategory, identify the top 3 products driving the decline
4. Summarize findings in bullet points ready for my team standup
```

Next Monday, you simply say: `Run my Monday Category Review skill`

**New feature — User Skills:** Personal, reusable workflows saved to your workspace. They run with your data access and can be triggered by name. See [User Skills documentation](https://docs.snowflake.com/en/user-guide/snowflake-cowork/using-cowork#user-skills).

---

## Bonus: Governance Demo

> *Instructor-led demonstration. Participants watch on the projector.*

The instructor asks the same question using two different roles:

```
What is total revenue across all departments this year?
```

| Role | Result |
|------|--------|
| HOL_ATTENDEE_ROLE | Returns only Home & Kitchen |
| COMMERCIAL_DIRECTOR_ROLE | Returns all four departments |

> *"Same agent, same question, same data. The only difference is the role. Jordan sees their world. The Commercial Director sees everything. No one configured this per-agent — it's inherited from the row access policy your admin already set up."*

**New feature — Row-Level Security inheritance:** CoWork doesn't have its own security model. It inherits whatever RBAC and row access policies your admin already configured in Snowflake. See [Row Access Policies documentation](https://docs.snowflake.com/en/user-guide/security-row-intro).

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

Key points:
- Every interaction is metered and attributable to a specific user and role
- Admins can set budgets and alerts using Snowflake's standard cost governance
- Deep Research consumes more credits than standard Q&A (multiple sub-queries)
- No opaque per-seat licensing — you pay for what you use

See [Cortex AI Usage History](https://docs.snowflake.com/en/sql-reference/account-usage/cortex_ai_functions_usage_history).

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
| 5 min | Logged in, oriented, selected agent | Find the right dashboard, check filters |
| 10 min | Identified the decline, found root cause | 2-3 analyst requests (2-5 days) |
| 10 min | Found growth story, analysed channels | Second analyst request |
| 10 min | Deep Research cited report | Analyst + BA project (3-5 days) |
| 10 min | Meeting brief, shared via Slack | Manual email/Slack + repeat effort weekly |
| **~45 min** | **Full Monday morning workflow** | **1-2 weeks of analyst time** |

### Feature Coverage

Each question introduced exactly one new CoWork capability:

| # | Prompt | Feature Taught |
|---|--------|---------------|
| Q1 | "How did H&K perform last week?" | Natural language Q&A + Verified Answers |
| Q2 | "Which subcategory drove the decline?" | Conversational context (follow-ups) |
| Q3 | "Show me KA revenue by week for 8 weeks" | Auto-visualization (line chart) |
| Q4 | "Which products declined most? Show as bar chart sorted by decline" | Chart customization + cross-table reasoning |
| Q5 | "What supplier, and any delivery delays?" | Multi-table joins in one question |
| Q6 | "Compare PB9000 and PB5000 weekly since June" | Multi-series comparison chart |
| Q7 | "Channel split for PB9000? Pie chart" | Explicit chart type override |
| Q8 | "Is PB9000 cannibalizing PB5000?" | Analytical reasoning (not just retrieval) |
| Q9 | Deep Research: Apex impact investigation | Multi-agent cited research |
| Q10 | "Summarise findings for my buyer meeting" | Synthesis from full conversation |
| Q11 | "Share to #merch-planning Slack" | MCP Connector (external action) |
| Bonus | "Create a skill called Monday Category Review" | User Skills (automation) |
| Bonus | Same question, different role | Row-Level Security inheritance |

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

- **Getting Started:** Keep tight — participants should be typing Q1 within 3-4 minutes.
- **Act 1 (Q1-Q5):** Fast. Each question answers in <10 seconds. Emphasize the "New feature" callout after each one. The detective arc builds naturally.
- **Act 2 (Q6-Q8):** Mood shift from problem to opportunity. The multi-series chart is the visual "aha."
- **Deep Research (Q9):** Takes 3-5 minutes. Use the wait time to explain multi-agent decomposition. Don't fill silence — let them watch the progress indicator.
- **Take Action (Q10-Q11):** Fast wrap. "Meeting prep done. Before lunch. Without writing SQL or filing a ticket."
- **Governance Demo:** Instructor-led. Have both roles ready. The role switch should be dramatic — same question, visibly different results.

---

> *"Two years of AI demos. Now for the hard part."*
>
> The hard part is deployment at enterprise scale — governance, trust, adoption, action. CoWork is built for the hard part.

---

*Built for Snowflake World Tour Auckland 2026*
