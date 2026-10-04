# Format Validation — 2026-10-01

**Status:** APPLIED — Fix Agent (OpenClaw main) xử lúc 2026-10-02 10:52 +07:00. CJK cleanup 9 file/11 dòng/26 ký tự (giữ 3 file hợp lệ: byte-level-bpe 中, hundred-years-humiliation 百年国耻, chinese-culture-confucianism 国家); rename slug 52→48 ký tự `src_why-youve-lost-your-curiosity-how-to-get-it-back` + 7 file link; vá mắt xích metrics vào src_ai-reflexivity-loop-is-same; 3 compiled_to; 2 broken wikilink bỏ; 9 khoá `- **Trạng thái:**` → `- **Status:** pending`. 4 claim trong báo cáo bị đính chính sau khi đo trực tiếp — xem `.openclaw/MEMORY.md` 2026-10-02.
**Issues found:** 405
**Created:** 2026-10-01 23:16:01 +0700
**Validator:** format-validator
**Files checked:** 1125 (612 concepts + 216 sources + 34 indexes + 263 topics)
**ERRORs**: 1
**WARNINGS**: 404
**INFOS:** 0
**Total issues**: 405
Files checked: 1125
Total issues: 405

Δ from 2026-09-30 23:15 run (pending — prior run): **0 net change, biến thể exact-zero-flat `no-compilation-happened` — mạnh nhất từ 09-29.** 1125→1125 files (**+0**), 405 issues giữ nguyên (1E+404W). 385 broken-link cá nhân + 19 forward-reference groups = 404; 273 unique targets, Top-20 giữ nguyên cả slug lẫn count (run thứ 11 liên tiếp). **Không có compile:** `grep -rl '2026-10-01' wiki/concepts wiki/sources` = **0** (không file nào có `date_compiled`/`last_updated` hôm nay), `find raw/ -newermt "2026-09-30 23:15"` = **0**, `git log --diff-filter=A` rỗng ⇒ **cả ba lớp wiki/raw/git đứng yên**. 19 file `??` trong `wiki/` là **đúng 19 file đã tính hôm qua** (16 batch 09-30 + 3 carry-over 09-26) — không file nào mới. **Nhưng tầng index CÓ chạy:** 288 tệp `M` với mtime đồng loạt **21:09 hôm nay** (25 tag + 258 topic + 5 topic `??`), tức Index Agent regenerate lại toàn bộ sau khi concept mới của 09-30 đã có mặt — chứng tỏ flat **không** phải vì pipeline chết, mà vì Compile Agent ngủ tiếp. 15 concept `M` có mtime **09-26/09-30** (batch hôm qua), không phải sửa hôm nay. **Backlog raw = 0** (`grep -l 'status: unprocessed'` = 0, giữ nguyên drain 09-30). 1 topic bị prune (`brain-threat-detection.md`) vẫn ` D` — carry-forward, đã ghi ở 09-30. **Backup cron dừng 7 ngày**: HEAD `e05f00ab` (`vault backup: 2026-09-24 20:51`) == `git ls-remote refs/heads/master` (`e05f00abf29e…`) ⇒ 19 file wiki + 18 report `??` chưa lên GitHub.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1125 | 612 | 216 | 34 | 263 |

## Delta so với 09-30

| Trục | 09-30 | 10-01 | Δ |
|---|---:|---:|---:|
| Files checked | 1125 | 1125 | **0** |
| — concepts | 612 | 612 | 0 |
| — sources | 216 | 216 | 0 |
| — topics | 263 | 263 | 0 |
| Total issues | 405 | 405 | 0 |
| ERRORs | 1 | 1 | 0 |
| WARNINGS | 404 | 404 | 0 |
| Individual broken | 385 | 385 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 273 | 273 | 0 |
| File mới (wiki) | 16 | **0** | −16 |
| Raw ingested | 4 | **0** | −4 |
| Index Agent regenerate | 298 | 298 | 0 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-09-30 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **0** (HEAD `e05f00ab`, 09-24 20:51 — backup cron dừng 7 ngày) |
| Untracked (wiki) | `git status --porcelain \| grep '^??'` | **19** — y hệt 09-30 (16 batch 09-30 + 3 carry-over 09-26); 0 file mới |
| Deletions | `git status --porcelain \| grep '^ D'` | **1** — `wiki/topic/brain-threat-detection.md` (carry-forward 09-30, Index Agent prune) |
| Raw layer | `find raw/ -newermt "2026-09-30 23:15"` + `grep -l 'status: unprocessed'` | **0** mới; **0** unprocessed — backlog vẫn cạn |
| Compile activity | `grep -rl '2026-10-01' wiki/concepts wiki/sources` | **0** — không concept/source nào biên soạch hôm nay |
| Modified (regenerate) | `find … -newermt` + `git status` | **288** tệp mtime đồng loạt **21:09** (25 tag + 263 topic, trong đó 5 topic `??`) = Index Agent chạy; 15 concept `M` mtime 09-26/09-30 |

Điểm cần nói rõ: **288 tệp có mtime hôm nay nhưng file count không đổi** — đây chính là lý do phải dùng `git status`/`grep date_compiled` chứ không dùng mtime để suy ra "KB đã tăng". 19 file `??` trong `wiki/` giống hệt danh sách hôm qua ⇒ không có file mới nào lọt vào giữa hai lượt.

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

Danh sách nhóm **không đổi** so với 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, cùng số ref.

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
- [x] Không có compile hôm nay: `grep -rl '2026-10-01' wiki/concepts wiki/sources` = **0**; `find raw/ -newermt` = **0**
- [x] 19 file `??` khớp **nguyên văn** danh sách 09-30 ⇒ 0 file mới, không dùng mtime để suy ra tăng trưởng
- [x] 288 tệp `M` mtime 21:09 hôm nay = Index Agent regenerate (25 tag + 263 topic), không tính delta; 15 concept `M` mtime 09-26/09-30
- [x] Unquoted-`parent` spot-check trên `wiki/tag/*.md`: 0 file — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau lượt regenerate thứ 6
- [x] Backlog raw vẫn 0 (`grep -l 'status: unprocessed' raw/*/*.md` = 0)
- [x] `wiki/topic/brain-threat-detection.md` vẫn ` D` — carry-forward 09-30, không phải sự kiện mới
- [x] HEAD `e05f00ab` (09-24 20:51) + `git ls-remote` remote `master` = cùng hash — **backup cron dừng 7 ngày**, lần xác minh thứ 4
- [x] ERROR slug >50 giữ nguyên từ 09-21→10-01 (11 run liên tiếp)
- [x] Top-20 và forward-ref group list không đổi so với 09-30

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog đứng yên ở **273 đích duy nhất / 19 nhóm** — run thứ 11 liên tiếp kể từ 09-20. Hôm nay flat vì **Compile Agent không chạy**, khác 09-30 (compile 16 file) và 09-29 (cả ba lớp tĩnh). Dù vậy backlog **không tự thoát khi Compile hoạt động** — bằng chứng là 09-30: 16 file được compile sạch (0 forward-ref) mà 273 đích vẫn nguyên. `[[game-theory]]` (10 ref) và `[[confirmation-bias]]` (8 ref) vẫn là concept chưa compile có nhiều ref nhất — ưu tiên của Compile Agent, không phải vi phạm format-spec.

ERROR duy nhất (slug 52 ký tự) đã carry-forward 11 run mà chưa được Fix Agent xử lý.