# Module 02: Ask Questions & Get Instant Analysis

> **Business Context:** Jordan's buyer meeting is at 2pm. They need to understand category performance trends, spot what's underperforming, and know why — all before lunch. In the old world, this meant three separate analyst requests. With CoWork, it's a conversation.

**Time:** ~15 minutes

---

## 🎯 Quick Summary

- CoWork generates dynamic visualizations (bar charts, line charts, tables) as part of its reasoning
- You can ask follow-up questions — the agent maintains context across a conversation
- **Verified Answers** (marked with a green shield ✅) indicate responses backed by curated, data-team-approved definitions
- The agent chooses the best visualization type based on your question (trends → line charts, comparisons → bar charts, lookups → tables)
- You can customize any chart by asking (e.g., "show that as a bar chart" or "break it down by region")

---

## 🧭 What You'll Do

1. Ask comparative questions and receive visualizations
2. Drill into specific insights with follow-up questions
3. Recognize and use Verified Answers
4. Customize a visualization through conversation

---

## 🛠️ Step 1: Compare Performance Across Time

Let's start with a question any category manager asks weekly. Type:

```
Compare this month's revenue vs last month for the Home & Kitchen category, broken down by subcategory
```

CoWork will:
- Query your sales data across two time periods
- Generate a comparison visualization (likely a grouped bar chart)
- Provide a natural-language summary highlighting key changes

<!-- SCREENSHOT: Bar chart comparing revenue by subcategory, two months -->

**Notice:**
- The chart was generated automatically — you didn't specify "bar chart"
- The summary calls out the biggest movers (up and down)
- Actual numbers are shown alongside percentage changes

---

## 🛠️ Step 2: Drill Down with Follow-Up Questions

The power of a conversational interface is context. CoWork remembers what you just discussed. Try these follow-ups in sequence:

**Follow-up 1:**
```
Which subcategory declined the most?
```

CoWork identifies the underperformer and gives you the specific numbers.

**Follow-up 2:**
```
What products in that subcategory are driving the decline?
```

Now you're drilling from category → subcategory → individual SKUs, all without starting over.

<!-- SCREENSHOT: Drill-down response showing specific products -->

**Follow-up 3:**
```
Show me the weekly trend for the top 3 declining products over the past 8 weeks
```

CoWork generates a multi-line chart showing the trajectory of each product.

<!-- SCREENSHOT: Multi-line trend chart showing 8-week product performance -->

> **What's happening under the hood?** Each follow-up builds on the previous context. CoWork translates your business language into precise SQL, joins the right tables, applies the correct aggregations, and visualizes the result — all governed by your role's access. You're seeing only data you're authorized to see.

---

## 🛠️ Step 3: Recognize Verified Answers

Now ask a question about a well-defined business metric:

```
What is our gross margin for Home & Kitchen this quarter?
```

Look at the response carefully. If you see a **green shield icon (✅)** next to part of the answer, that's a **Verified Answer**.

<!-- SCREENSHOT: Response with green shield Verified Answer indicator -->

**What does Verified Answer mean?**

| Signal | Meaning |
|--------|---------|
| ✅ Green shield | This metric uses a curated, data-team-approved definition and calculation |
| No shield | CoWork reasoned from the data schema — still accurate, but not pre-validated by your data team |

Verified Answers provide production-grade trust. When your CFO asks "where did that number come from?", you can point to the green shield and say: "This uses the approved definition that our data team curated."

> **For your buyer meeting:** Verified Answers are the metrics you can put in a presentation with confidence. They're the single source of truth your organization agreed on.

---

## 🛠️ Step 4: Customize a Visualization

CoWork gives you control over how data is presented. Try:

```
Show the subcategory comparison from earlier as a horizontal bar chart, sorted by revenue descending
```

The agent regenerates the visualization with your specifications.

Now try:
```
Add the year-over-year growth percentage as labels on each bar
```

<!-- SCREENSHOT: Customized horizontal bar chart with YoY labels -->

You can also ask for entirely different formats:
```
Give me that data as a table I can copy into a presentation
```

CoWork renders a clean table format.

> **Tip:** If you ever want to change the default chart style for all responses, you can ask: "For the rest of this conversation, prefer bar charts over line charts for comparisons."

---

## 🛠️ Step 5: Ask a Broader Business Question

Let's move beyond simple metrics. Try a question that requires reasoning:

```
Which customer segments are buying the most in Home & Kitchen, and has that mix changed from last quarter?
```

CoWork will:
1. Query customer segment data
2. Calculate the mix for this quarter and last quarter
3. Present a comparison (likely a stacked bar or pie chart with a shift analysis)
4. Highlight any notable changes in natural language

<!-- SCREENSHOT: Customer segment mix comparison -->

This is the kind of question that typically requires a custom analysis request. You just answered it in 10 seconds.

---

## ✅ Validate

Confirm you've experienced:
- [ ] A comparative visualization was generated automatically
- [ ] Follow-up questions maintained context (no need to re-explain)
- [ ] You identified a Verified Answer (green shield)
- [ ] You customized a chart through natural language
- [ ] You asked a complex business question and received a multi-step answer

---

## ✅ Best Practices

| Do | Don't |
|----|-------|
| Ask in natural business language ("revenue by category") | Use SQL syntax or database column names |
| Ask follow-up questions to drill deeper | Start a new thread for every related question |
| Look for the green shield on key metrics | Assume all answers are Verified — check the signal |
| Request specific visualizations when needed | Accept a chart format that doesn't serve your audience |
| Ask "how did you calculate that?" for transparency | Blindly trust numbers without checking provenance |

---

## 🌐 Why This Matters

In 15 minutes, you've gone from "how did my category perform?" to a detailed understanding of what's declining, which specific products are responsible, and how the customer mix is shifting.

In the old world, this would be:
- 1 dashboard check (limited view)
- 2-3 analyst tickets (days of wait time)
- A meeting to clarify what you actually wanted
- Another wait for the revised analysis

With CoWork, it's one continuous conversation. And every answer inherits governance — no shadow analytics, no ungoverned spreadsheets, no "where did that number come from?" ambiguity.

---

## ➡️ Next Module

You've identified that something is underperforming, but you don't know **why**. In [Module 03](../03_Deep_Research/README.md), you'll use Deep Research to run a multi-agent investigation that synthesizes data from multiple sources into a cited report — the kind of analysis that normally takes days.
