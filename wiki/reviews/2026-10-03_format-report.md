# Format Validation — 2026-10-03
**Status:** approved — Julius duyệt hàng loạt 2026-10-03
**Issues found:** 399
**Created:** 2026-10-03 23:15:53 +0700
**Validator:** format-validator
**Files checked:** 1139 (619 concepts + 218 sources + 34 indexes + 268 topics)
**ERRORs**: 0
**WARNINGS**: 399
**INFOS:** 0
**Total issues**: 399
Files checked: 1139
Total issues: 399

Δ from 2026-10-02 23:15 run (approved + applied 2026-10-03 09:27): **−3 issues (402→399), biến thể `dead-ref-removal`** — không phải drain có chọn lọc, mà là **5 ref vô đường giải quyết bị gỡ trọn vẹn**. 1134→1139 files (**+5**: 3 concept + 1 source + 1 topic), 402→399 issues (**0E+402W → 0E+399W**). **380 cá nhân + 19 forward-reference groups = 399**; unique targets **271→269 (−2)**. Toàn bộ −3 giải thích bằng `git diff -U0` đối chiếu từng ref với bộ đích resolve được: **11 ref unresolvable bị gỡ, 0 ref unresolvable được thêm**. Trong đó 6 ref đã được báo cáo 10-02 đếm rồi (4 ref slug cũ `...curiosity-and-how...` + `coordination-games` + `market-inefficiency`) ⇒ **phần mới hôm nay đúng 5 ref**: `[[multi-agent-systems]]` ×3 (`agent-harness.md`, `multi-agent-taxonomy.md`, và 1 trong `src_code-as-agent-harness-arxiv-2605-18747.md`) + `[[agent-initiated-code-artifacts]]` ×2 (cùng 2 file). **2/5 ref nằm trong forward-reference group** (`src_code-as-agent-harness-arxiv`: 6→4 ref) ⇒ chỉ **−3** vào cột cá nhân, group count giữ nguyên **19**. Cả 2 đích này đã được báo cáo 10-02 và 09-30 gọi tên là *vô đường giải quyết* — Fix Agent đã làm đúng. **🟢 `.md` trong wikilink: 82→0, đo bằng chính `validate.wikilink_style_issues()`** — batch dọn 10:11 xử lý nốt Issue 3 của báo cáo 10-02. **New-debt = 0, đo trực tiếp**: 4 file nội dung mới hôm nay (10 body ref, 8, 7, 7 ref) đều **0 broken**; 99 file `M` có ref thêm mới nhưng **0 match** với bộ 269 đích đang gãy. **⚠️ Hệ quả ngoài ý muốn của batch 10:11: 48 file mất newline cuối file** (không phải vi phạm format-spec — spec không có quy tắc này; xem Escalations). **Cả ba lớp đều chạy:** Compile 08:05–08:07 (3 concept + 1 source, tất cả từ `src_unreasonable-effectiveness-of-html`), Ingest 21:52–22:04 (3 post), Index Agent **full rebuild 21:07** (268 topic + 25 tag). **Backlog raw = 3** (cả 3 ingest sau giờ Compile 08:07 — bình thường). **Backup cron dừng 9,1 ngày:** HEAD `e05f00ab` (09-24 20:51) == `git ls-remote refs/heads/master` ⇒ 33 file wiki + report `??` chưa lên GitHub; lần xác minh thứ 6.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1139 | 619 | 218 | 34 | 268 |

## Delta so với 10-02

| Trục | 10-02 | 10-03 | Δ |
|---|---:|---:|---:|
| Files checked | 1134 | 1139 | **+5** |
| — concepts | 616 | 619 | +3 |
| — sources | 217 | 218 | +1 |
| — topics | 267 | 268 | +1 |
| — indexes | 34 | 34 | 0 |
| Total issues | 402 | 399 | **−3** |
| ERRORs | 0 | 0 | 0 |
| WARNINGS | 402 | 399 | −3 |
| Individual broken | 383 | 380 | −3 |
| Forward-ref groups | 19 | 19 | 0 |
| Unique broken targets | 271 | 269 | **−2** |
| New wiki content files | 16 | **4** | −12 |
| Raw ingested | 6 | **3** | −3 |
| Index Agent regenerate | 283 | **293** | +10 |

