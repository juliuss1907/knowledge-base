---
type: repo
title: OpenViking — The Context Database for AI Agents
url: https://github.com/volcengine/OpenViking
author: volcengine
date_published: [unknown]
date_ingested: 2026-08-30
status: unprocessed
source: github.com
language: Python
stars: 34356
license: AGPL-3.0
homepage: https://openviking.ai/
---

# OpenViking: The Context Database for AI Agents

Open-source context database for AI agents. Stores memories, resources, and skills as one virtual filesystem under the `viking://` protocol, so an agent browses its own context with `ls`, `tree`, and `find` instead of querying a black-box vector store. Content is processed into three tiers — L0 abstract, L1 overview, L2 details — and loaded on demand. Every retrieval leaves a trajectory you can watch and debug.

Website · Live Demo · GitHub · Issues · Docs

## What is OpenViking

OpenViking is an open-source context database for AI agents. It stores memories, resources, and skills as one virtual filesystem under the `viking://` protocol, so an agent browses its own context with `ls`, `tree`, and `find` instead of querying a black-box vector store. Content is processed into three tiers — L0 abstract, L1 overview, L2 details — and loaded on demand. Every retrieval leaves a trajectory you can watch and debug.

## Why OpenViking

- **One filesystem for all context.** Memories, resources, and skills each get a `viking://` URI. Agents locate and manipulate context deterministically, like a developer working with files.
- **Tiered loading cuts token spend.** Every entry is processed into L0 (abstract), L1 (overview), and L2 (details) on write, then loaded only as deep as the task requires.
- **Directory recursive retrieval.** Vector search first locates the highest-scoring directory, then drills down layer by layer, so results arrive with their surrounding context intact.
- **Observable retrieval.** Each query preserves its directory-browsing trajectory. When a result looks wrong, you can see exactly which path produced it.
- **Sessions become memory.** After a session commits, OpenViking asynchronously extracts user preferences and agent experience into long-term memory.

```
viking://
├── resources/              # Resources: project docs, repos, web pages, etc.
│   └── my_project/
│       ├── docs/
│       └── src/
└── user/
    └── {user_id}/
        ├── memories/
        │   └── preferences/
        │       ├── writing_style
        │       └── coding_habits
        ├── resources/
        ├── skills/
        └── peers/
```

The three loading tiers:

- **L0 (Abstract)**: a one-sentence summary for quick relevance checks.
- **L1 (Overview)**: core information and usage scenarios for planning.
- **L2 (Details)**: the full original data, read only when needed.

Each directory carries its own L0/L1 layers, so relevance can be judged before any full file is read.

## Proof it works

OpenViking 0.3.22 has been evaluated on long-conversation user memory (LoCoMo) and multi-turn agent tasks (tau2-bench).

- **User memory (LoCoMo)**: with OpenViking, all three agent integrations land at 80–83% accuracy — up from 24–57% on their native memory — while input tokens drop by 34.3–91.0% and query latency by 58.45–66.10%.
- **Agent experience (tau2-bench)**: experience memory lifts task success by +6.87pp (retail) and +11.87pp (airline) over the same LLM without memory.

## Quick start

Requires Python 3.10 or higher.

```bash
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start
```

`init` walks you through provider setup and writes `~/.openviking/ov.conf`. It supports Volcengine, OpenAI, Codex OAuth, Kimi, GLM, and local Ollama. The install already includes the `ov` client CLI:

```bash
ov status
ov add-resource https://github.com/volcengine/OpenViking # --wait
ov ls viking://resources/
ov tree viking://resources/volcengine -L 2
ov find "what is openviking"
ov grep "openviking" --uri viking://resources/volcengine/OpenViking/docs/en
```

## Use it with your agent

Integrations inject OpenViking recall into your agent's context and auto-commit session memory:

- Claude Code
- Codex
- OpenClaw
- Hermes
- Cursor
- TRAE / TRAE CN / TraeCode CLI 2.0
- OpenCode
- pi
- Agent Plugins 1.0
- MCP clients
- LangChain / LangGraph

## OpenViking Helper (Beta)

A desktop console, currently in beta for macOS and Windows x64: visual local agent setup, session trace inspection, and local memory/skill management.

## VikingBot

An AI agent framework built on top of OpenViking:

```bash
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```

## Deploy in production

For production, run OpenViking as a standalone HTTP service.

## Commercial editions

**The open-source edition is not crippled.** OpenViking in this repo is fully open source under AGPLv3: no feature gates, no account required, no activation key.

The two commercial editions answer "who operates it and where it runs", not "can I use it":

- **Managed SaaS** — officially hosted on Volcano Engine. Personal (free trial up to 50 files) and Enterprise tiers.
- **Self-Managed** — runs inside your own environment. Online (own cloud/VPC, BYOC) and Offline (air-gapped) modes.

## Research

OpenViking open-sources a subset of the core capabilities described in the VikingMem paper:

> **VikingMem: A Memory Base Management System for Stateful LLM-based Applications**
> Jiajie Fu, et al. arXiv:2605.29640, 2026. Accepted by VLDB 2026.

## Partner Projects

- deer-flow — Open-source long-horizon SuperAgent harness
- NoKV — AI native distributed file system
- loopx — Lightweight loop engineering state kernel
- Hermes Agent — The agent that grows with you

## License

Different licenses for different components:

- **Main Project**: AGPLv3
- **crates/ov_cli**: Apache 2.0
- **examples**: Apache 2.0
- **third_party**: Respective original licenses
