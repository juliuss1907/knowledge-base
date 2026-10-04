---
type: video
title: "Gemini 4 Argon explained in 5min.."
url: https://youtu.be/1ZbNgx6Gscw
author: Caleb Writes Code
date_published: 2026-10-01
date_ingested: 2026-10-02
status: processed
compiled_at: 2026-10-02
compiled_to: "[[src_gemini-4-argon-explained-in-5min]]"
source: youtube.com
duration: "4:56"
video_id: 1ZbNgx6Gscw
transcript_language: en
---

# Gemini 4 Argon explained in 5min..

Caleb Writes Code · 2026-10-01 · 4:56

## Transcript

[00:00] It's been about 7 months since Google announced a new flagship model, Gemini 4 Argon. Even during Google IO back in May, I expected Google to drop Gemini 3.5 Pro. But Google has been releasing a lot of flash models instead. And a lot of them basically struggle to get market adoption given a variety of other flagship models and cheaper alternatives from Chinese open models. And Google finally made a flagship model with the code name Argon. And the preliminary benchmark show a pretty strong number as you can see. The first thing you might have noticed here is coding benchmarks. More specifically, scoring 77.9% on Deep

[00:33] SWE, which would put Gemini 4 Argon above every other model we currently have. But it's always good to have some healthy skepticism here. Recently, Epoch found issues on deep benchmark, finding 23 tasks that are flawed. And looking back to when the benchmark was actually released back in May, the entire 113 tasks and their solutions are made public, which means labs that have access to these could easily study them during post training and benchmarks their models around public benchmarks. And when we look at other benchmarks that Google reported here, a large majority of them are public. So the further we go out in time, labs that

[01:07] release their models later have a slight advantage to potentially include them during post training. And of course, as users, all of this makes it really difficult to track real progress in AI since so many public benchmarks like Deep Suite can be contaminated pretty fast. Not only that, benchmarks get saturated a lot faster now than before, which forces benchmarks to be refreshed more frequently. So, consumers now carry a huge burden keeping track of real scientific progress in AI. But regardless of the case, achieving this kind of leap in benchmark is a huge improvement from Google. Now when we take a step back and look at how Google

[01:41] is competing with other labs, a lot of people still primarily use clot code, codeex or open harnesses when it comes to coding. And despite being a strong model, Google still hasn't really solved making their harness anti-gravity a truly competitive option for developers. From a recent report, Codex has more than double the amount of weekly active users at 5 million compared to 2.4 million for anti-gravity. And on face value, Gemini 4 Argon currently undercuts both Enthropic and OpenAI when it comes to the cost of intelligence until the temporary discount ends and the price doubles again. But the cost

[02:16] benefit that we find here doesn't actually translate in Pareto Frontier. As you can see, Argon falls below the Pareto Frontier, showing you that Enthropic and OpenAI still leads ahead in both the harness and model adoption. Now, one angle we should think about though is the upcoming IPO for Enthropic and possibly OpenAI. While OpenAI and Enthropic have a huge incentive to subsidize the model through subscription pretty heavily to grow their users, Google already sits on top of one. And given that Google is already a publicly traded company, they want to be more careful about how to allocate their

[02:49] existing compute towards actually creating value within their ecosystem, which could help increase their perceived revenue. Even looking at how Argon is being rolled out in segments, the model is set to be made available to ultra subscription users and paid API users where there's already a huge revenue being captured instead of fighting the subscription race in channeling their compute towards that. On a recent Google's Q2 earning call, they said that their API is processing 22 billion tokens per minute, which is 6 billion more than the previous quarter. That's more than 11 quadrillion tokens

[03:21] per year in just API channel alone. And when you start factoring in other channels that Google owns in its distribution, we really get a closer picture into what Google really means when they said that they're supply constrained. And eventually, OpenAI and Anthropic will have to solve this scaling problem while maintaining healthy margins at the same time, not just subsidizing subscription to capture more users. So looking at Gemini for Argon, Google is demonstrating their capability in keeping pace at the frontier while they also try to figure out how to capture value at scale. One interesting note on Argon is how Google

[03:55] extended their output tokens from 64,000 to 1 million tokens. This might not sound like a big deal, but it's definitely a huge move from Google because maintaining coherence as auto reggressive models generate longer and longer tokens get increasingly difficult the longer the output tokens get. Scientists like Yen Lakun made criticism on auto reggressive models for this very reason where auto reggressively generating one token after another can compound errors over long trajectory, let alone 1 million from Argon. If you can imagine each token that's 99%

[04:29] reliable, chaining 100 independent steps together would leave about 37% chance of every step being correct. Now, of course, that's just in theory, assuming that every token error is independent. But the fact that Google has enough confidence to extend their commercial product to 1 million output tokens really opens up door for longer trajectory tasks like code migration and long-running research tasks that could benefit from a model that can generate