---

| Lớp | Kiểm tra | Kết quả |
|---|---|---|
| Committed additions | `git log --since="2026-10-02 23:15" --diff-filter=A -- wiki/{concepts,sources,tag,topic}` | **0** — HEAD vẫn `e05f00ab` (09-24 20:51), backup cron dừng ⇒ **không dùng `git log` một mình** |
| Untracked (wiki content) | `git status --porcelain \| grep '^??'` | **33** = 16 concept + 7 source + 10 topic. Chỉ **4 là mới hôm nay** (3 concept + 1 source, 08:05–08:07); 12 file còn lại là carry-over 09-26/09-30/10-02 đã tính ở các lượt trước |
| Modified | `git status --porcelain` | **382** `M` (99 concept/source + 268 topic + 25 tag) + **1** `R` staged (rename slug 10-02) |
| Deletions | `git status \| grep '^ D'` | **1 trong wiki** — `wiki/topic/brain-threat-detection.md` (carry-forward 4 ngày, Index Agent prune); 6 `D` còn lại nằm trong `.hermes/skills/` |
| Raw layer | `find raw/ -newermt "2026-10-02 23:15"` + `grep -l 'status: unprocessed'` | **3 raw nội dung mới** (21:52–22:04, cả 3 `status: unprocessed`) + `raw/articles/articles.md` sửa lúc 09:31 (Fix Agent dọn 159/0) |
| Compile activity | `find wiki/concepts wiki/sources -newermt "2026-10-03 00:00"` | **11 file** 08:05–08:07 (3 concept `??` mới + 1 source `??` mới + 7 concept `M` cập nhật); `grep -rl '2026-10-03'` = 11 file |
| Index rebuild | `find wiki/topic wiki/tag -newermt "2026-10-03 00:00"` | **293** — 268 topic + 25 tag, mtime đồng loạt **21:07** |

Hai điểm phải nói rõ:

1. **`git diff` hôm nay phủ 9 ngày, không chỉ 24 giờ.** HEAD đứng từ 09-24 nên `git diff -U0` so với HEAD chứa **cả** batch Fix Agent 09-27 hôm nay **lẫn** batch dọn `.md` 10:11. Đã tách bằng cách trừ 6 ref đã báo cáo 10-02 đếm rồi — phần dư **5 ref** khớp chính xác với −3 cá nhân + 2 ref trong group. Không có cách nào khôi phục ranh giới 24h thật sự khi HEAD cũ hơn 9 ngày.
2. **10 topic `??` nhưng net chỉ +1 topic** (267→268). 258 topic đã tracked còn trên đĩa + 10 untracked = 268 ✓ (1 topic đã tracked bị prune). Vì cả 268 topic có mtime 21:07, không phân biệt được topic nào *được tạo mới* và topic nào chỉ *được Index Agent viết lại* — và 9/10 topic `??` đã có mặt trong `git status` của lượt trước. **Không suy đoán**; ghi nhận là giới hạn đo đạc do backup cron dừng.

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
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | **4** (6 → 4) |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| `wiki/sources/src_global-macro-investing.md` | 4 |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

Danh sách **không đổi** so với 10-02, 10-01, 09-30, 09-29, 09-28, 09-27, 09-26, 09-25 — cùng 19 file. Tổng **106 ref** (10-02: 108) — giảm 2 vì `src_code-as-agent-harness-arxiv` mất `multi-agent-systems` + `agent-initiated-code-artifacts`.

---

## Top 20 Broken Targets

| Target | Count |
|---|---:|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[deep-work]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
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

