# Format Validation — 2026-09-29
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 405
**Created:** 2026-09-29 23:15:25 +0700
**Validator:** format-validator
**Files checked:** 1112 (605 concepts + 212 sources + 34 indexes + 261 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1112
Total issues: 405

Δ from 2026-09-28 23:15 run (pending — prior run): **0 net change.** 1112→1112 files (+0); 405 issues giữ nguyên (1E+404W). 385 broken-link cá nhân + 19 forward-reference groups = 404; 273 unique targets, flat. Top-20 giữ nguyên cả slug lẫn count. Forward-ref group list không đổi — cùng 19 file. Biến thể exact-zero-flat **no-compilation-happened**, quay lại **dạng mạnh nhất**: `find raw/ -newermt "2026-09-28 23:15"` trả **0** — tầng raw cũng đứng yên, không chỉ tầng wiki. Ba lớp (wiki, raw, git) đều tĩnh trong 24h. 5 file wiki `??` là batch "do-less" 09-26 08:04, đã tính từ 09-26, **không phải file mới**. 309 tệp `M` (3 concept + 25 tag + 259 topic) là Index Agent regenerate — không tính delta. HEAD vẫn `e05f00ab` (`vault backup: 2026-09-24 20:51:08`) và `git ls-remote` xác nhận remote `master` cùng hash ⇒ **backup cron dừng 5 ngày**, đây là lần xác minh thứ hai trong ngày (Output 09-29 đã báo) và vẫn chưa phục hồi.

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

**Note:** Carry-forward 09-21→09-29 (lần thứ 9). Chưa có bằng chứng Fix Agent đã sửa — vẫn là ERROR duy nhất trong KB.

---

## New Files — cả ba lớp đứng yên

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-09-28 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | 0 (HEAD `e05f00ab`, 09-24 20:51 — backup cron 5 ngày chưa chạy) |
| Untracked (wiki) | `git status --porcelain \| grep '^??'` | 5 — batch "do-less", mtime 09-26 08:04, **đã tính từ 09-26, không phải mới** |
| Deletions/merges | `git log --diff-filter=D -- wiki/{concepts,sources}` | 0 — không có merge, không cần trừ |
| Raw ingested | `find raw/ -newermt "2026-09-28 23:15" -name "*.md"` | **0** — ngược lại 09-28 (4 file); Ingest ngày qua đã dừng |
| Modified (regenerate) | `git status \| cut -c1-2` | 309 `M` (3 concept + 25 tag + 259 topic) — Index Agent, không tính delta |

Cả 5 file wiki `??` đều **0 broken wikilink** (xác nhận 09-26, không đổi). 4 raw backlog từ 09-28 (`interconnects-ai`, `why-your-evenings`, `the-second-derivative`, `atom-project`) vẫn `??` unprocessed — **vẫn là cơ hội drain, chưa ai xử lý**. 12 report `??` trong `wiki/reviews/` chưa lên GitHub.

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

Danh sách nhóm **không đổi** so với 09-28, 09-27, 09-26, 09-25 — cùng 19 file, cùng số ref.

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
- [x] Git reconciliation: `git log --diff-filter=A` rỗng; `git status --porcelain` = 5 `??` wiki (batch 09-26) + 12 `??` report + 309 `M`; `--diff-filter=D` rỗng (0 merge)
- [x] Raw reconciliation: `find raw/ -newermt "2026-09-28 23:15"` = **0** — Ingest dừng sau 4 file 09-28
- [x] HEAD = `e05f00ab` (09-24 20:51) + `git ls-remote` remote `master` = cùng hash — **backup cron 5 ngày**, xác minh lần 2 trong ngày
- [x] Unquoted-`parent` spot-check trên `wiki/tag/*.md`: 0 file — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau 309 lần regenerate tag
- [x] ERROR slug >50 giữ nguyên từ 09-21→09-29 (9 run liên tiếp)
- [x] Top-20 và forward-ref group list không đổi so với 09-28

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog đứng yên ở **273 đích duy nhất / 19 nhóm** — run thứ 9 liên tiếp kể từ 09-20. Hôm nay flat là dạng mạnh nhất (wiki + raw + git đều đứng yên) nhưng **không phải tín hiệu tốt**: backlog không drain vì không có gì được compile, không phải vì đã được resolve. 4 raw backlog từ 09-28 vẫn nằm chờ — Compile Agent resume là điều kiện để 273 đích bắt đầu giảm. `[[game-theory]]` (10 ref) và `[[confirmation-bias]]` (8 ref) vẫn là concept chưa compile có nhiều ref nhất — ưu tiên của Compile Agent, không phải vi phạm format-spec.

ERROR duy nhất (slug 52 ký tự) đã carry-forward 9 run mà chưa được Fix Agent xử lý.
