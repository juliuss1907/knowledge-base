# _pending.md – Hermes Review Queue

Danh sách bài wiki đã được Hermes review, chờ Julius xử lý.
Julius đọc file này vào sáng Thứ Hai hàng tuần.

---

## Hướng dẫn xử lý

| Action | Julius cần làm |
|---|---|
| **PROMOTE** | Copy file từ wiki/concepts/ sang knowledge-base-personal/Content_Archive/, xoá file gốc |
| **REVISE** | Nhắn agent sửa lại, cập nhật status → `revising` |
| **REJECT** | Move file sang wiki/drafts/, cập nhật status → `rejected` |

---

## Prompt Recommendations cho Julius

### PROMOTE (11 bài)
Các bài sau đạt chất lượng tốt, có thể promote trực tiếp:

| # | Concept | Verdict | Lý do |
|---|---------|---------|-------|
| 1 | Brand-Degradation-IP-Licensing | PROMOTE | Nội dung có chiều sâu, ví dụ cụ thể, phân tích rõ ràng |
| 2 | MCP-Crypto-Trading | PROMOTE | Nội dung chi tiết, có classification MCPs, hướng ứng dụng cụ thể |
| 3 | Ocean-Warming-Marine-Predators | PROMOTE | Nội dung khoa học, có phân tích cơ chế và hệ quả |
| 4 | gut-transit-time | PROMOTE | Nội dung khoa học, có DOI, trích dẫn nghiên cứu cụ thể |
| 5 | heat-therapy-trungy | PROMOTE | Bảng huyệt đạo chi tiết, cảnh báo an toàn, chỉ dẫn rõ ràng |
| 6 | kelpdao-hack | PROMOTE | Phân tích cực kỳ chi tiết, timeline, so sánh hacking history |
| 7 | llm-flinch | PROMOTE | Insight quan trọng (flinch vs refusal), technical depth |
| 8 | mcp-vs-skills | PROMOTE | Comparison depth, có opinion và đề xuất practical |
| 9 | robotics-deployment-gap | PROMOTE | Phân tích rõ ràng, có timeline dự kiến |
| 10 | spec-driven-development | PROMOTE | Quy trình 4 bước cụ thể, phân cấp áp dụng, có chiều sâu |
| 11 | ternary-weight-llms | PROMOTE | Metrics cụ thể, so sánh kỹ thuật, viết tốt |

### REVISE (9 bài)
Các bài sau cần chỉnh sửa trước khi promote:

| # | Concept | Verdict | Vấn đề chính | Gợi ý sửa |
|---|---------|---------|--------------|-----------|
| 1 | AI-Content-Business-Minecraft | REVISE | Thiếu ví dụ case study thành công, thiếu phân tích rủi ro | Bổ sung case study, thêm section rủi ro |
| 2 | GitHub-Actions-CICD | REVISE | Nội dung quá generic, giống documentation | Thêm best practices, common pitfalls, ví dụ thực tế |
| 3 | WSL9x | REVISE | Nội dung quá nghèo (chỉ 3 bullet points) | Bổ sung context, trạng thái phát triển, link GitHub |
| 4 | agent-reach | REVISE | Cấu trúc không chuẩn, mix ngôn ngữ, thiếu Liên quan section | Chuẩn hoá cấu trúc, dịch sang tiếng Việt |
| 5 | camoufox | REVISE | Thiếu section Mô tả/Liên quan, toàn tiếng Anh | Thêm Mô tả ngắn, section Liên quan, chuẩn hoá format |
| 6 | firecrawl | REVISE | Tag #web3 sai, thiếu Liên quan, giống documentation | Đổi tag #web3 → #productivity, thêm insight riêng |
| 7 | keyboard-sound-museum | REVISE | Thiếu phân tích sâu, chỉ mô tả "là gì" | Thêm insight "tại sao đáng chú ý", section Liên quan |
| 8 | meilisearch | REVISE | Generic, thiếu so sánh alternatives, thiếu insight | Thêm comparison với Elasticsearch/Typesense/Algolia |
| 9 | openclaw-studio | REVISE | Chỉ nêu ưu điểm, thiếu limitation | Thêm insight khi nào CẦN Studio, thêm nhược điểm |

### REJECT (1 bài)

| # | Concept | Verdict | Lý do |
|---|---------|--------|-------|
| 1 | carcheck-vn | REJECT | Nội dung gần như trống — chỉ 1 câu mô tả, tự ghi "chưa được trích xuất đầy đủ". Cần Compile Agent xử lý lại source. |

---

## Chi tiết Review

Mỗi concept có file review riêng tại `wiki/reviews/2026-04-24_[tên-concept]-review.md`. Xem file review để biết chi tiết đầy đủ.

---

## Thống kê

- **Tổng concepts review:** 21
- **PROMOTE:** 11 (52%)
- **REVISE:** 9 (43%)
- **REJECT:** 1 (5%)
- **Ngày review:** 2026-04-24
- **Reviewer:** Hermes (Validation Agent)

---

## Vấn đề phát hiện chung

1. **Tags không chuẩn:** `#security` (kelpdao-hack) không có trong danh sách tags chuẩn. Gần nhất: `#research`. `#content` (AI-Content-Business-Minecraft) có trong danh sách nhưng cần xem xét lại. `#web3` (firecrawl) không phù hợp với nội dung.

2. **Cấu trúc không đồng nhất:** Nhiều concepts dùng cấu trúc khác với template chuẩn (thiếu `Mô tả`, dùng `Tóm tắt` thay thế, thiếu `Liên quan`, thiếu `Nguồn tham khảo` dạng wiki link). Cần Compile Agent chuẩn hoá.

3. **Mix ngôn ngữ:** Một số concepts viết toàn tiếng Anh (agent-reach, camoufox, firecrawl, meilisearch, openclaw-studio) trong khi đa số khác viết tiếng Việt. Nên thống nhất hoặc ghi rõ `language` trong frontmatter.

4. **Thiếu cross-references:** Hầu hết concepts thiếu section `Liên quan` hoặc tham chiếu đến concepts chưa tồn tại. Cần tạo thêm concepts để lấp đầy các tham chiếu chéo.