---
type: raw
source_type: article
source_url: https://brgsk.xyz/agent-memory-anatomy/
date_ingested: 2026-05-27
tags: [ai, agents, research]
status: processed
compiled_at: 2026-05-27
compiled_to: "[[src_agent-memory-anatomy]]"
---

# Agent Memory: An Anatomy

**Source:** brgsk.xyz  
**URL:** https://brgsk.xyz/agent-memory-anatomy/  
**Ingested:** 2026-05-27

---

## Original Content

every agent memory library uses the same words: episodic, semantic, sometimes procedural. they're cognitive science's vocabulary, lifted into the API. the engineering often isn't lifted with them. a library can have a procedural field that uses the same storage and retrieval as semantic — a label, not a separate system. the deeper slip is the word memory itself: most of what these libraries build is narrower than that, and the narrower term sharpens the problem.

the terminology comes from a 1972 chapter by Endel Tulving. he argued that what people had been treating as one thing — memory — was at least two: memory for events (what happened, where, when), and memory for facts (the capital of France, water's boiling point). he called them episodic and semantic. they behave differently and they fail differently.

most of what these libraries call "memory" is narrower than the word suggests: not a full cognitive memory system, but autobiographical content about the user held on the user's behalf — where they live, what they're working on, what they've decided.

## the anatomy of an agent memory system

an agent memory library is built from a small number of components. you can read any library's docs by knowing the parts.

the extractor. the thing that reads conversation transcripts and decides what to keep. usually an LLM call, sometimes with a strict prompt or a typed output schema. it produces statements — short, abstracted facts about the user, the world, or the task.

the most consequential choice an extractor makes is timing. extract eagerly, after every message, and you spend tokens on small talk that goes nowhere. extract lazily, at the end of a session, and the context you needed to resolve a pronoun is already gone. neither timing is wrong; each loses something the other keeps. the question worth asking of any library is what gets thrown away — coreference cues (which "he" refers to which person), temporal anchors ("yesterday," "next week"), and disambiguating local context are common casualties. extraction is, in cognitive terms, a compression from situated event to decontextualized fact: user mentioned over coffee on Tuesday that they prefer TypeScript becomes user prefers TypeScript. how aggressively a library compresses is one of its central design decisions.

the store. the database. one or more of: a vector index (entries indexed by semantic similarity), a relational table (entries indexed by columns you can filter on), a knowledge graph (entries connected by typed edges). each statement carries metadata — a timestamp, sometimes a confidence score, sometimes a source pointer back to the original conversation.

the hardest question a store answers isn't where to put things. it's what to do when a new statement contradicts an old one. the user lived in Paris until April, then moved to Amsterdam — and the store now has both, each presenting as current. the choice is whether to

- overwrite (one truth, no history)
- append (both, leave it to retrieval to sort out)
- keep both with the old marked as superseded.

a store that can't answer what did I believe last month? isn't a memory system. it's a snapshot with a timestamp on it.

the retriever. at query time, this component turns the current question into a search and returns the statements most likely to be relevant. vector similarity is the baseline. keyword search on top of that is common. a reranker is the standard third layer. structurally this is RAG; the corpus is the user's accumulated statements rather than a document library. some libraries also run a time filter (don't return statements known to be out of date) and a presupposition check — detect when the question itself assumes a stale fact and block it from being pulled into context.

every difference between agent memory libraries lives in one of these three parts. you can describe any library in terms of them without yet knowing what it's for.

## the kinds of memory

cognitive science's canonical taxonomy consists of four kinds: episodic, semantic, procedural, and working. working memory in agents is the context window — a different machine from the one this post is about, worth setting aside. that leaves three. add prospective — it isn't in the canonical taxonomy, but it names a gap the field hasn't filled.

**episodic memory.** specific events tied to a time and place. I had coffee with Aleksandra last Tuesday at the place on Mostowa. the memory is dated, situated, and personal. you experienced it. recall feels like re-experiencing — you can place yourself back in the scene.

agent memory libraries handle this with a table of timestamped statements. user mentioned they live in Berlin (2026-03-14). each entry is a single event the system observed. some libraries keep the raw conversation episode alongside the extracted facts.

