# Format Validation — 2026-10-02
- **Status:** APPLIED — Fix Agent (Kara AX400, OpenClaw main) xử lúc 2026-10-03 09:27 +07:00. Đã sửa 4 file: ai-lab-business-model.md (stub bullet + bỏ quotes 3 body wikilink + merge 3 bullet Google → 2 + dịch 4 cụm English lẫn), harness-engineering.md (bỏ quotes 3 body wikilink), ai-evals.md (bỏ .md khỏi 4 wikilink), raw/articles/articles.md (159/0, stale sau compile 08:08). Verify: validate.py 1138 files, ERROR 0, WARNING 402. Issue 1 nói target ai-capex-as-credit-cycle không tồn tại — SAI, file có thật (compile 09-30); stub bullet vẫn là defect thật. Chưa xử: Issue 5 Defect B (cần chốt mức trùng lặp), Issue 4 (2 forward-ref raw=0), Issue 3 tồn dư 19 file + 78/82 wikilink .md. Chi tiết: .openclaw/MEMORY.md 2026-10-03.
**Issues found:** 402
**Created:** 2026-10-02 23:15:49 +0700
**Validator:** format-validator
**Files checked:** 1134 (616 concepts + 217 sources + 34 indexes + 267 topics)
**ERRORs**: 0
**WARNINGS**: 402
**INFOS:** 0
**Total issues**: 402
Files checked: 1134
Total issues: 402

Δ from 2026-10-01 23:15 run (approved + applied 2026-10-02 10:52): **−3 issues, biến thể `error-resolved-first-drain` — ngày 0 ERROR đầu tiên kể từ 09-20 (12 lượt), và lần drain đầu tiên sau 11 ngày đứng yên.** 1125→1134 files (**+9**: 4 concept + 1 source + 4 topic), 405→402 issues (**1E+404W → 0E+402W**). **ERROR slug 52 ký tự đã đóng:** Fix Agent rename `src_why-youve-lost-your-curiosity-and-how-to-get-it-back` → `...-curiosity-how-to-get-it-back` (48 ký tự) lúc 10:52, staged `R100` trong git index, 4 ref cũ trong concept bị gỡ và 7 file link được cập nhật ⇒ validator không còn ERROR nào. **−2 broken-link cá nhân** là 2 ref không có đường giải quyết mà báo cáo Output 09-30 đã khuyến nghị bỏ: `[[coordination-games]]` (`nash-equilibrium.md`) và `[[market-inefficiency]]` (`reflexivity-soros.md`) — Fix Agent đã làm đúng. **Unique targets 273→271, thoát plateau 11 lượt** (09-20→10-01 đứng yên đúng 273). 383 cá nhân + 19 forward-reference groups = 402; 201/271 đích chỉ có đúng 1 ref. **16 file wiki mới hôm nay đóng góp 0 broken wikilink** (đo trực tiếp: trong 92 ref được thêm vào 29 file `M`, không ref nào trỏ tới đích đang gãy; 19 file `??` concept/source không chứa ref nào tới đích gãy) ⇒ new-debt = 0. **Cả ba lớp đều chạy** (khác 10-01): Compile 11:20 (5 concept `last_updated: 2026-10-02` + 1 source `date_compiled: 2026-10-02`), Ingest 2 lượt (09:50 video, 19:20 article), Index Agent **full rebuild 21:04** (258 topic + 25 tag regenerate). **Backlog raw = 1** (`raw/articles/2026-05-20_unreasonable-effectiveness-of-html.md`, ingest 19:20 sau giờ Compile ⇒ bình thường). 3 raw `compiled_to` thiếu từ 09-30 **đã đóng** (Fix Agent thêm đủ, kể cả file sai chính tả `compile_to:` → nay là `compiled_to:`). **Backup cron dừng 8 ngày:** HEAD `e05f00ab` (`vault backup: 2026-09-24 20:51`) == `git ls-remote refs/heads/master` ⇒ 28 file wiki + 21 report `??` chưa lên GitHub; đây là lần xác minh thứ 5.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1134 | 616 | 217 | 34 | 267 |

## Delta so với 10-01

