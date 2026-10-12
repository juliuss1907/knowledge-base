# Output Validation — 2026-10-04

**Status:** approved — Julius duyệt 2026-10-12
**Approved by:** Julius
**Issues found:** 7 (0 ERROR, 6 WARNING, 1 INFO)
**Created:** 2026-10-04 23:14:22
**Validator:** output-validator
**Files checked:** 848 (221 sources + 627 concepts)
**New files:** 14 (3 sources + 11 concepts), tất cả biên soạch 08:05–08:09

---

## Tóm tắt

Batch lớn nhất kể từ 09-30 (14 file từ **3 nguồn** — đa dạng hơn hẳn 10-03 chỉ dùng 1 nguồn). Nội dung ở mức **tốt nhất của các batch gần đây**: mọi con số định lượng đều đối chiếu được với raw, không có mâu thuẫn nội tại, không có claim nào thiếu nguồn. 6 WARNING đều là **defect biên soạn hoặc tầng index**, không phải lỗi hiểu biết. 0 ERROR.

**7 claim carry-forward từ 10-03 đã đo lại trên đĩa** (bài học 09-27): 3 đã đóng, 2 còn treo, 2 bị chặn bởi cùng một câu hỏi ngưỡng chưa được Julius chốt.

| Loại | Kết quả |
|---|---|
| Dropped-i variant 5 (4 sub-pattern) | **0** — chuỗi **14 lượt** (08-23 → 10-04) |
| 4 typo variant cũ (ngưởi, double-i, spacing merge, capital-I) | 0 |
| Defect A (frontmatter sources vs body `## Sources`) | **3/3 PASS** (5/5, 2/2, 3/3) |
| Source section-name drift (`## Key points`) | **3/3 đúng** — 0 vi phạm |
| `.md` trong wikilink | 0 (đóng từ 10-03) |
| Wikilink hỏng trong 14 file hôm nay | **0** — 45/45 target resolve bằng exact-filename |
| Raw `status: processed` thiếu `compiled_to` | **0** (221/221 có backlink) |
| CJK trong vùng nội dung | 3 file, đều hợp lệ — 0 injection |
| Độ chính xác định lượng | 12/12 con số khớp raw |

---

## Issue 1: [Defect B — lần 3] Nhân bản số liệu adoption vào concept hôm nay

**File:** `wiki/concepts/harness-engineering.md:36`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Bullet mới hôm nay chép nguyên văn một cặp số liệu đã tồn tại ở 2 concept khác, mà **không nguồn nào trong file này sinh ra nó**.
**Evidence:**
```
harness-engineering.md:36  ... Codex đạt 5 triệu weekly active users so với 2,4 triệu
                            của anti-gravity ...
model-vs-harness-adoption.md:21  **Codex có 5 triệu weekly active users so với 2,4 triệu
                            của anti-gravity** — Codex hơn gấp đôi dù model không mạnh hơn rõ rệt
agent-harness.md:25  Codex có 5 triệu weekly active users so với 2,4 triệu của anti-gravity,
                            dù model của Google mạnh và rẻ hơn
```
**Xác nhận là dòng MỚI hôm nay:** `git diff 3b891e34~1 3b891e34 -- wiki/concepts/harness-engineering.md` cho thấy `+ - **Adoption là phép đo cuối cùng:** ...` nằm trong block 5 bullet mới. Trước đó file có 8 bullet và **không** có "5 triệu".
**Vấn đề nhân bản kép:** (a) hai nguồn mới hôm nay (`src_how-to-make-infinite-ads-with-claude-code`, `src_motion-design-studio-with-opus-5-5`) **không nhắc tới Codex hay anti-gravity**; (b) 10-02 đã gọi đây là Defect B và nó **chưa được xử** ("cần chốt mức trùng lặp") — giờ tái hiện lần thứ 3 ở file khác.
**Suggested fix:** Gộp — `harness-engineering.md:36` giữ link trỏ `[[model-vs-harness-adoption]]` và bỏ cặp số, hoặc bỏ hẳn bullet vì bullet ngay trên (`:33`, `:34`) đã nêu đúng luận điểm "harness quyết định output". **Không tự sửa.**

---

## Issue 2: [Defect B — 2 ý trùng giữa 2 concept cùng nguồn]

