---
type: post
title: "save it > run it tonight"
url: https://x.com/alexsssaint/status/2102420062023946602
author: alex saint (@alexsssaint)
date_ingested: 2026-09-23
status: unprocessed
source: x.com
---

# save it > run it tonight

$38,914.11 in the wallet. Up $3,286.35. Plus 9.22%.

I did not place any of those trades. A model answers one question every 15 seconds, and a second model rewrites the first one's rules at three in the morning.

A tweet in Morse code pulled $175,000 out of an AI's wallet in May. This is the whole build, including the part that makes that attack do nothing.

## who is writing this

I build in public and I post the numbers either way. Not sponsored. Nothing is gated, nothing is sold at the end, the method is the numbered part below.

What runs right now: one $8 VPS, two models, two wallets. The wallet is called JEV TEST because that is what it is, a test I am running where you can see it. It sits at $38,914.11, up $3,286.35, and it has been running since the week Jev shipped.

Eight days. I will say it before you do. Eight days is a sample, not a track record, and anyone annualising 9.22% in their head right now should stop. The loop has been right more often than wrong so far, which was also true of every strategy in the week before it stopped working.

Your feed has been wall to wall Jev for a week. Demos, takes, threads about a model most of the posters installed an hour before posting. Almost nobody has shown it deciding anything that costs them money.

Mine decides every 15 seconds against a live Solana wallet. That is the only reason this article exists.

If you already run agents against a live wallet, skip to step 7. Step 7 is the one most people get wrong.

## what's inside

- what Jev actually is, and why a chat model cannot do this job
- the three question types, with the trading version of each
- why I never hand the model a number
- the twelve words that are the entire state
- the nightly rewrite, and the paper it comes from
- the gate that stops a model editing its own rules
- the two wallets, and why no model has ever seen a key
- what it costs, what broke, and the FAQ

## the reframe

Most people building this pick a model, then argue about which one.

Between 18 October and 3 November 2025 a benchmark called Alpha Arena gave six frontier models ten thousand dollars each of real money and identical prompts. Same market, same fees, same instructions.

Qwen3 Max finished up about 22%. GPT-5 finished down about 59%. Every US flagship ended underwater, Claude included. Check the leaderboard yourself, it is public.

Identical prompts. Roughly eighty points of spread.

And you are not trading against people anyway. In March 2026 humans moved $6.7 billion on Solana DEXs. Bots moved $134.1 billion.

So the model is not the edge. The prompt you wrote on day one is not the edge either, because it was written by someone who had not yet watched it lose.

The edge is having something that reads yesterday and rewrites the prompt tonight.

That needs two models at two speeds: one too fast to think, one too slow to trade.

## 1. use a decision model, not a chat model

A chat model writes you a paragraph about the market. You then parse the paragraph. That is two failure modes stacked on each other and it costs you a second and a half.

I use Jev, from TypeSafe AI, built by Diogo Almeida, who co-created ChatGPT and RLHF and then spent two years in stealth on a different way to train models. It came out on 15 September 2026, eight days before I wrote this. It does not generate text. It takes a state and typed questions, and returns the answer with a probability on it, in one pass. TypeSafe publishes 70 to 500 milliseconds and $0.042 per million input tokens, output free because there is no output. Those are their numbers, not a benchmark anyone independent has run yet. The one below is mine.

Their CEO put it better than I can: sequential LLMs are "totally useless for computers".

Copy this and you have the loop's heart:

```shell
curl -s https://api.typesafe.ai/v1/systemone \
 -H "authorization: Bearer $TYPESAFE_API_KEY" \
 -H "content-type: application/json" \
 -d '{
 "model": "jev-latest",
 "state": "thin bot_war pumping violent flat green wide calm early mid quiet held",
 "questions": {
 "action": {
 "type": "choice",
 "instructions": "buy on strength only when the book can absorb it",
 "criteria": {
 "buy": "the move is strong and depth is not thin",
 "sell": "the move is fading or fees are climbing",
 "hold": "anything else"
 }
 },
 "skip_this_cycle": {
 "type": "noul",
 "instructions": "conditions are too hostile to trade at all"
 }
 }
 }'
```

What comes back is already a decision, not a paragraph to parse:

```shell
{
 "action": { "type":"choice", "choice":"hold",
 "probabilities": { "buy":0.11, "sell":0.08, "hold":0.81 },
 "confidence":0.81 },
 "skip_this_cycle": { "type":"noul", "noul":0.22 }
}
```

