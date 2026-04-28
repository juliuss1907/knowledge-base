---
type: raw
source_type: article
source_url: https://hackernoon.com/how-i-built-a-multi-agent-development-system-that-plans-executes-and-remembers
date_ingested: 2026-04-28
batch: tech
tags: [#coding, #ai, #productivity]
status: unprocessed
approved_by: julius
---
# How I Built a Multi-Agent Development System That Plans, Executes, and Remembers
## Chinar Amrutkar

**Link gốc:** https://hackernoon.com/how-i-built-a-multi-agent-development-system-that-plans-executes-and-remembers
**Published:** 2026-04-27
**Author:** Chinar Amrutkar — Data Engineer obsessed with automation

---

## Tóm tắt

Tác giả xây dựng một hệ thống Multi-Agent development trong OpenClaw để giải quyết vấn đề "context leak" khi solo developer làm việc nhiều ngày rồi quay lại project. Hệ thống gồm: coordinator agent, parallel sub-agents, và file-based memory layer. Output là research-backed plan với verification commands, không cần người hướng dẫn từng bước.

---

## Vấn đề

Solo development có "context problem" — không phải motivation hay tooling, mà là structural. Khi developer rời đi vài ngày, context bị mất, quyết định đã quên, task drift, scope creep.

---

## Kiến trúc

### 3 thành phần chính

1. **Coordinator Agent** — luôn chạy, không execute trực tiếp, mà orchestrate. Nó spawn sub-agents, assign research briefs, collect outputs, route accumulated context qua các stages. Chỉ track file paths và summaries, không đọc full research files (vì đọc everything chậm và tốn kém).

2. **Sub-agents** — isolated workers, mỗi cái được deploy với 1 research question cụ thể, output path rõ ràng, và strict instructions: write findings to file, return 2-3 sentence summary. Chạy song song.

3. **Memory Layer** — flat files trên disk. Research outputs, architecture drafts, gap analyses, phase plans đều được write vào temporary planning directory, clean up sau khi plan committed to git. Files bền, inspectable, diffable.

### Project Planning Workflow

**Stage 0: Setup**
- Coordinator tạo timestamped working directory
- Có `research/` subdirectory cho raw findings
- Có `waves/` subdirectory cho follow-up research
- Directory structure cố định và known to all sub-agents by contract

**Stage 1: Discovery**

Coordinator deploys 3 research sub-agents song song:

- **Lesson Researcher:** Tìm patterns từ past documentation, memory files, solutions directory. Ngăn hệ thống lặp lại known mistakes.
- **Current State Researcher:** Đọc codebase hiện tại, config files, integration points. Trả lời: implementation thực sự trông thế nào, không phải wish it looked.
- **Constraints Researcher:** Kiểm tra deadlines, dependencies, budget limitations, technical boundaries.

Sau initial pass → **Gap Analysis**: Coordinator đọc 3 research files và classify mọi remaining question vào 3 buckets:
- **RESEARCHABLE:** Câu trả lời tồn tại và có thể tìm được với more investigation.
- **USER_INPUT:** Đây là human judgment call thật sự — scope decision, priority trade-off, design preference.
- **DEFERRABLE:** Có thể decide trong implementation mà không block plan.

Coordinator chạy tối đa 3 research waves để fill RESEARCHABLE gaps.

**Stage 2: Feature Research**
- Coordinator deploys second wave của targeted research sub-agents
- Nhìn vào specific angles: integration points, dependency implications, security considerations, performance boundaries, error-handling patterns
- Đây là fan-out phase
- Output: validation check — có phải mọi requirements cho planning thực sự knowable tại điểm này không?

**Stage 3: Planning**
- **Architect sub-agent** đọc tất cả research files và produce high-level architecture document (component overview, responsibilities, interfaces, data flow, technology decisions)
- Với complex features → coordinator deploys **phase planners** — một per major section — để produce detailed phase plans
- Mỗi plan gồm: overview, task list với specific files và dependencies, verification commands
- Coordinator integrate all phase plans thành coherent structure: README với task index pointing to individual phase documents

**Stage 4: Cleanup**
- Temporary planning directory deleted
- Final plan committed to git
- Feature ready to move into implementation

---

## Tại sao những quyết định này

**Why file-based coordination?**
Files durable và inspectable hơn in-memory context. Sub-agent writing to disk là something coordinator có thể verify later. Files survive session boundaries — coordinator có thể restart và research context vẫn persist.

**Why subagents over single agent?**
Parallel research fundamentally faster than sequential. Ba câu hỏi answered simultaneously beat ba câu hỏi answered sequentially.

**Why structured stages?**
Without structure, research loops forever. Stage gates force system make decisions về when to stop investigating và start synthesising. Maximum-three-research-waves rule là một instance của principle này.

---

## What this demonstrates

- System runs autonomously: given a feature brief, produces research-backed plan với verification commands, không cần human guide through each step.
- Human in the loop cho judgment calls — scope decisions, design preferences, trade-offs.
- Multi-agent coordination pattern explicit và traceable. Coordinator deploys sub-agents với specific briefs, collects summaries, routes outputs through stage gates.
- Structured stages impose discipline. Researchable gaps exhausted within fixed number of waves. USER_INPUT questions surfaced as discrete options, not vague requests.
- Output measurable: mỗi phase plan chứa specific files to edit, dependencies to check, verification commands to run.

---

## Quote đáng chú ý

> "The interesting work is not the implementation — it is the structure that makes implementation reliable, repeatable, and auditable."