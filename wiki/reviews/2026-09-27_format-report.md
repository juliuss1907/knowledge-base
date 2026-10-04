# Format Validation — 2026-09-27
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 405
**Created:** 2026-09-27 23:15:40 +0700
**Validator:** format-validator
**Files checked:** 1112 (605 concepts + 212 sources + 34 indexes + 261 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1112
Total issues: 405

Δ from 2026-09-26 23:15 run (pending — prior run): **0 net change.** 1112→1112 files (+0); 405 issues unchanged (1E+404W). 385 individual broken wikilinks + 19 forward-reference groups = 404; 273 unique targets, flat. Top-20 targets identical (cùng slug, cùng count). Forward-ref group list identical — cùng 19 file, cùng số ref. Biến thể exact-zero-flat **no-compilation-happened**, mạnh nhất từ trước tới nay: **0 file wiki mới, 0 raw file mới, 0 commit** — cả ba lớp đều đứng yên. 287 file `M` trong `git status` (25 tag + 259 topic + 3 concept) là Index Agent/Output Validator regenerate, không phải file mới. 5 file `??` untracked vẫn là batch "do-less" đã báo cáo hôm qua — backup cron chưa commit.

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

**Note:** Carry-forward 09-21→09-27 (lần thứ 7). Chưa có bằng chứng Fix Agent đã sửa — vẫn là ERROR duy nhất trong KB.

---

## New Files (0) — pipeline idle

Không có file mới nào trong `wiki/concepts/`, `wiki/sources/`, `wiki/tag/`, `wiki/topic/`.

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-09-26 23:15" --diff-filter=A` | 0 (git log gần nhất: `e05f00ab vault backup: 2026-09-24 20:51:08`) |
| Untracked additions | `git status --porcelain \| grep '^??'` | 5 — batch "do-less" đã tính hôm qua, chưa backup |
| Deletions/merges | `git log --diff-filter=D` | 0 — ngày không có merge, không cần trừ |
| Raw ingested | `find raw/ -newermt "2026-09-26 23:15"` | 0 — Ingest cũng idle |
| Modified (regenerate) | `git status \| cut -c1-2` | 287 `M` (3 concept + 25 tag + 259 topic) — Index Agent regenerate, không tính vào delta |

Cả 5 file untracked đều **0 broken wikilink** — đã xác nhận lại trong run 09-26. Batch "do-less" (`creative-incubation`, `stress-habituation`, `src_do-less`, `doing-less-mind-space`, `ai-trading-agent-safety`) vẫn là toàn bộ phần nợ forward-ref chưa có nguồn resolve.

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

Danh sách nhóm **không đổi** so với 09-26 và 09-25 — cùng 19 file, cùng số ref.

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
- [x] Git reconciliation: `git log --diff-filter=A` rỗng (0 commit mới); `git status --porcelain` = 5 `??` + 287 `M`; `git log --diff-filter=D` rỗng (0 merge)
- [x] Raw reconciliation: 0 raw file mới kể từ 09-26 23:15 — Ingest idle, Compile Agent không có việc
- [x] Unquoted-`parent` spot-check trên `wiki/tag/*.md`: 0 file — [SPEC CONFLICT] 08-29/08-30 vẫn đóng, không tái phát sau 287 lần regenerate tag
- [x] ERROR slug >50 giữ nguyên từ 09-21→09-27 (7 run liên tiếp)
- [x] Top-20 và forward-ref group list không đổi so với 09-26

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog đứng yên ở **273 đích duy nhất / 19 nhóm** — run thứ 7 liên tiếp kể từ 09-20. Hôm nay là ngày flat "sạch" nhất: không có file mới ở **cả ba lớp** (wiki, raw, git), nên backlog không có cơ hội nào dịch chuyển. `[[game-theory]]` (10 ref) và `[[confirmation-bias]]` (8 ref) vẫn là concept chưa compile có nhiều ref nhất — đây là vấn đề ưu tiên của Compile Agent, không phải vi phạm format-spec.

ERROR duy nhất (slug 52 ký tự) đã carry-forward 7 run mà chưa được Fix Agent xử lý.
