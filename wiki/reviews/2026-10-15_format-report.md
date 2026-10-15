# Format Validation — 2026-10-15

**Status:** pending
**Issues found:** 394
**Created:** 2026-10-15 23:16:00 +0700
**Validator:** format-validator
**Files checked:** 1163 (632 concepts + 223 sources + 34 indexes + 274 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1163
Total issues: 394

Δ from 2026-10-14 23:16:00 run (pending — prior run): **0 net change, biến thể exact-zero-flat KB-growth (chu kỳ 24h, 10-14 → 10-15).** 1158→1163 files (**+5**: +3 concepts, +1 source, +1 topic), 394 issues giữ nguyên (**0E+394W+0I**). **375 cá nhân + 19 forward-reference groups = 394**; unique targets **267 flat** (ngày thứ 7 tại 267: 10-04, 10-10, 10-11, 10-12, 10-13, 10-14, 10-15). Top-20 targets giữ nguyên toàn bộ slug và count (hạng 19-20 đồng hạng 3 ref). **Tầng wiki hoạt động:** Compile Agent biên soạn thành công 4 file mới (1 source + 3 concepts) từ Quanta Magazine (`raw/articles/2026-10-12_is-attention-the-essence-of-intelligence.md`); toàn bộ 4 file đạt chuẩn PROMOTE 10/10, 0 format error, 0 broken wikilink. **Tầng raw:** Raw backlog = 0 (`status: unprocessed` = 0). **Tầng index hoạt động:** Index Agent tạo 1 topic mới (`attention-mechanism-foundation.md`) và rebuild lúc 21:00–21:05 (300 file: 25 tag + 274 topic + 1 topic mới). **Git & backup:** 🟢 `vault backup` cron hoạt động trơn tru (nhiều commit tự động trong ngày), HEAD cục bộ khớp master.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1163 | 632 | 223 | 34 | 274 |

## Delta so với 10-14

| Trục | 10-14 | 10-15 | Δ |
|---|---:|---:|---:|
| Files checked | 1158 | 1163 | **+5** |
| — concepts | 629 | 632 | +3 |
| — sources | 222 | 223 | +1 |
| — topics | 273 | 274 | +1 |
| — indexes | 34 | 34 | 0 |
| Total issues | 394 | 394 | **0** |
| ERRORs | 0 | 0 | 0 |
| WARNINGS | 394 | 394 | 0 |
| Individual broken | 375 | 375 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 267 | 267 | **0** |
| New wiki content files | 0 | **4** | **+4** |
| Raw ingested (unprocessed) | 0 | **0** | 0 |
| Index Agent regenerate | 298 | **300** | +2 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-10-14 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **5** file wiki mới (3 concepts, 1 source, 1 topic) |
| Deleted | `--diff-filter=D -- wiki/` | **0** |
| Modified (git status) | `git status --porcelain` | Chỉ `.hermes/skills/.usage.json` modified; vùng wiki/ và raw/ sạch |
| Untracked | `git status --porcelain \| grep '^??'` | **0** file trong wiki/ và raw/ |
| Compile activity | `find wiki/concepts wiki/sources -newermt "2026-10-14 23:15"` | 4 file mới; Output Validator 23:05 đánh giá **PROMOTE 4/4** (0 issue) |
| Index rebuild | `find wiki/topic wiki/tag -newermt "2026-10-15 00:00"` | **299** (274 topic + 25 tag) — mtime đồng loạt **21:00–21:05** hôm nay |
| Raw layer | `grep -l 'status: unprocessed' raw/*/*.md` | **0** file — backlog raw = 0 |
| Backup state | `git log -1 --oneline` | `85aea070` (23:10:31) — backup cron chạy đều đặn liên tục |

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

Danh sách **không đổi** so với 10-14, 10-13, 10-12, 10-11, 10-10, 10-04, 10-03, 10-02, 10-01, 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, tổng **106 ref** (không đổi).

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

Danh sách **không đổi** so với 10-14, 10-13, 10-12, 10-11, 10-10, 10-04 (plateau 267 unique targets, ngày thứ 7 liên tiếp).

---

## Escalations

Không có escalation mới.
- 0 ERROR vi phạm cấu trúc format.
- Toàn bộ 394 WARNING là nợ forward-reference kế thừa từ các concept chưa biên soạn.
- 5 file mới được biên soạn và đánh chỉ mục trong 24h qua tuân thủ 100% định dạng format, đóng góp 0 format error và 0 broken wikilink.

---

## Verification

- [x] Chạy `validate.py` trên 1163 file toàn KB: 0 ERROR, 394 WARNING, 0 INFO.
- [x] Phân tích bằng `parse_issues.py`: 375 broken cá nhân, 19 groups, 267 unique targets.
- [x] Xác minh đối chiếu git log và mtime: 5 file wiki mới được thêm trong 24h qua (+3 concepts, +1 source, +1 topic).
- [x] Kiểm tra tầng raw: 0 unprocessed files (backlog = 0).
- [x] Kiểm tra cross-file integrity qua `verify_integrity.py` và `ad-hoc-verify.py`.
