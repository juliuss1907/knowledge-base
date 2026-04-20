# brain_index – Agent Workspace

> Đọc file này TRƯỚC KHI làm bất kỳ việc gì.  
> Đây là điểm vào duy nhất cho toàn bộ nowledge-base-agent/.

---

## 0. File hệ thống quan trọng

| File | Mục đích | Đọc khi nào |
|---|---|---|
| [[AGENTS.md]] | Rules đầy đủ cho từng agent (ingest, compile, task, validation) | Luôn luôn – trước mọi task |
| [[SYSTEM_RULES.md]] | Tone, format, cấu trúc bài viết | Trước khi viết bất kỳ content nào |
| [[agents/openclaw/HEARTBEAT.md]] | Checklist heartbeat 30 phút | Mỗi lần heartbeat |
| [[wiki/reviews/_pending.md]] | Danh sách bài Hermes đã review, chờ Julius xử lý | Sáng Thứ Hai |

---

## 1. Các loại nhiệm vụ và nơi đọc/ghi

| Nhiệm vụ | Đọc ở đâu | Ghi output vào đâu |
|---|---|---|
| Ingest bài mới | — | `raw/[loại]/YYYY-MM-DD_[slug].md` |
| Compile raw sang wiki | `raw/` (status: unprocessed) + `Readwise/` | `wiki/sources/` + `wiki/concepts/` |
| Viết bài / thread | `wiki/concepts/` + `SYSTEM_RULES.md` | `Tasks/articles/` hoặc `Tasks/tweets/` |
| Nghiên cứu | `wiki/concepts/` + Onyx RAG | `Tasks/research/` |
| Q&A nhanh | `wiki/questions/` hoặc Onyx | `wiki/questions/q_[chủ-đề].md` |
| Health check | `wiki/` toàn bộ | `agents/openclaw/memory/health-check.md` |
| Hermes review | `wiki/concepts/` (status: draft, ready_review) | `wiki/reviews/YYYY-MM-DD_[tên]-review.md` |

---

## 2. Quy tắc cứng

- **KHÔNG xoá file trong `raw/`** — chỉ đọc, không bao giờ xoá.
- **KHÔNG tự promote bài sang `knowledge-base-personal/`** — Julius phải approve thủ công.
- **KHÔNG viết vào `nowledge-base-personal/`** — vault đó là read-only với mọi agent.
- Mọi file tạo ra phải có **frontmatter YAML đầy đủ**.
- Khi không chắc lưu vào đâu → lưu vào `Tasks/inbox/` và ghi chú lý do.
- **IngestAgent KHÔNG tóm tắt** — copy nguyên nội dung, không chỉnh sửa.

---

## 3. API routing – Dùng model nào cho việc nào

> Đây là rule bắt buộc. Sai model = tốn tiền hoặc bị rate limit.

| Việc | Model / Provider | Ghi chú |
|---|---|---|
| Compile, TaskAgent, Q&A | **MiniMax** (Starter $10/tháng) | Model chính cho production |
| Hermes validation | **OpenRouter** – NousResearch/Hermes-3-Llama-3.1-70B | Free tier, chỉ dùng cho review |
| Heartbeat, job nhẹ | **OpenRouter** – free models | Không tốn MiniMax quota |
| **Z.ai** | ❌ **Julius dùng tay – agent KHÔNG được gọi** | Rate limit rất thấp, dành cho Julius chat trực tiếp |

---

## 4. Status lifecycle của wiki/concepts/

```
draft        → mới tạo bởi CompileAgent, chờ Hermes review lần đầu
ready_review → agent sửa xong sau lệnh REVISE, chờ Hermes review lại
revising     → Julius đã đọc REVISE note, agent đang sửa (Hermes BỎ QUA)
promoted     → Julius đã approve, file đã copy sang nowledge-base-personal/
rejected     → Julius đã xác nhận, file đã move sang wiki/drafts/
```

**Hermes chỉ đọc:** `draft` và `ready_review`  
**Hermes bỏ qua:** `revising`, `promoted`, `rejected`

---

## 5. Lịch định kỳ hệ thống

| Thời gian | Job | Agent |
|---|---|---|
| Hàng ngày 07:00 | Readwise sync | IngestAgent |
| Hàng ngày 08:00 | Compile `raw/` → `wiki/` | CompileAgent |
| Hàng ngày 21:00 | Index update (`_index.md`) | CompileAgent |
| Thứ Sáu 17:00 | Weekly health check | CompileAgent |
| Thứ Sáu 18:00 | Batch review wiki/concepts/ | Hermes |
| Hàng đêm 22:00 | Git auto-commit + push | Task Scheduler |
| Mỗi 30 phút | Heartbeat check | IngestAgent |

> Nếu một task có thể đợi đến lịch chạy tự động → không cần xử lý ngay trong heartbeat.

---

## 6. Scope của Onyx RAG

- Onyx **chỉ index** `nowledge-base-agent/wiki/` — không index `raw/`, `Tasks/`, `agents/`
- Gọi Onyx khi cần Q&A phức tạp hoặc tìm kiếm cross-concept
- Onyx sync mỗi 15–30 phút → file mới từ CompileAgent sẽ có trong index sau tối đa 30 phút
- Endpoint local: `http://localhost:3000` | Agent: `Julius Research Agent`

---

## 7. Khi không chắc phải làm gì

1. Đọc lại [[AGENTS.md]] — section tương ứng với loại task
2. Nếu vẫn không rõ → lưu output vào `Tasks/inbox/` + ghi chú lý do bị kẹt
3. **Không tự phát minh rule mới** — không làm gì còn hơn làm sai

