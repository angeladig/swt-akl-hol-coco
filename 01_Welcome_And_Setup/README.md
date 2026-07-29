# Module 01: Welcome & Getting Started

> **Business Context:** Every Monday morning, Jordan Chen opens their laptop to a full inbox and a 2pm buyer meeting. The old workflow was: check a static dashboard, email the analytics team with follow-up questions, wait hours (or days) for answers, then scramble to prep. Today, we're going to change that with one conversational interface.

**Time:** ~10 minutes

---

## 🎯 Quick Summary

- CoWork is a conversational AI agent built into Snowflake — no separate tool to install
- It connects directly to your governed enterprise data (structured and unstructured)
- Every answer respects your existing role-based access and data policies automatically
- You interact entirely through natural language — no SQL, no code, no query builders
- Your data team has already configured the agent — you just log in and ask

---

## 🧭 What You'll Do

1. Log in to Snowflake CoWork
2. Explore the conversational interface
3. Understand what data is available to you
4. Ask your first question

---

## 🛠️ Step 1: Log In to Snowflake CoWork

1. Open your browser and navigate to the Snowflake URL provided by your lab instructor
2. Sign in with the credentials provided (or your existing Snowflake credentials)
3. From the left navigation panel, click **CoWork**

You should see the CoWork chat interface — a clean conversational window ready for your questions.

<!-- SCREENSHOT: CoWork landing page with chat interface -->

> **What just happened?** You opened CoWork, which is powered by a Cortex Agent configured by your data team. The agent already knows your data — tables, relationships, business metrics — because it's connected to a semantic view that maps business language to your physical data. You didn't have to configure anything.

---

## 🛠️ Step 2: Explore the Interface

Take a moment to notice the key elements:

| Element | What It Does |
|---------|-------------|
| **Chat input bar** | Where you type natural-language questions |
| **+ button** | Access Deep Research, file uploads, and other modes |
| **Thread history** (left panel) | Previous conversations you can revisit |
| **Your role** (top right) | Shows which Snowflake role you're using — this controls what data you can see |

<!-- SCREENSHOT: Annotated CoWork interface elements -->

> **Governance in action:** Notice your role in the top-right corner. Every question you ask is answered using only the data your role is authorized to access. If a colleague in a different role asks the same question, they may see different results — or no results at all. This isn't a feature you configure; it's automatic.

---

## 🛠️ Step 3: Understand Your Data

Let's start with a discovery question. Type the following into the chat:

```
What data do I have access to?
```

CoWork will respond with a summary of the data domains available to you. For this lab, you should see something like:

- **Sales transactions** — revenue, units, orders by product/category/region
- **Product catalog** — SKUs, categories, suppliers, pricing
- **Customer data** — segments, purchasing patterns, lifetime value
- **Inventory** — stock levels, reorder points, warehouse data

<!-- SCREENSHOT: CoWork response showing available data summary -->

> **How does CoWork know this?** Your data team connected CoWork to a semantic view — a business-friendly layer that maps terms like "revenue" and "category" to the actual database columns. This is what we mean by "day-one usefulness." The agent understands your business vocabulary from the start.

---

## 🛠️ Step 4: Ask Your First Question

Now let's ask something specific. Type:

```
How did the Home & Kitchen category perform last week?
```

Watch what happens:
1. CoWork interprets your question
2. It queries your data (you'll see a brief "thinking" indicator)
3. It returns a natural-language summary with key metrics

You should see metrics like total revenue, units sold, and a comparison to the prior week — presented in plain language with a supporting table or chart.

<!-- SCREENSHOT: First question response with metrics -->

**Congratulations!** You just got an answer that would normally require an analyst ticket, a SQL query, and a wait time. It took seconds.

---

## ✅ Validate

Before moving on, confirm:
- [ ] You can see the CoWork chat interface
- [ ] You received a response showing available data domains
- [ ] Your first question about Home & Kitchen returned meaningful results
- [ ] You can see your role displayed (confirming governance is active)

---

## 🌐 Why This Matters

You didn't install anything. You didn't write a query. You didn't wait for anyone. You asked a question about your business in your own words, and you got an immediate, governed answer.

This is the fundamental shift: **from "request and wait" to "ask and act."**

The agent didn't just understand your question — it understood your data, your metrics, your business context. And it did so while respecting every access policy your admin set up. That's what "governance travels with the data" means in practice.

---

## ➡️ Next Module

Now that you're oriented, let's put CoWork to real work. In [Module 02](../02_Ask_Questions_Get_Insights/README.md), you'll ask progressively complex questions, generate visualizations, and see how Verified Answers provide production-grade trust.