**File:** `wiki/concepts/content-generation-workflow.md:29` và `:30` vs `wiki/concepts/ai-animation-ad-pipeline.md:21` và `:23`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Compile Agent thêm `src_how-to-create-ai-animation-ads-with-gemini` vào `content-generation-workflow.md` (file có sẵn từ 06-17) và bê nguyên 2 ý đã nằm trong concept mới `ai-animation-ad-pipeline.md` — cùng một nguồn, gần nguyên văn.
**Evidence:**
```
content-generation-workflow.md:29  8. **Prompt phải đúng đích đầu cuối:** prompt sinh ra từ
                                    LLM phải feed thẳng được vào model video; thêm bước dịch
                                    thủ công giữa các tool là phần chi phí lớn nhất bị bỏ phí
ai-animation-ad-pipeline.md:21  - **Prompt viết đúng đích:** prompt sinh từ LLM phải feed thẳng
                                    được vào model video, không cần bước dịch trung gian giữa
                                    các tool — nếu không, chi phí dịch thủ công nuốt hết lợi nhuận

content-generation-workflow.md:30  9. **Định khung bằng chi phí...:** ... "12 cent mỗi video,
                                    thay freelancer" ...
ai-animation-ad-pipeline.md:23  - **Chi phí được thiết kế bằng công thức credit:** 25.000
                                    credit/tháng ÷ 15 credit ≈ 1.666 video → ~12 cent/video
```
**Đánh giá:** `content-generation-workflow.md` là file cũ (6 ý gốc từ 2 nguồn khác), giờ có 3 nguồn. 2 ý mới được thêm vào đúng chỗ liên quan nhất (mở rộng sang video) — **hướng thêm đúng, nhưng không dedup**. Ý `:29` và `:30` bản đầy đủ hơn (có số 12 cent, có câu "giá trị nằm ở lợi nhuận biên") ⇒ nên giữ bản ở `content-generation-workflow.md`, biến 2 ý ở `ai-animation-ad-pipeline.md` thành pointer 1 dòng, hoặc ngược lại.
**Suggested fix:** Cần Julius chốt ngưỡng trùng lặp (câu hỏi **đang treo từ 10-02**, chưa có câu trả lời). Trước mắt: giữ bản chi tiết hơn, ở bản kia để pointer.

---

## Issue 3: [Typo biến thể MỚI] Mất dấu `ự` — "19.000 ký t"

**File:** `wiki/concepts/directors-brief.md:20`
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Cùng file dùng đúng "ký tự" ở vế trước của cùng một câu, rồi viết thiếu dấu ở vế sau. Lỗi nằm trong **file mới hôm nay**, không phải carry-over.
**Evidence:**
```
directors-brief.md:20  - **Bằng chứng về quy mô:** các brief được chia sẻ công khai dài 9.500 ký tự
                        (một nhân vật nói với máy 5 phút, agent chạy 12 giờ, ra video 142 giây)
                        và 19.000 ký t cho một tác phẩm khác — thang này hoàn toàn khác
                        một prompt một dòng
```
**Đối chiếu raw — ý định rõ ràng:** `raw/posts/2026-09-27_...:915` → `@pradeepXkapoor's "Pip" robot film used a 19,000-character brief`. Đúng là "ký tự".
**Đây là biến thể thứ 6 của cùng một họ lỗi:** variant 1–4 là *người* (sai dấu, nhân đôi, mất khoảng trắng, hoa/thường), variant 5 là mất `i`, giờ là **mất `ự`** ở "ký tự" → "ký t". Cùng cơ chế: Compile Agent bỏ ký tự cuối của từ tiếng Việt có dấu.
**Phạm vi thật:** `grep -rPl 'ký t[^ự]' wiki/concepts/ wiki/sources/` = **4 file**, nhưng 3 file kia là **false positive** — `ký tên` là từ hợp lệ (`ai-legal-personhood.md:23`, `saudi-pakistan-defense-agreement.md:16`, `src_aaron-wright-ai-agents-legal-body.md:28`), và cả 3 đều có trong `3b891e34` (carry-over, không phải lỗi). **Chỉ `directors-brief.md` là lỗi thật.**
**Suggested fix:** `sed -i 's/19\.000 ký t /19.000 ký tự /' wiki/concepts/directors-brief.md`. Đồng thời: vì quick-scan chưa có regex biến thể 6, đề xuất thêm `grep -rPl 'ký t[^ự]'` vào `scripts/quick-scan.sh` với whitelist `ký tên`.