| Trục | 10-01 | 10-02 | Δ |
|---|---:|---:|---:|
| Files checked | 1125 | 1134 | **+9** |
| — concepts | 612 | 616 | +4 |
| — sources | 216 | 217 | +1 |
| — topics | 263 | 267 | +4 |
| — indexes | 34 | 34 | 0 |
| Total issues | 405 | 402 | **−3** |
| ERRORs | 1 | **0** | **−1** |
| WARNINGS | 404 | 402 | −2 |
| Individual broken | 385 | 383 | −2 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 273 | **271** | **−2** |
| New files (wiki) | 0 | **16** | +16 |
| Raw ingested | 0 | **6** | +6 |
| Index Agent regenerate | 298 | 283 | −15 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Compitted additions | `git log --since="2026-10-01 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **0** — HEAD vẫn `e05f00ab` (09-24 20:51), backup cron dừng ⇒ **không dùng `git log` một mình** |
| Untracked (wiki) | `git status --porcelain \| grep '^??'` | **49** = 13 concept + 6 source + 9 topic + 21 report. Trong đó **16 file mới hôm nay** (5 concept 11:25–11:29, 2 source 10:57/11:25, 9 topic 21:06 — 5 topic là carry-over bị Index Agent ghi lại mtime, 4 topic thật sự mới) |
| Modified | `git status --porcelain` | **313** `M` (26 concept + 3 source + 258 topic + 25 tag + 1 `_action-required.md`) + **1** `R` staged (rename slug) |
| Deletions | `git status \| grep '^ D'` | **1** — `wiki/topic/brain-threat-detection.md` (carry-forward 3 ngày, Index Agent prune) |
| Raw layer | `find raw/ -newermt "2026-10-01 23:15"` + `grep -l 'status: unprocessed'` | **6 raw nội dung** (4 file `M` được thêm `compiled_to`, 1 `??` đã compile 11:20, 1 `??` ingest 19:20 còn `unprocessed`) |
| Compile activity | `grep -rl '2026-10-02' wiki/concepts wiki/sources` | **11** — 5 concept `last_updated: 2026-10-02` + 6 concept `M` (cập nhật) + 1 source `date_compiled: 2026-10-02` |
| Mtime-only | `find wiki/ -newermt "2026-10-02 00:00"` | **322** — 283 index regenerate (21:06) + 39 content; **không suy ra tăng trưởng từ mtime** |

Hai điểm phải nói rõ:

1. **Net +9 không khớp +16 file mới** ⇒ 2 file nội dung (1 concept + 1 source) biến mất khỏi đĩa mà **không để lại dấu vết git** (file chưa từng được track nên git không thấy). Khả năng cao là Compile Agent thay thế bản nháp cũ khi recompile. **Không khẳng định** nguyên nhân — backup cron đã dừng 8 ngày nên không thể đối chiếu lịch sử. Ghi nhận như quan sát, không phải finding.
2. **`src_interconnects-ai.md` có `date_compiled: 2026-09-30` nhưng file sinh lúc 10:57 hôm nay** ⇒ nguyên liệu là raw ingest 09-28, bị compile trễ 4 ngày. Không phải lỗi format (validate.py không kiểm tra ngày trùng batch), nhưng Output Validator nên biết để phân loại "file mới".

---

## Forward-Reference Groups (19)

| File | Broken refs |
|---|---:|
| `wiki/sources/src_mental-models-of-art.md` | 9 |
| `wiki/sources/src_mental-models-of-economics.md` | 9 |
| `wiki/sources/src_thought-experiment.md` | 9 |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| `wiki/concepts/third-order-thinking.md` | 6 |
| `wiki/concepts/thought-experiment.md` | 6 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

Danh sách **không đổi** so với 10-01, 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, cùng số ref. Tổng 108 ref trong 19 nhóm.

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

So với Top-20 hôm qua: **thứ tự `decision-making`/`career-design`/`ai-coding-agents` đổi chỗ** (cùng count 5), `first-order-thinking` (3) **thoát khỏi** Top-20, `stoicism` (3) **vào** Top-20 — đủ để phá vỡ chuỗi "Top-20 giữ nguyên 11 lượt", nhưng chỉ là **hoán đổi chỗ ngang hàng**, không phải thay đổi cấu trúc backlog.

---

## Verification

- [x] `validate.py`: 1134 files, 0 lỗi đọc, 402 issues, 0 ERROR
- [x] `parse_issues.py`: 0 ERROR, 402 WARNING; 383 cá nhân + 19 nhóm; 271 đích duy nhất (201 đích chỉ 1 ref)
- [x] Đối chiếu file count thủ công: `wiki/concepts` 616, `wiki/sources` 217, `wiki/topic` 267, `wiki/tag` 25 + 6 raw sub-index + `raw/raw.md` + `wiki/wiki.md` + `context/context.md` = 34 index ⇒ khớp header
- [x] **ERROR slug 52 ký tự đã đóng**: slug mới 48 ký tự, `git diff --cached` = `R100` staged, `grep -rn 'why-youve-lost-your-curiosity-and-how' wiki/` chỉ còn hit trong `original:` (hợp lệ, trỏ raw) + report cũ
- [x] **−2 broken link có nguồn gốc**: `git diff -U0` trên 29 file `M` cho thấy đúng 6 ref bị gỡ — 4 ref slug cũ (mục tiêu vẫn resolve sau rename) + `coordination-games` + `market-inefficiency` (không có concept/source/raw) ⇒ giải thích trọn vẹn 385→383
- [x] **New-debt = 0, đo trực tiếp**: 92 ref thêm vào 29 file `M`; đối chiếu từng ref với bộ 271 đích đang gãy ⇒ 0 match; 19 file `??` concept/source ⇒ 0 match
- [x] `git log --diff-filter=A` rỗng **không** được dùng để kết luận "pipeline idle" — `git status ??` + ctime cho thấy 16 file mới (bằng chứng 10-02: `git log` alone sai)
- [x] Net +9 vs +16 mới: 2 file nội dung mất dấu vết git, ghi nhận dưới dạng quan sát, không suy đoán nguyên nhân
- [x] Unquoted-`parent` trên 25 tag file: **0** — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau lần full rebuild thứ 7
- [x] 3 raw `compiled_to` từ 09-30 đã đủ (`will-ai-replace-systems-thinking`, `suyash-karn-...-static-website`, `google-cloud-agent-sandbox-runtimes`); `grep -rn '^compile_to:' raw/` = 0
- [x] Backlog raw = 1 (`unreasonable-effectiveness-of-html`, ingest 19:20 sau giờ Compile 11:20) — hành vi bình thường
- [x] `wiki/topic/brain-threat-detection.md` vẫn ` D` — carry-forward 3 ngày, không phải sự kiện mới
- [x] HEAD `e05f00ab` (09-24 20:51) == `git ls-remote refs/heads/master` — backup cron dừng 8 ngày, lần xác minh thứ 5
- [x] Forward-ref group list không đổi (cùng 19 file, cùng số ref)

---

## Escalations

Không có escalation mới.

**Standing note (không phải escalation):** forward-reference backlog **thoát plateau 11 lượt** — 273 → 271 đích duy nhất, nhờ 2 ref không có đường giải quyết bị gỡ. Nhưng đây là **drain có chọn lọc**, không phải backlog tự thoát: 201/271 đích chỉ có đúng 1 ref, và 92 ref mới hôm nay đều trỏ tới đích đang tồn tại. `[[game-theory]]` (10) và `[[confirmation-bias]]` (8) vẫn là concept chưa compile có nhiều ref nhất — ưu tiên của Compile Agent, không phải vi phạm format-spec. **Không escalate `[[naval-ravikant]]`/`[[agent-initiated-code-artifacts]]`/`[[multi-agent-systems]]`/`[[walk-forward-analysis]]`**: đã xác minh không có concept, source, lẫn raw nào ⇒ forward-ref vô đường giải quyết, xử lý bằng cách bỏ link (như Fix Agent vừa làm với 2 ref kia), không phải lỗi format-spec.

**Hai việc Fix Agent đã hoàn thành hôm nay** (đóng, không cần báo lại): (1) rename slug 52→48 ký tự + 7 file link — chấm dứt chuỗi carry-forward 12 lượt (09-21→10-02); (2) bỏ 2 wikilink vô đường giải quyết theo khuyến nghị của Output 09-30.

**Việc còn treo:** `vault backup` dừng 8 ngày. Không phải vấn đề format, nhưng nó làm mất khả năng đối chiếu lịch sử cho mọi validator — ví dụ hôm nay 2 file biến mất mà không có dấu vết git. Hygiene Inspector đang theo dõi; không re-escalate ở đây.
