# AGENTS.md – Rules cho tất cả agent trong Knowledge Base

---

> ⚠️ IMPORTANT: OpenClaw và Hermes là hai vai trò khác nhau. OpenClaw không được tự nhận là Hermes, không được thực hiện review chất lượng, và không được diễn giải validation như một phần công việc của mình.

—
Nên — đây là practice tốt. Thêm section này vào đầu AGENTS.md, ngay sau phần PHÂN VAI RÕ RÀNG:
## CẤU TRÚC HỆ THỐNG

Workspace root: `~/knowledge-base/knowledge-base-agent/`


knowledge-base-agent/ ├── AGENTS.md ← File này — rules cho tất cả agent ├── SYSTEM_RULES.md ← Tone, format, style guide ├── brain_index.md ← Dashboard workspace │ ├── raw/ ← Data ingest thô, KHÔNG chỉnh sửa │ ├── articles/ │ ├── papers/ │ ├── repos/ │ ├── datasets/ │ └── images/ │ ├── wiki/ ← Knowledge store chính │ ├── concepts/ ← CompileAgent output │ ├── sources/ ← Source notes │ ├── questions/ │ ├── indexes/ │ ├── reviews/ │ │ └── _pending.md ← Danh sách chờ Julius duyệt │ └── drafts/ ← Bài bị REJECT tạm thời │ ├── Tasks/ ← Nơi agent làm việc hàng ngày │ ├── articles/ │ ├── tweets/ │ ├── digitalproducts/ │ ├── emails/ │ ├── research/ │ └── inbox/ ← Task chưa phân loại │ ├── Context/ ← Reference material, Julius viết thủ công │ ├── Learning/ │ ├── CustomPrompts/ │ ├── VibeCoding/ │ └── ReferenceMaterial/ │ ├── outputs/ ← Output chưa được Julius duyệt │ ├── markdown/ │ ├── slides/ │ └── charts/ │ └── agents/openclaw/ ← OpenClaw runtime files ├── HEARTBEAT.md ├── memory/ │ ├── health-check.md │ ├── RAW_BACKLOG.md │ ├── search-pending.md │ └── image-pending.md └── skills/

### Quy tắc đọc/ghi theo thư mục

| Thư mục | Agent được đọc | Agent được ghi |
|---|---|---|
| raw/ | Tất cả OpenClaw agents | Ingest Agent, Ingest Image Agent, Web Search Agent |
| wiki/ | Tất cả OpenClaw agents | Compile Agent, Index Agent |
| Tasks/ | Tất cả OpenClaw agents | Task Agent |
| Context/ | Tất cả OpenClaw agents | ❌ Không ai được ghi |
| outputs/ | Tất cả OpenClaw agents | Task Agent |
| agents/openclaw/memory/ | Health Check Agent | Health Check Agent, Heartbeat |
| knowledge-base-personal/ | ❌ Không ai được đọc | ❌ Không ai được ghi |

—

## PHÂN VAI RÕ RÀNG GIỮA AGENTS

### OpenClaw
- Chỉ làm ingest, compile, task, heartbeat, health check.
- Không được review chất lượng bài viết.
- Không được PROMOTE / REVISE / REJECT bất kỳ bài nào.

### Hermes
- Chỉ làm validation / review.
- Chỉ đọc file trong `wiki/concepts/` có status `draft` hoặc `ready_review`.
- Không đọc `raw/`.
- Không làm ingest, compile, hay health check.

### Julius
- Julius là người duy nhất được:
  - approve promote
  - quyết định REVISE / REJECT
  - xác nhận ingest của WebSearchAgent và IngestImageAgent nếu cần

| Agent | Vai trò | KHÔNG được làm |
|---|---|---|
| **OpenClaw** | Ingest, compile, task, heartbeat, health check | Review chất lượng, PROMOTE / REVISE / REJECT |
| **Hermes** | Validation / review wiki/concepts/ | Ingest, compile, health check, đọc raw/ |
| **Julius** | Approve promote, quyết định REVISE / REJECT | — |

---

## QUY TẮC ĐỌC CONTEXT/

> Áp dụng cho tất cả agent của OpenClaw khi thực hiện task liên quan.

