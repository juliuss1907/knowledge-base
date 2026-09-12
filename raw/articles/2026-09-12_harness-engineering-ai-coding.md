---
type: article
title: Harness Engineering
url: https://habitat-thinking.github.io/ai-literacy-superpowers/plugins/ai-literacy-superpowers/explanation/harness-engineering/
author: Birgitta Boeckeler (original), Habitat-Thinking (plugin adaptation)
date_published: 2026-09-12
date_ingested: 2026-09-12
status: unprocessed
source: habitat-thinking.github.io
---

# Harness Engineering

Harness engineering is the practice of surrounding AI-assisted code generation with deterministic tooling, agent-based review, and periodic entropy checks so that AI-generated code stays correct and coherent over time.

## The Origin

The term comes from Birgitta Boeckeler's article on martinfowler.com, written in the ThoughtWorks context of teams shipping real software with AI coding assistants. Boeckeler observed something that many teams had noticed independently: AI assistants produce plausible-looking code, but left unconstrained they drift. They forget conventions, repeat mistakes, and slowly erode the internal consistency of a codebase. The code continues to compile and pass tests. The degradation is quiet.

Boeckeler's insight was that this problem already has a solved analogue in software engineering: the test harness. Tests do not make code correct by construction. They detect when code stops being correct. A test harness is not a constraint on what code you write; it is a mechanism that continuously checks whether what you wrote meets a standard. The harness does not trust the programmer. It verifies.

The same logic applies to AI-assisted development, with one crucial difference. Test harnesses check functional correctness: does the program do what it is supposed to do? A harness for AI coding needs to check something broader: does the codebase still embody the architectural decisions, naming conventions, security constraints, and structural rules that the team has agreed on? Functional tests are necessary but not sufficient for this. You need a different kind of harness.

That is what harness engineering provides.

## The Three Components

Boeckeler describes three categories of concern that a harness must address.

### Context Engineering

An AI coding assistant can only work within what it knows. If it does not know that your project uses a particular logging library, it will invent its own approach. If it does not know that you never use mutable global state, it will use it when convenient. If it does not know that all database writes must go through a specific abstraction layer, it will bypass that layer.

Context engineering is the discipline of making sure the AI knows what it needs to know. In practice, this means maintaining a document — HARNESS.md in this plugin's conventions — that captures the stack, the architectural decisions, the naming conventions, the constraints, and the rationale behind each of them. This document is not a README for humans. It is a knowledge base for the AI. It needs to be accurate, specific, and kept current.

The distinction matters: a README explains what the project does. A context document tells an AI agent what it must and must not do, and why. These are different documents with different audiences and different update rhythms.

### Architectural Constraints

Knowing the rules and enforcing the rules are separate problems. You can write every constraint into HARNESS.md and the AI will still violate them, because the AI is a probabilistic system optimising for plausibility, not a rule-following machine. Context engineering reduces violations. It does not eliminate them.

Architectural constraints are the mechanisms that catch violations. Boeckeler calls the enforcement points "verification slots" — defined moments in the development workflow where a check runs and either passes or blocks progress. The key design decision for each verification slot is whether it uses a deterministic tool or an agent-based review.

A deterministic tool is a linter, a script, a regex check, a file-structure assertion — anything that produces a pass/fail result without judgment. These are preferable when the constraint can be expressed precisely. They are fast, cheap, and completely reliable within their specification.

An agent-based review is a language model looking at code against a constraint description and making a judgment. This is necessary when the constraint involves intent, semantics, or patterns that are difficult to express as a mechanical rule. Agents are more expensive and less deterministic, but they can catch things that no script can catch.

Both types of verification slots belong in a harness. The goal over time is to migrate constraints from agent-based to deterministic as your understanding of the constraint sharpens enough to specify it precisely. This is the progressive hardening principle.

### Garbage Collection

A codebase is a living system. Even with good context engineering and strict architectural constraints, entropy accumulates. Dead code grows. TODO comments persist for months. Dependencies go stale. Abstractions that made sense at one stage of the project become obstacles at a later stage. Conventions established early get quietly abandoned when they become inconvenient.