**So với Top-20 hôm qua:** `career-design` lên từ hạng 3 lên hạng 4 (cùng count 5, hoán đổi chỗ với `decision-making`/`ai-coding-agents`); `first-order-thinking` (3) **thoát** khỏi Top-20 lần thứ 2 (và 10-03, 10-02 nó đã vào rồi lại ra); `stoicism` (3) ở hạng 21. Ngoài hoán đổi chỗ ngang hàng, **không có đích nào rời khỏi nhóm có count ≥ 3** — cấu trúc backlog giữ nguyên.

---

## Verification

- [x] `validate.py`: 1139 files, 0 lỗi đọc, 399 issues, **0 ERROR**
- [x] `parse_issues.py`: 0 ERROR, 399 WARNING; **380 cá nhân + 19 nhóm**; **269 đích duy nhất**
- [x] Đối chiếu file count thủ công: `wiki/concepts` 619, `wiki/sources` 218, `wiki/topic` 268, `wiki/tag` 25 + 6 raw sub-index + `raw/raw.md` + `wiki/wiki.md` + `context/context.md` = 34 index ⇒ khớp header
- [x] **−3 giải thích trọn vẹn bằng đo, không suy đoán**: `git diff -U0` trên 99 file `M` ⇒ 11 ref unresolvable bị gỡ / **0** ref unresolvable được thêm. Trừ 6 ref đã báo cáo 10-02 đếm ⇒ 5 ref mới; 2 trong số đó thuộc group `src_code-as-agent-harness-arxiv` (6→4) ⇒ −3 cá nhân, group 19 giữ nguyên
- [x] Xác minh 2 đích vừa gỡ không còn đường giải quyết: `multi-agent-systems` issues=0 live-refs=0; `agent-initiated-code-artifacts` issues=0 live-refs=0
- [x] Xác minh slug cũ vẫn gãy, slug mới resolve: `src_why-youve-lost-your-curiosity-and-how-to-get-it-back` issues=0 (đã hết ref) nhưng file cũ **không** tồn tại; `src_why-youve-lost-your-curiosity-how-to-get-it-back.md` có thật và 4 ref trong `curiosity-hijacking.md` + `dopamine-baseline-reset.md` đã trỏ sang slug mới
- [x] **New-debt = 0**: 4 file mới (10/8/7/7 body ref) → 0 broken; 99 file `M` có ref thêm → 0 match với 269 đích đang gãy
- [x] **`.md` wikilink 82→0**: `grep -rEo '\[\[[^]]+\.md(\|[^]]*)?\]\]' wiki/concepts wiki/sources` = **0** (body + frontmatter). Đóng Issue 3 của báo cáo 10-02
- [x] `git log --diff-filter=A` rỗng **không** dùng để kết luận "pipeline idle" — `git status ??` cho thấy 4 file mới hôm nay
- [x] **⚠️ Regression mới đo được: 48/99 file `M` mất newline cuối file** (HEAD có `0a`, bản đĩa không). Đối chiếu từng file với `git show HEAD:<path>` — **48 lost, 4 pre-existing, 0 gained**. Toàn bộ nằm trong batch 10:11. `format-spec.md` **không** có quy tắc newline cuối file (`grep -ni 'newline|EOF|trailing'` chỉ trả về dòng 314 "No trailing spaces in values") ⇒ **không phải vi phạm format-spec**, `validate.py` không bắt, không tính vào 399 issue
- [x] Unquoted-`parent` trên 25 tag file: **0** — [SPEC CONFLICT] 08-29/08-30 vẫn đóng sau full rebuild thứ 8
- [x] Forward-ref group list không đổi (cùng 19 file); tổng ref 108→106
- [x] `wiki/topic/brain-threat-detection.md` vẫn không tồn tại (đã prune) — carry-forward 4 ngày, Hygiene E10 đang theo dõi
- [x] HEAD `e05f00ab` (09-24 20:51) == `git ls-remote refs/heads/master` (`e05f00abf29e…`) — backup cron dừng **9,1 ngày**, lần xác minh thứ 6. Ghi nhận thêm: remote `refs/heads/main` = `ead50c82` (khác `master`) — nhánh mặc định trên remote là `main`, không phải `master`
- [x] `## Notes` **không** phải lỗi format: `format-spec.md:135` ghi rõ là *optional INFO*. 74/619 concept thiếu `## Notes` — trong đó 4 file mới hôm nay (`frontend-design-agent`, `code-visualization`, `design-process`, `product-vs-prototype`) chỉ thiếu mục này nhưng có đủ 4 section khác. Output Validator 10-03 đã báo dưới dạng WARNING — **ghi nhận là đúng ưu tiên Compile Agent, không phải vi phạm spec**

