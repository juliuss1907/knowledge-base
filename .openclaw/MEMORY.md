---

---

## 2026-08-11 09:18 — Fix Agent: Applied 9 approved Hermes reports (08-07 through 08-10)

### Reports applied:
1. **08-07 Output** — Fixed 1 carry-over dropped-i typo: "hàng triệu ngườ" → "hàng triệu người" in wiki/concepts/new-leverage-digital-assets.md
2. **08-07 Format** — 430W forward-references, no structural fixes needed
3. **08-07 Hygiene** — state/ and wiki/HEARTBEAT.md already absent
4. **08-08 Format** — 430W forward-references, no structural fixes needed
5. **08-08 Hygiene** — state/ and wiki/HEARTBEAT.md already absent
6. **08-09 Format** — 430W forward-references, no structural fixes needed
7. **08-09 Hygiene** — state/ and wiki/HEARTBEAT.md already absent
8. **08-10 Format** — Added `## Co-occurring tags` to wiki/tag/layer2.md and wiki/tag/perpdex.md (same pattern as opinion.md/research.md fixed on 08-06)
9. **08-10 Hygiene** — state/, wiki/HEARTBEAT.md, memory/ already absent

### Files modified:
- wiki/concepts/new-leverage-digital-assets.md — 1 typo fix
- wiki/tag/layer2.md — added `## Co-occurring tags` section
- wiki/tag/perpdex.md — added `## Co-occurring tags` section
- wiki/reviews/_action-required.md — all 9 reports marked APPLIED

### Notes:
- state/, wiki/HEARTBEAT.md, and memory/ were all already absent from the filesystem at time of apply — likely cleaned by a previous process
- 3 Format reports (08-07/08-08/08-09) had 430W each — all forward-reference broken wikilinks, expected in growing KB
- 08-10 Format ERRORs matched the opinion.md/research.md pattern from 08-06 — Index Agent should be updated to always include `## Co-occurring tags` section

## 2026-08-11 08:40 — Compiled (daily cron)

- **Batch:** 6 raw files processed (0 failed)
- **Source notes:** 3 created (files 4-6), 3 already existed (files 1-3)
- **Concepts:** 7 new + 5 existing updated + 4 cross-referenced from prior partial run
- **Raw backlog:** 0 unprocessed remaining

### Per-file details:

1. **raw/articles/2026-08-09_what-is-a-product.md** (pre-existing source + concept)
   - Source: wiki/sources/src_what-is-a-product.md (đã có)
   - Concepts: [product-vs-prototype] (đã có)
   - Tags: main=#ai, sub=[#opinion, #vibecode], topic=product-vs-prototype
   - Action: raw file → processed (was unprocessed despite source/concept existing)

2. **raw/posts/2026-08-10_faith-and-fear-are-the-exact-same-thing.md** (pre-existing source + concept)
   - Source: wiki/sources/src_faith-and-fear-are-the-exact-same-thing.md (đã có)
   - Concepts: [fear-alchemy] (đã có)
   - Tags: main=#productivity, sub=[#psychology, #opinion], topic=fear-alchemy
   - Action: raw file → processed

3. **raw/posts/2026-08-09_how-to-get-maximum-results-with-minimum-effort-game-theory.md** (pre-existing source + concept)
   - Source: wiki/sources/src_how-to-get-maximum-results-with-minimum-effort-game-theory.md (đã có)
   - Concepts: [asymmetric-positions, game-selection, information-asymmetry] (đã có)
   - Tags: main=#productivity, sub=[#strategy, #opinion], topic=game-theory-productivity
   - Action: raw file → processed

4. **raw/posts/2026-07-27_how-to-come-back-from-anything-game-theory.md**
   - Source: wiki/sources/src_how-to-come-back-from-anything-game-theory.md
   - Concepts mới: [comeback-strategy, survival-first, variance-in-loss, sunk-cost-fallacy]
   - Concepts cập nhật: [costly-signal, repeated-games] (thêm source + related concepts)
   - Concepts cross-ref: [iterated-game-theory, costly-signaling] (từ prior run 08:40)
   - Tags: main=#productivity, sub=[#strategy, #psychology, #research], topic=game-theory-comeback

5. **raw/posts/2026-08-09_just-let-go-cipheron.md**
   - Source: wiki/sources/src_just-let-go-cipheron.md
   - Concepts mới: [identity-transformation, letting-go]
   - Concepts cập nhật: [internal-foundation-identity, psychological-survival] (thêm source + related concepts)
   - Concepts cross-ref: [identity-detachment, role-playing-self] (từ prior run 08:40)
   - Tags: main=#health, sub=[#psychology, #opinion], topic=identity-transformation

6. **raw/posts/2026-08-10_long-range-career-advice.md**
   - Source: wiki/sources/src_long-range-career-advice.md
   - Concepts mới: [career-compounding]
   - Concepts cập nhật: [leverage] (thêm source + related concepts)
   - Tags: main=#productivity, sub=[#strategy, #opinion], topic=career-strategy

### Cross-reference cleanup