Three ways to ask, and you will use all three eventually:

- **choice**: pick one from a list you define. "buy, sell or hold."
- **score**: rate against a scale you define. "how hostile is this book, calm to unfillable."
- **noul**: a yes or no returned as a probability, not a flag. "conditions are too hostile to trade at all."

Ask all three about the same state in one request and they come back in parallel. One question or fifteen, the response time barely moves. That matters for the bill later.

The part that makes the whole loop possible is the confidence. Jev is trained to be calibrated, which means when it says 0.8 it is meant to be right about eighty percent of the time. A chat model that sounds certain gives you nothing to audit. A calibrated number does. Every night the slow model goes looking for the cases where 0.8 was wrong, and that search only means something if 0.8 meant something.

High confidence, act on it. Low confidence, hold. That rule is two lines of code and it is most of the risk management in this system.

In my loop each answer takes 0.3 seconds and costs $0.00002.

## 2. never hand it a number

This is the step people argue with, so the research goes first and it is short.

Models do not read numbers, they read tokens. The same number splits differently depending on what sits next to it: 87439 becomes 874 and 39 in one place, 87 and 439 in another. Arithmetic runs right to left. Generation runs left to right. The canonical failure is a model ruling that 9.11 is larger than 9.9, because the suffix tokenises as its own comparable number.

You were about to hand this thing your slippage.

So the code does the arithmetic and hands over an adjective:

```shell
// thresholds are yours, they live in code, and they are testable
const depth = slippage1k > 0.006 ? "thin" : "deep" // 0.0087 -> thin
const fees = feeRatio > 2.5 ? "bot_war" : "quiet" // 3.2 -> bot_war
const move = return15m > 0.02 ? "pumping" : "flat" // +0.034 -> pumping
const vol = stdev > 0.008 ? "violent" : "calm" // 0.0091 -> violent
```

Those four cut points are mine and they came from watching, not from theory. Yours will be different. The shape is the part that transfers.

The model never sees a decimal. It sees "thin bot_war pumping violent" and it is very good at that.

## 3. keep the whole state to twelve words

Not twelve fields. Twelve words.

```shell
thin bot_war pumping violent flat green wide calm early mid quiet held
```

Every extra word is another dimension the model can flip on, and a flip is a fee. Small state, fewer flips. Twelve is where mine stopped helping.

## 4. ask one question that can only be answered one way

Not a conversation. Not a persona. A choice with three criteria and a confidence attached, plus one noul that can veto the whole cycle.

That second question is cheap insurance. It rides the same request, and a bot that can answer "do not trade at all right now" beats a bot that must always pick one of three.

The instruction line and the three criteria are in the request above. Copy them, then let the night shift rewrite them for you. Mine have been rewritten more times than I have written them.

## 5. log every answer with its confidence

One line per decision, append only:

```shell
{"t":"2026-09-22T14:03:15Z","state":"thin bot_war pumping violent flat green wide calm early mid quiet held","action":"hold","conf":0.81,"skip":0.22,"px_in":null,"px_15m":-0.004}
```

The last field is the one that does the work: what the price did after the model was sure.

You will never read this file. It is not for you. It is the training material for the night shift. Without it the loop repeats its first opinion forever.

## 6. give the night to the slow model

```shell
0 1 * * * cd /srv/jev && node night-rewrite.mjs >> /var/log/jev-night.log 2>&1
```

At 01:00 that wakes Fable 5.1.

It does not read all 5,760 lines. A raw day is about three hundred thousand tokens and most of it is the loop agreeing with itself. It reads the disagreements: every cycle where confidence was above 0.8 and the next fifteen minutes went the other way, plus a one-line summary of everything else. That is a few thousand tokens. Then it writes new instruction text for step 4.

8.8 seconds, and a few cents.

Compress the log before the night run or this step quietly becomes the most expensive thing you own.

And it is not my idea. There is a paper called GEPA, an ICLR 2026 oral, that does exactly this: reflect on your own traces in plain language, rewrite the instructions, repeat. It beats reinforcement learning by up to 19 points using up to 35 times fewer attempts. Writing down why you were wrong beats gradient descent on the same budget. I pointed it at a trading log.

## 7. the night model proposes. it does not deploy.

Here is where the Morse code comes back.

On 4 May 2026 someone replied to Grok in Morse code. Grok decoded it into plain English. Bankrbot, the finance agent listening downstream, read the decoded English as an instruction and executed a transfer. Three billion tokens gone, about $175,000, the price down 40% in minutes.

