---
type: article
title: Agent Memory — the 7 types you should know before you ship to production
source_url: https://jamwithai.substack.com/p/agent-memory-the-7-types-you-should
author: jamwithai (Substack)
date_published: 2026-07-27
date_ingested: 2026-07-27
status: unprocessed
tags: []
---

# Agent Memory — the 7 types you should know before you ship to production

> If you have ever built a chatbot, you know that first version feels almost magical. You ask a question, it answers. You ask a follow-up, and it answers that too, picking up on exactly what you just said. Then the conversation ends. The same user comes back an hour later, says hello, and the agent has no idea who they are. Brilliant one minute, a complete stranger the next.

That blank slate is the problem the word "memory" is meant to solve. A language model on its own remembers nothing once a chat session finishes, so the moment you want it to actually know the people and tasks it works with, you reach for memory.

This is where it gets confusing, because "memory" turns out to be a single word for several very different things. Remembering what a user said three messages ago is not the same as remembering, weeks later, that they prefer Python. Recalling how a task failed last time is not the same as knowing the steps to run it. And neither is the same as remembering to follow up with someone next Tuesday.

Those are distinct kinds of memory, each with its own way of being stored, recalled, and going wrong. Lumping them together is where most "we added memory and the agent got worse" stories begin. Pile everything into one store and the agent gets slower, more expensive, and oddly inconsistent: old preferences stay active long after they should, irrelevant conversations resurface, and a one-time instruction quietly becomes a permanent rule.

> More memory is not a better agent. A better agent forgets on purpose.

So the useful design question is not "how do we add memory to the agent?" It is: **what should the agent remember, for how long, and under what conditions should that information come back?**

This post is the framework we use to answer that. There is no shortage of content explaining what a vector database does. What is missing is a way to decide which of seven different things you are actually building when you say "memory," and how to wire each one correctly. We will define all seven, show where each one breaks in production, point at what actually implements it, and then run a single real request through all of them so you can see the system instead of the parts.

## The Seven Types

1. In-context / working memory
2. Semantic memory
3. Episodic memory
4. Procedural memory
5. External / retrieval memory
6. Parametric memory
7. Prospective memory

Most agents use several of these. Very few need all seven.

## The Mental Model

These categories are not arbitrary. They map onto the kinds of memory cognitive scientists have studied for decades (semantic versus episodic, declarative versus procedural), and that mapping was formalized for LLM agents in [CoALA: Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) (Sumers, Yao, Narasimhan, and Griffiths, 2023).

The practitioner takeaway from that work is simple and useful: **an agent has one short-term working memory and several optional long-term memories, and naming each one tells you which slot your system is missing.**

Hold on to two distinctions as you read:

### Stored versus Active
Your application can hold an entire conversation in a database, but the model cannot reason over a single byte of it until those bytes are placed back into the current prompt. **Storage is potential. Working memory is what the model can actually use right now.**

### What versus Where
Semantic, episodic, and procedural memory describe **what** is being remembered. Retrieval and parametric memory are about **where** knowledge lives and how it gets back to the model. Mixing these two axes is why "just add a vector DB" feels like an answer and then quietly fails.

Every type below is some combination of those two ideas.

## 1. In-context / Working Memory

**What it is:** A language model forgets everything the moment it finishes a reply. Once the call ends, the last message is gone from its mind. So to make a conversation work at all, your app re-sends the entire chat or last N messages every time the user says something new: the instructions you gave the model, all the earlier messages, any results from tools, and anything you looked up for it. That whole package of text you send in is working memory. It is the only thing the model can see while it writes its answer.

**Why it matters:** The model can only use what is in that package right now. If something is not in there, it may as well not exist. Say a user mentions early on that they are on AWS and cannot use Kubernetes. Ten messages later the agent is still suggesting ECS (Amazon's non-Kubernetes option) instead of EKS (its Kubernetes one). It looks like the agent remembered the rule. It did not. That first message is simply still part of the package being re-sent each turn, so the model can still read it. Stop including it and the "memory" vanishes.

**Where it breaks:** That package has a size limit, called the context window: the maximum amount of text a model can read at once. Text is measured in tokens, which are roughly small chunks of words. A short chat fits with room to spare. A long one does not. Once the conversation grows past the limit, you have to choose what to keep, what to shorten, and what to drop.

---

*[Content truncated at 8000 chars — full article available at source URL]*