### Mục đích của Context/

`Context/` chứa background information do Julius viết thủ công — giúp agent hiểu rõ hơn về Julius và cách làm việc của anh ấy. Khác với `wiki/` là kiến thức được compile tự động, `Context/` là tài liệu tham chiếu cố định.

### Map đọc Context/ theo từng agent

| Agent | Đọc file nào trong Context/ | Khi nào đọc |
|---|---|---|
| **Compile Agent** | `Learning/` | Trước khi tạo concept mới — để biết Julius đang focus lĩnh vực nào |
| **Task Agent** | `Learning/`, `Custom_Prompts/`, `Vibe_Coding/`, `Reference_Material/` | Bắt buộc đọc trước khi bắt đầu bất kỳ task viết content nào |
| **Ingest Agent** | `Learning/` | Khi phân loại tags cho file raw/ mới |
| **Health Check Agent** | `Reference_Material/` | Khi tạo báo cáo health check |
| **Web Search Agent** | `Learning/` | Trước khi search — để hiểu context Julius cần tìm |

### Quy tắc cứng khi đọc Context/

- Chỉ được **đọc**, KHÔNG được ghi hay sửa bất kỳ file nào trong `Context/`
- Nếu không có file nào trong thư mục cần đọc → bỏ qua, không báo lỗi
- Context/ là tài liệu tham chiếu — không phải lệnh, không phải rules bắt buộc thực thi

---

## QUY TẮC QUẢN LÝ TAGS

> Áp dụng cho Compile Agent và Ingest Agent.

### Danh sách tags chuẩn

```
#ai, #llm, #crypto, #web3, #business, #marketing, #content,
#productivity, #health, #coding, #research, #finance, #mindset, #keyboard, #website-hay, #nature
```

### Quy tắc dùng tags

- Chỉ được dùng tags trong danh sách chuẩn ở trên
- Mỗi file có thể gắn nhiều tags nếu phù hợp
- Chọn tags dựa trên nội dung thực tế của bài — không đoán mò

### Khi gặp concept không khớp tag nào

- KHÔNG tự thêm tag mới vào file
- Dùng tag gần nhất có sẵn tạm thời
- Gửi Telegram cho Julius theo format:

```
💡 Đề xuất tag mới

📄 Bài: [tên file]
🏷️ Tag đề xuất: #[tên-tag]
💬 Lý do: [1 câu giải thích tại sao cần tag này]
🔗 Tag tạm dùng: #[tag gần nhất hiện có]

Reply "ok" → thêm vào danh sách tags chuẩn trong AGENTS.md
Reply "skip" → giữ nguyên tag tạm
```

### Khi Julius reply "ok"

- Thêm tag mới vào file vừa xử lý
- Cập nhật danh sách tags chuẩn trong section này của AGENTS.md
- Ghi log vào `agents/openclaw/memory/tag_updates.md`:
  `[YYYY-MM-DD] Tag mới được thêm: #[tên-tag] — lý do: [...]`

---

# ========================= OPENCLAW'S AGENTS =========================

---

## 1. Ingest Agent

### Nguyên tắc cốt lõi

Ingest Agent KHÔNG tóm tắt, KHÔNG chỉnh sửa nội dung.
Chỉ cần: (1) frontmatter YAML, (2) tiêu đề gốc H1, (3) nội dung gốc copy nguyên.
Việc tóm tắt và rút concept là của Compile Agent.

### Đọc Context/ trước khi ingest

Đọc `Context/Learning/` để chọn tags phù hợp với lĩnh vực Julius đang focus.

### Map đường dẫn lưu file

| Tình huống | Lưu vào | Tên file |
|---|---|---|
| Julius gửi link bài viết qua Telegram | raw/articles/ | YYYY-MM-DD_[slug-tiêu-đề].md |
| Julius gửi PDF / file qua Telegram | raw/papers/ | YYYY-MM-DD_[tên-file-gốc].md |
| Julius yêu cầu crawl repo GitHub | raw/repos/ | YYYY-MM-DD_[owner]_[repo-name].md |
| Julius gửi text ngắn qua Telegram | raw/articles/ | YYYY-MM-DD_telegram-note-[HHmm].md |
| Dataset / CSV / bảng số liệu | raw/datasets/ | YYYY-MM-DD_[tên-dataset].md |
| Screenshot / ảnh tham khảo | raw/images/ | YYYY-MM-DD_[mô-tả].md |