---

## Issue 4: `raw/websites/websites.md` — Stats và Items liệt kê 2 file là "unprocessed" nhưng đã compile xong

**File:** `raw/websites/websites.md:20-24`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Sub-index tầng raw khẳng định 2 file còn backlog. Cả hai đã `status: processed`, có `compiled_to` trỏ đúng, và đã có source trong `wiki/sources/`.
**Evidence:**
```
raw/websites/websites.md:22  - [[2026-09-28_interconnects-ai]] — ... (unprocessed)
raw/websites/websites.md:23  - [[2025-08-04_atom-project-american-truly-open-models]] — ... (unprocessed)
raw/websites/websites.md:19  - By status: 5 processed, 2 unprocessed        <-- thực tế 7 processed, 0 unprocessed
```
**Đo lại trên đĩa:**
| File | `status:` | `compiled_to:` | Source trong wiki |
|---|---|---|---|
| `2026-09-28_interconnects-ai.md` | `processed` | `[[src_interconnects-ai]]` | `src_interconnects-ai.md` ✓ |
| `2025-08-04_atom-project-american-truly-open-models.md` | `processed` | `[[src_atom-project-american-truly-open-models]]` | `src_atom-project-american-truly-open-models.md` ✓ |
**Đây chính là lỗi "no compiled_to" ngược chiều:** scan chuẩn (`status: processed` mà thiếu `compiled_to`) trả **0** — tức lớp raw ĐÃ sạch. Nhưng **văn bản index chưa được regenerate** sau lần compile 09-30. Index ở đây không phải auto-generated (`auto_generated: false`), nên phải ai đó sửa tay.
**Suggested fix:** Sửa `websites.md` — 2 dòng `(unprocessed)` → `(processed)`, `By status: 5 processed, 2 unprocessed` → `7 processed, 0 unprocessed`. Lưu ý cho Index Agent: `raw/websites/websites.md` và `raw/websites/2026-07-25_tools.md` (Issue 5) đều là index tay, không tự cập nhật.

---

## Issue 5: Sub-index mồ côi `2026-07-25_tools.md` + `[[tools]]` không resolve

**File:** `raw/websites/2026-07-25_tools.md`, `raw/raw.md:23`
**Severity:** WARNING
**Dimension:** Completeness (link resolution)
**Issue:** Ba lỗi liên kết, cùng một gốc.
**Evidence:**
```
raw/websites/2026-07-25_tools.md:3-5   type: index / level: 2 / scope: tools
                                       parent: "[[raw]]"        ← khai báo là con của raw
raw/raw.md:23                           - [[tools]] — Công cụ, phần mềm, quy trình
grep -rn '2026-07-25_tools' raw/ wiki/   →  0 hit              ← không ai trỏ tới
[ -f raw/tools/tools.md ]              →  MISS
[ -f raw/websites/tools.md ]          →  MISS
[ -f wiki/concepts/tools.md ]          →  MISS
[ -f wiki/tag/tools.md ]               →  OK (khác namespace — tag, không phải sub-index)
```
**Ba điểm:**
1. **`raw/raw.md:23` treo `[[tools]]`** không có file đích — đây là dangling link ở tầng index gốc.
2. **`2026-07-25_tools.md` nằm sai thư mục.** Quy ước KB là `raw/<category>/<category>.md`; nó đặt trong `raw/websites/` trong khi `scope: tools`, và 2 item nó liệt kê đều nằm ở `raw/websites/`.
3. **Không ai trỏ tới nó** (0 hit) — mồ côi hoàn toàn, kể cả từ `websites.md`.
**Phân loại:** carry-over từ lâu. `git log` cho thấy commit đầu tiên thêm file là `70cb2887` (2026-08-06) — **đã đứng gần 2 tháng**.
**Suggested fix:** Đây là lỗi cấu trúc tầng raw, thuộc việc Ingest/Hygiene hơn là Output. Hai đường: (a) dựng `raw/tools/tools.md` đúng quy ước và dọn 2 file tools ra `raw/tools/`; (b) bỏ cả sub-index `tools` khỏi `raw/raw.md:23` và xoá file mồ côi. **Không tự sửa — ngoài write zone.**

---

## Issue 6: 2 wikilink gãy không có raw — carry-forward từ 10-03, chưa đóng