Do có prior compile run lúc 08:40 tạo 4 concepts (iterated-game-theory, costly-signaling, identity-detachment, role-playing-self) mà không cập nhật raw files, lần compile này đã:
- Tạo cross-references 2 chiều giữa concepts mới và concepts từ prior run
- Không xóa concept files nào — giữ lại để preserve nội dung và tránh broken links
- duplicated line cleanup: 4 raw files có duplicate compiled_at/compiled_to đã được fix

### File inventory

- **Source notes mới:** 3 (src_how-to-come-back, src_just-let-go, src_long-range-career)
- **Concepts mới:** 7 (comeback-strategy, survival-first, variance-in-loss, sunk-cost-fallacy, identity-transformation, letting-go, career-compounding)
- **Concepts updated:** 5 (costly-signal, repeated-games, internal-foundation-identity, psychological-survival, leverage)
- **Concepts cross-ref:** 4 (iterated-game-theory, costly-signaling, identity-detachment, role-playing-self)
- **Raw files updated:** 6/6 → status: processed

## 2026-08-10 22:45 — Indexed (incremental)

- **Scanned:** 11 files changed (2 sources + 9 concepts)
- **Tags indexed:** 26 regenerated (co-occurrence updated)
- **Topics indexed:** 6 updated (time-perception-childhood new, 5 existing updated)
- **Orphans deleted:** 1 (career — not in TAGS.md taxonomy)
- **Invalid tags found:** 0
- **Errors:** 0
- **New tag index created:** strategy (Pool B)

## 2026-08-10 08:50 — Ingested

- **File:** `raw/posts/2026-08-10_faith-and-fear-are-the-exact-same-thing.md`
- **Source:** https://x.com/jlowetransforms/status/2085766731654418669
- **Type:** post
- **Author:** Jlowe (@jlowetransforms)
- **Status:** unprocessed
- **Note:** Fear/faith reframe + journaling protocol để trung hòa năng lượng sợ hãi. Julius gửi qua Telegram.

---

## 2026-08-10 08:45 — Ingested

- **File:** `raw/posts/2026-08-10_long-range-career-advice.md`
- **Source:** https://x.com/spakhm/status/2085049411332087891
- **Type:** post
- **Author:** Slava Akhmechet (@spakhm)
- **Status:** unprocessed
- **Note:** Career compounding framework — main loop + background loop + failure modes. Julius gửi qua Telegram.

---

## 2026-08-09 08:58 — Ingested

- **File:** `raw/articles/2026-08-09_what-is-a-product.md`
- **Source:** https://roge.onwrite.app/what-is-a-product
- **Type:** article
- **Author:** [unknown]
- **Status:** unprocessed
- **Note:** Julius gửi link 3 lần (07/08, 09/08) trước khi xử lý được. Đã fetch full content thành công.

---

## 2026-08-05 21:00 — Indexed (Skip)

- **Mode:** incremental check
- **Last success:** 2026-08-01T21:00:00+07:00
- **Changed files:** 0
- **Action:** Skip — không có file nào thay đổi từ lần index trước
- **Note:** KB ổn định, không cần rebuild indexes

---

## 2026-08-05 08:00 — Compiled

- **Mode:** daily cron (Compile Agent)
- **Raw scanned:** 161 files across all types
- **Unprocessed found:** 0
- **Compiled:** 0
- **Concepts created/updated:** 0
- **Tag proposals:** 0
- **Note:** Tất cả file đã được xử lý. Raw backlog sạch.

---

## 2026-08-04 21:00 — Indexed (Skip)

- **Mode:** incremental check
- **Last success:** 2026-08-01T21:00:00+07:00
- **Changed files:** 0
- **Action:** Skip — không có file nào thay đổi từ lần index trước
- **Note:** KB ổn định, không cần rebuild indexes

---

## 2026-08-04 08:00 — Compiled

- **Mode:** daily cron (Compile Agent)
- **Raw scanned:** 161 files across all types
- **Unprocessed found:** 0
- **Compiled:** 0
- **Concepts created/updated:** 0
- **Tag proposals:** 0
- **Note:** All raw files already processed. CompileAgent idle.

---

## 2026-08-02 08:00 — Compiled

- **Mode:** daily cron (Compile Agent)
- **Raw scanned:** 148 files across all types
- **Unprocessed found:** 0
- **Compiled:** 0
- **Concepts created/updated:** 0
- **Tag proposals:** 0
- **Note:** All raw files already processed. CompileAgent idle.

---

## 2026-08-01 21:00 — Indexed

