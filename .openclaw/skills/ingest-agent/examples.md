# Ingest Agent — Example Raw Files

Sample outputs for each of the 6 content types. Use these as reference when ingesting new content.

---

## Example 1: Article

**File:** `raw/articles/2026-05-04_claude-code-skills-guide.md`

```markdown
---
type: article
title: The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work
url: https://bibek-poudel.medium.com/the-skill-md-pattern-72a3169dd7ee
author: Bibek Poudel
date_published: 2026-02-26
date_ingested: 2026-05-04
status: unprocessed
source: medium.com
---

# The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work

If your skill does not trigger, it is almost never the instructions. It is the description.

That is the thing most people figure out after an hour of frustration. You write a SKILL.md, drop it in the right folder, ask the agent to use it, and nothing happens. You rewrite the instructions. Still nothing. The problem was never what you wrote inside the skill. It was the two lines at the top that the agent uses to decide whether to activate it at all.

## What Is an Agent Skill?

A Skill is not a plugin. It is not a script you wire up to an API. Think of it like writing an onboarding guide for a new team member. Instead of re-explaining your workflows and preferences in every conversation, you package them once and the agent picks them up automatically whenever your request matches.

At its core, a skill is just a folder:

​```
your-skill-name/
├── SKILL.md 
├── scripts/ 
├── references/ 
└── assets/
​```

The only required file is `SKILL.md`. Everything else is optional but becomes important as skills grow in complexity.

[... rest of article content ...]
```

**Notes:**
- Long-form content preserved with headings and structure
- Code blocks maintained
- Author byline captured
- Publication date from article metadata

---

## Example 2: Post (X/Twitter thread)

**File:** `raw/posts/2026-05-03_anthropic-extended-thinking.md`

```markdown
---
type: post
title: Anthropic announces Extended Thinking for Claude
url: https://x.com/AnthropicAI/status/1234567890
author: @AnthropicAI
date_published: 2026-05-03
date_ingested: 2026-05-03
status: unprocessed
source: x.com
---

🧵 Introducing Extended Thinking for Claude — a new capability that lets Claude reason through complex problems step-by-step before responding.

---

Extended Thinking is now available in Claude Code and via API. When enabled, Claude can take extra time to think through multi-step problems, showing its reasoning process in real-time.

---

Key benefits:
• Better accuracy on complex tasks
• Transparent reasoning you can follow
• Useful for code review, system design, debugging

Try it with `/ultrathink` in Claude Code or set `thinking_budget` in the API.

---

Early results show 40% improvement on challenging coding tasks and 60% on mathematical reasoning benchmarks.

Read more: https://anthropic.com/extended-thinking
```

**Notes:**
- Thread concatenated with `---` separator
- @mentions preserved as plain text
- Emoji kept
- Each tweet becomes a section

---

## Example 3: Video

**File:** `raw/videos/2026-05-02_andrej-karpathy-llm-intro.md`

```markdown
---
type: video
title: Intro to Large Language Models
url: https://www.youtube.com/watch?v=zjkBMFhNj_g
author: Andrej Karpathy
date_published: 2023-11-22
date_ingested: 2026-05-02
status: unprocessed
source: youtube.com
---

# Intro to Large Language Models

**Duration:** 1:00:15

## Description

This is a 1 hour general-audience introduction to Large Language Models: the core technical component behind systems like ChatGPT, Claude, and Bard. What they are, where they are headed, comparisons and analogies to present-day operating systems, and some of the security-related challenges of this new computing paradigm.

## Transcript

[00:00] Hi everyone, today I want to give you an introduction to large language models. These are the core technology behind ChatGPT, Claude, and similar systems.

[00:15] Let's start with what a language model actually is. At its core, it's a system that predicts the next word in a sequence...

[02:30] The breakthrough came with the Transformer architecture in 2017. This allowed models to process text in parallel rather than sequentially...

[... full transcript continues ...]

## Key Points

- LLMs are trained on massive text datasets (trillions of tokens)
- Transformer architecture enables parallel processing
- Emergent capabilities appear at scale
- Security challenges: prompt injection, jailbreaks, data leakage
- Future: multimodal models, agents, tool use
```

**Notes:**
- Transcript included when available
- Duration and key points extracted
- Timestamps preserved in transcript
- Description from video metadata

---

## Example 4: Paper

**File:** `raw/papers/2026-04-28_vaswani-attention-is-all-you-need.md`

