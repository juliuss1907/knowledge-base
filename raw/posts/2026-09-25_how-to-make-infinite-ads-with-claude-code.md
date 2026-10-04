---
type: post
title: "How to make infinite ads with Claude Code (Full Guide)"
url: https://x.com/shivsakhuja/status/2103379767311691891
author: Shiv (@shivsakhuja)
date_published: 2026-09-25
date_ingested: 2026-10-03
status: processed
compiled_at: 2026-10-04
compiled_to: "[[src_how-to-make-infinite-ads-with-claude-code]]"
source: x.com
---

# How to make infinite ads with Claude Code (Full Guide)

**Post type:** X Article (long-form), shared via https://x.com/shivsakhuja/status/2103379767311691891
**Article title:** How to make infinite ads with Claude Code (Full Guide)
**Author:** Shiv (@shivsakhuja)
**Published:** 2026-09-25 07:03 UTC
**Engagement at ingest:** 33 likes, 6 reposts, 19 replies, 71 bookmarks, 5,304 views
**Tweet text:**

> Our users have generated over 30,000 ad creatives with it in the last 2 months using this exact workflow. You can copy the workflow here for free and make creatives that actually feel like your brand. All you need is a Claude subscription + OpenAI key.

**Requires:** Claude Code + a Fal or OpenAI API key

---

Our users have generated over 30,000 ad creatives with it in the last 2 months using this exact workflow. You can copy the workflow here for free.

All you need is Claude Code + a Fal or OpenAI API key.

Here are some ads made with this exact workflow for one DTC brand Kolkata Chai.