No exploit. No stolen key. No compromised model. And Bankrbot had once had a hardcoded block on Grok-originated replies. It was dropped in a maintenance rewrite.

A model that can rewrite the rules of something that spends money is the same shape of risk with better manners. So:

```shell
night-rewrite.mjs writes -> proposals/2026-09-22.json (never the live prompt)
Telegram gets the diff -> I approve or I do not
approved -> prompt.v(n+1).json, one version per rewrite, all kept
```

Mine is a tap on my phone. A test suite is stricter and I will get there. Either beats the third option, which is nothing.

Anything that can change how money moves gets a human or a test between the idea and the execution.

```shell
Phantom holds everything signs only on a tap never on the server
Bot wallet holds the stake only fresh keypair on the VPS swaps via Jupiter
```

Profits sweep to Phantom every night. Worst case the hot wallet loses what is in it, which is a number I chose while calm.

Neither model has ever seen a key. Jev sees twelve words. Fable sees a log. The keys live in code that neither of them reads.

## 9. run it somewhere that cannot take you down with it

Hermes Agent, from Nous Research, on a $8 VPS. Launched February 2026, around 214,000 GitHub stars. It keeps the loop alive, restarts it when it dies, and pings Telegram when something needs me.

Not your laptop. Your laptop closes.

## the scar

Nothing has blown up yet, and I am not going to dress that up as a war story.

Eight days is exactly the length of time in which a loop like this looks like it works. The failure I expect is not a crash. It is a 01:00 rewrite that reads perfectly at 01:00, tightens a rule that did not need tightening, and quietly costs me a percent a day for a week before I notice, because the loop will keep answering confidently the whole time.

That is why step 7 exists, and why the gate is a tap and not a cron. When it happens I will post the number the same way I posted this one.

## what it actually costs to run

- VPS: $8 a month.
- Jev: $0.00002 an answer. The request above asks two questions per cycle, so 11,520 answers a day. That is $0.23.
- Fable: one run a night, a few cents.
- Solana fees and Jupiter slippage: the only line here that scales with your size, and the only one worth modelling before you start.

Under thirty cents a day of model, plus a five dollar box. The compute is lunch money. The risk is the stake.

## will this work for you

Honestly: the loop will work. The strategy is yours and it might be bad.

What is in this article is a machine, not an edge. Two models at two speeds, words instead of numbers, a log, a nightly rewrite, and keys the models cannot reach. All of it transfers to things that are not trading. Point it at ad bids, at inventory, at support triage, at anything that makes the same small decision thousands of times a day and leaves a trail.

If you do point it at a market, size the hot wallet at what you can lose outright.

## faq

**Is this just riding the Jev hype?** Both things are true. The trend is real and I am in it. The difference is that this one has a balance attached, and I will tell you exactly how long it has been running and on what.

**Why not just use Claude for the 15 second decision?** Cost and latency. Fable is 8.8 seconds and $0.014 per call for me. At one call every 15 seconds that is a bill in the hundreds of dollars a day and a loop that misses its own window. The slow model gets one call a night, where it is worth every cent.

**Is the model picking the strategy?** No, and this is the most common misread. Jev answers one question. The thresholds that turn numbers into words, the position sizing, the gate and the wallet split are all code I wrote and can test. The model is a judgment layer, not a trader.

**What if the API call fails?** No answer means hold. Make that the default in your code before you make anything else work, because the failure mode of a trading loop that guesses on timeout is the expensive one.

**What if the night model proposes something bad?** It proposes to a file. I read the diff on my phone. Step 7 exists for exactly this.

**Does this only work for trading?** No. Point it at anything that makes the same small decision thousands of times a day and leaves a trail. Ad bids, inventory, support triage. The market is just the version where the feedback arrives in fifteen minutes instead of a quarter.

## the short version

- Fast model decides, slow model rewrites the fast one's rules. Never one model doing both.
- Do the arithmetic in your code. Hand the model adjectives, never decimals.
- Whole state in twelve words. Every extra word is a flip, and a flip is a fee.
- One typed question with fixed answers, plus a noul that can veto the cycle.
- Log every decision with its confidence and what the price did next.
- Cron the slow model at 01:00 against the disagreements, not the whole log.
- The night model writes a proposal. A human or a test approves it. Always.
- Two wallets. The hot one holds the stake only. No model ever sees a key.
- Run it on a $8 box under something that restarts it and pings you.

## sign-off

The interesting machines this year are not the ones that think harder. They are the ones that keep a diary and read it back.