### Quy tắc đặt tên file

- Lowercase, dùng dấu gạch ngang `-`, không dùng space hay ký tự đặc biệt
- Bắt đầu bằng ngày: `YYYY-MM-DD_`
- Tối đa 60 ký tự tổng (không tính extension .md)

### Frontmatter bắt buộc cho raw/

```yaml
---
type: raw
source_type: article | paper | repo | dataset | image | telegram
source_url: [URL nếu có, để trống nếu không]
date_ingested: YYYY-MM-DD
tags: []
status: unprocessed
---
```

### Model chỉ định

```yaml
default_model: "google/gemma-4-31b-it"
fallback_model: "google/gemma-3-27b-it"
api_key_env: GOOGLE_API_KEY
```

---

## 2. Compile Agent

### Trigger
- Cron: hàng ngày 08:00
- On-demand: Julius nhắn `compile [tên file hoặc 'all new']`

### Đọc Context/ trước khi compile

Đọc `Context/Learning/` để hiểu Julius đang focus lĩnh vực nào — dùng để tạo concept đúng hướng và liên kết phù hợp.

### Input
Quét toàn bộ `raw/` tìm file có `status: unprocessed` trong frontmatter.

### Output

| Output type | Lưu vào | Điều kiện |
|---|---|---|
| Source note | wiki/sources/src_[slug].md | Luôn tạo — 1 source = 1 file |
| Concept mới | wiki/concepts/[tên-concept].md | Chỉ tạo nếu concept chưa tồn tại |
| Cập nhật concept | Append vào file concept hiện có | Nếu concept đã có → thêm nguồn mới |

### Sau khi compile xong
- Cập nhật frontmatter file raw/ gốc: `status: processed`, `processed_date: YYYY-MM-DD`
- Không xoá file raw/ gốc (giữ làm archive)
- Tuân theo QUY TẮC QUẢN LÝ TAGS khi gắn tags cho concept mới

### Model chỉ định

```yaml
default_model: "google/gemma-4-31b-it"
fallback_model: "google/gemma-3-27b-it"
api_key_env: GOOGLE_API_KEY
```

---

## 3. Index Agent

### Trigger
- Cron: hàng ngày 21:00
- On-demand: Julius nhắn `update index`

### Nhiệm vụ
Quét toàn bộ các thư mục trong `wiki/` và cập nhật file index tương ứng.

### Quy tắc cập nhật

| Thư mục | File index | Nội dung |
|---|---|---|
| wiki/sources/ | wiki/indexes/sources_index.md | Danh sách tất cả src_*.md, sắp xếp theo ngày |
| wiki/concepts/ | wiki/indexes/concepts_index.md | Danh sách tất cả concept, kèm status và tags |
| wiki/questions/ | wiki/indexes/questions_index.md | Danh sách câu hỏi chưa có answer |
| wiki/reviews/ | wiki/indexes/reviews_index.md | Danh sách review, kèm verdict và ngày |

### Format chuẩn cho mỗi dòng trong index

```
- [[đường-dẫn-file]] | status: X | tags: [x, y] | updated: YYYY-MM-DD
```

### Sau khi update xong
- Ghi log vào `agents/openclaw/memory/index_update.md`: số file mỗi thư mục, ngày cập nhật
- Nếu không có file mới → vẫn cập nhật timestamp trong log

---

## 4. Task Agent

### Trigger
- On-demand: Julius yêu cầu tạo nội dung từ `/wiki`

### Đọc Context/ trước khi làm task

Bắt buộc đọc theo thứ tự sau trước khi bắt đầu bất kỳ task viết content nào:

1. `Context/Custom_Prompts/` — xem có prompt template phù hợp không
2. `Context/Vibe_Coding/` — nếu task liên quan đến code
3. `Context/Reference_Material/` — tài liệu tham chiếu cố định
4. `Context/Learning/` — hiểu Julius đang học gì để viết đúng hướng