Garbage collection is the periodic process of fighting this entropy. Unlike the other two components, which operate at the moment of code generation or review, GC operates on a schedule. It is not triggered by a specific coding event. It runs because time has passed.

In a harness engineering framework, GC rules are explicit declarations of what "clean" looks like, paired with scheduled agents or scripts that check whether the codebase still meets those standards. The output is not a list of errors to block a PR; it is a report that draws attention to accumulating problems before they become serious.

## The Living Harness

The most important property of a well-maintained harness is that it is not static. A harness that was written once and never updated reflects the understanding of the team at one point in time. The codebase continues to evolve. New patterns emerge. Old constraints become irrelevant. New categories of AI-generated mistake appear that the original authors did not anticipate.

HARNESS.md is designed as a self-referential document. It does not only describe what constraints are in force; it tracks the status of each constraint: whether it is currently unverified, under agent review, or enforced deterministically. The document declares what should be true. Agents, hooks, and CI checks verify whether it is true. The harness auditor — a scheduled agent in this plugin — reads the results of those checks and updates the status entries in HARNESS.md to reflect reality.

This creates a feedback loop. The document is both a specification and a health record. Reading HARNESS.md at any point in time tells you not just what the team has agreed should be true about the codebase, but how well those agreements are actually being maintained.

The self-referential property is what distinguishes a living harness from a document that gets outdated and ignored. Because the harness itself is a target of enforcement — the harness-audit agent checks whether HARNESS.md accurately reflects the current state of verification — neglecting the harness becomes visible rather than invisible.

## Progressive Hardening

Not all constraints are equal, and not all constraints are ready to be enforced deterministically from the start. Progressive hardening is the promotion ladder that describes how constraints mature.

**Unverified** is the starting state. You have declared a constraint in HARNESS.md. You believe it is important. You do not yet have a mechanism to check it. This state is not a failure; it is honest accounting.

**Agent** is the second state. You have written an agent prompt that checks the constraint as part of PR review or a scheduled inspection. The constraint is being enforced, but by a language model making a judgment, not by a deterministic rule.

**Deterministic** is the final state. You have expressed the constraint precisely enough to encode it as a script, a linter rule, or a structural check. It runs in CI. It either passes or it blocks the merge. There is no judgment involved.

The direction of movement is always toward deterministic. When an agent repeatedly catches the same class of violation, that repetition is a signal: the pattern is now understood well enough to automate. Write the script, retire the agent check, and move the entry to deterministic status.

Progressive hardening prevents two failure modes: trying to enforce everything deterministically from the start (impossible for novel constraints), and accepting agent-based enforcement as a permanent state (expensive and unreliable).

## Three Enforcement Loops

**Inner loop (advisory, edit-time):** Lightweight checks on file save or session completion. Optimized for low friction. Makes problems visible early without stopping work.

**Middle loop (strict, PR-time):** Full suite of agent-based and deterministic checks on pull request. Has authority to block a merge. Main enforcement point for architectural constraints.

**Outer loop (investigative, scheduled):** Garbage collection rules, fitness functions, and harness audits on a schedule (daily/weekly). Produces reports rather than blocks. Findings feed back into the harness as potential new constraints.

Agents operate with bounded trust. No agent has unilateral authority to modify production code or merge changes. Agents review, suggest, report, and flag. Humans decide.

## The Self-Improving Dimension

After each coding session, a /reflect command captures what went well, what failed, what conventions were violated, and what new patterns emerged. These reflections accumulate in a learnings log. The harness agents read from this log when making decisions, so patterns of past mistakes inform current review.

Regression detection looks at the history of constraint violations to identify patterns: are the same constraints being violated repeatedly? If so, that is a signal that the constraint needs a stronger enforcement mechanism, or that the context document does not explain the rationale clearly enough, or that the constraint itself is wrong.

The auto-harness additions extend this further: the harness-init process reads existing code to infer constraints that are already present but not yet declared. The agent bootstraps a candidate HARNESS.md from observed patterns and asks the developer to confirm, reject, or refine each entry.

## Further Reading

Primary reference: Birgitta Boeckeler's article on martinfowler.com. Also Addy Osmani's [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/) which sharpens the model-plus-harness distinction and the "every line earned" discipline.