**File:** `wiki/concepts/frontend-design-agent.md:36`, `wiki/concepts/code-visualization.md:35`
**Severity:** WARNING
**Dimension:** Completeness (link resolution)
**Issue:** `[[ai-assisted-development]]` và `[[diagram-as-code]]` vẫn không resolve. Cả hai **không có** concept, **không có** source, **không có** raw ⇒ không có đường giải quyết tự nhiên.
**Evidence:**
```
frontend-design-agent.md:36   - [[ai-assisted-development]]   → NOCONCEPT NOSOURCE raw=0
code-visualization.md:35      - [[diagram-as-code]]            → NOCONCEPT NOSOURCE raw=0
```
**Kiểm exact-filename** (`[ -f "wiki/concepts/$t.md" ]` + `[ -f "wiki/sources/src_$t.md" ]` + `find raw/ -name`), **không dùng `find -iname`** — theo bài học 10-01, `find -iname` cho false positive làm link gãy trông như đã resolve.
**Phân loại:** carry-forward — đã có trong `HEAD` trước batch hôm nay; Compile Agent hôm nay không thêm link hỏng mới (14 file mới: 45 target, **0 broken**).
**Suggested fix:** Hai lựa chọn như mọi forward-ref: (a) compile concept khi có nguồn phù hợp, (b) Fix Agent bỏ link. Không auto-drop.

---

## Issue 7: Trộn tiếng Anh trong mệnh đề tiếng Việt

**File:** `harness-engineering.md`, `content-generation-workflow.md`, `src_how-to-create-ai-animation-ads-with-gemini.md`
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** Giữ thuật ngữ kỹ thuật tiếng Anh là đúng — vấn đề là các từ đó nằm trong mệnh đề tiếng Việt, đọc lủng củng.
**Evidence:**
```
harness-engineering.md:34   ... khác biệt thật nằm ở render engine, thư viện chuyển động,
                              beat grid, và vòng tự soi frame ...
content-generation-workflow.md:18  Hệ thống tạo content sử dụng AI với quy trình 4 bước:
                              generate ideas từ strategy ... (cả Definition viết 1 câu)
src_how-to-create-ai-animation-ads-with-gemini.md:29  ... thay thế hoàn toàn phí editor và
                              thời gian chờ turnaround nhiều ngày
```
**Đo bằng heuristic chuẩn (EN words ÷ VN diacritics), 14 file hôm nay:**

| File | Tỉ lệ | | File | Tỉ lệ |
|---|---|---|---|---|
| `harness-engineering.md` | **1.91** | | `directors-brief.md` | 1.22 |
| `src_...ai-animation-ads-with-gemini.md` | **1.67** | | `code2video-render-loop.md` | 1.26 |
| `content-generation-workflow.md` | **1.64** | | `ai-animation-ad-pipeline.md` | 1.25 |
| `src_motion-design-studio-with-opus-5-5.md` | 1.48 | | `critique-loop-self-scoring.md` | 0.99 |
| `src_...infinite-ads-with-claude-code.md` | 1.53 | | `llm-judge-loop.md` | 1.00 |

Ngưỡng cảnh báo của skill là 3.0 ⇒ **không file nào vượt ngưỡng**. `harness-engineering.md` cao nhất vì là file gộp 5 nguồn với 8 bullet tiếng Anh có sẵn; 5 bullet mới hôm nay đều viết tiếng Việt — hướng đi đúng.
**Suggested fix:** Cải thiện văn phong, không chặn tham chiếu. "render engine / beat grid" → "bộ render / lưới nhịp"; "turnaround" → "thời gian quay vòng".

---

## Kiểm chứng độ chính xác định lượng — 12/12 khớp raw

Không có claim định lượng nào trong 14 file hôm nay sai. Đã đối chiếu từng con số với raw:

