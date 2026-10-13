# Format Validation — 2026-10-13

**Status:** pending
**Issues found:** 394
**Created:** 2026-10-13 23:19:15 +0700
**Validator:** format-validator
**Files checked:** 1158 (629 concepts + 222 sources + 34 indexes + 273 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1158
Total issues: 394

Δ from 2026-10-12 23:16:13 run (pending — prior run): **0 net change, biến thể exact-zero-flat KB-growth (chu kỳ 24h, 10-12 → 10-13).** 1153→1158 files (**+5**: +2 concepts, +1 source, +2 topics), 394 issues giữ nguyên (**0E+394W+0I**). **375 cá nhân + 19 forward-reference groups = 394**; unique targets **267 flat** (ngày thứ 5 tại 267: 10-04, 10-10, 10-11, 10-12, 10-13). Top-20 targets giữ nguyên toàn bộ slug và count (hạng 19-20 đồng hạng 3 ref). **Tầng wiki hoạt động trở lại:** Compile Agent biên soạn thành công 1 bài viết từ raw (`src_how-i-stopped-feeling-overwhelmed`, `creative-overwhelm`, `separation-of-creation-and-judgment`), Index Agent tạo 2 topic mới (`creative-overwhelm-habits`, `creative-process`). Toàn bộ 5 file mới đóng góp **0 format error và 0 broken wikilink** (`validate.py` sạch 100%). **Tầng raw:** `raw/articles/2026-07-29_how-i-stopped-feeling-overwhelmed.md` đã chuyển sang `status: processed`, backlog raw = 0 unprocessed. **Tầng index:** Index Agent full rebuild lúc 21:00 hôm nay (298 file: 25 tag + 273 topic). **Git & backup:** 🟢 `vault backup` cron hoạt động bình thường (nhiều commit tự động trong ngày), HEAD cục bộ khớp master.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1158 | 629 | 222 | 34 | 273 |

## Delta so với 10-12

| Trục | 10-12 | 10-13 | Δ |
|---|---:|---:|---:|
| Files checked | 1153 | 1158 | **+5** |
| — concepts | 627 | 629 | +2 |
| — sources | 221 | 222 | +1 |
| — topics | 271 | 273 | +2 |
| — indexes | 34 | 34 | 0 |
| Total issues | 394 | 394 | **0** |
| ERRORs | 0 | 0 | 0 |
| WARNINGS | 394 | 394 | 0 |
| Individual broken | 375 | 375 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 267 | 267 | **0** |
| New wiki content files | 0 | **3** | **+3** |
| Raw ingested (unprocessed) | 1 | **0** | **−1** |
| Index Agent regenerate | 294 | **298** | +4 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-10-12 23:16" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **5** file wiki: `creative-overwhelm.md`, `separation-of-creation-and-judgment.md`, `src_how-i-stopped-feeling-overwhelmed.md`, `creative-overwhelm-habits.md`, `creative-process.md` |
| Deleted | `--diff-filter=D -- wiki/` | **0** |
| Modified (git status) | `git status --porcelain` | Chỉ `.hermes/skills/.usage.json` modified; vùng wiki/ và raw/ sạch |
| Untracked | `git status --porcelain \| grep '^??'` | **0** file trong wiki/ và raw/ |
| Compile activity | `find wiki/concepts wiki/sources -newermt "2026-10-12 23:16"` | **3** file mới (`src_how-i-stopped-feeling-overwhelmed`, `creative-overwhelm`, `separation-of-creation-and-judgment`) + 2 concept updated (`attention-management`, `consumption-vs-action`) lúc 08:03:26 |
| Index rebuild | `find wiki/topic wiki/tag -newermt "2026-10-13 00:00"` | **298** (273 topic + 25 tag) — mtime đồng loạt **21:00** hôm nay |
| Raw layer | `grep -l 'status: unprocessed' raw/*/*.md` | **0** file — backlog raw = 0 (bài `how-i-stopped-feeling-overwhelmed` đã compile) |
| Backup state | `git log -1 --oneline` | `ebbe1b35` (23:09:46) — backup cron chạy đều đặn liên tục |

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

Danh sách **không đổi** so với 10-12, 10-11, 10-10, 10-04, 10-03, 10-02, 10-01, 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, tổng **106 ref** (không đổi).

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

Danh sách **không đổi** so với 10-12, 10-11, 10-10, 10-04 (plateau 267 unique targets, ngày thứ 5 liên tiếp).

---

## Escalations

Không có escalation mới.
- 0 ERROR vi phạm cấu trúc format.
- Toàn bộ 394 WARNING là nợ forward-reference kế thừa từ các concept chưa biên soạn.
- 5 file mới hôm nay tuân thủ 100% format-spec.md và không tạo thêm forward-ref mới.

---

## Verification

- [x] Chạy `validate.py` trên 1158 file toàn KB: 0 ERROR, 394 WARNING, 0 INFO.
- [x] Phân tích bằng `parse_issues.py`: 375 broken cá nhân, 19 groups, 267 unique targets.
- [x] Xác minh 5 file mới hôm nay (2 concepts, 1 source, 2 topics): 0 lỗi format, 0 broken wikilink.
- [x] Đối chiếu git log và mtime: 5 file mới được commit bởi vault backup cron (`73f093a1` và `a77afbaf`).
- [x] Kiểm tra tầng raw: 0 unprocessed files (bài nạp ngày 10-12 đã compile thành công).
- [x] Kiểm tra cross-file integrity qua `verify_integrity.py` và `ad-hoc-verify.py`.
