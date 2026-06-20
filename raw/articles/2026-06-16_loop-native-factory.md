---
type: article
title: "Loop Native Factory"
url: https://bitsquarks.substack.com/p/loop-native-factory
author: bitsquarks
date_published: 2026-06-16
date_ingested: 2026-06-16
status: processed
compiled_at: 2026-06-17
compiled_to: "[[src_loop-native-factory]]"
source: Substack
---

# Loop Native Factory

**Author:** bitsquarks  
**Source:** Substack  
**URL:** https://bitsquarks.substack.com/p/loop-native-factory

---

By the end of this piece, you will know what changed when the loop replaced the keystroke as the atomic unit of software work, why most enterprises trying to go AI-native are accelerating in the wrong direction, what the new factory looks like in concrete architectural terms, the failure modes that have already cost public companies their headcount and their reputations, and the structural moves that make everything else compound. If even one of those reframes lands, the read will have done its job.

For most of 2025 we watched enterprise teams across the globe adopt coding agents the way the field told them to. Cursor for the engineers. Claude Code for the seniors. A pilot. A productivity number. A press release. The numbers were real. Acceptance rates climbed. Tickets closed faster. The dashboards looked exactly the way the vendor decks promised.

And six months later the same projects would come up for review and the conversation would be about why the wrong system had been built faster.

That gap, between generation and rightness, is the most expensive gap in software. I have come to think of it as the most important thing an engineering leader can manage. What I find genuinely useful about the gap is that it is not a mystery. It is structural. It can be named, decomposed, and engineered against. That is what this piece is about.

## The 1970s software factory standardized the process. The 2026 factory standardizes the loop.

That sentence carries more weight than it looks. The phrase software factory was first used at Hitachi's Software Works in Kamatsu in 1969, then spread across Toshiba, NEC, and Fujitsu through the 1980s. The model standardized process phases, measured everything (defects per KLOC, documentation pages, lines per programmer-hour), enforced reuse libraries, and trained relatively low-skilled programmers into interchangeable roles. Toshiba's software workbenches reached 50% reuse rates by the late 1980s. The model worked for narrow, repeating product families like mainframe COBOL and telecom switching. It broke when applied to novel problems. The Western reception, hostile to the implication of treating programmers as fungible, produced the Agile counter-revolution at Snowbird in February 2001. Agile got right that requirements are emergent and small empowered teams beat large process-bound ones. It got wrong that measurement was the enemy.

DevOps emerged from Ghent in October 2009 and collapsed the dev-ops boundary into continuous flow. SRE, codified by Google in the 2016 O'Reilly book, added error budgets and toil caps, restoring measurement on the outer loop without the brittleness of LOC counts. Platform engineering crystallized with Team Topologies in 2019 and Spotify Backstage in 2020, making the developer's environment the product. Each paradigm answered "how do we produce software at scale?" differently: by process, by people, by flow, by reliability budget, by paved road.

In every case, the unit of production stayed the same. A developer wrote code. A team shipped a feature. A program shipped a release. The atom did not move.

**The atom has moved. The atom is now the loop.**

A loop is a model running in a harness, with tools, against a context, under a policy, until a verifier terminates the work.

Every meaningful agent in production today is a loop in this sense. The coding assistant editing your file. The overnight migration agent rebuilding your Java 8 services. The reviewer agent catching bugs in the PR queue. The customer-support router triaging tickets at three in the morning. They all share the same five elements. Model, harness, tools, context, verifier. Around each loop sit six primitives that the harness has to manage: spec, context, tools, verifier, memory, policy. The visual below shows the geometry. Model in the middle. Verifier in blue, because it is the only thing that terminates the loop.

Loops compose. A coding agent's edit-test-fix loop nests inside a feature loop, which nests inside a delivery loop, which closes through a customer-state change. Anthropic's renamed Claude Agent SDK in September 2025 confirms the generality. It now powers almost all of their major agent loops. Community analysis of the leaked Claude Code source estimated roughly 1.6% of the codebase is AI decision logic and 98.4% is operational infrastructure: sandboxing, hooks, permission classifiers, context plumbing, sub-agent dispatch. The harness is where the work is.

When the loop becomes the atomic unit, three things change at once.

**The unit of production stops being deterministic.** The same prompt, run twice, produces different artifacts. Correctness is graded along a continuum. The verifier sits inside the production line and gates promotion before anything reaches the next consumer. Quality assurance is no longer a downstream stage. It is part of the production line itself.

**The marginal cost of generation collapses.** Senior engineers at the model labs ship dozens of pull requests a day with ten or fifteen concurrent sessions and have effectively stopped writing code by hand. Recent estimates put roughly four percent of public GitHub commits as Claude-Code-authored. Anthropic's own product page states that the majority of code at the company is now written by Claude Code. When generation is free, upstream alignment becomes the only thing that is expensive.

**The scaffolding gets absorbed by the model on every release.** Every clever workaround written this quarter becomes dead code next quarter when the model subsumes the capability. The harness has to compound capability rather than compensate for limits. This is the bitter lesson applied to agents.

These three changes do not just demand new tools. They demand a new operating model.

## The factory has three planes. Each runs continuously. Each fails differently.

**The inner loop** is where humans and agents collaborate inside a single problem. The IDE, terminal, and chat surfaces. The local sandbox. The structural test runner. The diff reviewer. The Microsoft-era inner loop of local code-build-test-debug maps cleanly here, with one change. The agent is now the primary editor. The human stays above the loop, scrutinizing artifacts at handoff boundaries.

