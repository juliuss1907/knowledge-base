---
title:
source: "https://defi0xjeff.substack.com/p/inference-is-the-new-oil-the-economics"
author:
  - "[[0xJeff]]"
date_ingested: 2026-04-21
created: 2026-04-21
tags:
type: "raw"
source_type: "article"
status: "unprocessed"
---
![](https://substackcdn.com/image/fetch/$s_!ZmSA!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f41ccd0-24d7-47cd-bc5b-ddad3aa98d82_1456x1048.png)

How the competition of AI progresses have been nothing short of exciting. We’re seeing new frontier models that get more intelligent every 6 months.

We also see new agent frameworks & harnesses that take these intelligent models and make them a lot more capable every single month — OpenClaw in Jan, Hermes last month.

The agents are getting so good and consume a lot of inferences to the point that Anthropic ban them.

### What we’re covering today

- **[Inference War](https://defi0xjeff.substack.com/i/193693272/what-were-covering-today)**: Why AI usage is exploding & why inference is the new oil
- **[Closed AI Labs](https://defi0xjeff.substack.com/i/193693272/the-economics-of-closed-ai-labs)**: How frontier AI labs subsidize power users to win enterprise clients and what their economics look like
- **[Open-Weight Labs](https://defi0xjeff.substack.com/i/193693272/the-economics-of-open-weight-ai-labs-full-stack)**: How open-source players compete with frontier players and what their economics look like
- **[Crypto AI Labs](https://defi0xjeff.substack.com/i/193693272/the-economics-of-decentralizedcrypto-ai-labs)**: How tokenized incentives drive growth in the inference economy and what their economics look like

## Anthropic is getting aggressive

You see, Anthropic heavily subsidizes its inference cost for users — for every max subscription ($200/month), up to ~$5,000 inference credits are given to them if they max out every week’s sessions.

This is their playbook

- Get power users to pay $20, $100, $200/month
- Subsidize them with more inference credits so they can build cool stuff
- Retain them with cool features like Artifacts, Claude Code, Cowork, Claude Browser, etc
- Hoping that these power users recommend Claude at work, talk about it on social media, and pull their friends & their companies into Enterprise deals

This model is similar to ChatGPT but Anthropic leans harder into developer/coder because their models excel at coding/agentic tasks.

Key thing here is “Subsidize power users to scale Enterprise clients”

This is all well and cool BUT Anthropic has been a lot more aggressive with this strategy in the past weeks

- Faster rate limits in each 5 window session (especially during peak hours)
- Outright ban on agents & harnesses like OpenClaw

People used to plug OpenClaw into Claude, utilizing Claude subscription. OpenClaw uses a lot of tools, it consumes a lot more tokens compared to normal chat or coding sessions. This result in $5,000 inference credit maxed out in each month which is bad for Anthropic.

So they ban the agents, to save up the compute/inference capacity for enterprise clients & for its own model training (”Mythos” which supposedly beat all the benchmarks vs other models)

Even though Claude workflows/features are great. The ban prompted many agent users to move from Claude to Codex. As an agent user, the only way to continue using Claude is to directly top up & buy credits which won’t make sense.

For those who want to save, open-source Chinese AI labs offer subscription package as low as $10/month (Opencode Go)with similar level of practical productivity to Claude $200/month subscription

---

## The Economics of Closed AI Labs

Major closed AI labs like Anthropic & OpenAI currently operates with heavy losses. They’re gambling that their frontier models stay meaningfully smarter than open-source alternatives + the sticky developer ecosystem they build (tools, agents, workflows, enterprise integrations) will give them pricing power and ~70-80% gross margins.

Akin to NVIDIA’s positioning & lucrative margins (~75% margins from monopoly-like dominance) that it enjoys on its chips today.

Right now closed AI labs are losing money subsidizing inference to grow adoption, but the long-term hope is that the moat lets them charge premium forever while costs continue to fall.

### What their PnL look like

![](https://substackcdn.com/image/fetch/$s_!Axni!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d1ebba5-e171-4e66-bafb-97d78b2d81dc_1200x675.png)

**Revenue drivers**

- Consumer subscriptions (~40-50% of revenue): ChatGPT/Claude Pro/Max tiers ($20–$200/mo). Subsidized heavily for power users to drive habit + virality
- Enterprise & API usage (~40-50%+ of revenue, highest margin): Committed contracts, high-volume API calls, dedicated quotas/SLAs. This is the “real money” — enterprises pay 2-5× more effectively than consumers
- Others (small but growing): Partnerships, fine-tuning services, agents/platform fee

**Cost drivers**

- Inference OPEX (70-90% of total costs now): The dominant line item. Running every query/chat/agent. This is the recurring “server bill” that scales with usage.
- Training CAPEX (one-time per model, but still huge): Amortized over the model’s life. Now only ~10-20% of lifetime spend per model.
- People + R&D + overhead (~10-15%): Engineers, safety, etc.
- Data center / infra overhead: Power contracts, networking.

Most of the costs aren’t for Training. They’re for running inference. While the cost for running inference (token cost) decrease at ~10x per year, usage is up 100x.

Revenue grows extremely fast but inference cost is growing even faster. Inference cost = everything required to generate one token/response in real time. GPUs/hardware contribute 40-60%, electricity 10-20%, and the rest is cooling infra.

This is why people say “invest in infrastructure that powers AI” — datacenters, GPUs, electricity, cooling are getting all the $$$.

But you know what toughest challenge for closed AI labs is?

It’s open-weight AI labs

---

## The Economics of Open-Weight AI Labs (Full-Stack)

Open-Weight AI Labs have been commoditizing intelligence faster than ever.