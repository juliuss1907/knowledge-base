# Format Validation — 2026-09-28
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 405
**Created:** 2026-09-28 23:15:40 +0700
**Validator:** format-validator
**Files checked:** 1112 (605 concepts + 212 sources + 34 indexes + 261 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1112
Total issues: 405

Δ from 2026-09-27 23:15 run (pending — prior run): **0 net change.** 1112→1112 files (+0); 405 issues giữ nguyên (1E+404W). 385 broken-link cá nhân + 19 forward-reference groups = 404; 273 unique targets, flat. Top-20 giữ nguyên cả slug lẫn count. Forward-ref group list không đổi — cùng 19 file, cùng số ref. Biến thể exact-zero-flat **no-compilation-happened**, nhưng lần đầu **tầng raw KHÔNG đứng yên**: 4 raw mới ingest 19:53–20:43 hôm nay (Output Validator 09-28 đã báo) — `raw/websites/2026-09-28_interconnects-ai.md`, `raw/posts/2026-02-03_why-you-waste-your-evenings-neuroscience.md`, `raw/articles/2026-07-02_the-second-derivative-why-no-one.md`, `raw/websites/2025-08-04_atom-project-american-truly-open-models.md`, đều `??` untracked, đều chờ Compile Agent. HEAD vẫn `e05f00ab` (`vault backup: 2026-09-24 20:51:08`) — **4 ngày backup cron không chạy**, nên `git log --diff-filter=A` rỗng và tầng wiki có 5 file `??` tích tụ. 287 file `M` (3 concept + 25 tag + 259 topic) là regenerate, không tính delta; 2 file topic trong số đó (`ai-trading-agent-safety`, `doing-less-mind-space`) có mtime **09-28 21:06** — Index Agent chạy lại tối nay nhưng chỉ regenerate, không tạo file mới.

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

**Note:** Carry-forward 09-21→09-28 (lần thứ 8). Chưa có bằng chứng Fix Agent đã sửa — vẫn là ERROR duy nhất trong KB.

---

## New Files — wiki layer 0, raw layer +4

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-09-27 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | 0 (HEAD `e05f00ab`, 09-24 20:51 — backup cron 4 ngày chưa chạy) |
| Untracked (wiki) | `git status --porcelain \| grep '^??'` | 5 — batch "do-less", mtime 09-26 08:04, chưa backup |
| Deletions/merges | `git log --diff-filter=D -- wiki/{concepts,sources}` | 0 — không có merge, không cần trừ |
| Raw ingested | `find raw/ -newermt "2026-09-27 23:15" -name "*.md"` | **4 file mới** (+3 index `??` cập nhật) — ingest chạy 19:53–20:43 |
| Modified (regenerate) | `git status \| cut -c1-2` | 287 `M` (3 concept + 25 tag + 259 topic) — Index Agent, không tính delta |

Cả 5 file wiki `??` đều **0 broken wikilink** (đã xác nhận ở run 09-26, không đổi). 4 raw mới chưa qua validate.py (nằm ngoài lớp wiki) nhưng frontmatter đều parse sạch: `type: article|post|website`, `title`, `url`, `author`, `date_published` — không có lỗi format ở tầng raw.

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

Danh sách nhóm **không đổi** so với 09-27, 09-26, 09-25 — cùng 19 file, cùng số ref.

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
- [x] Git reconciliation: `git log --diff-filter=A` rỗng; `git status --porcelain` = 5 `??` + 287 `M`; `--diff-filter=D` rỗng (0 merge)
- [x] Raw reconciliation: **4 raw mới** (ingest 19:53–20:43) — khác 09-27, Ingest đã chạy lại nhưng Compile Agent chưa xử lý
- [x] HEAD = `e05f00ab` (09-24 20:51) — vault backup cron trễ 4 ngày, `git log` không phản ánh hoạt động thực tế; đã cross-check bằng `git status ??` + mtime như skill yêu cầu
- [x] Unquoted-`parent` spot-check trên `wiki/tag/*.md`: 0 file — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau 287 lần regenerate tag
- [x] ERROR slug >50 giữ nguyên từ 09-21→09-28 (8 run liên tiếp)
- [x] Top-20 và forward-ref group list không đổi so với 09-27
- [x] 4 raw mới: frontmatter parse sạch, không lỗi format tầng raw

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog đứng yên ở **273 đích duy nhất / 19 nhóm** — run thứ 8 liên tiếp kể từ 09-20. Hôm nay backlog vẫn đứng yên nhưng **lý do đã đổi**: 09-27 là "cả ba lớp đứng yên", hôm nay là "tầng wiki đứng yên còn tầng raw đã chạy" — Compile Agent có việc nhưng chưa làm. 4 raw mới trong hàng đợi là cơ hội drain đầu tiên sau 8 ngày. `[[game-theory]]` (10 ref) và `[[confirmation-bias]]` (8 ref) vẫn là concept chưa compile có nhiều ref nhất — vấn đề ưu tiên của Compile Agent, không phải vi phạm format-spec.

ERROR duy nhất (slug 52 ký tự) đã carry-forward 8 run mà chưa được Fix Agent xử lý.