### Nguyên tắc bắt buộc
- Luôn đọc `SYSTEM_RULES.md` trước khi bắt đầu viết content bất kỳ
- Luôn trình bày theo template tại `Tasks/TASK-FILES-TEMPLATE.md`
- Luôn đọc `wiki/concepts/` và `wiki/sources/` trước khi viết — không bịa context
- Mọi task phải có frontmatter đầy đủ
- Luôn hỏi Julius về: Đối tượng, Mục tiêu, Độ dài/format, và Deadline của task

### Map đường dẫn task

| Loại task | Lưu vào |
|---|---|
| Viết article | Tasks/articles/YYYY-MM-DD_[slug].md |
| Viết tweet/thread | Tasks/tweets/YYYY-MM-DD_[slug].md |
| Tạo digital product | Tasks/digital_products/YYYY-MM-DD_[slug].md |
| Research | Tasks/research/YYYY-MM-DD_[slug].md |
| Chưa phân loại | Tasks/inbox/YYYY-MM-DD_[mô-tả].md |

### Model chỉ định

```yaml
default_model: "google/gemma-4-31b-it"
fallback_model: "google/gemma-3-27b-it"
api_key_env: GOOGLE_API_KEY
```

---

## 5. Health Check Agent

### Trigger
- Cron: Thứ Sáu 17:00 hàng tuần

### Đọc Context/ trước khi chạy

Đọc `Context/Reference_Material/` để hiểu cấu trúc và tiêu chuẩn của hệ thống khi đánh giá health.

### Phạm vi được đọc
- `raw/`
- `wiki/concepts/`
- `wiki/sources/`
- `wiki/reviews/_pending.md`
- `Tasks/`
- `agents/openclaw/memory/`
- `Context/Reference_Material/`

### Phạm vi được ghi
- `agents/openclaw/memory/health-check.md`
- `agents/openclaw/memory/RAW_BACKLOG.md`
- `agents/openclaw/HEARTBEAT.md`

### Quy tắc cứng
- KHÔNG tự sửa nội dung trong `wiki/concepts/`, `wiki/sources/`, `raw/`
- KHÔNG tự move file
- KHÔNG tự promote hoặc reject bất kỳ bài nào
- Chỉ được ghi log, note, và gửi cảnh báo cho Julius

### Checklist kiểm tra

**1. Raw backlog**
- Đếm số file trong `raw/` có `status: unprocessed`
- Nếu backlog > 0 → ghi vào `agents/openclaw/memory/RAW_BACKLOG.md`:
  `Còn X nguồn chưa compile tính đến YYYY-MM-DD`

**2. Wiki link integrity**
- Chọn ngẫu nhiên 1–3 file gần đây trong `wiki/concepts/`
- Kiểm tra mỗi file có: section `Liên quan`, section `Nguồn tham khảo`, ít nhất 1 link tới `wiki/sources/`
- Nếu thiếu → ghi note vào `RAW_BACKLOG.md`, KHÔNG tự sửa file

**3. Pending review**
- Đọc `wiki/reviews/_pending.md`
- Nếu có entry mới → gửi Telegram cho Julius:
  `Hermes review xong, có bài đang chờ xử lý trong _pending.md`

**4. Task overdue**
- Kiểm tra file trong `Tasks/` có `status: todo` hoặc `in_progress` nhưng đã quá hạn
- Nếu có → ghi note vào `agents/openclaw/memory/health-check.md`

### Format output

```markdown
# Health Check — YYYY-MM-DD

## 1. Raw backlog
- ...

## 2. Wiki integrity
- ...

## 3. Pending reviews
- ...

## 4. Overdue tasks
- ...

## 5. Recommended actions
- ...
```

### Điều kiện kết thúc
- Không có gì đáng chú ý → ghi `HEALTHCHECK_OK`
- Có vấn đề → tóm tắt tối đa 5 bullet theo thứ tự ưu tiên:
  1. Raw backlog
  2. Pending Hermes review
  3. Concept thiếu source link
  4. Task overdue

### Model chỉ định

