# Format Validation — 2026-09-26
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 405
**Created:** 2026-09-26 23:15:34 +0700
**Validator:** format-validator
**Files checked:** 1112 (605 concepts + 212 sources + 34 indexes + 261 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1112
Total issues: 405

Δ from 2026-09-25 18:12 run (pending — prior run): **0 net change.** 1107→1112 files (+5: 2 concepts + 1 source + 2 topics); 405 issues unchanged (1E+404W). 385 individual broken wikilinks + 19 forward-reference groups = 404; 273 unique targets, flat. Top-20 targets identical (cùng slug, cùng count). 5 file mới đều **0 broken wikilink**. Biến thể exact-zero-flat, kb-grows-backlog-does-not: batch "do-less" (Finlay, X 2026-09-24) compile sạch về format. Git reconciliation: 0 commit mới kể từ 09-25 18:00 — 5 file mới vẫn untracked (`??`), phát hiện qua `git status` chứ không phải `git log`; 0 file xóa.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1112 | 605 | 212 | 34 | 261 |

---

## Issue 1: Slug exceeds 50 characters

**File:** `wiki/sources/src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug `why-youve-lost-your-curiosity-and-how-to-get-it-back` dài 52 ký tự, vượt giới hạn 50.
**Current:** 52 ký tự
**Expected:** ≤50 ký tự theo `wiki/meta/format-spec.md` §3.1
**Suggested fix:** Đổi slug thành `why-youve-lost-curiosity-how-to-get-back` và cập nhật mọi internal wikilink.

**Note:** Carry-forward 09-21→09-25→09-26 (lần thứ 6). Chưa có bằng chứng Fix Agent đã sửa — vẫn là ERROR duy nhất trong KB.

---

## New Files (5) — 0 format issues

| File | Type | Result |
|---|---|---|
| `wiki/sources/src_do-less.md` | source | PASS — 5 sections đúng thứ tự, `original: "[[2026-09-24_do-less]]"` resolve được trong `raw/posts/` |
| `wiki/concepts/creative-incubation.md` | concept | PASS — 5 sections, `main_tag: productivity` ∈ Pool A, `status: draft` hợp lệ |
| `wiki/concepts/stress-habituation.md` | concept | PASS — 5 sections, `main_tag: health` ∈ Pool A |
| `wiki/topic/doing-less-mind-space.md` | topic | PASS — `topic` khớp filename, `auto_generated: true`, 3 sections |
| `wiki/topic/ai-trading-agent-safety.md` | topic | PASS — `topic` khớp filename, `auto_generated: true`, 3 sections |

Không file mới nào sinh broken wikilink, không vi phạm `.md`-suffix, không vi phạm unquoted-wikilink trong frontmatter.

---

## Forward-Reference Groups (19)

| File | Broken refs |
|---|---:|
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_thought-experiment.md` | 9 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

Danh sách nhóm **không đổi** so với 09-25 — cùng 19 file, cùng số ref.

---

## Top 20 Broken Targets

| Target | Count |
|---|---:|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[deep-work]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[attention-economy]]` | 3 |
| `[[ai-assisted-development]]` | 3 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[intellectual-humility]]` | 3 |
| `[[network-effects]]` | 3 |
| `[[goal-setting]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[homeostasis]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[cognitive-dissonance]]` | 3 |
| `[[power-imbalance]]` | 3 |

---

## Verification

- [x] `validate.py`: 1112 files, 0 lỗi đọc, 405 issues
- [x] `parse_issues.py`: 1 ERROR, 404 WARNING; 385 cá nhân + 19 nhóm; 273 đích duy nhất
- [x] Git reconciliation: 0 commit mới kể từ 09-25 18:00; 5 file mới untracked (`git status --porcelain`), 0 file xóa
- [x] 5 file mới validate thủ công: frontmatter, section order, topic-filename match — 0 issue
- [x] Raw reconciliation: 1 raw file mới uncompiled (`raw/posts/2026-09-24_do-less.md`) — đã compile xong 23:14, nằm trong 5 file mới ở trên
- [x] ERROR slug >50 giữ nguyên từ 09-21→09-26 (6 run liên tiếp)
- [x] Top-20 không đổi

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog đứng yên ở **273 đích duy nhất / 19 nhóm** — run thứ 6 liên tiếp kể từ 09-20. KB +5 file nhưng 0 file mới sinh broken link, nên backlog vẫn đứng yên. `[[game-theory]]` (10 ref) và `[[confirmation-bias]]` (8 ref) vẫn là concept chưa compile có nhiều ref nhất — đây là vấn đề ưu tiên của Compile Agent, không phải vi phạm format-spec.

ERROR duy nhất (slug 52 ký tự) đã carry-forward 6 run mà chưa được Fix Agent xử lý.
