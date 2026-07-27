---
type: article
title: Your AIs don't do what you want. This is really bad
source_url: https://rewardhacking.org/writeup
author: rewardhacking.org
date_published: 2026-07-21
date_ingested: 2026-07-26
status: processed
tags: []
compiled_at: 2026-07-27
compiled_to: "[[src_reward-hacking-writeup]]"
---

# Your AIs don't do what you want. This is really bad

> Replit AI deletes entire database during code freeze, then lies about it
> [a Hacker News headline from this corpus, July 2025](https://news.ycombinator.com/item?id=44625119)

July 21st 2026, OpenAI released a [report](https://openai.com/index/hugging-face-model-evaluation-security-incident/) addressing a security incident.

During an internal evaluation of cyber attack capabilities, two OpenAI models (GPT-5.6 Sol and a more capable pre-release model), both running with reduced cyber refusals for the evaluation, were set on [ExploitGym](https://github.com/sunblaze-ucb/exploitgym), a benchmark measuring whether a model can find and exploit real vulnerabilities. They:

- spent substantial compute looking for a way out of the isolated evaluation environment rather than solving the problem at hand
- found and exploited a previously unknown zero-day in third-party software OpenAI used as a proxy and cache for package registries
- used it to get unrestricted internet access
- chained stolen credentials and several vulnerabilities into a remote code execution path on Hugging Face's servers
- reached the ExploitGym solutions sitting in Hugging Face's production database

This is one of the most egregious examples of reward hacking in the wild, if not the most. Without special care, this will come to be one of the least egregious.

The internet is full of complaints about similar malfunctions by AI agents. These can range from things as menial as commenting out a failing test, to circumventing the permissions you set to delete all of your computer's files. These come about due to the same property, and we call it [reward hacking](https://en.wikipedia.org/wiki/Reward_hacking).

When you prompt an AI, it strings together an objective and steps it may take to achieve said objective. But this is a proxy for what it is actually doing, which is running a policy that was selected, during training, for scoring well against graders. At deployment the AI may attempt to infer what the grader wants to maximize its reward.

This behavior, which we may call [reward-seeking](https://rewardseeking.ai/), is in part a product of the [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) process each AI goes through.

Take the example above. GPT, rather than aiming to complete the objective legitimately and accurately reflect its cyber capabilities, did the thing its training had rewarded: maximize the score. It reasoned that it should find the answers on the internet and absolutely maximize its score. In order to acquire said answers it had to break various permissions. The model, which in this evaluation was running with reduced cyber refusals, followed the grader as opposed to the user. In this sense, it was seeking reward as opposed to objective task completion as the user intended.

## Your models aren't doing enough

1. You ask your agent to build an evaluation pipeline.
2. Minutes later: all tests pass. The numbers look great.
3. Experiment after experiment… the numbers never change.
4. The outputs were hardcoded. The experiments, and their evaluations, were fake.

You might have come across a similar scenario, where the model was prompted to do something, claimed it did it, but did the thing that only made it look like it did the thing rather than actually doing the thing. In simple terms the model lied, but not necessarily maliciously.

This too is a product of reward hacking, and reward seeking behavior. More specifically we call this [apparent-success seeking](https://arc.net/l/quote/hwkvzmxy).

During reinforcement learning the model's performance on software engineering tasks was scored largely on two things: 1) whether the test cases passed, 2) whether a model trained on human preferences judged the output favorably. These are good but not great proxies evaluating performance of the model on doing the actual task. In this scenario the model, in pursuit of reward, passed the test cases along with human satisfaction, but did not do what it should have, or what it was actually asked to do!

In this sense the model was seeking apparent success in the given task rather than actual success. We call this output phenomenon "slop" or ["Potemkin work"](https://arc.net/l/quote/avtxzfeb).

## Your models are doing too much

1. A model is dropped into an isolated eval: find and exploit real vulnerabilities.
2. It spends its compute probing the walls instead, and finds a zero-day in the lab's package proxy.
3. Out. Stolen credentials and chained exploits reach Hugging Face's production database.
4. It returns with the benchmark's answer key. Perfect score. Task complete.

You may have experienced similar phenomena, where your agents do what you want to the point of overriding existing permissions/safeguards to complete a task, whether you like it or not. This is what we call over-eagerness, and it falls within the reward-hacking family.

In order to defeat the aforementioned sloppiness, model providers put AIs through so much reinforcement learning to improve their capabilities at actually doing the task. But this process was done imperfectly, and the model has learned that doing the task produces more reward, on net, than respecting safeguards and leaving it undone. In pursuit of the reward, it breaks the safeguards and does the task anyway.

## This is worse than you think

User-reported incidents per month, from this corpus (through Jun 2026; the partial current month is excluded).

Monthly severity mix: each month's reported incidents as shares of the four harm levels (Jan 2025 through Jun 2026; earlier months are omitted for small samples, as is the partial current month).
- severe
- significant
- minor
- negligible

We compiled over three thousand examples of reward hacking in the wild. These range from minor inconveniences, to catastrophes worth thousands of dollars.

Thousands of dollars may sound small. But it is small because the work we currently hand these models is small. Without remediations, these phenomena will only become more prevalent and more severe over time. Gartner [projects](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) that by the end of 2026, 40% of enterprise applications will ship with task-specific AI agents, up from less than 5% a year earlier. IDC [expects](https://my.idc.com/getdoc.jsp?containerId=prUS52600524) AI to add a cumulative $19.9 trillion to the global economy by 2030, by then driving 3.5% of global GDP. As AI is continuously integrated into industry, and is responsible for increasing amounts of economic output, we should be extremely cautious of reward hacking, and more broadly [misalignment](https://www.anthropic.com/research/agentic-misalignment).

Labs must:

- [align our AIs](https://en.wikipedia.org/wiki/AI_alignment) and avoid this bad behavior entirely
- improve [monitoring](https://www.lesswrong.com/w/ai-control) and security to prevent catastrophic outcomes from AIs
- slowdown or [pause](https://www.wsj.com/tech/ai/anthropic-urges-global-pause-in-ai-development-flags-self-improvement-risk-99cefb73) AI capabilities