- **Mode:** incremental (11 files changed since 2026-07-30)
- **Scanned:** 9 concepts + 2 sources
- **Tags indexed:** 8 (2 cập nhật: #economic, #tools, #opinion, #research, #tutorial; 1 tạo mới: #career)
- **Topics indexed:** 6 (4 tạo mới: semiconductor-industry, moores-law, cuoc-dua-khong-di-lui, technology-society)
- **Orphans deleted:** 0
- **Invalid tags found:** 0
- **Errors:** 0

---

## 2026-08-01 08:00 — Compiled

- **Raw:** [[raw/articles/2026-07-31_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md]]
- **Source note:** [[wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md]]
- **Concepts:** [cuoc-dua-khong-di-lui, semiconductor-industry-consolidation, moores-law-economics, technology-driven-dependence]
- **Tags applied:** main=#economic, sub=[#opinion, #tech], topic=cuoc-dua-khong-di-lui
- **Action:** created 4 concept files

---

## 2026-07-31 20:30 — Heartbeat Check

**Check ID:** 3e70fe54-de76-4781-9342-c1ab2a73ebd4

### Status
✅ **HEARTBEAT_OK**

### Results
| Check | Status | Details |
|-------|--------|---------|
| Inbox | ✓ Clean | 0 items #agent/inbox |
| Raw backlog | ✓ Clean | 1 file unprocessed (mới ingest hôm nay) |
| Pending reviews | ⚠️ Attention | 1 report pending — Hygiene 07-30 (raw/tools/) |

### Stats
- Raw files: 169 total
- Wiki concepts: 500
- Wiki sources: 160
- Tag indexes: 24
- Topic indexes: 181
- Unprocessed: 1 file (2026-07-31_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md)

### Context
- File mới ingest lúc 20:03 từ curiositypocket (Substack)
- CompileAgent sẽ xử lý vào 08:00 ngày mai
- 1 pending hygiene report (raw/tools/ folder) chờ Julius quyết định

**Action:** Không cần hành động khẩn cấp. Hệ thống ổn định.

---

## 2026-07-31 08:00 — Compiled

**Batch:** KB Compile Daily (cron:b91792a8-9b52-4856-b608-ca6a0f8f6f16)

### Files Processed

| File | Type | Concepts | Tags |
|------|------|----------|------|
| 2026-07-30_lam-the-nao-e-ra-quyet-inh-khi-con-thankvn.md | article | 5 | #productivity, [psychology, tutorial] |

### Concepts Created

**From Decision Making Under Uncertainty article:**
- [[type-1-vs-type-2-decisions]] — Framework phân loại quyết định của Jeff Bezos
- [[colin-powell-40-70-rule]] — Nguyên tắc quyết định khi có 40-70% thông tin
- [[decision-cost-analysis]] — Phân tích chi phí quyết định sai
- [[optionality-principle]] — Ưu tiên lựa chọn giữ nhiều cửa mở
- [[small-bets-strategy]] — Chiến lược cược nhỏ để thu thập thông tin

### Summary

- **Processed:** 1/1 files
- **Failed:** 0
- **Source notes created:** 1
- **Concepts created:** 5
- **Concepts updated:** 0
- **Tag proposals:** 0

---

## 2026-07-30 08:00 — Compiled

**Batch:** KB Compile Daily (cron:b91792a8-9b52-4856-b608-ca6a0f8f6f16)

### Files Processed

| File | Type | Concepts | Tags |
|------|------|----------|------|
| 2026-07-27_agent-memory-7-types-substack.md | article | 8 | #ai, [tools, research] |
| 2026-07-27_the-let-them-theory-gabriel-reality.md | article | 5 | #health, [psychology, opinion] |
| 2026-07-29_how-to-remember-everything-you-read-dan-koe.md | article | 5 | #productivity, [tutorial, psychology] |

### Concepts Created

**From Agent Memory article:**
- [[in-context-memory]] — Working memory trong LLM agents
- [[semantic-memory]] — Facts và general knowledge storage
- [[episodic-memory]] — Specific experiences và user history
- [[procedural-memory]] — Skills và workflows
- [[external-retrieval-memory]] — On-demand retrieval từ external sources
- [[parametric-memory]] — Knowledge encoded trong model weights
- [[prospective-memory]] — Future tasks và scheduling
- [[coal-framework]] — Cognitive Architectures for Language Agents

**From Let Them Theory article:**
- [[let-them-theory]] — Chấp nhận ngưởi khác đúng như họ là
- [[intolerance-of-uncertainty]] — Neurological response to ambiguity
- [[control-trap]] — Belief effort sẽ change ngưởi không muốn change
- [[anterior-cingulate-cortex]] — Brain region monitors errors
- [[stoic-dichotomy-of-control]] — Phân biệt trong/ngoài tầm kiểm soát

**From Dan Koe Learning article:**
- [[cybernetics-learning-model]] — Learning như feedback system
- [[output-based-learning]] — Learning through output, not input
- [[goal-directed-learning]] — Goals tạo filter cho relevance
- [[error-signal-learning]] — Gap giữa current và target drives learning
- [[learning-filter]] — Cognitive mechanism determines retention

### Summary

- **Processed:** 3/3 files
- **Failed:** 0
- **Source notes created:** 3
- **Concepts created:** 18
- **Concepts updated:** 0
- **Tag proposals:** 0

---

## 2026-07-29 21:00 — Indexed (Incremental)

**Task:** KB Index Daily (cron:5de7b598-808b-4182-abfb-6bdeed920af4)

### Mode
- **Type:** Incremental
- **Files changed since last index:** 6
- **Last success:** 2026-07-26T21:00:00

### Files Scanned

1. `wiki/sources/src_reward-hacking-writeup.md` — source, #ai, [research, hack, opinion]
2. `wiki/concepts/reward-seeking.md` — concept, #ai, [research]
3. `wiki/concepts/ai-safety-monitoring.md` — concept, #ai, [research, tools]
4. `wiki/concepts/ai-alignment.md` — concept, #ai, [research]
5. `wiki/concepts/reward-hacking.md` — concept, #ai, [research, hack]
6. `wiki/concepts/apparent-success-seeking.md` — concept, #ai, [research]

### Tag Indexes Updated

| Tag | Before | After | Change |
|-----|--------|-------|--------|
| #ai | 168 | 174 | +6 |
| #research | 237 | 243 | +6 |
| #hack | 18 | 20 | +2 |
| #opinion | 230 | 231 | +1 |
| #tools | 178 | 179 | +1 |

### Topic Indexes Created

- `wiki/topic/ai-reward-hacking-alignment.md` — 5 concepts + 1 source

### Summary

- **Scanned:** 6 files (incremental)
- **Tag indexes updated:** 5
- **Topic indexes created:** 1
- **Orphans deleted:** 0
- **Invalid tags found:** 0
- **Errors:** 0

---

## 2026-07-27 08:00 — Compiled

**Batch:** KB Compile Daily (cron:b91792a8-9b52-4856-b608-ca6a0f8f6f16)

### Files Processed

1. **raw/articles/2026-07-26_reward-hacking-writeup.md**
   - **Source note:** [[wiki/sources/src_reward-hacking-writeup.md]]
   - **Concepts created:** 5 mới
     - [[reward-hacking]] ✨
     - [[reward-seeking]] ✨
     - [[apparent-success-seeking]] ✨
     - [[ai-alignment]] ✨
     - [[ai-safety-monitoring]] ✨
   - **Tags:** main=#ai, sub=[research, hack, opinion], topic=ai-reward-hacking-alignment

### Summary

- **Raw files processed:** 1/1
- **Source notes created:** 1
- **Concepts created:** 5 mới
- **Concepts updated:** 0
- **Tags applied:** 1 combination
- **Raw status updated:** processed (1 file)
- **Index updated:** raw/articles/articles.md

**Next step:** Index Agent sẽ chạy lúc 21:00 để cập nhật tag và topic indexes.

---

## 2026-07-26 08:00 — Compiled

**Batch:** KB Compile Daily (cron:b91792a8-9b52-4856-b608-ca6a0f8f6f16)

### Files Processed

1. **raw/tools/2026-07-25_monid-ai-agent-tool-platform.md**
   - **Source note:** [[wiki/sources/src_monid-ai-agent-tool-platform.md]]
   - **Concepts created:** 3 mới
     - [[ai-agent-tool-orchestration]] ✨
     - [[unified-api-gateway]] ✨
     - [[pay-per-call-pricing]] ✨
   - **Tags:** main=#ai, sub=[tools, automation], topic=ai-agent-tool-platform

2. **raw/tools/2026-07-25_introducing-backsearch-gr-inc.md**
   - **Source note:** [[wiki/sources/src_introducing-backsearch-gr-inc.md]]
   - **Concepts created:** 3 mới
     - [[agent-backtesting]] ✨
     - [[frozen-corpus-search]] ✨
     - [[point-in-time-data]] ✨
   - **Tags:** main=#ai, sub=[tools, research], topic=agent-backtesting

### Summary

- **Raw files processed:** 2/2
- **Source notes created:** 2
- **Concepts created:** 6 mới
- **Concepts updated:** 0
- **Tags applied:** 2 combinations
- **Raw status updated:** processed (2 files)
- **Index updated:** raw/tools/tools.md

**Next step:** Index Agent sẽ chạy lúc 21:00 để cập nhật tag và topic indexes.

---

## 2026-07-25 23:30 — Heartbeat Check

**Check ID:** 3e70fe54-de76-4781-9342-c1ab2a73ebd4

### Status
✅ HEARTBEAT_OK

### Results
| Check | Status | Details |
|-------|--------|---------|
| Inbox | ✓ Clean | 0 items #agent/inbox |
| Raw backlog | ✓ Clean | 0 files >24h unprocessed |

### Context
- Last compile: 2026-07-25 08:00
- Last Hermes review: 2026-07-24 18:00
- Pending reviews: 0

**Action:** Không cần hành động. Hệ thống ổn định.

---

## 2026-07-25 08:00 — Compiled

**Batch:** KB Compile Daily (cron)

### Files Processed

1. **raw/websites/2026-07-24_openai-explains-gpt-5-6-sol.md**
   - **Source note:** [[wiki/sources/src_openai-explains-gpt-5-6-sol.md]]
   - **Concepts created:** 4 mới
     - [[gpt-5-6-sol]] ✨
     - [[model-distillation]] ✨
     - [[chain-of-thought-reasoning]] ✨
     - [[long-context-processing]] ✨
   - **Tags:** main=#ai, sub=[research, tools], topic=gpt-5-6-release

### Summary

- **Raw files processed:** 1/1
- **Source notes created:** 1
- **Concepts created:** 4 mới
- **Concepts updated:** 0
- **Tags applied:** 1 combination
- **Raw status updated:** processed (1 file)

---

## 2026-07-24 18:00 — Hermes Review Complete

**Reviewer:** Hermes (RK800)

### Results
- **Files reviewed:** 5
- **PROMOTE:** 3
- **REVISE:** 1
- **REJECT:** 1

### Details
| File | Decision | Notes |
|------|----------|-------|
| wiki/concepts/gpt-5-6-sol.md | PROMOTE | Đủ depth, sources đầy đủ |
| wiki/concepts/model-distillation.md | PROMOTE | Definition rõ ràng |
| wiki/concepts/chain-of-thought-reasoning.md | PROMOTE | Good key ideas |
| wiki/concepts/long-context-processing.md | REVISE | Thiếu related concepts |
| wiki/sources/src_gpt-5-6-sol.md | REJECT | Concept thay thế đủ tốt |

**Action taken:** Đã update `wiki/reviews/_action-required.md` cho Julius.

---

## 2026-07-24 08:00 — Compiled

**Batch:** KB Compile Daily (cron)

### Files Processed

1. **raw/articles/2026-07-23_efficient-training-transformers.md**
   - **Source note:** [[wiki/sources/src_efficient-training-transformers.md]]
   - **Concepts created:** 3 mới
     - [[mixture-of-experts]] ✨
     - [[gradient-checkpointing]] ✨
     - [[sparse-attention]] ✨
   - **Tags:** main=#ai, sub=[research, tools], topic=transformer-training

2. **raw/articles/2026-07-22_defi-yield-optimization.md**
   - **Source note:** [[wiki/sources/src_defi-yield-optimization.md]]
   - **Concepts created:** 2 mới
     - [[yield-aggregation]] ✨
     - [[impermanent-loss-hedging]] ✨
   - **Concepts updated:** 1
     - [[automated-market-maker]] (thêm sources)
   - **Tags:** main=#crypto, sub=[defi, tools], topic=defi-yield-strategies

### Summary

- **Raw files processed:** 2/2
- **Source notes created:** 2
- **Concepts created:** 5 mới
- **Concepts updated:** 1
- **Tags applied:** 2 combinations
- **Raw status updated:** processed (2 files)

---

## 2026-07-23 14:30 — Heartbeat Check

**Check ID:** 7a4c9e2f-b8d1-4235-9e9f-3c2a1b0d8e7f

### Status
⚠️ RAW BACKLOG DETECTED

### Results
| Check | Status | Details |
|-------|--------|---------|
| Inbox | ✓ Clean | 0 items #agent/inbox |
| Raw backlog | ⚠️ Warning | 3 files unprocessed, oldest 2 days |
| Pending reviews | ✓ Clean | 0 pending |

### Context
- Files: raw/articles/2026-07-21_trends-2026.md, raw/articles/2026-07-20_productivity-hacks.md, raw/websites/2026-07-19_new-framework.md
- Compile schedule: 08:00 daily

**Action:** Logged to backlog. CompileAgent sẽ xử lý vào 08:00 sáng mai.

---

## 2026-07-20 10:15 — Telegram Ingest

**Source:** Telegram message from Julius
**File saved:** raw/articles/2026-07-20_productivity-hacks.md

### Frontmatter
- type: article
- title: "The Productivity Hacks That Actually Work"
- source_url: https://example.com/article
- date_ingested: 2026-07-20
- status: unprocessed

**Next step:** CompileAgent sẽ xử lý vào 08:00 sáng mai.

---

## 2026-07-19 21:00 — Index Update

**Agent:** Index Agent

### Indexes Updated
- wiki/tag/ai.md — 47 concepts, 23 sources
- wiki/tag/crypto.md — 12 concepts, 8 sources
- wiki/tag/tools.md — 31 concepts, 19 sources
- wiki/topic/transformer-training.md — 3 concepts, 2 sources
- wiki/topic/defi-yield-strategies.md — 2 concepts, 1 source

**Total indexes:** 47 tag files, 12 topic files

---

## 2026-07-19 08:00 — Compiled

**Batch:** KB Compile Daily (cron)

### Files Processed

1. **raw/papers/2026-07-18_attention-is-all-you-need-revisited.md**
   - **Source note:** [[wiki/sources/src_attention-is-all-you-need-revisited.md]]
   - **Concepts created:** 1 mới
     - [[transformer-architecture]] ✨
   - **Concepts updated:** 2
     - [[self-attention]] (thêm sources)
     - [[positional-encoding]] (thêm sources)
   - **Tags:** main=#ai, sub=[research], topic=transformer-architecture

### Summary

- **Raw files processed:** 1/1
- **Source notes created:** 1
- **Concepts created:** 1 mới
- **Concepts updated:** 2
- **Tags applied:** 1 combination
- **Raw status updated:** processed (1 file)

---

## 2026-07-18 16:45 — Manual Compile Triggered

**Triggered by:** Julius via Telegram

### Files Processed

1. **raw/videos/2026-07-18_attention-explained-3b1b.md**
   - **Source note:** [[wiki/sources/src_attention-explained-3b1b.md]]
   - **Concepts created:** 2 mới
     - [[self-attention]] ✨
     - [[positional-encoding]] ✨
   - **Tags:** main=#ai, sub=[tutorial, research], topic=attention-mechanism

### Summary

- **Raw files processed:** 1/1
- **Source notes created:** 1
- **Concepts created:** 2 mới
- **Tags applied:** 1 combination

---

## 2026-07-18 08:00 — Compiled

**Batch:** KB Compile Daily (cron)

### Status
✅ No unprocessed files found

**Result:** HEARTBEAT_OK — Không có file nào cần xử lý.

---

## 2026-07-17 14:20 — Heartbeat Check

**Check ID:** 2f8a6c4d-1e9b-4c3a-8f7e-5d2b9a0c6e1d

### Status
✅ HEARTBEAT_OK

### Results
| Check | Status | Details |
|-------|--------|---------|
| Inbox | ✓ Clean | 0 items #agent/inbox |
| Raw backlog | ✓ Clean | 0 files >24h unprocessed |
| Concept backlinks | ✓ Clean | 2/2 files checked có backlink đầy đủ |
| Pending reviews | ✓ Clean | 0 pending |

**Action:** Không cần hành động. Hệ thống ổn định.

---

*OpenClaw MEMORY.md — Append-only log*
*Last updated: 2026-07-27 08:00*

---

## 2026-07-27 09:19 — Ingest: Agent Memory — 7 Types (Substack)

**Agent:** Ingest Agent (Kara AX400)  
**Action:** Ingested article https://jamwithai.substack.com/p/agent-memory-the-7-types-you-should  
**File:** `raw/articles/2026-07-27_agent-memory-7-types-substack.md`

### Content Summary
Bài viết từ jamwithai (Substack) phân tích 7 loại memory trong AI agents — framework để thiết kế agent memory trước khi deploy production.

### The 7 Types of Agent Memory
1. **In-context / working memory** — What the model can see right now in the prompt
2. **Semantic memory** — Long-term facts and concepts
3. **Episodic memory** — Specific experiences and events
4. **Procedural memory** — How to perform tasks (skills)
5. **External / retrieval memory** — Data fetched from outside
6. **Parametric memory** — Knowledge encoded in model weights
7. **Prospective memory** — Remembering to do things in the future

### Key Insights
- "More memory is not a better agent. A better agent forgets on purpose."
- Distinction: stored vs active, what vs where
- Based on CoALA: Cognitive Architectures for Language Agents (Sumers et al., 2023)
- Common pitfall: "just add a vector DB" — fails when mixing what/where axes

### Status
- Unprocessed, chờ Compile Agent xử lý 08:00 ngày mai


---

## 2026-07-27 10:19 — Ingest: The "Let Them" Theory (Gabriel Reality)

**Agent:** Ingest Agent (Kara AX400)  
**Action:** Ingested article https://gabrielrealityofficial.substack.com/p/the-let-them-theory-will-change-your  
**File:** `raw/articles/2026-07-27_the-let-them-theory-gabriel-reality.md`

### Content Summary
Bài viết từ Gabriel Reality (Substack) về "Let Them" theory — cách tiếp cận relationships khi đối phó với ngườii có behavior inconsistent.

### Core Concept
- Đừng cố giải thích hay thay đổi ngườii có behavior inconsistent
- Hãy "let them" — chấp nhận họ đúng là những gì họ đang thể hiện
- Update behavior của mình thay vì cố fix họ

### Key Insights
- Brain's intolerance of uncertainty response — anterior cingulate cortex fires khi gặp unpredictable behavior
- "The confusion is the answer" — inconsistency là thông tin về who they are
- Control trap: Staying feels like loyalty, explaining feels like honesty, trying harder feels like commitment
- Letting them là chọn finite discomfort (grief, clarity) thay vì indefinite discomfort (the chase loop)

### Quotes
- Jane Goodall: "You cannot get through a single day without having an impact..."
- Epictetus: "People are disturbed not by things, but by the views which they take of things."
- Coco Chanel: "The most courageous act is still to think for yourself. Aloud."
- Abraham Joshua Heschel: "Self-respect is the root of discipline..."

### Status
- Unprocessed, chờ Compile Agent xử lý 08:00 ngày mai


---

## 2026-07-29 19:23 — Ingest: How to Remember Everything You Read (Dan Koe)

**Agent:** Ingest Agent (Kara AX400)  
**Action:** Ingested article https://letters.thedankoe.com/p/how-to-remember-everything-you-read  
**File:** `raw/articles/2026-07-29_how-to-remember-everything-you-read-dan-koe.md`

### Content Summary
Bài viết từ Dan Koe (Substack) về cách học thực sự hiệu quả — không phải memorization mà là understanding thông qua goals và projects.

### Key Insights
- "If you need to remember it, it's not important. If it's important, you will remember it."
- Learning is an OUTPUT process, not input process — output demands input
- Cybernetic learning process: Reference signal (goal) → Sensor → Comparator (gap/error) → Actuator
- Goals create error signals → filters → relevance → retention
- "Second brain" và note-taking systems are largely useless without action
- Treat life as projects: mind, body, relationships, finances

### Framework
- Don't start with learning — take the first step toward the goal instead
- Being extreme changes your brain and enhances neuroplasticity
- "Burn the boats. Change your life."

### Status
- Unprocessed, chờ Compile Agent xử lý 08:00 ngày mai


---

## 2026-07-30 09:45 — Applied Fixes (Format 07-26 + Hygiene 07-26)

**Agent:** Fix Agent (Kara AX400)  
**Action:** Applied 2 approved reports  
**Reports:** 2026-07-26_format-report.md, 2026-07-26_hygiene-report.md

### Format Fixes Applied
- **No fixes required** — All 357 WARNINGs were forward-reference broken wikilinks (content gaps, not format defects) or validator false positives (4 instances).
- 0 ERRORs — structural format quality clean across all 839 files.
- Report recommendation: APPROVE without fixes.

### Hygiene Fixes Applied
- **No fixes required** — Clean run with 0 issues across 51,997 paths.
- All validation dimensions passed (path whitelist, naming conventions, orphan detection).
- Prior recurring issues resolved: `memory/` folder absent third consecutive run.

### Actions Taken
- Updated report status: `approved` → `applied`
- Archived reports to: `wiki/reviews/archive/2026-07/`
- Updated `_action-required.md`

### Post-Fix Status
- 0 reports pending review
- 0 approved reports waiting for Fix Agent
- System: HEARTBEAT_OK


---

## 2026-07-30 19:10 — Ingest: Làm thế nào để ra quyết định khi còn mơ hồ (thankvn)

**Agent:** Ingest Agent (Kara AX400)  
**Action:** Ingested article https://thankvn.substack.com/p/lam-the-nao-e-ra-quyet-inh-khi-con  
**File:** `raw/articles/2026-07-30_lam-the-nao-e-ra-quyet-inh-khi-con-thankvn.md`

### Content Summary
Bài viết từ thankvn (Substack) về cách ra quyết định trong điều kiện mơ hồ, thiếu thông tin.

### Key Concepts
- Sự mơ hồ là điều kiện mặc định của mọi quyết định đáng giá
- Hai loại quyết định: Cửa hai chiều (Type 2) vs Cửa một chiều (Type 1)
- Quy tắc 40-70% của Colin Powell: Quyết định khi có 40-70% thông tin
- Phần thông tin cuối cùng luôn đắt nhất và ít giá trị nhất
- Thiết kế quyết định sao cho sai thì rẻ

### Techniques
- Thu nhỏ đơn vị cược (small bets)
- Đặt điểm thoát trước khi vào (pre-commitment)
- Chọn phương án giữ nhiều cửa nhất (optionality)

### Three Questions When Uncertain
1. "Điều tôi thực sự chưa biết là gì?"
2. "Chi phí của việc không quyết là gì?"
3. "Sáu tháng nữa nhìn lại, tôi tiếc điều gì hơn?" (regret minimization)

### Status
- Unprocessed, chờ Compile Agent xử lý 08:00 ngày mai


## 2026-07-30 21:03:37 — Indexed

- **Scanned:** 495 concepts + 159 sources = 654 total files
- **Tags indexed:** 23 (9 main-tags + 14 sub-tags)
- **Topics indexed:** 181
- **Orphans deleted:** 0 tag indexes + 0 topic indexes
- **Invalid tags found:** 0
- **Errors:** 0 files skipped

---

## 2026-07-31 20:03 — Ingest: Cuộc đua xem ai không đi lùi (curiositypocket)

**Agent:** Ingest Agent (Kara AX400)  
**Action:** Ingested article https://curiositypocket.substack.com/p/cuoc-ua-xem-ai-khong-i-lui  
**File:** `raw/articles/2026-07-31_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md`

### Content Summary
Bài viết từ curiositypocket (Substack) so sánh cuộc sống hiện đại với máy bay bay ngược hướng quay của Trái Đất — không phải để tiến nhanh, mà để không bị cuốn đi.

### Key Concepts
- **Máy bay bay về phía tây:** Vẫn đang bay về phía đông (theo Trái Đất), chỉ là chậm hơn
- **Cuộc chơi đã đổi hướng:** Từ "ai nhanh hơn" sang "ai trụ lâu hơn"
- **Ngành bán dẫn:** Cuộc đua sinh tử — 30 công ty (2001) → chỉ còn TSMC (2025)
- **Định luật Moore xã hội:** Ngưỡng sống sót liên tục bị nâng lên
- **Công nghệ làm suy yếu năng lực con ngườii:** Giao việc cho máy → quên cách làm

### Key Stories
- **GlobalFoundries (2018):** Dừng phát triển 7nm vì chi phí vượt khả năng thu hồi vốn
- **Intel (2018-2020):** Trì hoãn liên tục 10nm và 7nm
- **Samsung (2021):** Vấp ở tiến trình 4nm, mất đơn hàng Qualcomm sang TSMC
- **TSMC (2025):** Gần như độc quyền sản xuất chip 3nm và 5nm

### Status
- Unprocessed, chờ Compile Agent xử lý 08:00 ngày mai


---

## 2026-08-01 09:13 — Fix Agent Applied 4 Approved Reports

**Agent:** Fix Agent (Kara AX400)  
**Action:** Applied fixes from 4 Hermes reports approved by Julius  
**Reports:** Format 08-01, Output 08-01, Hygiene 08-01, Hygiene 07-30

### Fixes Applied

#### Format 08-01 (5 ERRORs + 433 WARNINGs)
**Files modified (5):**
1. `wiki/concepts/moores-law-economics.md`
   - Fixed: sub_tags [tech→tools], removed field: semiconductor_economics
   - Fixed typos: mớii→mới, ngườii→ngườii (proper noun)

2. `wiki/concepts/optionality-principle.md`
   - Fixed: sub_tags [economic→career]

3. `wiki/concepts/semiconductor-industry-consolidation.md`
   - Fixed: sub_tags [tech→tools], removed core_industry: semiconductor
   - Fixed typos: loạii→loại, mớii→mới

4. `wiki/concepts/technology-driven-dependence.md`
   - Fixed: sub_tags [tech→tools], removed field: technology_impact
   - Fixed typos: ngườii→ngườii, lạii→lại

5. `wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md`
   - Fixed: sub_tags [tech→tools]
   - Fixed typos: ngườii→ngườii, thế giớii→thế giới, lạii→lại

#### Output 08-01 (Typo fixes)
**Double-i typos fixed:** mớii→mới, ngườii→ngườii, lạii→lại, thế giớii→thế giới
**Spacing merge:** Fixed in 4 files
**Files affected:** 4 concept files + 1 source file

#### Hygiene 08-01 & 07-30 (raw/tools/ folder)
**Actions:**
- Moved `raw/tools/2026-07-25_introducing-backsearch-gr-inc.md` → `raw/websites/`
- Moved `raw/tools/2026-07-25_monid-ai-agent-tool-platform.md` → `raw/websites/`
- Moved `raw/tools/tools.md` → `raw/websites/`
- Removed `raw/tools/` folder
- Note: memory/ folder was already clean (no action needed)

### Reports Archived
All 4 reports moved to `wiki/reviews/archive/2026-08/`:
- 2026-08-01_format-report.md
- 2026-08-01_output-report.md
- 2026-08-01_hygiene-report.md
- 2026-07-30_hygiene-report.md

### System Status
- ✅ 0 files unprocessed
- ✅ 0 reports pending
- ✅ 504 concepts, 161 sources, 183 topics, 24 tags
- ✅ 1,030 wiki files total

- 2026-08-05 08:35: Ingested: raw/articles/2026-08-05_why-time-felt-slower-when-we-were-kids.md — "why time felt slower when we were kids" (Contemplation Station, Substack)

## 2026-08-06 08:00:00 — Compiled

- **Raw:** [[raw/articles/2026-08-05_why-time-felt-slower-when-we-were-kids.md]]
- **Source note:** [[wiki/sources/src_why-time-felt-slower-when-we-were-kids.md]]
- **Concepts:** [oddball-effect, proportional-theory-time-perception, predictability-trap, mindfulness-presence]
- **Tags applied:** main=#health, sub=[#psychology, #research, #tutorial], topic=time-perception-childhood
- **Action:** created 4 concept files
- 2026-08-06 09:28: Ingested: raw/posts/2026-07-27_how-to-come-back-from-anything-game-theory.md — "How To Come Back From Anything (Game Theory)" by @incentivising (X.com tweet, 3300 likes)

## 2026-08-06 13:58 — Applied Fixes (Batch 08-01 to 08-05)

### Summary
- **Format fixes (3):** optionality-principle.md sub_tag career→strategy; opinion.md + research.md added Co-occurring tags header
- **Output fixes (1):** 22 double-i typos fixed across 5 files
- **Hygiene (3):** memory/, state/, raw/websites/tools.md — already resolved by Julius

### Files Modified
- wiki/concepts/optionality-principle.md (sub_tag fix)
- wiki/tag/opinion.md (Co-occurring tags header)
- wiki/tag/research.md (Co-occurring tags header)
- wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md (7 typos)
- wiki/concepts/cuoc-dua-khong-di-lui.md (5 typos)
- wiki/concepts/moores-law-economics.md (3 typos)
- wiki/concepts/semiconductor-industry-consolidation.md (3 typos)
- wiki/concepts/technology-driven-dependence.md (4 typos)

### Reports Archived
- 9 reports → wiki/reviews/archive/2026-08/

## 2026-08-10 21:48 — Ingest
- File: raw/posts/2026-08-09_how-to-get-maximum-results-with-minimum-effort-game-theory.md
- Source: https://x.com/incentivising/status/2086512889595072685
- Type: post (X/Twitter article)
- Author: Incentivising (@incentivising)
- Title: How to Get Maximum Results with Minimum Effort (Game Theory)
- Status: unprocessed

## 2026-08-11T14:01:27.409091+00:00 — Indexed (full rebuild)

- **Scanned:** 524 concepts + 168 sources = 692 total files
- **Tags indexed:** 24 (9 main-tags + 15 sub-tags)
- **Topics indexed:** 195
- **Orphans deleted:** 2 tag indexes + 0 topic indexes
- **Invalid tags found:** 0
- **Errors:** 0 files skipped due to invalid frontmatter
- **Mode:** full (28 files changed since last run, ≥20 threshold)
