---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: agent-context-database
sources:
  - "[[src_openviking]]"
last_updated: 2026-08-31
---

# Context Database

## Definition

Context database là hệ thống lưu trữ chuyên dụng cho AI agents, quản lý memories, resources và skills dưới dạng cấu trúc có thể duyệt deterministic — khác với vector store truyền thống là black-box. OpenViking tiên phong với mô hình virtual filesystem (`viking://` protocol), nơi agent duyệt context bằng `ls`, `tree`, `find` thay vì query embedding. Mỗi entry được xử lý thành ba tầng nội dung (L0 abstract, L1 overview, L2 details) và chỉ load sâu theo mức task cần, giúp cắt giảm token spend đáng kể.

## Key ideas

- **Virtual filesystem model:** Memories, resources, skills mỗi loại có URI riêng; agent locate và manipulate context deterministic
- **Tiered loading (L0/L1/L2):** Mỗi entry xử lý thành 3 tầng ngay khi write, load on-demand theo độ sâu cần thiết
- **Directory recursive retrieval:** Vector search tìm directory thay vì file đơn lẻ, giữ context xung quanh khi drill-down
- **Observable retrieval:** Mỗi query để lại trajectory để debug — biết chính xác path nào tạo ra kết quả
- **Session-to-memory pipeline:** Sau session commit, async trích xuất user preferences và agent experience vào long-term memory
- **Kết quả vượt trội:** LoCoMo accuracy 80–83% (từ 24–57% native), token input giảm 34.3–91.0%, latency giảm 58.45–66.10%
- **Nền tảng VikingMem:** Paper arXiv:2605.29640 được VLDB 2026 chấp nhận
- **Khác với RAG truyền thống:** RAG chỉ retrieve chunks từ vector store, context database còn quản lý cấu trúc thư mục, phân tầng nội dung, và duy trì trajectory

## Related concepts

- [[agent-memory-taxonomy]]
- [[progressive-disclosure]]
- [[context-window-management]]
- [[retrieval-augmented-generation]]
- [[external-memory-providers]]

## Sources

- [[src_openviking]]