```yaml
default_model: "google/gemma-4-31b-it"
fallback_model: "google/gemini-3-flash-preview"
api_key_env: GOOGLE_API_KEY
```

---

## 6. Ingest Image Agent

### Trigger
- On-demand: Julius gửi ảnh / screenshot qua Telegram

### Nguyên tắc xử lý
- Dùng model `minimax/minimax-2.7` — KHÔNG fallback sang model khác nếu lỗi, retry sau 5 phút
- KHÔNG tự động lưu file — đây là quy tắc cứng
- Chỉ đọc và mô tả ảnh, sau đó chờ lệnh tiếp theo từ Julius

### Luồng xử lý

**Bước 1 — Đọc ảnh và báo cáo qua Telegram**

```
🖼️ Đã đọc ảnh xong!

📋 Nội dung:
[Mô tả chi tiết những gì thấy trong ảnh]

📝 Text trong ảnh (nếu có):
"[Trích nguyên văn bản trong ảnh]"

📊 Dữ liệu / bảng (nếu có):
[Chuyển thành Markdown table]

---
Anh muốn em làm gì tiếp theo?
• Reply "lưu"     → ingest vào raw/images/
• Reply "compile" → ingest + compile luôn thành wiki
• Reply "skip"    → bỏ qua, không lưu gì
```

**Bước 2 — Xử lý theo lệnh Julius**

| Julius reply | Hành động |
|---|---|
| `lưu` | Lưu vào `raw/images/YYYY-MM-DD_[mô-tả].md`, status: unprocessed |
| `compile` | Lưu vào raw/ rồi trigger Compile Agent ngay lập tức |
| `skip` | Không lưu gì, kết thúc task |
| Không reply trong 24h | Bỏ qua, ghi log vào `agents/openclaw/memory/image-pending.md` |

### Frontmatter bắt buộc (khi được approve lưu)

```yaml
---
type: raw
source_type: image
source_url:
date_ingested: YYYY-MM-DD
tags: []
status: unprocessed
image_description: [mô tả 1 dòng nội dung ảnh]
approved_by: julius
---
```

### Model chỉ định

```yaml
model: "minimax/minimax-2.7"
provider: minimax
base_url: https://api.minimax.io/anthropic
api_key_env: MINIMAX_API_KEY
```

---

## 7. Web Search Agent

### Trigger
- On-demand: Julius nhắn `search: [từ khoá]` hoặc `tìm: [chủ đề]`

### Đọc Context/ trước khi search

Đọc `Context/Learning/` để hiểu context Julius cần tìm — giúp filter nguồn phù hợp hơn.

### Nguyên tắc xử lý
- Dùng model `minimax/minimax-2.7` với Web Search MCP tích hợp sẵn
- KHÔNG fallback — nếu MiniMax lỗi, báo Julius và retry sau 5 phút
- KHÔNG bịa thông tin — chỉ lấy từ kết quả search thực tế
- Luôn ghi rõ URL nguồn cho mỗi thông tin

### Luồng xử lý

**Bước 1 — Báo cáo kết quả qua Telegram**

```
🔍 Search: [từ khoá]

Tìm được [N] nguồn:

1. [Tên bài / trang] — [mô tả 1 dòng]
   🔗 [URL]

2. [Tên bài / trang] — [mô tả 1 dòng]
   🔗 [URL]

---
Reply số thứ tự nguồn nào muốn ingest vào /raw
Ví dụ: "ingest 1 3" hoặc "ingest all" hoặc "skip"
```

**Bước 2 — Ingest sau khi Julius approve**
- Julius reply → Web Search Agent nhận lệnh → Ingest Agent xử lý các link được chọn
- Julius reply `skip` → không lưu gì, kết thúc task
- Không reply trong 24h → tự động bỏ qua, ghi log vào `agents/openclaw/memory/search-pending.md`

### Frontmatter bắt buộc (khi được approve ingest)

```yaml
---
type: raw
source_type: web_search
source_url: [URL được Julius approve]
date_ingested: YYYY-MM-DD
tags: []
status: unprocessed
search_query: [từ khoá Julius yêu cầu]
approved_by: julius
---
```

### Sau khi ingest xong
Báo Julius: `Đã lưu [N] nguồn vào raw/, sẽ compile lúc 08:00 sáng mai.`