**semantic memory.** facts about the world that aren't tied to any specific event. Berlin is the capital of Germany. the boiling point of water is 100°C at sea level. you know these things; you can't usually recall when you learned them. the knowledge is decontextualized.

most of what people mean by "agent memory" is this. user prefers TypeScript started as an episodic observation — they said it on Tuesday — but by the time it lands in the store, the context is gone and what remains is a fact about the user, true until contradicted.

**procedural memory.** knowing how to do things. tying shoes, riding a bike, the muscle memory of a keyboard shortcut. you can't usually verbalize procedural memory — try explaining how you keep your balance — but it shapes behavior reliably.

procedural memory is the cleanest litmus test for the gap between what a library claims and what it implements. LangMem treats it as a distinct mechanism — evolving the system prompt from scored trajectories, so what's remembered isn't a retrievable fact but a behavioral disposition encoded in instructions. Mem0 exposes the procedural label but writes it into the same index it uses for facts — metadata.memory_type = "procedural" is the only difference. Graphiti doesn't expose procedural memory at all; everything lands in the same bitemporal graph regardless of source.

**prospective memory.** remembering to do something in the future. don't forget to send the contract tomorrow. next time the user asks about pricing, mention the new tier. prospective memory is one of the most studied failure modes in humans — people forget intentions far more often than they forget facts. the closest analogs in production are scheduled triggers in agent frameworks; they solve the do Y at time T case but not the harder do Y when condition X next appears, which is the form prospective memory actually takes. no production library I've seen ships this. open territory.

## what these libraries actually are

of these four kinds, three are mostly absent from production memory libraries — episodic gets compressed to semantic at extraction, procedural is mostly mislabeled semantic, prospective barely exists.

what's left is semantic memory, and within semantic, one specific subset: autobiographical memory — the facts a person knows about their own life. borrowing the term loosely: the agent isn't remembering its own life, it's maintaining the user's by proxy.

when people say agents should "remember the user," what they usually mean is autobiographical content held on the user's behalf: where they live, what they're working on, who matters to them, what they've asked for and decided — facts the agent keeps about the user's life and preferences to act consistently across sessions. most agent memory libraries are autobiographical memory systems with extra steps. the field's central problem is narrower than "memory" — and clearer when you name it.

## where the analogy breaks

the three parts have rough biological analogs. extraction is the agent analog of consolidation — the slow compression from situated experience to decontextualized fact (in humans, during sleep, over hours; in agents, at conversational speed and at scale). the store maps to long-term memory — though the analog is the weakest of the three, since what's actually implemented is a state machine with no plausible biological equivalent. retrieval maps to both cued recall (with the same fixed-cutoff bias as top-k — once a cue activates a memory, the search stops) and source monitoring, the fragile human process of deciding whether a remembered fact is yours, current, real.

these analogies — together with the Tulving categories from the opening — are useful for vocabulary. they are dangerous as a design guide.

biological memory has properties that agent memory libraries variously lack, can't have, or shouldn't try to have. these aren't details; they're load-bearing parts of what makes biological memory work. the question worth asking of each property is which of the three categories it falls into.

**consolidation.** in humans, sleep replays the day's experiences and prunes the redundant ones — slow compression from situated event to abstract knowledge. agent labs have started shipping the equivalent: offline passes that revisit stored material and rewrite it, deduplicating, resolving contradictions, and surfacing patterns across sessions. Anthropic's Dreams and Letta's sleep-time compute are two production examples as of mid‑2026; both run scheduled passes over accumulated memory and produce reorganized stores. this is a property worth importing. the libraries that run extraction synchronously on every message are doing a degenerate version of consolidation under live latency budgets; the ones that run it offline, against accumulated material, are doing the version that matches the biology. whether it produces better outputs is still an open empirical question — but the structural argument is cleaner. absent, but addressable.

