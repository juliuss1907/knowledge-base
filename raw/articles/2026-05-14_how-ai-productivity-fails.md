---
title: "How AI Productivity Fails"
author: "Shrivu"
source_url: "https://open.substack.com/pub/shrivu/p/how-ai-productivity-fails"
date_published: 2026-05-14
date_ingested: 2026-05-14
type: article
main_tag: ai
sub_tags: [productivity, engineering]
topic: ai-productivity
---

# How AI Productivity Fails

Most AI users today get ~10–20% more productive no matter how "game changing" they claim it is or how many lines of code they output. Yet, I still think **2x or even 10x+ is both real and reasonably expected**. Real transformation requires two changes at once: **personal practice and organizational refactoring**. Whether the output lands as 10x leverage or 10x slop depends on the practice and the org around it.

So far in 2026, I've seen **exponential increases in output but linear increases in realized impact**. This post covers some of the issues I've found "debugging" the issue.

---

## Personal Pitfalls

### 1. No Planning, Just Generation

AI removes the friction that used to force planning. Without something pushing back on bad abstractions, the upfront thinking gets skipped silently. You ship systems you can't debug or extend, full of blanks AI quietly filled in.

**Fix:** Outline first: headers, structure, audience, plan, principles, what-done-looks-like, then let AI fill it in. Review shifts up the stack: outcome-vs-plan instead of line-by-line. The interrogation belongs inside planning: spawn subagent critics to red-team the plan before you let anything generate against it.