---

## Escalations

### ⚠️ [REGRESSION] Batch dọn `.md` wikilink 10:11 làm mất newline cuối file ở 48 concept/source

Không phải vi phạm `format-spec.md` (spec không có quy tắc này), nhưng là **hậu quả đo được của một batch sửa đúng mục đích** — nên nêu để không lặp lại:

- **48 file** trong 99 file `M` mất byte `\n` cuối cùng (`git show HEAD:<path> | tail -c 1` = `0a` → bản đĩa = byte khác).
- Toàn bộ thuộc batch sửa 10:11 (99 file, 360 dòng thêm / 203 dòng xoá) — batch dọn `.md` trong wikilink mà báo cáo 10-02 gọi là "tồn dư 78/82".
- Cơ chế: `metacognition.md` cho thấy `No newline at end of file` ngay sau khi bỏ quotes trong body — công cụ ghi file không bảo toàn newline cuối.
- **Baseline KB:** 101/837 file concept+source vốn đã thiếu newline (trong đó 4 file trong batch này thuộc nhóm đó) ⇒ 48 là **mới**, không phải kế thừa.
- **Không nên vá `validate.py` bằng cách thêm ERROR** — sẽ tạo 101 ERROR giả. Nếu muốn theo dõi, chỉ nên thêm **INFO** và chỉ cho file mới sửa.
- **Khuyến nghị cho Fix Agent:** giữ newline cuối file khi thực hiện thay thế wikilink hàng loạt.

### Việc đã đóng (không cần báo lại ở lượt sau)

1. **`.md` trong wikilink 82→0** — Issue 3 của báo cáo 10-02 đóng trọn vẹn, đo bằng chính `validate.wikilink_style_issues()`.
2. **5 ref vô đường giải quyết bị gỡ** (`multi-agent-systems` ×3, `agent-initiated-code-artifacts` ×2) — đúng khuyến nghị của báo cáo 10-02; `naval-ravikant` (3) và `walk-forward-analysis` (1) là 2 mục còn lại trong cùng nhóm, đã xác minh raw=0.
3. **Unquoted-`parent`** trên 25 tag file vẫn 0 sau full rebuild thứ 8 — [SPEC CONFLICT] 08-29/08-30 không tái phát.

**Standing note (không phải escalation):** forward-reference backlog **đi ngược 2 ngày liên tiếp** — 273 (plateau 11 lượt) → 271 (10-02) → **269**. Cả 2 lượt đều do gỡ ref vô đường giải quyết, **không** do Compile Agent compile nốt forward-ref. 269 đích trong đó phần lớn chỉ có đúng 1 ref; `[[game-theory]]` (10) + `[[confirmation-bias]]` (8) vẫn cao nhất và là ưu tiên của Compile Agent, **không phải** vi phạm format-spec.

**Việc còn treo (không thuộc format):** `vault backup` dừng **9,1 ngày**. Không phải lỗi format, nhưng nó làm mất khả năng đối chiếu lịch sử — hôm nay `git diff` phủ 9 ngày nên ranh giới 24h phải suy ra thay vì đo. Hygiene Inspector đang theo dõi; không re-escalate ở đây.