![image 2103376683818774528](https://pbs.twimg.com/media/HTCx8yPbcAAcHgh.jpg)

This post walks through the whole system so you can build it yourself in Claude Code. If you'd rather skip the setup, there's a one-prompt install at the end.

## Who this is for

This is for founders and marketers at DTC brands who run Meta ads and always need more creatives.

If you keep running into creative fatigue and you want an AI agent like Claude Code to do most of the heavy lifting, this is for you.

If you don't know what creative fatigue is, it might be why your ads aren't performing.

## Why the usual ways don't work

Meta needs a lot of creatives to work well. Your success on Meta depends heavily on how many good creatives you can push. and how fast you can push them.

Most teams can't keep up with that. Designers are too slow to ship quality creatives at the volume Meta wants.

So people try AI. They use an AI creative tool, or they ask ChatGPT to make an ad. And it's usually disappointing. It's slow and inconsistent. The copy is bad, or it says things your brand would never say. The ads don't feel like your brand, the ideas are off, and everything starts to look the same.

What you actually need is a system around the model.

The agent needs knowledge so it understands your brand. It needs a skill so it knows how to do the work. It needs tools so it can actually do the work. And it needs a loop so it gets better every time you use it.

Here's what that looks like for ads.

## The system

Here's the entire system, in a nutshell.

![image 2103377682994176000](https://pbs.twimg.com/media/HTCy28daIAAZw-V.jpg)

This workflow is for static ad creatives, but a lot of the concepts are similar for video ads as well. I'll write an in-depth tutorial about video ads soon. Follow [@shivsakhuja](https://x.com/@shivsakhuja).

There are five steps. Let's go through them one by one.

## Step 1: Build a brand brain

A brand brain is just a folder that has everything about your brand in it. Claude reads it every time it makes an ad, so it never starts from zero.

Here's how I'd set it up:

![image 2103377778595028992](https://pbs.twimg.com/media/HTCy8gmbYAAEr06.jpg)

brand-brain/
├── brand-overview.md
├── visual-language.md
├── rules.md
├── judge-rubric.md
├── product-catalog/
│   └── <product>/
│       ├── notes.md
│       └── images/
└── creative-templates/
    ├── product-hero.jpg
    ├── ugc-testimonial.png
    └── before-after.png
campaigns/
└── <campaign>/
    ├── brief.md
    └── ads/
.claude/skills/make-static-ads/SKILL.md

What goes where:

- brand-overview.md: the basics of your brand.

- visual-language.md: how your brand looks, like colors, fonts, and logo usage.

- rules.md: your always and never list. It starts small and grows over time (more on that in Step 5).

- judge-rubric.md: what the judge checks every ad against (Step 4).

- product-catalog/: one folder per product, with notes and images for each.

- creative-templates/: ad templates you want to remix.

Shameless Plug: If you want this your whole team to have a brand brain like this, just install Gooseworks. It scrapes your product catalog and brand identity and manages the brand brain on its own. It also manages your generation rules, learns from your feedback, and is shared across your whole team. But you can also do this yourself by reading the rest of this guide! 

## Step 2: Get the skill

You'll need a Fal or OpenAI API key for GPT Image 2.5 Flare, and a good skill.

A great skill does five things:

1. Understands the campaign.

1. Grabs the relevant products from your product catalog.

1. Grabs a creative template from your templates folder.

1. Writes the prompt.

1. Sends the prompt, the product images, and the template to GPT Image 2.5 Flare at medium or high effort.

Here's a starting point you can drop into .claude/skills/make-static-ads/SKILL.md:

```markdown
---
name: make-static-ads
description: Make on-brand static Meta ads for a campaign.
---

1. Read the campaign brief in campaigns/<campaign>/brief.md.
   If there isn't one, write it and stop for my review.
2. Read brand-brain/ (overview, visual language, rules).
3. For each angle in the brief, pick the products from
   product-catalog/ and one template from creative-templates/.
4. Write an image prompt that follows rules.md.
5. Send the prompt + product images + template to
   GPT Image 2.5 Flare (medium effort).
6. Judge the result against judge-rubric.md.
   If it fails, send the image + an edit prompt to
   GPT Image 2.5 Sunburst, then judge it again.
7. Save the passing ads to campaigns/<campaign>/ads/.
```

If you want the exact skill file, install [Gooseworks](https://gooseworks.ai).

## Step 3: Write the brief before you generate anything

Have Claude write a creative brief first, and actually read it before any image gets made. If you skip it, a lot of your creatives won't make sense or they'll have bad angles and ideas.

A good creative brief includes:

- The goal

- Who it's for

- The products

- The offer

- The angles or concept

- Anything else that matters for this campaign

Bring your own angles if you have them. LLMs will often propose really generic angles, or angles that don't fit your brand at all.

Then make a lot of ads at once. You won't like every generation, so it's better to make lots of variants and pick the ones you like. It works out to about 10 to 20 cents per finished creative, so you can afford to.

Your templates give you visual variety. Your angles give you variety in the ideas. Use both.

## Step 4: Add a judge

When an image comes back, don't look at it yet. Let a judge look at it first.

I use Claude Opus 5.5 as the judge. It scores every ad against a rubric that lives in judge-rubric.md. Here's a starter:

![image 2103378533418713088](https://pbs.twimg.com/media/HTCzociawAAqrFF.jpg)

Score each ad pass/fail on:

- Hallucinations: anything invented that isn't in the brief, the catalog, or the template?

- Product accuracy: does the product match the catalog images?

- Logo fidelity: is the logo correct, undistorted, and placed where rules.md says?

- Brand identity: does it look and sound like us?

- add anything else you care about


If it fails: write a short edit prompt that fixes only the problem.

If the ad passes: you keep it.

If the judge wants changes, the image goes back to GPT Image 2.5 Sunburst with the judge's edit prompt. Sunburst is the better model for precise edits, so it fixes the problem without redoing the whole ad.

By default, our skill will try the fix 1-2x before giving up on an image. You can loop it more times if you like.

Pro tip: If the judge fails on too many dimensions, don't keep looping, it might not be worth it.

## Step 5: Turn your feedback into rules

Every time you review a batch and something's off, add it to rules.md. Things like:

- Never use this font.

- Never use this language.

- Always include the logo.

- Prefer the logo in the bottom left.

The skill reads these rules on every run, so it stops making the same mistake. Without this loop, you'll waste a lot of cycles fixing the same things over and over.

## What doesn't work

A few things I'd avoid:

- Generating with no template. GPT Image 2.5 does a great job working off your templates. It's much harder to get good ads from text-to-image alone. Templates matter a lot, so spend time finding great ones.

- Letting the LLM pick all the angles. You'll get generic ideas that don't sound like you.

- Skipping the brief. You'll end up throwing away most of the batch.

- Expecting every image to be good. It won't be. Make a lot and pick.

- Fixing the same mistake twice. If you correct something, turn it into a rule.

## Set it up in 2 minutes

If you want all of this without building it yourself, paste this into Claude Code:

Install the Gooseworks skills for yourself: in the terminal, run
`npx gooseworks install --all`. It'll open a browser to sign in and
set up the tools, then confirm it worked. Then run /gooseworks onboard me

That sets you up with our marketing skills, a brand brain, and the ad creative tools.

Then you can just say 
"/gooseworks plan my campaign and make me a batch of ad creatives"