**The easy review at the end is only easy because the hard review at the start was good.** If you find it taxing to review your own AI generated output, [you didn't shift left](https://en.wikipedia.org/wiki/Shift-left_testing).

### 2. Tasks Too Small

Context overhead doesn't shrink with task size, and small tasks are mostly edges. AI handles the middle 80% of work well but can be brittle on the first and last 10%: setup, edge cases, final-mile review.

With AI, often a two-line fix pays the same setup cost as a full feature. So you spend more time briefing the agent than just writing it. Even then it lacks context, ships something subtly wrong, and you redo it.

**Fix:** Lift task ambition until the context cost is justified. The heuristic: if it's smaller than a meaningful unit of work (a PR, a section, a chart, a campaign), it's probably too small. Starting "small" with AI might be the reason you don't graduate to larger leaps of AI-driven outcomes.

### 3. Cognitive Ceiling on Parallel Agents

AI scales generation, not your human-bound working memory. The ceiling on parallel agents is how many threads a human can hold without dropping context or understanding, and that number is small.

You either single-thread with a coffee break while you watch it code or overshoot and abandon five threads.

**Fix:** Stay at ~three or fewer active in your cognitive window, or close the loop (next section) and pull fully out. If you are only running a single session at a time, you are probably not delegating enough. If you are struggling to manage dozens of sessions, consider whether you even need to be "managing" them, whether sessions should take longer leaps (fewer agents that do more work), or to intentionally stay linear until you invest in the right skills and context.

### 4. The Last 1% Requires You

Closing the last 1% is verification infrastructure and an incredibly well-defined definition of done: a different discipline than generation, so people skip it and layer AI on top of existing handoffs instead. You become the screenshot human, the agent waiting on your click or upload to validate.

**Fix:** Close the loop end-to-end: tests, queries, sandboxes, browser tools, type checks, real API responses. Whatever lets the agent see its own output and iterate without you. Before automating the surrounding process, delete it.

Closed loops are how you exceed the ~3-agent ceiling: work runs underneath your cognitive window because it doesn't need to be in it.

**AI can handle the "fuzzy" verifications well too with the right pre-defined context**, including the "does this actually make sense for long-term system architecture" and "is this the right feature to be adding to the product" questions.

### 5. Not Codifying Taste

Our chat interfaces often treat every session as ephemeral. Taste is a reusable artifact, but the interface gives you nowhere to deposit it. So encoding never starts, or you overcorrect and write one skill per task, ending up with a directory of one-shots nobody else can use.

**Fix:** Build skills for the class of task, not the instance. Some are specs (how to do a thing); others are principles (how to think about a class of things). The durable artifact is the skill (often literally some markdown file), not the prompt.

The recognition signal is concrete: **any time you find yourself editing or "bullying" the output for a better answer, that's a rule you can codify once and stop bullying forever.** Consider even meta skills that regularly take feedback and make the right skill or context modifications from accumulated learnings.

**Refuse to edit an AI output manually** or in a way that doesn't feed into learnings for next time. Tell it why it's being dumb, how you think, and make sure that sticks for next time.

### 6. Skill Atrophy

Skill comes from cognitive struggle, and AI removes the struggle by completing the thought before you've had it. The learning loop never closes—you can't tell when the model is wrong, you can't operate without it, the domain skill quietly atrophies.

You grow through resistance: edit, interrogate, override.

**Fix:** Bootstrap by using AI on tasks where you're the domain owner, so the friction is real and the corrections you push back are correct. **Juniors get hit hardest:** they offload cognition before building the capacity to evaluate output.

The people who can evaluate (taste-holders, domain owners) need to be the ones encoding skills and quality-bars even if traditionally the Super Senior ICs and managers used to not touch the codebase.

No task should be permanently too hard for an AI system and as it learns, **human effort moves up the stack to architecting the system AI builds**: a place where AI is genuinely worse and the friction lives. AI will get good at that as well, so you just [keep moving up to harder and harder meta derivative skill building](https://blog.sshh.io/i/185693126/you-can-work-on-the-derivative).

---

## Organization Pitfalls

The personal pitfalls above and the organizational ones below are one problem at two scales. AI optimizes individual roles but leaves the process that constrains them intact. Personal practice is where you collapse the steps; organizational design is where you collapse the handoffs. **The gains only show up when there's shared ambition large enough to do both.**

### 7. Rewarding Usage, Not Impact

Usage is easy to measure; impact is hard. Managers and leadership often carry the cultural pressure to praise visible use over invisible value. Tokens land in perf reviews and in the next cycle Claude loops get left running to inflate counts. Teams ship new AI-shaped systems instead of fixing the existing ones that matter.

**Fix:** Reward what shipped, not what got used. Track usage as a leading indicator for enablement and resistance (where to focus training and tooling, especially early in a rollout), but never as the long-term goal.

**Critically:** Pure short-term impact with no recurring AI-powered leverage (often) does not maximize long-term business goals. **Weight outcomes by the reusable leverage they leave behind:** closed loops, AI-friendly architected systems, codified skills, shared context that make the next ship exponentially cheaper than this one.

### 8. No Curator After Build Cost Fell

Build cost used to be the de facto curator. Only worthwhile tools got built. AI removed that filter without replacing it, people keep shipping, and not everyone has the right taste filter. Discovery becomes harder than building another tool, and context gets inconsistently duplicated across teams and roles.

**Fix:** An architect-owner at the top should be accountable for the taxonomy across what you build, what you buy, and which providers you standardize on.

**Pilots at the bottom**—small, scoped, not broadcast prematurely—are how new tools earn graduation, with telemetry and explicit retirement criteria so dead tools get pulled. Consolidate tools where you can and enforce a maintained shared context layer they pull from.

### 9. Skills Without Taste-Holders

Authoring used to require the expertise being authored. AI broke that coupling, so production no longer signals authority. You get ten invokable ways to do anything, knowledge fragmented across wikis and CLAUDE.mds, personal skills bleeding into shared with no quality bar.

**Fix:** A top-down architect or domain-expert should decide the core skill set and assign ownership to the taste-holders who'll build it. **If the people who know what good looks like aren't writing the skills, the skills are mediocre by default.**

Personal vs. shared context is an explicit split: personal skills can be loose, shared skills are operating practice and have to be built like one, with review and a real quality bar.

### 10. Review as Bottleneck

Generation outpaces review, AI doesn't progressively disclose, and authorship gets fuzzy when "the prompt" wrote it. Long docs nobody reads, PRs reviewers can't keep up with, slop ships because no one wants to compromise "productivity".

**Fix:** Hold people accountable for the artifact even when AI generated it; build pushback culture with harsh, specific feedback when output crosses into slop.

Use AI and assume that at the end of the day **all content will be AI-generated.** And despite this, you have to understand what you ship well enough to defend it under questioning.

Reviewers should refuse to be the debugger of last resort. People shipping AI output need domain ownership themselves with consistent reliance on skills built and maintained by domain owners.

### 11. Handoffs, Not Loops

Most orgs are organized by function, so getting anything done means handoffs. Coding was always ~20% of the cycle; the other 80% (approvals, reviews, syncs) was the rest. AI (if you are doing it right) compressed the 20% to near-zero, leaving the 80% as the entire bottleneck.

A 5-minute fix sits 3 days in review; sync meetings spring up to unblock work AI already finished.

**Fix:** Loop ownership should replace function ownership: **one person closes the chain from problem to deployment**, with the right guardrails so they can move without sacrificing function-level taste.

Specialists shift to platform—encoding their taste into the systems, prompts, and context that loop owners' agents use. Bottom-up speed alone hits a wall here; the org has to reorient around loops to absorb the acceleration. This is called [transposing your organization](https://blog.sshh.io/p/the-transposed-organization).

### 12. Mandates Without Taste

Mandates transmit behavior, not taste or judgment. Without ground truth at the top, each layer strips intent on the way down. Engineers get pushed into reviewing AI slop instead of being elevated into architects of it—the job becomes downstream cleanup, not upstream design, and replacement fear takes root underneath.

**Fix:** Mandate is still a powerful lever. What's often missing is clarity: explicit expectations, updated role-definitions, and the why behind the importance and urgency of AI adoption.

Be intentional about when top-down is the right lever and when bottom-up is. And don't kill the fun of building. People like building things and you want people to like what they do — it's the top-down's job to make sure they are building useful things.

### 13. No Shared Target

Bottom-up energy needs a target to compound against. Without a shared definition of return, every team optimizes locally and the gains never aggregate. Usage looks great while token spend decouples from business outcomes, and sprawl goes unchecked.

**Fix:** Make ROI legible: every team articulates return on its AI investment, even crudely. Wire working behaviors—closed loops, codified skills, outcome-aligned spend—into career pathways so the right behaviors get rewarded structurally, not just culturally.

---

## Summary

The 2x version of you isn't a token-count away. AI multiplies what you already do well and whatever your org already enables.

- **If your practice is loose, AI compounds the looseness.**
- **If your org runs on handoffs, AI accelerates the frequency of handoffs.**

Both have to change at once, or neither change matters.

The 10–20% is free at this point. Anything past that is rebuilding: personal practice on one side, organizational design on the other. I think most folks still have an uncomfortable amount of self-refactoring left to do.