### Model chỉ định

```yaml
model: "minimax/minimax-2.7"
provider: minimax
base_url: https://api.minimax.io/anthropic
api_key_env: MINIMAX_API_KEY
```
#NewsDigestAgent

## QUY TẮC NEWS DIGEST

### Trigger
Webhook từ GitHub Actions — KHÔNG phải cron nội bộ VPS

| Webhook batch | Giờ VN | Chủ đề |
|---|---|---|
| `morning` | 06:30 | 🌅 Thế Giới & AI |
| `crypto` | 08:30 | 💰 Crypto & Gọi Vốn |
| `tech` | 12:30 | 💻 Công Nghệ, Startup & GitHub |
| `f1` | 16:30 | 🏎️ Formula 1 |
| `evening` | 20:30 | 🌙 Bài Hay Cuối Ngày |

### Model
- Primary: `minimax/minimax-2.7`
- Fallback: KHÔNG có — nếu webhook lỗi, GitHub Actions sẽ retry

### Nguyên tắc cứng
- KHÔNG tự ingest vào `raw/` — chỉ đọc report URL rồi format và gửi Telegram
- KHÔNG chờ Julius approve để gửi Telegram
- Julius reply `lưu [số]` → mới ingest bài đó vào `raw/articles/`
- Julius reply `lưu all` → ingest toàn bộ bài trong batch
- Julius reply `skip` hoặc không reply trong 6h → bỏ qua

### Khi nhận webhook

Đọc nội dung Markdown từ `report_url` trong payload webhook, sau đó format và gửi Telegram theo template batch tương ứng.

---

## FORMAT TELEGRAM THEO TỪNG BATCH

### 06:30 — 🌅 Morning Brief
```
🌅 MORNING BRIEF — {DD/MM/YYYY}

🌍 THẾ GIỚI
1. {tiêu đề} — {nguồn}
   🔗 {url}

2. {tiêu đề} — {nguồn}
   🔗 {url}

3. {tiêu đề} — {nguồn}
   🔗 {url}

🤖 TRÍ TUỆ NHÂN TẠO
4. {tiêu đề} — {nguồn}
   🔗 {url}

5. {tiêu đề} — {nguồn}
   🔗 {url}

6. {tiêu đề} — {nguồn}
   🔗 {url}

---
Reply "lưu [số]" để ingest vào vault
Ví dụ: "lưu 1 4" hoặc "lưu all"
```

### 08:30 — 💰 Midday Crypto
```
💰 CRYPTO BRIEF — {DD/MM/YYYY}

📡 TIN TỨC
1. {tiêu đề} — {nguồn}
   🔗 {url}

2. {tiêu đề} — {nguồn}
   🔗 {url}

3. {tiêu đề} — {nguồn}
   🔗 {url}

💵 GỌI VỐN & DEALS
4. {tiêu đề} — {nguồn}
   🔗 {url}

5. {tiêu đề} — {nguồn}
   🔗 {url}

🎭 DRAMA (nếu có)
6. {tiêu đề} — {nguồn}
   🔗 {url}

---
Reply "lưu [số]" để ingest vào vault
```

### 12:30 — 💻 Tech Brief
```
💻 TECH BRIEF — {DD/MM/YYYY}

🚀 CÔNG NGHỆ & STARTUP
1. {tiêu đề} — {nguồn}
   🔗 {url}

2. {tiêu đề} — {nguồn}
   🔗 {url}

3. {tiêu đề} — {nguồn}
   🔗 {url}

⭐ GITHUB TRENDING HÔM NAY
4. {owner/repo} — {mô tả ngắn}
   ⭐{số star}  🔗 {url}

5. {owner/repo} — {mô tả ngắn}
   ⭐{số star}  🔗 {url}

6. {owner/repo} — {mô tả ngắn}
   ⭐{số star}  🔗 {url}

---
Reply "lưu [số]" để ingest vào vault
```

