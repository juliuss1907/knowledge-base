# Format Validation — 2026-09-30
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 405
**Created:** 2026-09-30 23:16:54 +0700
**Validator:** format-validator
**Files checked:** 1125 (612 concepts + 216 sources + 34 indexes + 263 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1125
Total issues: 405

Δ from 2026-09-29 23:15 run (pending — prior run): **0 net change, nhưng KB KHÔNG còn đứng yên — pipeline đã chạy lại.** 1112→1125 files (**+16 mới, −1 xoá, net +13**): 7 concept + 4 source + 5 topic mới, trừ 1 topic bị xoá (`wiki/topic/brain-threat-detection.md`, tracked trong HEAD nhưng không còn trên đĩa). 405 issues giữ nguyên (1E+404W). 385 broken-link cá nhân + 19 forward-reference groups = 404; 273 unique targets, flat. Top-20 giữ nguyên cả slug lẫn count. Forward-ref group list không đổi — cùng 19 file, cùng số ref. 16 file mới **đóng góp 0 broken wikilink** (`grep` tên từng file trong output validator = 0 match); topic bị xoá cũng 0 ⇒ **exact-zero-flat, biến thể KB-growth** (không phải `no-compilation-happened` như 09-29). **Cơ hội drain 8 ngày đã dùng:** 4 raw backlog từ 09-28 (`interconnects-ai`, `atom-project`, `the-second-derivative`, `why-your-evenings`) được Compile Agent xử lý lúc **08:07–08:17**, `status: processed` toàn bộ, `grep -l 'status: unprocessed' raw/*/*.md` = **0** — backlog raw đã cạn lần đầu kể tờ 09-22. 298 tệp `M` (15 concept + 25 tag + 258 topic) là Index Agent regenerate / sửa nội dung, không tính delta. **Backup cron dừng 6 ngày**: HEAD `e05f00ab` (`vault backup: 2026-09-24 20:51:09`) và `git ls-remote` xác nhận remote `master` cùng hash `e05f00abf29e...` ⇒ 19 file wiki + 15 report `??` chưa lên GitHub.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1125 | 612 | 216 | 34 | 263 |

## Delta so với 09-29

| Trục | 09-29 | 09-30 | Δ |
|---|---:|---:|---:|
| Files checked | 1112 | 1125 | **+13** |
| — concepts | 605 | 612 | +7 |
| — sources | 212 | 216 | +4 |
| — topics | 261 | 263 | +2 |
| Total issues | 405 | 405 | 0 |
| ERRORs | 1 | 1 | 0 |
| WARNINGS | 404 | 404 | 0 |
| Individual broken | 385 | 385 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 273 | 273 | 0 |
| File mới (wiki) | 0 | 16 | +16 |
| File bị xoá | 0 | 1 | +1 |
| Raw backlog chờ compile | 4 | **0** | −4 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-09-29 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | 0 (HEAD `e05f00ab`, 09-24 20:51 — backup cron dừng 6 ngày) |
| Untracked (wiki) | `git status --porcelain \| grep '^??'` | **19** — 16 file mới hôm nay + 3 file batch 09-26 (`creative-incubation`, `stress-habituation`, `src_do-less`, đã tính từ 09-26) |
| Deletions | `git status --porcelain \| grep '^ D'` | **1** — `wiki/topic/brain-threat-detection.md` (tracked ở HEAD, không còn trên đĩa) |
| Raw ingested/compiled | `find raw/ -newermt "2026-09-29 23:15"` | **4** — mtime 08:10–08:16, cả 4 `status: processed`; `grep 'status: unprocessed' raw/*/*.md` = **0** |
| Modified (regenerate) | `git status \| cut -c1-2` | 298 `M` (15 concept + 25 tag + 258 topic) — Index Agent / sửa nội dung, không tính delta |

19 file wiki `??` = 16 mới hôm nay (9 concept + 4 source + 5 topic, mtime 08:07–21:03) + 3 carry-over từ batch 09-26. 15 report `??` trong `wiki/reviews/` chưa lên GitHub.

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

Danh sách nhóm **không đổi** so với 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, cùng số ref.

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

- [x] `validate.py`: 1125 files, 0 lỗi đọc, 405 issues
- [x] `parse_issues.py`: 1 ERROR, 404 WARNING; 385 cá nhân + 19 nhóm; 273 đích duy nhất
- [x] Đối chiếu file count thủ công: `wiki/concepts` 612, `wiki/sources` 216, `wiki/topic` 263 — khớp header `validate.py`
- [x] Git reconciliation: `git log --diff-filter=A` rỗng; `git status --porcelain` = 19 `??` (16 mới + 3 carry-over 09-26) + 1 `D` + 298 `M`
- [x] Raw reconciliation: 4 raw mới (mtime 08:10–08:16) `status: processed`; **0 raw `unprocessed`** — backlog 4 file từ 09-28 đã được Compile Agent drain
- [x] 16 file mới **không có broken wikilink nào**: `grep -cE 'creative-incubation|second-derivative-thinking|...|src_do-less|src_interconnects-ai|...' /tmp/issues.txt` = **0**
- [x] HEAD = `e05f00ab` (09-24 20:51) + `git ls-remote` remote `master` = cùng hash — **backup cron dừng 6 ngày**, lần xác minh thứ 3
- [x] Topic deletion: `wiki/topic/brain-threat-detection.md` ` D` — có trong `git ls-files`, không có trên đĩa (Index Agent prune); 258 tracked + 5 `??` = 263 ✓
- [x] Unquoted-`parent` spot-check trên `wiki/tag/*.md`: 0 file — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau 298 lần regenerate
- [x] ERROR slug >50 giữ nguyên từ 09-21→09-30 (10 run liên tiếp)
- [x] Top-20 và forward-ref group list không đổi so với 09-29

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog đứng yên ở **273 đích duy nhất / 19 nhóm** — run thứ 10 liên tiếp kể từ 09-20. Hôm nay flat **không phải vì pipeline đứng yên** (như 09-29): 16 file được compile và 4 raw backlog đã drain, nhưng 273 đích vẫn không giảm. Nghĩa là backlog **không tự thoát** khi Compile Agent hoạt động trở lại — batch hôm nay compile sạch (0 forward-ref), còn 273 đích cũ cần Compile Agent chủ động gọi tên mới giải phóng. `[[game-theory]]` (10 ref) và `[[confirmation-bias]]` (8 ref) vẫn là concept chưa compile có nhiều ref nhất — ưu tiên của Compile Agent, không phải vi phạm format-spec.

ERROR duy nhất (slug 52 ký tự) đã carry-forward 10 run mà chưa được Fix Agent xử lý.
