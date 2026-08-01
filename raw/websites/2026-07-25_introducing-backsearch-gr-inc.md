---
type: article
title: Introducing BackSearch
source_url: https://www.gr.inc/releases/introducing-backsearch
author: General Reasoning (GR.inc)
date_published: 2026-07-24
date_ingested: 2026-07-25
status: processed
compiled_at: 2026-07-26
compiled_to: "[[src_introducing-backsearch-gr-inc.md]]"
tags: []
---

# Introducing BackSearch

**Release:** 24th July 2026  
**Source:** General Reasoning (GR.inc)

## Letting agents search the web as it was

Language models are increasingly asked to predict the future. The obvious way to check whether they are any good at it is to ask them about a future that has already happened. But you can only do that if you can hold the world still.

Quantitative finance solved a version of this problem with backtesting: replay a strategy against history and see how it would have done. That works because the input to a trading strategy is a price series, and price series can be truncated at a date. An agent's input is the internet. It learns about the world by making web searches and synthesising various sources of information. To backtest an agent you need the state of the web at a point in time.

Live search APIs with a date filter are insufficient for this purpose. They rank today's index with hindsight, and hand you today's bytes for a page that may have been rewritten since the event resolved. This means there is a risk of leakage.

BackSearch is our answer: two endpoints for searching and fetching the web over a frozen news archive. Every request carries an as_of date. Search returns only documents crawled on or before it, and fetch returns the article's text as it was archived at that time. The corpus never moves, so the same query with the same as_of returns the same results forever.

We're releasing BackSearch today as a narrow preview: news domains only, covering December 2025 to July 2026. We plan to widen the domain coverage and expand the backdated period following initial feedback.

## Quickstart

The base URL is https://search.openreward.ai. Authenticate with your existing OpenReward or_... key in the x-api-key header. There is no separate credential to obtain.

Each hit comes back with the archived URL, title, snippet, host, and two dates:

The one thing worth internalising: as_of gates on crawl_date, not on the article's own stated publish date. A page first archived after your cutoff will not be returned even if it claims to have been published before it. That is deliberate: a self-reported date is exactly the field a backdated crawl can't trust, and gating on the crawl is what guarantees nothing post-cutoff leaks in.

Fetch is the point-in-time counterpart. Give it a URL and a cutoff, and you get the extracted article text from the latest capture on or before that date: not today's version of the page.

## Give it to a model

Here it is wired to GPT-5.6 Sol through the OpenAI Responses API:

The model searches, reads a few of the pages it finds, and answers:

## What you can use it for

### Forecasting
Score a model on questions whose answers you already know, with the evidence horizon pinned before resolution.

### Quant Finance
Backtest a research-and-trade loop. Step an agent through a past window where it reads the news as it breaks.

### RL Environments
A stable, replayable web to train against for agentic RL environments and evaluations.

## Pricing

Pay-as-you-go against your prepaid OpenReward balance, with no subscription: $10 per 1,000 searches and $2 per 1,000 fetches. Only successful requests are billed — a search that errors, or a fetch that finds no capture on or before your cutoff and returns 404, costs nothing. An exhausted balance returns 402.

Check what you've spent with orwd usage or GET /v1/billing/api-usage.

## Inside OpenReward Environments

The same engine is available as a toolset on OpenReward, so an environment can hand its agent backdated web access without you writing any of the plumbing above. Declare it at the class level:

The agent gets web_search and web_fetch, both bounded to the cutoff. The cutoff resolves in order: an explicit as_of= argument, then env.web_as_of, then the OPENREWARD_WEB_AS_OF environment variable, then the backend default. For time-stepped environments, expose web_as_of as a property and the agent's window advances with your simulation clock — the world opens up one day at a time, as it did.

Outside an environment, the Backsearch and Backfetch classes in the Python SDK do the same job directly. Full details are in the backdated web tools docs.

## An early alp