| Claim trong wiki | Raw |
|---|---|
| 25.000 credit ÷ 15 ≈ 1.666 video → ~12 cent | `...gemini.md` — "1,666 full animation videos", "about 12 cents per video" ✓ |
| >30.000 creative / 2 tháng · 10–20 cent | `...infinite-ads...md` — "over 30,000 ad creatives … in the last 2 months", "10 to 20 cents per finished creative" ✓ |
| Opus 5.5 phát hành 22/09/2026 · Fable 5.1 rẻ hơn 40% | `...opus-5-5.md:39,49` ✓ |
| 900 lần gọi / 15 giây / 60fps | `...opus-5-5.md` — "calls it 900 times for 15 seconds at 60 fps" ✓ |
| 163 lần gọi · 62,7 triệu token (96% cache) · ~34 USD · ~6¾ giờ | `...opus-5-5.md:1117` ✓ |
| 9.500 ký tự · 19.000 ký tự · 142 giây · 5 phút dictation · 12 giờ | `...opus-5-5.md:49,913,915,941` ✓ |
| contact sheet `fps=2,scale=270:-1,tile=6x5` | `...opus-5-5.md` — câu lệnh ffmpeg giống hệt ✓ |
| Preset spring: snappy / default / heavy / playful | `...opus-5-5.md` §08 — "Snappy UI… Default… Heavy… Playful" ✓ |
| Banned look: bouncy easing, glow, gradient UI chrome, particle burst | `...opus-5-5.md:436,484` ✓ |
| "brief contagion" | `...opus-5-5.md` ✓ |
| Dead beat · stutter ở loop seam | `...opus-5-5.md:1095` ✓ |
| `original:` cả 3 source trỏ đúng file raw | cả 3 `find raw/ -name` khớp ✓ |

---

## Carry-over từ 10-03 — đo lại toàn bộ

| Issue 10-03 | Trạng thái 23:14 hôm nay | Bằng chứng |
|---|---|---|
| **1. ERROR** — `long-context-models.md` tự mâu thuẫn 200K vs 1M | 🟢 **ĐÃ ĐÓNG** | `:18` → "Claude Opus 4.7+ (các bản Opus trước đó chỉ 200K max)"; `:49` → "N/A (200K tại thời điểm benchmark)"; `:55` thêm ghi chú mốc thời gian. Ba dòng đã thống nhất. |
| **2. WARNING** — 2 wikilink gãy raw=0 | ⏳ **CÒN** | → Issue 6 |
| **3. WARNING** — 4/10 concept thiếu `## Notes` | 🟢 **ĐÃ ĐÓNG** | `frontend-design-agent`, `code-visualization`, `design-process`, `product-vs-prototype` — cả 4 giờ đều có `## Notes` |
| **4. WARNING** — cùng một ý "nhiều hướng + nhãn trade-off" ở 3 file | ⏳ **CÒN, chờ ngưỡng** | `product-vs-prototype.md:30`, `multi-file-artifact-workflow.md:22`, `design-process.md:27` — nguyên trạng. 10-03 đã kết luận "redundancy có chủ đích"; vẫn treo câu hỏi ngưỡng từ 10-02. |
| **5. INFO** — trộn tiếng Anh | ⏳ **CÒN** | → Issue 7 (tỉ lệ cao nhất batch nay là 1.91, dưới ngưỡng) |
| **[SYSTEMATIC] Defect B** | ⏳ **CÒN, tái hiện lần 3** | → Issue 1 + Issue 2 |

**Câu hỏi ngưỡng vẫn treo (lần thứ 3):** Compile Agent nên dedup ý giữa các concept lúc compile, hay để mỗi file gắn cùng một ý với góc nhìn riêng? Hiện tại 2 ý bị nhân bản ở `harness-engineering.md`, 3 ý ở `content-generation-workflow.md`, 3 file ở nhóm "trade-off". **Cần Julius chốt.**

---

## Ghi chú vận hành

- **Cả ba lớp đều chạy:** Compile 08:05–08:09 (3 source + 11 concept) · tầng index 21:04 (topic rebuild) · `date_ingested: 2026-10-04` = **0** (không có raw mới — 3 nguồn hôm nay đã nằm sẵn trong backlog từ trước).
- **Backup cron đã phục hồi.** HEAD `68f644e7` khớp `refs/heads/master` của remote. Chuỗi "dừng 9,11 ngày" trong báo cáo Hygiene 10-03 **kết thúc tại đây** — nhưng remote default branch vẫn là `main` (`ead50c82`), khác `master`, nên cần xác nhận máy chính push đúng nhánh.
- **Raw backlog = 0** (221/221 `status: processed`, 221/221 có `compiled_to`, 0 misspell `compile_to:`).
- **Write zone:** chỉ `wiki/reviews/`. Không file nào trong `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`, `wiki/tag/`, `wiki/topic/` hay `raw/` bị sửa — xác minh bằng `find -newermt` + `git status` sau khi viết report.