```markdown
---
type: paper
title: Attention Is All You Need
url: https://arxiv.org/abs/1706.03762
author: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
date_published: 2017-06-12
date_ingested: 2026-04-28
status: unprocessed
source: arxiv.org
---

# Attention Is All You Need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin

**Published:** June 12, 2017 (NeurIPS 2017)

**arXiv ID:** 1706.03762

**DOI:** 10.48550/arXiv.1706.03762

## Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.

## 1. Introduction

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15].

[... paper content continues ...]

## 6. Conclusion

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art.

## References

[1] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. arXiv preprint arXiv:1607.06450, 2016.

[... references continue ...]
```

**Notes:**
- Abstract preserved in full
- Authors list complete
- arXiv ID and DOI included
- Introduction and conclusion sections kept
- References section included
- Full paper content if available, otherwise abstract only

---

## Example 5: Repo

**File:** `raw/repos/2026-05-01_anthropics-anthropic-sdk-python.md`

```markdown
---
type: repo
title: anthropic-sdk-python
url: https://github.com/anthropics/anthropic-sdk-python
author: Anthropic
date_published: 2023-08-15
date_ingested: 2026-05-01
status: unprocessed
source: github.com
---

# anthropic-sdk-python

**Repository:** anthropics/anthropic-sdk-python

**Language:** Python

**Stars:** 1,234

**License:** MIT

**Description:** The official Python library for the Anthropic API

## README

# Anthropic Python API library

[![PyPI version](https://img.shields.io/pypi/v/anthropic.svg)](https://pypi.org/project/anthropic/)

The official Python library for the Anthropic API

## Installation

​```bash
pip install anthropic
​```

## Usage

The library needs to be configured with your account's secret key, which is available in your [Anthropic Console](https://console.anthropic.com/settings/keys).

​```python
import anthropic

client = anthropic.Anthropic(
    api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)
