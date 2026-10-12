# Format Validation — 2026-10-10

**Status:** approved — Julius duyệt 2026-10-12
**Approved by:** Julius
**Issues found:** 394
**Created:** 2026-10-10 23:16:18 +0700
**Validator:** format-validator
**Files checked:** 1153 (627 concepts + 221 sources + 34 indexes + 271 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1153
Total issues: 394

Δ from 2026-10-04 23:15:38 run (pending — prior run): **0 net change, biến thể exact-zero-flat `no-compilation-happened` (chu kỳ giãn 6 ngày, 10-04 → 10-10).** 1153→1153 files (**+0**), 394 issues giữ nguyên (**0E+394W+0I**). **375 cá nhân + 19 forward-reference groups = 394**; unique targets **267 flat** (ngày thứ 2 tại 267). Top-20 targets giữ nguyên toàn bộ slug và count (hạng 19-20 đồng hạng 3 ref). **Pipeline đứng yên ở tầng nội dung:** 0 wiki file mới trong 6 ngày (`git log` + `find -newermt` đều 0), 0 raw file mới (`find raw/ -newermt` rỗng), raw backlog = 0 (222/222 dated raw đã `processed`). Output Validator hôm nay 23:03 chạy `[SILENT]` vì không có file mới. **Tầng index hoạt động bình thường:** Index Agent full rebuild lúc 21:04 hôm nay (293 file: 25 tag + 268 topic + 3 topic untracked `??` kế thừa từ 10-04), đóng góp 0 broken wikilink. **Git & backup:** HEAD vẫn là `68f644e7` (2026-10-04 19:41), khớp `refs/heads/master` trên remote; remote default branch vẫn là `main` (`ead50c82`). 293 file `M` + 3 topic `??` chưa commit vào git (chờ vault-backup cron).

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1153 | 627 | 221 | 34 | 271 |

## Delta so với 10-04

| Trục | 10-04 | 10-10 | Δ |
|---|---:|---:|---:|
| Files checked | 1153 | 1153 | **0** |
| — concepts | 627 | 627 | 0 |
| — sources | 221 | 221 | 0 |
| — topics | 271 | 271 | 0 |
| — indexes | 34 | 34 | 0 |
| Total issues | 394 | 394 | **0** |
| ERRORs | 0 | 0 | 0 |
| WARNINGS | 394 | 394 | 0 |
| Individual broken | 375 | 375 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 267 | 267 | **0** |
| New wiki content files | 12 | **0** | −12 |
| Raw ingested (unprocessed) | 0 | **0** | 0 |
| Index Agent regenerate | 293 | **293** | 0 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-10-04 23:30" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **0** — Không có commit mới kể từ 10-04 19:41 (`68f644e7`) |
| Deleted | `--diff-filter=D -- wiki/` | **0** |
| Modified (git status) | `git status --porcelain` | **293** `M` = 268 topic + 25 tag (Index Agent rebuild lúc 21:04 hôm nay). **0 `M` ở `wiki/concepts`/`wiki/sources`** |
| Untracked | `git status --porcelain \| grep '^??'` | **3** topic (`ai-ad-creative-system`, `ai-animation-ads-workflow`, `ai-motion-design-pipeline`) — kế thừa từ 10-04, chưa commit |
| Compile activity | `find wiki/concepts wiki/sources -newermt "2026-10-04 23:30"` | **0** file — không có biên soạn mới |
| Index rebuild | `find wiki/topic wiki/tag -newermt "2026-10-10 00:00"` | **296** (293 `M` + 3 `??`) — mtime đồng loạt **21:04** hôm nay |
| Raw layer | `find raw/ -newermt "2026-10-04 23:30"` | **0** raw mới — backlog raw = 0 (222/222 dated raw đã `processed`) |
| Backup state | `git ls-remote origin refs/heads/{master,main}` | `master` = `68f644e7` khớp HEAD. `main` = `ead50c82` (vẫn lệch nhánh mặc định trên GitHub) |

---

## Forward-Reference Groups (19)

| File | Broken refs |
|---|---:|
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 4 |
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

Danh sách **không đổi** so với 10-04, 10-03, 10-02, 10-01, 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, tổng **106 ref** (không đổi).

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
| `[[stoicism]]` | 3 |

**So với Top-20 10-04:** danh sách **giống hệt** 10-04, cả 20 đích đều giữ nguyên số count. `[[game-theory]]` (10) + `[[confirmation-bias]]` (8) tiếp tục dẫn đầu.

---

## Verification

- [x] `validate.py`: 1153 files, 0 lỗi đọc, 394 issues, **0 ERROR**
- [x] `parse_issues.py`: 0 ERROR, 394 WARNING; **375 cá nhân + 19 nhóm**; **267 đích duy nhất**; 481 tổng ref instance (375 cá nhân + 106 trong group)
- [x] Đối chiếu file count thủ công: `wiki/concepts` 627, `wiki/sources` 221, `wiki/topic` 271, `wiki/tag` 25 + 6 raw sub-index + `raw/raw.md` + `wiki/wiki.md` + `context/context.md` = 34 index ⇒ khớp header (1153 tổng cộng)
- [x] **0 net change xác nhận qua đo đạc trực tiếp**: 0 wiki content file mới, 0 raw mới, 0 commit git trong 6 ngày (10-04 → 10-10)
- [x] **`.md` trong wikilink = 0** trên 848 concept+source — sạch
- [x] **Unquoted-`parent` trên 25 tag file: 0** — [SPEC CONFLICT] vẫn đóng sau rebuild của Index Agent hôm nay (21:04)
- [x] **Format-spec cross-check**: `format-spec.md` không có vi phạm nào
- [x] `## Notes` không phải lỗi format: `format-spec.md:135` ghi rõ optional INFO
- [x] `raw/websites/2026-07-25_tools.md` không có `compiled_to` — mồ côi, không phải lỗi format
- [x] HEAD `68f644e7` khớp `refs/heads/master`. Remote default branch vẫn là `main` (`ead50c82`)

---

## Escalations

### ⚠️ Chu kỳ giãn 6 ngày không có biên soạn mới (10-04 → 10-10)

Kể từ lần validate gần nhất (2026-10-04 23:15), pipeline đứng yên ở tầng nội dung:
- 0 raw file mới được nạp vào `raw/`.
- 0 wiki content file mới được Compile Agent tạo ra trong `wiki/concepts/` hoặc `wiki/sources/`.
- Output Validator hôm nay lúc 23:03 chạy `[SILENT]`.
- Tầng duy nhất hoạt động tự động là Index Agent (chạy hàng ngày 21:04 regenerate tag và topic).

### ⚠️ 293 file Index rebuild + 3 topic mới chưa commit vào git

293 file `M` (268 topic + 25 tag) và 3 topic untracked `??` (`ai-ad-creative-system`, `ai-animation-ads-workflow`, `ai-motion-design-pipeline`) vẫn chưa được commit lên git. Cần vault-backup cron gom lại.

### Việc đã đóng (không cần báo lại ở lượt sau)

1. **Clean streak ERROR tiếp tục**: 0 ERROR ngày thứ 9 liên tiếp (kể từ khi fix slug 10-02).
2. **Backlog raw = 0**: 222/222 dated raw file đã `processed`.
3. **`.md` wikilink = 0, unquoted-`parent` = 0**: duy trì sạch sau các đợt rebuild của Index Agent.

**Standing note (không phải escalation):** forward-reference backlog duy trì ổn định ở **267 unique targets** (ngày thứ 2 liên tiếp). 394 cảnh báo toàn bộ là forward-references đến các concept chưa được biên soạn. `[[game-theory]]` (10) và `[[confirmation-bias]]` (8) là ưu tiên hàng đầu cho Compile Agent.
