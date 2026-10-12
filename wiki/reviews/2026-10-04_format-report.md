# Format Validation — 2026-10-04
**Status:** approved — Julius duyệt 2026-10-12
**Approved by:** Julius
**Issues found:** 394
**Created:** 2026-10-04 23:15:38 +0700
**Validator:** format-validator
**Files checked:** 1153 (627 concepts + 221 sources + 34 indexes + 271 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1153
Total issues: 394

Δ from 2026-10-03 23:15 run (approved + applied 10-04 09:27): **−5 issues (399→394), biến thể `dead-ref-removal` lần 2** — 1139→1153 files (**+14**: 8 concept + 3 source + 3 topic), 399→394 (**0E+399W → 0E+394W**). **375 cá nhân + 19 forward-reference groups = 394**; unique targets **269→267 (−2)**. 5 ref bị gỡ là `[[ai-assisted-development]]` ×3 và `[[diagram-as-code]]` ×2, đo từng file với baseline `e05f00ab`: cả 5 đều nằm trong 4 concept sửa lúc 11:48 (`ai-frontend-design-guidance`, `frontend-design-agent`, `vibe-coding`, `architecture-as-code`, `code-visualization`), và **0 ref gãy nào được thêm**. Tuy nhiên **12 file nội dung mới hôm nay mang 48 broken refs** (đã đếm ở báo cáo 10-03 là carry-forward trong bộ 269) ⇒ **−5 là thành quả rò của −48**, không phải drain thật. **New-debt từ file mới thật sự = 0**: 12 file mới (9 concept + 3 source, 08:05–08:09) → 0 broken; 3 topic mới → 0 broken. **48 ref nằm trong 62 concept/source mà Compile Agent sửa lúc 11:28–11:48** (batch backfill không có raw tương ứng — 63 concept + 11 source có mtime 10-04 nhưng chỉ 12 là file mới thật). **🟢 Backup cron đã phục hồi** — chuỗi "dừng 9,1 ngày" kết thúc: HEAD `68f644e7` (19:41) khớp `refs/heads/master` (`68f644e7…`), commit 19:14 `3b891e34` đóng băng 10 ngày thay đổi. **🟢 4 file mất newline hôm nay đã được sửa** (48→49 disk, nhưng so với blob `e05f00ab`: **0 lost, 4 gained**). **⚠️ 293 file `M` (268 topic + 25 tag) vẫn chưa được backup** — Index Agent full rebuild 21:04.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1153 | 627 | 221 | 34 | 271 |

## Delta so với 10-03

| Trục | 10-03 | 10-04 | Δ |
|---|---:|---:|---:|
| Files checked | 1139 | 1153 | **+14** |
| — concepts | 619 | 627 | +8 |
| — sources | 218 | 221 | +3 |
| — topics | 268 | 271 | +3 |
| — indexes | 34 | 34 | 0 |
| Total issues | 399 | 394 | **−5** |
| ERRORs | 0 | 0 | 0 |
| WARNINGS | 399 | 394 | −5 |
| Individual broken | 380 | 375 | −5 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 269 | 267 | **−2** |
| New wiki content files | 4 | **12** | +8 |
| Raw ingested (unprocessed) | 3 | **0** | −3 |
| Index Agent regenerate | 293 | **293** | 0 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-10-03 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **43** — 24 concept + 10 source + 10 topic trong `3b891e34` (19:14) + 3 topic `??`. HEAD đã bắt kịp ⇒ `git log` **dùng được** lượt này (khác 10-03) |
| Deleted | `--diff-filter=D -- wiki/` | **1** — `wiki/topic/brain-threat-detection.md` (Index Agent prune; **10 ngày** carry-forward) |
| Renamed | `--diff-filter=R -- wiki/` | **1** — `src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md` → `...how-to-get-it-back.md` (rename staged trong `3b891e34`) |
| Modified | `git status --porcelain` | **293** `M` = 268 topic + 25 tag (Index Agent full rebuild 21:04). **0 `M` ở `wiki/concepts`/`wiki/sources`** — toàn bộ 74 file content hôm nay đã được commit |
| Untracked | `git status --porcelain \| grep '^??'` | **3** topic (`ai-ad-creative-system`, `ai-animation-ads-workflow`, `ai-motion-design-pipeline`) — Index Agent tạo sau commit 19:14, chờ backup cron |
| Compile activity | `find wiki/concepts wiki/sources -newermt "2026-10-04 00:00"` | **74** file: 12 file mới thật (08:05–08:09) + 62 file `M` cũ (11:28–11:48, backfill) |
| Index rebuild | `find wiki/topic wiki/tag -newermt "2026-10-04 00:00"` | **293** — 268 topic + 25 tag, mtime đồng loạt **21:04** |
| Raw layer | `find raw/ -newermt "2026-10-03 23:15"` | **3** raw (08:06–08:09) — cả 3 đã `processed` + có `compiled_to`. **Backlog raw = 0** (222/222 không còn `status: unprocessed`; 1 file `raw/websites/2026-07-25_tools.md` mồ côi không có `compiled_to`, carry-forward từ Output 10-04) |
| Backup state | `git ls-remote origin refs/heads/{master,main}` | `master` = `68f644e7` **khớp HEAD** ⇒ 🟢 phục hồi. `main` = `ead50c82` (vẫn lệch — remote default branch là `main`) |

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
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| `wiki/sources/src_probabilistic-thinking.md` | 6 |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| `wiki/sources/src_ai-future-skills.md` | 4 |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 4 |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

Danh sách **không đổi** so với 10-03, 10-02, 10-01, 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file, tổng **106 ref** (không đổi).

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
| `[[first-order-thinking]]` | 3 |

**So với Top-20 hôm qua:** danh sách **giống hệt** 10-03, chỉ đổi chỗ hạng 19↔20 — `first-order-thinking` (3) vào lại Top-20 ở hạng 20, `stoicism` (3) rơi xuống hạng 21. Cả hai dao động quanh ngưỡng 3 ref, **không có đích nào rời khỏi nhóm count ≥ 3**. `[[game-theory]]` (10) + `[[confirmation-bias]]` (8) vẫn cao nhất.

---

## Verification

- [x] `validate.py`: 1153 files, 0 lỗi đọc, 394 issues, **0 ERROR**
- [x] `parse_issues.py`: 0 ERROR, 394 WARNING; **375 cá nhân + 19 nhóm**; **267 đích duy nhất**; 481 tổng ref instance (375 cá nhân + 106 trong group)
- [x] Đối chiếu file count thủ công: `wiki/concepts` 627, `wiki/sources` 221, `wiki/topic` 271, `wiki/tag` 25 + 6 raw sub-index + `raw/raw.md` + `wiki/wiki.md` + `context/context.md` = 34 index ⇒ khớp header
- [x] **−5 giải thích trọn vẹn bằng đo, không suy đoán**: replay đúng luật `validate.py` (`probe = target[:-3]` + 5 thư mục wiki + 7 raw subdir có glob `*_{probe}.md`) trên 848 content file, đối chiếu từng file với blob HEAD (`68f644e7`) bằng cùng một luật ⇒ **0 CLEARED / 0 NEWLY / 0 count-change** giữa HEAD và đĩa. Vì HEAD đã bắt kịp 19:14, phải lùi baseline thêm 1 bước: **`e05f00ab`** (vault backup cuối 09-24). So với đó: 7 target chuyển từ broken → sạch, trong đó 2 đã báo cáo 10-03 (`multi-agent-systems`, `agent-initiated-code-artifacts`) và **5 ref mới hôm nay = `ai-assisted-development` ×3 + `diagram-as-code` ×2**, tất cả nằm trong 5 concept sửa lúc 11:48
- [x] Xác minh 5 ref vừa gỡ không còn đường giải quyết: `ai-assisted-development` raw=0, live-refs=0 (grep toàn KB); `diagram-as-code` raw=0, live-refs=0. Cùng nhóm còn treo từ 10-03: `naval-ravikant` (3) và `walk-forward-analysis` (1)
- [x] **New-debt từ file mới thật = 0**: 12 file nội dung mới hôm nay (9 concept + 3 source, 08:05–08:09, cả 3 từ batch `animation/motion-design`) → 0 broken; 3 topic mới → 0 broken. **0/12 concept mới thiếu `## Notes`**
- [x] **48 ref gãy mới hôm nay đến từ batch 11:28–11:48, không phải file mới**: 62 concept/source cũ được sửa lúc 11:28–11:48 mang 48 broken refs / 44 đích duy nhất (`prompt-injection` 2, `emotional-boundaries` 2, `goal-setting` 2, `workflow-automation` 2, còn lại 1 mỗi đích). Batch này **không có raw tương ứng** — chỉ 3 raw file trong ngày, cả 3 đã compile sang 12 file wiki 08:05–08:09. Đây là nợ có sẵn trong bộ 267 đích, chỉ bị dồn vào file cũ
- [x] **`.md` trong wikilink = 0** trên 848 concept+source (quét `[[….md]]` và `[[….md|alias]]`) — giữ nguyên kết quả 10-03
- [x] **Unquoted-`parent` trên 25 tag file: 0** — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau full rebuild thứ 9
- [x] **Newline cuối file — so với blob `e05f00ab`: 0 lost, 4 gained, 49 pre-existing** trên 848 concept+source. Đối chiếu độc lập bằng `tail -c1 | xxd -p` cũng ra **49/848 thiếu**. ⇒ 4 file mất newline trong batch 10:11 đã được sửa; 49 file còn lại là **kế thừa từ trước**, không phải hậu quả batch hôm nay. `topic` + `tag` (296 file): **0 thiếu**
- [x] **Format-spec cross-check**: `format-spec.md` **không** có quy tắc newline cuối file ⇒ không tính vào 394 issue, `validate.py` không bắt, không vá bằng ERROR (sẽ thành 49 ERROR giả)
- [x] `## Notes` **không** phải lỗi format: `format-spec.md:135` ghi rõ *optional INFO*
- [x] `raw/websites/2026-07-25_tools.md` không có `compiled_to` — mồ côi, Output 10-04 đã báo; không phải lỗi format
- [x] `wiki/topic/brain-threat-detection.md` vẫn không tồn tại — **10 ngày** carry-forward, Hygiene E10 theo dõi
- [x] HEAD `68f644e7` khớp `refs/heads/master` — 🟢 backup cron phục hồi, chuỗi "dừng 9,1 ngày" kết thúc. Remote default branch vẫn là `main` (`ead50c82`) — **cần Julius xác nhận máy chính push đúng nhánh**

---

## Escalations

### 🟢 Đã đóng — backup cron phục hồi (chuỗi 9,1 ngày kết thúc)

HEAD đứng ở `e05f00ab` (09-24 20:51) suốt 6 lượt validate trước vì `vault backup` cron không chạy. Hôm nay có **2 commit thủ công của Julius** giải quyết trọn:

- `3b891e34` (19:14) — đóng băng **10 ngày thay đổi** (496 file, +11.345/−2.077): 24 concept + 10 source + 10 topic mới, 293 file Index rebuild, 1 rename slug, 1 topic prune.
- `68f644e7` (19:41) — `.gitignore` chặn agent home 6,3 GB + gỡ 283 path khỏi tracking.

Hệ quả tích cực cho validator: `git diff` hôm nay **phủ đúng 24 giờ** thay vì 10 ngày, nên ranh giới delta đo được trực tiếp thay vì suy ra. **293 file `M` + 3 topic `??` chưa được backup** — backup cron sẽ gom ở lượt kế tiếp nếu nó thật sự đã phục hồi; nếu lượt 10-05 lại thấy HEAD đứng yên ở `68f644e7` thì đây là lần xác minh thứ 2.

### ⚠️ Nợ mới 48 ref từ batch backfill 11:28–11:48 — không có raw tương ứng

Biến thể chưa từng gặp: 62 concept/source cũ bị sửa lúc 11:28–11:48 mang theo **48 broken wikilink / 44 đích**, trong khi **3 raw file duy nhất trong ngày đã compile sang 12 file wiki lúc 08:05–08:09**. Nghĩa là batch này viết nội dung không bám raw — nguồn thật chưa xác định từ lớp `raw/`.

- Đích mới nổi bật: `prompt-injection` (2), `emotional-boundaries` (2), `workflow-automation` (2), `goal-setting` (+1 → 3), còn 40 đích đều 1 ref.
- **Đây không phải vi phạm format-spec** — broken wikilink chỉ là WARNING, và forward-reference là trạng thái bình thường của KB đang lớn. Nhưng nó là **nợ mới phát sinh từ batch không có provenance**, khác 48 ref mà báo cáo 10-03 gọi là hậu quả ngoài ý muốn của batch dọn `.md`.
- **Không đòi Fix Agent gỡ** — 44 đích này phần lớn là concept hợp lệ chưa được compile; Compile Agent compile nốt mới đúng. Việc cần Fix Agent/Julius xem là: **vì sao batch 11:28 sửa 62 file mà không ingest raw tương ứng**.

### ⚠️ 293 file Index rebuild + 3 topic mới chưa vào git

`git status` cho **293 `M`** (268 topic + 25 tag, mtime 21:04) + **3 `??` topic**. Commit 19:14 đã bắt được rebuild **trước** đó (21:04 hôm nay thuộc về sau commit) — nên 293 file này là kết quả Index Agent **mới nhất**, chưa có backup. Không phải lỗi format; ghi nhận để Hygiene kiểm tra lượt tới.

### Việc đã đóng (không cần báo lại ở lượt sau)

1. **4 file mất newline cuối file** trong batch dọn 10:11 đã được sửa — đo trên blob `e05f00ab`: **0 lost / 4 gained**. 49 file còn thiếu là kế thừa từ trước, tách bạch với thiệt hại mới.
2. **5 ref vô đường giải quyết bị gỡ** (`ai-assisted-development` ×3, `diagram-as-code` ×2) — `raw=0`, `live-refs=0`, đúng mẫu Fix Agent đã làm đúng ở 10-03.
3. **Backlog raw = 0** — 3 raw file 10-04 đều `processed` + có `compiled_to`; 222/222 dated raw file không còn `status: unprocessed`.
4. **Rename slug `curiosity`** chốt bằng commit (`R100`), `## Notes` của 12 concept mới đầy đủ, `.md` wikilink = 0, unquoted-`parent` = 0 sau full rebuild thứ 9.

**Standing note (không phải escalation):** forward-reference backlog đi ngược **3 ngày liên tiếp** — 273 (plateau 11 lượt) → 271 → 269 → **267**. Cả 3 lượt đều do gỡ ref vô đường giải quyết, **không** do Compile Agent compile nốt forward-ref. 267 đích trong đó phần lớn chỉ có đúng 1 ref; `[[game-theory]]` (10) + `[[confirmation-bias]]` (8) vẫn cao nhất và là ưu tiên của Compile Agent, **không phải** vi phạm format-spec.

**Việc còn treo (không thuộc format):** remote default branch là `main` (`ead50c82`) trong khi HEAD local theo `master` (`68f644e7`). 3 lượt xác minh đều ghi nhận, chưa escalate — cần Julius xác nhận máy chính push đúng nhánh.