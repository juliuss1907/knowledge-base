# Format Validation — 2026-09-25
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 405
**Created:** 2026-09-25 18:12:45 +0700
**Validator:** format-validator
**Files checked:** 1107 (603 concepts + 211 sources + 34 indexes + 259 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1107
Total issues: 405

Δ from 2026-09-24 08:50 run (pending — prior run): **0 net change.** 1107→1107 files; 405 issues unchanged (1E+404W). 385 individual broken wikilinks + 19 forward-reference groups = 404; 273 unique targets. Top-20 targets unchanged. Git xác nhận 0 file thêm/xóa trong `wiki/concepts`, `wiki/sources`, `wiki/tag`, `wiki/topic`; 0 raw file mới. Biến thể exact-zero-flat, no-compilation-happened: wiki layer static, backlog đứng yên.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1107 | 603 | 211 | 34 | 259 |

---

## Issue 1: Slug exceeds 50 characters

**File:** `wiki/sources/src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Slug `why-youve-lost-your-curiosity-and-how-to-get-it-back` dài 52 ký tự, vượt giới hạn 50.
**Current:** 52 ký tự
**Expected:** ≤50 ký tự theo `wiki/meta/format-spec.md` §3.1
**Suggested fix:** Đổi slug thành `why-youve-lost-curiosity-how-to-get-back` và cập nhật mọi internal wikilink.

**Note:** Carry-forward từ 09-21→09-24; chưa có bằng chứng Fix Agent đã sửa.

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

- [x] `validate.py`: 1107 files, 0 lỗi đọc, 405 issues
- [x] `parse_issues.py`: 1 ERROR, 404 WARNING; 385 cá nhân + 19 nhóm; 273 đích duy nhất
- [x] Git reconciliation: 0 file thêm, 0 file xóa kể từ lần chạy 09-24 08:50
- [x] Raw reconciliation: 0 raw file mới
- [x] ERROR slug >50 giữ nguyên từ 09-21→09-24
- [x] Top-20 không đổi

---

## Escalations

Không có escalation mới. Forward-reference backlog đứng yên ở 273 đích dù wiki layer không đổi. Lỗi duy nhất là slug dài 52 ký tự, chưa được sửa.