**The outer loop** runs across problems. The PR queue. The CI/CD pipeline. The deployment system. The incident response stack. The customer feedback ingestion. The eval suite execution. This is where the multi-agent review pattern lives. This is where Cognition's settled position emerged: single-threaded writes, multi-agent intelligence around the writer. A manager agent spawns child agents through internal MCP for read-mostly subtasks. Only one writer mutates code at a time. A reviewer agent catching two bugs per PR with 58% rated severe is now production reality at multiple labs.

**The governance plane** runs orthogonal to both. It owns policy, which tools each agent class may call, which data each agent class may see, which actions require human approval. It owns evals, the proprietary scored test suite that gates promotion. It owns telemetry, the OpenTelemetry GenAI spans, OpenInference span kinds, agent trace stores. It owns the alignment graph that 8090 names as the substrate of bidirectional traceability. The governance plane is the part most enterprises do not have. Without it, the outer loop is a compliance event waiting to happen.

Humans operate above the loop. They specify intent. They approve checkpoints. They scrutinize artifacts at handoff boundaries. They adjudicate when the verifier disagrees with the producer. Agents operate inside the loop. They generate. They call tools. They write to the sandbox. They ask the verifier. They retry. They escalate. The factory floor's geometry is straightforward. Humans set the policy. Agents do the work. Verifiers grade the work. The governance plane records the trajectory. The harness compounds with every successful and failed loop.

Every prior factory had its boundary at the team interface. The loop-native factory's boundary sits at the policy layer. Why? Because the producer is non-deterministic. You cannot reason about an agent's output by reasoning about its source code. You reason about it through evals, traces, and policy. Wide structured events in unified columnar storage become the load-bearing wall of the entire system.

## Coding agents have quietly become the most capable code generation tools in history.

They understand codebases. They follow patterns. They scaffold entire applications from short prompts. If your problem is that it takes too long to write code, that problem is effectively solved.

If your problem is that the code being written is solving the wrong thing, coding agents do not help. They make it worse. Speed amplifies whatever is upstream. If your requirements carry invisible assumptions, the agent implements those assumptions at scale. If your blueprint compresses the customer's intent through five translation layers, the agent ships the compression as code.

Coding agents are exceptionally good at building things. They cannot, on their own, determine whether the thing is the right thing. That still requires alignment. And alignment still requires engineering.

**The bottleneck has shifted. It is no longer writing code. It is knowing what code to write, and why.**

8090 Solutions has crystallized this in their April 2026 Alignment Engineering series, the cleanest published statement of the principle I have come across. Their definition is the one to anchor on.

> Alignment is the convergence of multiple systems, people, documents, and code, onto the same understanding of what should happen and why.

When alignment holds, the customer's intent, the team's interpretation, and the software's execution all point at the same target. When it breaks, they diverge. The distance between them is the cost.

Alignment decomposes into five layers where it must hold. **Ontological:** do we agree on what things are? **Teleological:** do we agree on what success looks like? **Behavioral:** do we agree on what the system does in unplanned situations? **Temporal:** does this stay true over time? **Reflexive:** does the system know when it is drifting?

It decays under three forces. **Lossy translation** as intent moves through people and documents. **Butterfly-effect amplification** as small misunderstandings compound through the system. **Incentive drift** as teams optimize for the metric in front of them rather than the customer outcome behind it. There is no neutral position. The absence of active manufacturing means decay.

You do not achieve alignment. You manufacture it. Continuously. Deliberately. Or not at all.

## The loop-native factory decomposes into eight modules.

Each one owns a specific class of failure mode. The boundary between modules is the boundary between teams. The contracts between modules are the substance of the engineering organization's internal API.

**The Spec Module** owns intent capture. The customer-state map. The product requirement. The feature requirement. The technical requirement. Its failure mode is ontological drift, the same word meaning different things to different stakeholders. The non-negotiable invariant: specs must be machine-readable and bidirectionally linked to code.

**The Loop Runtime** owns the inner-loop execution. The agent loop, the sandbox, the tool layer, the memory file (CLAUDE.md, AGENTS.md), kept under roughly a hundred lines and only containing rules that fix recurring mistakes. Its failure modes are unbounded loops, runaway costs, and tool misuse. Anthropic's /loop and Claude Code's auto-mode classifier (84% reduction in permission prompts internally) are reference implementations. The non-negotiable: the loop must be observable and interruptible at every step.

**The Context Plane** owns retrieval. The codebase index, the semantic graph, the embedding store. The pattern that has surprised most engineers is that plain glob and grep, driven by the model, beat everything more sophisticated for a wide class of code tasks. Sourcegraph's RSG (Repo-level Semantic Graph) handles 90+ GB monorepos. Cursor's Composer-1 was trained via RL on Cursor-bench. Anthropic's MCP makes the context plane portable across harnesses. Failure modes: context starvation when the model does not see the right files, context poisoning when the model sees adversarial content. The non-negotiable: every loop trace must record what context was injected.

**The Verifier Bank** owns automated grading. Unit tests, structural lints, type checks, property-based tests, and the new addition of generator-verifier pairs where one agent's output is graded by another. The reviewer-zero-shared-context pattern works counterintuitively well. A reviewer agent without producer context catches more issues. Competitive parallel runs (the same task given to three model-harness combinations simultaneously, then comparing outputs) are emerging as a high-signal pattern for hard problems. The non-negotiable: the verifier must be cheaper than the producer. Otherwise the loop is uneconomical.

**The Policy Plane** owns what agents may do. Tool allow-lists, data scopes, auth gates, and the trifecta-cutter. Any agent must lack at least one of: private data access, untrusted content exposure, ability to externally communicate. Real incidents have hit GitHub MCP, Writer.com, GitLab Duo, Microsoft 365 Copilot (CVE-2025-32711), and Gemini Enterprise.
