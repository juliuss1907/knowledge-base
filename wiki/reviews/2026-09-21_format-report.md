# Format Validation — 2026-09-21

**Status:** pending
**Issues found:** 405
**Created:** 2026-09-21 23:16:23
**Validator:** format-validator
**Files checked:** 1103 (600 concepts + 210 sources + 34 indexes + 259 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405

Files checked: 1103
Total issues: 405

Δ from 2026-09-20 23:16 run (pending — prior run): +18 files (+8 concepts, +2 sources, +0 indexes, +8 topics); +1 total issue (404→405); +1 ERROR (0→1 — new slug >50 chars); individual broken wikilinks flat 385→385; forward-ref groups flat 19→19; unique targets flat 273→273. WARNING count unchanged 404→404. New ERROR on newly compiled source file; new files contribute 0 broken wikilinks to the forward-reference pool.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1103 | 600 | 210 | 34 | 259 |

Phạm vi: 810 tệp nội dung (concepts + sources); thêm 34 chỉ mục và 259 trang chủ đề. Không có lỗi đọc tệp.

Git xác nhận 18 tệp wiki mới kể từ 09-20 23:16 (8 concepts, 2 sources, 8 topics — batch 09-21 vault backup 08:07 + 21:08), 0 tệp xóa. Pipeline biên soạn hoạt động bình thường.

---

## 20 lỗi nghiêm trọng nhất

### Lỗi nghiêm trọng (1)

| # | File | Severity | Category | Issue |
|---|---|---|---|---|
| 1 | `wiki/sources/src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md` | ERROR | Naming | Slug exceeds 50 chars (52 chars) |

**Detail:**
- **File:** `wiki/sources/src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md`
- **Severity:** ERROR
- **Category:** Naming
- **Issue:** Slug `why-youve-lost-your-curiosity-and-how-to-get-it-back` is 52 characters, exceeding the 50-character maximum per format-spec.md §1.2
- **Current:** 52-char slug
- **Expected:** ≤50-char slug
- **Suggested fix:** Rename to `why-youve-lost-curiosity-how-to-get-back` (46 chars) or similar truncated variant; update all internal wikilinks

### Cảnh báo liên kết riêng lẻ (385)

385 broken wikilinks trong 128 files — tất cả là forward-references đến concepts chưa được biên soạn. Chi tiết trong pipe-delimited output (`/tmp/issues.txt`).

### Nhóm forward-references (19)

| File | Broken count |
|---|---|
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

---

## Top 20 broken targets

| Target | Count |
|---|---|
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

Top-20 identical to 09-20 on both names and counts.

---

## Escalations

### [SLUG VIOLATION] — new ERROR on 09-21

`src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md` slug 52 chars exceeds 50-char limit. Compile Agent produced this file in the 09-21 batch. Fix Agent rename needed.

---

## Verification

- [x] format-spec.md read and rules applied
- [x] All wiki files scanned (concepts, sources, indexes, topics)
- [x] Frontmatter compliance checked
- [x] Section structure checked
- [x] Naming conventions checked
- [x] Markdown syntax checked (wikilinks)
- [x] Report written to `wiki/reviews/2026-09-21_format-report.md`
- [x] Delta computed against prior approved/pending report
- [x] Top-20 broken targets enumerated
- [x] Forward-reference groups listed