​```

## Streaming

​```python
with client.messages.stream(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
​```

[... rest of README ...]

## Repository Structure

​```
anthropic-sdk-python/
├── src/anthropic/
│   ├── __init__.py
│   ├── _client.py
│   ├── types/
│   └── resources/
├── tests/
├── examples/
└── README.md
​```

## Recent Commits

- `feat: add streaming support` (2026-04-30)
- `fix: handle rate limit errors` (2026-04-28)
- `docs: update examples` (2026-04-25)
```

**Notes:**
- README.md content preserved
- Repo metadata (stars, language, license) included
- Code examples maintained with syntax highlighting
- Repository structure outlined
- Recent commits noted if relevant

---

## Example 6: Website

**File:** `raw/websites/2026-04-30_cursor-ai-editor.md`

```markdown
---
type: website
title: Cursor - The AI-first Code Editor
url: https://cursor.sh
author: Cursor Team
date_published: 2024-01-15
date_ingested: 2026-04-30
status: unprocessed
source: cursor.sh
---

# Cursor - The AI-first Code Editor

**Website:** https://cursor.sh

**Category:** Developer Tools / Code Editor

**Pricing:** Free tier available, Pro at $20/month

## Overview

Cursor is an AI-first code editor built on VSCode. It integrates AI assistance directly into your coding workflow, allowing you to write, edit, and understand code faster.

## Key Features

### AI Chat
- Ask questions about your codebase
- Get explanations for complex code
- Generate new code from natural language

### Inline Editing
- Edit code with AI suggestions
- Refactor entire functions
- Fix bugs automatically

### Codebase Understanding
- AI indexes your entire project
- Answers questions with context
- Suggests relevant files and functions

### Multi-file Editing
- Make changes across multiple files
- Maintain consistency
- Refactor with confidence

## Pricing

| Plan | Price | Features |
|---|---|---|
| Free | $0 | 50 AI requests/month, basic features |
| Pro | $20/month | Unlimited requests, GPT-4, priority support |
| Business | Custom | Team features, admin controls, SSO |

## Technical Details

- Built on VSCode (fork)
- Supports all VSCode extensions
- Available for macOS, Windows, Linux
- Local-first architecture
- Privacy-focused (code stays on your machine)

## Getting Started

1. Download from cursor.sh
2. Install like any other app
3. Sign in with GitHub
4. Start coding with AI assistance

## Use Cases

- **Learning:** Understand unfamiliar codebases quickly
- **Debugging:** Get AI help finding and fixing bugs
- **Refactoring:** Modernize legacy code safely
- **Documentation:** Generate docs from code automatically

## Requirements

- macOS 10.15+, Windows 10+, or Linux
- 4GB RAM minimum
- Internet connection for AI features

## Community

- Discord: 50k+ members
- GitHub Discussions: Active community
- Twitter: @cursor_ai
```

**Notes:**
- Landing page content structured
- Pricing table preserved
- Features list extracted
- Technical requirements noted
- Use cases and getting started guide included
- No authentication required to view

---

## Format Consistency Rules

All examples follow these patterns:

### Frontmatter
- Always 8 fields in same order
- Dates in YYYY-MM-DD format
- `status: unprocessed` for all new files
- `type` matches folder name (singular)

### Content Structure
- Title as H1 (`#`)
- Metadata section if relevant
- Main content preserved with original formatting
- Code blocks with language tags
- Links as markdown `[text](url)`

### File Naming
- Date prefix from `date_published` or `date_ingested`
- Slug from title (lowercase-hyphen)
- Max 50 chars for slug
- `.md` extension

### Content Cleaning
- No `<script>` tags
- No navigation/footer HTML
- No ads or tracking pixels
- Preserve semantic HTML converted to markdown
- Keep inline links and images

---

## Edge Case Examples

### Multi-part thread (concatenated)

```markdown
---
type: post
title: How we built Claude Code (thread)
url: https://x.com/AnthropicAI/status/1234567890
author: @AnthropicAI
date_published: 2026-05-01
date_ingested: 2026-05-01
status: unprocessed
source: x.com
---

1/ We're excited to share how we built Claude Code, our AI-powered development environment.

---

2/ The core challenge was making AI assistance feel natural in a developer's workflow, not like a chatbot bolted onto an editor.

---

3/ We started with three principles:
• Context-aware: AI should understand your entire codebase
• Non-intrusive: Never interrupt flow state
• Trustworthy: Always show what the AI is doing

---

[... rest of thread ...]
```

### Video without transcript

```markdown
---
type: video
title: Building Production LLM Apps
url: https://www.youtube.com/watch?v=abc123
author: Jane Developer
date_published: 2026-04-15
date_ingested: 2026-05-01
status: unprocessed
source: youtube.com
---

# Building Production LLM Apps

**Duration:** 45:30

## Description

A practical guide to deploying LLM applications in production. Covers prompt engineering, caching strategies, error handling, and cost optimization.

[Transcript not available]

## Key Topics (from description)

- Prompt engineering best practices
- Caching and latency optimization
- Error handling and fallbacks
- Cost management strategies
- Monitoring and observability
```

### Paper behind paywall

```markdown
---
type: paper
title: Scaling Laws for Neural Language Models
url: https://arxiv.org/abs/2001.08361
author: Jared Kaplan, Sam McCandlish, Tom Henighan, et al.
date_published: 2020-01-23
date_ingested: 2026-05-01
status: unprocessed
source: arxiv.org
---

# Scaling Laws for Neural Language Models

**Authors:** Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei

**Published:** January 23, 2020

**arXiv ID:** 2001.08361

## Abstract

We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range.

[Full text not available - abstract only]

## Citation

​```bibtex
@article{kaplan2020scaling,
  title={Scaling laws for neural language models},
  author={Kaplan, Jared and McCandlish, Sam and Henighan, Tom and Brown, Tom B and Chess, Benjamin and Child, Rewon and Gray, Scott and Radford, Alec and Wu, Jeffrey and Amodei, Dario},
  journal={arXiv preprint arXiv:2001.08361},
  year={2020}
}
​```
```

### Non-English content

```markdown
---
type: article
title: 大型语言模型的未来发展
url: https://example.com/llm-future-zh
author: 张伟
date_published: 2026-04-20
date_ingested: 2026-05-01
status: unprocessed
source: example.com
language: zh
---

# 大型语言模型的未来发展

[Original Chinese content preserved as-is]

人工智能技术的快速发展，特别是大型语言模型（LLM）的出现，正在深刻改变我们与计算机交互的方式...

[... rest of content in Chinese ...]
```

**Note:** `language: zh` added to frontmatter, content not translated. Compile Agent will handle translation if needed.

---

## Validation Checklist

Before considering an ingestion complete, verify:

- [ ] File exists in correct `raw/<type>/` folder
- [ ] Filename follows `YYYY-MM-DD_<slug>.md` pattern
- [ ] Frontmatter has all 8 required fields
- [ ] `status: unprocessed` is set
- [ ] Dates are valid YYYY-MM-DD format
- [ ] Content is markdown (not HTML)
- [ ] No `<script>` tags present
- [ ] Code blocks have language tags
- [ ] Links are markdown format `[text](url)`