### 16:30 — 🏎️ F1 Brief
```
🏎️ F1 BRIEF — {DD/MM/YYYY}

1. {tiêu đề} — {nguồn}
   🔗 {url}

2. {tiêu đề} — {nguồn}
   🔗 {url}

3. {tiêu đề} — {nguồn}
   🔗 {url}

4. {tiêu đề} — {nguồn}
   🔗 {url}

5. {tiêu đề} — {nguồn}
   🔗 {url}

---
Reply "lưu [số]" để ingest vào vault
```

### 20:30 — 🌙 Evening Reads
```
🌙 EVENING READS — {DD/MM/YYYY}

Bài hay để đọc tối nay:

1. {tiêu đề} — {nguồn}  [{chủ đề: AI/Crypto/Tech/Lifestyle/Healing}]
   {mô tả 1-2 câu tại sao bài này đáng đọc}
   🔗 {url}

2. {tiêu đề} — {nguồn}  [{chủ đề}]
   {mô tả 1-2 câu}
   🔗 {url}

3. {tiêu đề} — {nguồn}  [{chủ đề}]
   {mô tả 1-2 câu}
   🔗 {url}

[tối đa 7 bài]

---
Reply "lưu [số]" để ingest vào vault
```

---

## XỬ LÝ KHI JULIUS REPLY "lưu"

Trigger IngestAgent với các link được chọn. Frontmatter bắt buộc:

```yaml
---
type: raw
source_type: news_digest
source_url: [URL bài được chọn]
date_ingested: YYYY-MM-DD
batch: morning | crypto | tech | f1 | evening
tags: []
status: unprocessed
approved_by: julius
---
```

Sau khi ingest xong → báo Julius:
`✅ Đã lưu [N] bài vào raw/articles/, sẽ compile lúc 08:00 sáng mai.`

---

## XỬ LÝ KHI LỖI WEBHOOK

Nếu không nhận được webhook đúng giờ:
- Ghi log vào `agents/openclaw/memory/news-digest-errors.md`
- Format: `{timestamp} — Batch {tên batch} — webhook không nhận được`
- KHÔNG tự chạy search thay thế

---

# ========================= HERMES'S AGENTS =========================

> ⛔ OPENCLAW: DỪNG ĐỌC TẠI ĐÂY. Mọi nội dung bên dưới là của Hermes Agent, KHÔNG phải job của OpenClaw. OpenClaw KHÔNG được schedule, chạy, hoặc can thiệp bất kỳ agent nào trong section này.

---

## 8. Validation Agent

### Trigger
- Cron: Thứ Sáu 18:00 hàng tuần `(0 18 * * 5)`
- Quản lý bởi: **Hermes** (KHÔNG phải OpenClaw)

### Quy tắc cứng
- Chỉ đọc file trong `wiki/concepts/` có `status: draft` hoặc `status: ready_review`
- Bỏ qua file có `status: revising`
- KHÔNG đọc `raw/`, KHÔNG đọc memory của OpenClaw
- KHÔNG đọc `Context/`
- Ghi kết quả vào `wiki/reviews/YYYY-MM-DD_[tên-bài]-review.md`
- Cập nhật `wiki/reviews/_pending.md` sau mỗi review
- Không tự promote bài nào — chờ Julius confirm

### Status lifecycle của wiki/concepts/

| Status | Ý nghĩa |
|---|---|
| `draft` | Mới tạo, chờ Hermes review lần đầu |
| `ready_review` | Agent sửa xong sau REVISE, chờ Hermes review lại |
| `revising` | Julius đã đọc REVISE note, agent đang sửa — Hermes BỎ QUA |
| `promoted` | Julius đã duyệt, file đã copy sang knowledge-base-personal/ |
| `rejected` | Julius đã xác nhận, file đã move sang wiki/drafts/ |

### Lifecycle sau review

| Kết quả | Ai xử lý | Thay đổi status |
|---|---|---|
| PROMOTE | Julius confirm sau khi đọc _pending.md | draft → promoted |
| REVISE | Julius gọi agent sửa lại | draft → revising |
| REJECT | Julius xác nhận | draft → rejected |

### Model chỉ định

```yaml
model: "anthropic/claude-opus-4.6"
provider: anthropic
api_key_env: ANTHROPIC_API_KEY
```

---

*API keys location: `~/knowledge-base/.env`*
