# Output Validation — 2026-10-03

**Status:** approved — Julius duyệt hàng loạt 2026-10-03
**Issues found:** 5 (1 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-10-03 23:10:42
**Validator:** output-validator
**Files checked:** 837 (218 sources + 619 concepts)
**New files:** 4 genuinely new (1 source + 3 concepts) + 7 existing concepts updated today by Compile Agent

---

## Batch summary

Compile Agent xử lý **11 file** hôm nay, tất cả từ một nguồn duy nhất: `src_unreasonable-effectiveness-of-html` (Thariq Shihipar, Anthropic, 2026-05-20 — bài viết về việc chuyển Markdown sang HTML làm output format mặc định của Claude Code).

Phân biệt file mới vs file cũ bằng `git ls-files --error-unmatch` + `git diff`, **không dùng mtime** (bài học 08-27):

| File | Trạng thái | Nguồn |
|---|---|---|
| `wiki/sources/src_unreasonable-effectiveness-of-html.md` | **MỚI** (untracked) | raw/articles/2026-05-20_... |
| `wiki/concepts/html-as-agent-output-format.md` | **MỚI** (untracked) | 1 |
| `wiki/concepts/multi-file-artifact-workflow.md` | **MỚI** (untracked) | 1 |
| `wiki/concepts/throwaway-editing-interface.md` | **MỚI** (untracked) | 1 |
| `agentic-coding.md` | cũ, +2 key idea | 2→3 |
| `frontend-design-agent.md` | cũ, +3 key idea | 1→2 |
| `code-visualization.md` | cũ, +3 key idea | 1→2 |
| `long-context-models.md` | cũ, +4 key idea | 1→3 |
| `human-judgment-ai.md` | cũ, +2 key idea | 1→2 |
| `design-process.md` | cũ, +2 key idea | 1→2 |
| `product-vs-prototype.md` | cũ, +2 key idea | 2→3 |

**Chất lượng batch cao.** 11/11 file đọc tự nhiên, claim cụ thể có căn cứ trong raw (đã đối chiếu từng claim mới với `raw/articles/2026-05-20_unreasonable-effectiveness-of-html.md` — "Claude Design dựa trên HTML", "diff + margin annotation color-code theo severity", "slider/knob", "tradeoff label", "Fig E explainer với navigation/collapsible/tabbed" đều có trong raw). Đây là batch sạch nhất kể từ 10-02.

---

## Issue 1: Contradiction nội tại về context window của Claude Opus

**File:** `wiki/concepts/long-context-models.md`
**Severity:** ERROR
**Dimension:** Factual | Coherence
**Issue:** Cùng một file khẳng định hai điều trái ngược về Claude Opus. Dòng 18 và dòng 49 nói Opus max **200K token**; dòng 30 (thêm hôm nay) nói Opus 4.7 có context window **1 triệu token**. Hai con số không thể cùng đúng.
**Evidence:**
```
:18  ... DeepSeek V4 đạt 1M tokens, vượt xa Claude Opus (200K max) ...
:30  - **Context rộng làm output format tốn token trở nên vô nghĩa:** Thariq Shihipar (Anthropic)
     dùng Opus 4.7 với context window 1 triệu token ...
:49  | Claude Opus | ~87 | N/A (200K max) |
```
**Phân loại:** `:18` và `:49` là **carry-over** (có trong `HEAD`, đến từ `src_deepseek-v4-architecture`). `:30` là **dòng mới hôm nay** từ `src_unreasonable-effectiveness-of-html` — bài viết gốc viết "the 1MM context window in Opus 4.7". Compile Agent đã paste con số của một model vào concept mà không đối chiếu với claim đã có trong file.
**Suggested fix:** Không tự quyết con số nào đúng. Hai khả năng: (a) Opus 4.7 thực sự có 1M context ⇒ cập nhật `:18` và `:49`; (b) con số 200K là đúng cho benchmark dùng ở đây ⇒ giới hạn claim ở `:30` thành "context window lớn" bỏ con số, hoặc ghi rõ đây là claim của một nguồn chưa kiểm chứng. Cần xác minh ngoài KB trước khi sửa — **tôi không tự sửa file**. Dạng lỗi này (paste claim định lượng từ nguồn mới vào concept đã có claim mâu thuẫn) là **biến thể mới**, khác Defect B (nhân bản số liệu giữa nhiều file) ở chỗ nó xảy ra *trong cùng một file*.

---

## Issue 2: 2 wikilink gãy không có raw — carry-forward từ file cũ

**File:** `wiki/concepts/frontend-design-agent.md:36`, `wiki/concepts/code-visualization.md:35`
**Severity:** WARNING
**Dimension:** Completeness (link resolution)
**Issue:** `[[ai-assisted-development]]` và `[[diagram-as-code]]` không resolve. Cả hai **không có** concept, **không có** source, **không có** raw ⇒ không có đường giải quyết tự nhiên.
**Evidence:**
```
frontend-design-agent.md:36   - [[ai-assisted-development]]
code-visualization.md:35      - [[diagram-as-code]]
```
**Phân loại:** carry-forward — `git show HEAD` xác nhận cả hai đã có trong `HEAD` ở dòng 32 và 31. Hôm nay Compile Agent chỉ thêm dòng, không thêm link hỏng mới.
**Đã kiểm tra bằng exact-filename test** (`[ -f "wiki/concepts/$t.md" ]` + `[ -f "wiki/sources/src_$t.md" ]` + `find raw/ -name`), **không dùng `find -iname`** — theo bài học 10-01, `find -iname` cho false positive làm link gãy trông như đã resolve. `ls wiki/concepts/ | grep -E 'assisted-development|diagram'` chỉ trả về `causal-loop-diagram.md` (không phải target).
**Suggested fix:** Hai lựa chọn như các forward-ref khác: (a) compile concept khi có nguồn phù hợp, (b) Fix Agent bỏ link. Không auto-drop.

---

## Issue 3: 4/10 concept thiếu `## Notes` — lệch so với concept cùng batch

**File:** `frontend-design-agent.md`, `code-visualization.md`, `design-process.md`, `product-vs-prototype.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 4 concept mới/cập nhật hôm nay không có `## Notes`; 6 concept còn lại trong cùng batch có. Bất nhất trong một batch đơn lẻ cho thấy template không nhất quán.
**Evidence:**
```
có Notes:      agentic-coding, html-as-agent-output-format, multi-file-artifact-workflow,
               throwaway-editing-interface, long-context-models, human-judgment-ai
thiếu Notes:   frontend-design-agent, code-visualization, design-process, product-vs-prototype
```
**Lưu ý:** `## Notes` rỗng là **cố ý** theo template Compile Agent — không phải lỗi nội dung. Điểm cần sửa là **sự thiếu vắng mặt của section**, không phải nội dung rỗng bên trong.
**Suggested fix:** Thêm `## Notes` (rỗng) vào 4 file cho khớp 6 file kia. Format Validator nên bắt được; nếu nó không bắt thì kiểm tra `required_sections` trong `validate.py` — có thể nó coi concept không có `## Notes` là hợp lệ. Đây là điểm cần Format Validator xác nhận, không phải lỗi tôi tự kết luận.

---

## Issue 4: [SYSTEMATIC] Cùng một ý được diễn đạt lại ở 3 file khác nhau

**File:** `product-vs-prototype.md:30`, `multi-file-artifact-workflow.md:22`, `design-process.md:27`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Cùng một ý từ `src_unreasonable-effectiveness-of-html` — "dàn nhiều hướng khác biệt rõ cạnh nhau trong một trang, mỗi hướng gắn nhãn trade-off" — xuất hiện gần nguyên văn ở 3 concept khác nhau, chỉ khác văn phong.
**Evidence:**
```
product-vs-prototype.md:30     ... dàn nhiều phương án khác biệt rõ trong một trang,
                               gắn trade-off của từng phương án, rồi mới chọn ...
multi-file-artifact-workflow.md:22  ... nhiều hướng cạnh nhau trong một trang,
                               mỗi hướng gắn nhãn trade-off của nó ...
design-process.md:27           ... dàn nhiều hướng khác biệt rõ (layout, tone, density)
                               cạnh nhau trong một trang, mỗi hướng gắn nhãn trade-off ...
```
**Khác Defect B (10-02):** Defect B là nhân bản **số liệu định lượng** (5M/2,4M, 113 task, 22 tỷ token). Lần này là nhân bản **một mô tả thủ pháp**. Cùng root cause (Compile Agent không dedup giữa các concept), cùng khuếch đại (một source sinh ra nhiều concept).
**Đánh giá:** Ở mức chấp nhận được — mỗi file gắn ý với góc nhìn riêng (`product-vs-prototype` = giảm rủi ro chọn sai hướng, `multi-file-artifact-workflow` = lợi thế HTML ở giai đoạn exploration, `design-process` = song song hóa bước 2 của Christopher Alexander). **Đây là redundancy có chủ đích, không phải defect.** Cần Julius chốt ngưỡng — cùng câu hỏi còn treo từ 10-02.
**Suggested fix:** Không hành động cho tới khi ngưỡng được chốt. Nếu chốt "1 bullet là chủ", 2 file kia đổi thành pointer 1 dòng.

---

## Issue 5: Trộn tiếng Anh trong mệnh đề tiếng Việt

**File:** `src_unreasonable-effectiveness-of-html.md`, `frontend-design-agent.md`, `code-visualization.md`, `long-context-models.md`
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** Một số cụm tiếng Anh nằm trong mệnh đề tiếng Việt, đọc lủng củng. Giữ thuật ngữ kỹ thuật tiếng Anh là đúng — vấn đề là các từ thường nằm trong mệnh đề.
**Evidence:**
```
frontend-design-agent.md:17   ... có design vocabulary để critique, audit, polish ...
code-visualization.md:17      ... agent có layout judgment nên chọn hierarchy, routes
                              và emphasis phù hợp với intent ...
long-context-models.md:30     ... để sinh output HTML dày thông tin thay vì Markdown
                              tiết kiệm token ...
```
**Đo lại bằng heuristic chuẩn** (EN words ÷ VN diacritics): `frontend-design-agent.md` 1.5, `code-visualization.md` 1.5 — cao nhất batch. Ngưỡng cảnh báo của skill là 3.0 ⇒ **không file nào vượt ngưỡng**. 7 file còn lại ≤ 1.0.
**Suggested fix:** Cải thiện văn phong, không chặn tham chiếu. Cân nhắc: "design vocabulary" → "từ vựng thiết kế"; "layout judgment" → "phán đoán bố cục"; "output dày thông tin" → "output giàu thông tin".

---

## Kiểm tra đã PASS

| Hạng mục | Kết quả |
|---|---|
| **Dropped-i variant 5** (4 sub-pattern) | **0 match** — `ngườ`, `thờ`, `thay v `, `chính lờ`/`bằng lờ` đều 0. Chuỗi sạch **13 lượt** (08-23 → 10-03) |
| 4 typo variant cũ (ngưởi, double-i, spacing merge, capital-I) | 0 file, 0 instance |
| **CJK injection** | **0** trong 11 file hôm nay. KB-wide content scope = **3 file / 3 dòng**, cả 3 đều **hợp lệ**: `byte-level-bpe.md:26` (`Asian scripts (中): 3 bytes` — ví dụ giáo dục), `hundred-years-humiliation.md:16` (`百年国耻` — khái niệm lịch sử chủ đề), `chinese-culture-confucianism.md`. Không cần hành động |
| **Defect A** (fm `sources:` vs body `## Sources`) | **10/10 PASS** — 3/3, 2/2, 2/2, 1/1, 1/1, 1/1, 3/3, 2/2, 2/2, 3/3. 0 sai lệch |
| `.md` trong wikilink | **0** ở 11 file hôm nay; đo bằng chính `validate.wikilink_style_issues()` (body-only) |
| Quoted wikilink trong body | **0** — 22 dòng match đều là frontmatter, đúng house style (frontmatter quoted, body bare) |
| Cấu trúc source | `## Key points` đúng chuẩn (không phải `## Key ideas`) — Defect C không tái diễn |
| Summary source | 4 câu (tiêu chuẩn 3–5) |
| Key points source | 12 bullet (tiêu chuẩn 5–10 — hơi cao, không sao) |
| Definition 10 concept | 2–4 câu, tất cả trong khoảng chuẩn 2–3 (±1) |
| Truncated file | 0 |
| Empty section | 0 |
| `original:` của source mới | trỏ đúng `raw/articles/2026-05-20_unreasonable-effectiveness-of-html.md` |
| Raw `compiled_to` thiếu | **0** — cả file sai chính tả `compile_to:` cũng = 0 match |

---

## Carry-over từ báo cáo 10-02 — đã đóng, không báo lại

Đo lại từng claim trên đĩa (quy trình 09-27). **Toàn bộ đã được xử lý:**

| Claim 10-02 | Claimed | Verified hôm nay | Kết luận |
|---|---|---|---|
| CJK injection 9 file | 9 file | **0** (3 file hợp lệ) | ✅ đóng 10-02 10:52 |
| Raw `compiled_to` thiếu | 3 file | **0** | ✅ đóng |
| `.md` trong wikilink | 82 occurrence | **0** | ✅ đóng (đo bằng `wikilink_style_issues()`) |
| Quoted wikilink trong body | 25 file | **0** | ✅ đóng |
| `ai-lab-business-model.md:38` bullet rỗng | có | **không còn** — `:38` giờ là bullet nội dung đầy đủ | ✅ đóng |
| `agent-harness.md` 2 forward-ref raw=0 | có | **link đã bị bỏ** | ✅ đóng |
| `ai-lab-business-model.md` 3 bullet trùng | có | **đã gộp** — vùng đó giờ là `## Related concepts` | ✅ đóng |
| Backlog raw = 1 | 1 file | **drained** — `status: processed`, `compiled_to` trỏ đúng | ✅ đóng |

**Lưu ý về backlog raw:** 10-02 ghi backlog = 1. Hôm nay có **3 raw mới `status: unprocessed`** (`2026-07-02_how-to-create-ai-animation-ads-with-gemini`, `2026-09-27_motion-design-studio-with-opus-5-5`, `2026-09-25_how-to-make-infinite-ads-with-claude-code`) — cả 3 đều `date_ingested: 2026-10-03`, ingest **sau** giờ Compile 08:00. Hành vi bình thường, không cần hành động; lượt sau xác nhận đã drain.

---

## Đề xuất review compile-agent/SKILL.md — lý do đã đổi lần nữa

Lượt 10-02 đề nghị vì batch lộ 3 shape defect mới (bullet rỗng, body-quoted wikilink, nhân bản số liệu). **Cả 3 đã đóng.** Lượt hôm nay, batch sạch hơn hẳn — nhưng lộ **một dạng mới**: paste claim định lượng từ nguồn mới vào concept đã có claim mâu thuẫn mà không đối chiếu (Issue 1). Đề nghị thêm quy tắc: **trước khi thêm một con số/claim vào concept đã có, kiểm tra claim cũ có xung đột không.**

5 biến thể tokenization tiếng Việt vẫn 0 — vấn đề tokenization đã ổn định, đã đóng. Vấn đề còn lại là **tính nhất quán giữa các nguồn khi aggregate**, không phải lỗi ký tự.

---

## Actions needed

1. **Julius — chốt ngưỡng redundancy** (treo từ 10-02, giờ áp cho Issue 4). Sau đó mới sweep 2 file vệ tinh ở `product-vs-prototype.md:30` + `multi-file-artifact-workflow.md:22` + `design-process.md:27` → pointer 1 dòng.
2. **`long-context-models.md`** — xác minh ngoài KB: Opus 4.7 context window là 200K hay 1M. Sửa `:30` **hoặc** `:18`+`:49`, không để hai claim trái ngược cùng file.
3. **2 broken link** (`ai-assisted-development`, `diagram-as-code`) — compile khi có nguồn, hoặc Fix Agent bỏ.
4. **4 concept thiếu `## Notes`** — Format Validator xác nhận có bắt không; nếu không thì vá `validate.py` trước rồi thêm section vào file.
5. **Cải thiện văn phong** 4 file (Issue 5) — không chặn.
6. **Không hành động** CJK, `.md` wikilink, quoted wikilink — tất cả đã về 0.
7. **Đề nghị bổ sung quy tắc kiểm tra xung đột claim** vào `compile-agent/SKILL.md` (xem mục trên).