**emotional salience.** in humans, the amygdala flags experiences with strong affect for stronger encoding — fear, surprise, embarrassment all leave deeper traces than neutral content. nothing in a text-only agent has this signal. there's no body, no autonomic system, no analog to the physiological substrate that produces affect. the input is purely textual tokens. attempts to add this via importance scoring exist — Park et al.'s Generative Agents rate memories 1–10 for poignancy — but those are LLM-judged proxies, not affect: the same model that lacks affect is asked to estimate it. it's a structural absence that follows from operating on text alone. multimodal models with environmental grounding may eventually have an analog. text-only agents can't.

**forgetting.** biological memory actively forgets — decay, interference, pruning, all running constantly under the floor. some agent memory libraries try to imitate this with recency weighting, importance scores, or scheduled cleanup jobs. the assumption is that an agent should forget the way a person does, because that's how memory is supposed to work.

this is mostly mistaken. forgetting in biological memory is a constraint, not a feature — the brain forgets because it can't afford to store everything, not because forgetting is the goal. an agent memory system has no such constraint. it can keep everything for the cost of disk. and a system that keeps everything is also a system that can answer "what did we know last March?" — which is auditable, debuggable, and often what users actually need. a system that aggressively forgets loses that.

the real problem behind biological forgetting — that retrieval degrades as the store grows — doesn't go away just because disk is cheap. but biological-style forgetting isn't the answer. what an agent memory system needs is for the kept information to stay findable. that's a retrieval problem (rank current facts above stale ones, narrow searches to relevant themes) and an adjudication problem (mark superseded facts without deleting them). consolidation systems like Dreams attack the same problem from the other end — non-destructive offline reorganization between sessions, producing a cleaner store without losing the input. the question of whether there's a principled forgetting rule at all is still open. but the framing "biological memory forgets, therefore agent memory should too" imports the constraint as if it were the lesson. biological-style forgetting belongs in the third category — shouldn't. whether some other forgetting rule belongs anywhere is a separate question.

the four kinds of memory and the three anatomical parts are not a recipe. they're a map. when you read a library's docs, you can place its choices on this map — which kinds of memory it handles, which parts it implements versus stubs out, where it took the vocabulary without doing the engineering. Sebastian Lund's "Ultimate Guide to LLM Memory" is worth reading — it cuts the territory differently (by what fills the prompt at runtime) and the two views compose.

the vocabulary is more stable than the products. learn the parts. the products name themselves around them.

---

## References

1. Endel Tulving, "Episodic and Semantic Memory," in Organization of Memory, eds. Tulving & Donaldson (Academic Press, 1972). the procedural distinction is later, in Tulving's "How Many Memory Systems Are There?" American Psychologist 40 (1985). working memory as a separate system is Baddeley & Hitch (1974).

2. Sarah Wooders (Letta) and Harrison Chase (LangChain) argue memory isn't a separable system — it's whatever the harness keeps in context. within a session they're right. across sessions something has to outlive any one harness's choices — that's the substrate the three components describe.

3. cognitive science also draws a higher line: declarative memory (semantic plus episodic — facts and events you can verbalize) versus non-declarative (procedural skills, conditioning, priming). agent libraries handle declarative natively; non-declarative is mostly absent.

4. the three open-source memory libraries cited: LangMem (github.com/langchain-ai/langmem), Mem0 (github.com/mem0ai/mem0), Graphiti (github.com/getzep/graphiti, by Zep). all as of mid-2026; APIs change.

5. two production examples as of mid-2026: Letta's sleep-time compute — background subagents that rewrite and consolidate archival memory during idle time — and Anthropic's Dreams — an offline pipeline that ingests a memory store plus past session transcripts and writes a new store with duplicates merged and contradictions resolved on the latest value.

6. Joon Sung Park et al., "Generative Agents: Interactive Simulacra of Human Behavior," arXiv:2304.03442 (2023). scores each memory 1–10 for poignancy via an LLM call, weights retrieval by recency × importance × relevance.

7. not literally just disk — indexing, retrieval latency, and token costs grow with the store, and governance constraints (PII, retention/DSR, audit) apply regardless of storage cost.

8. Sebastian Lund's "Ultimate Guide to LLM Memory" (fastpaca.com/blog/ultimate-guide-to-llm-memory/) uses four layers — working, episodic, semantic, document.
