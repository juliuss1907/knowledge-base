---
type: concept
status: draft
tags: [#ai, #productivity]
---

# Xây dựng Knowledge Base cho LLM (LLM Knowledge Base Construction)

## Mô tả
Phương pháp xây dựng hệ thống tri thức bên ngoài (External Brain) bằng cách sử dụng LLM như một "thủ thư" (Librarian) để quản lý, kết nối và tổng hợp thông tin thay vì chỉ sử dụng như một công cụ trả lời câu hỏi đơn lẻ.

## Nội dung chính
- **Librarian Model vs Answer Machine Model**:
    - **Answer Machine**: Quy trình Hỏi $\rightarrow$ Đáp $\rightarrow$ Quên. Tri thức bị phân mảnh và không tích lũy.
    - **Librarian**: Quy trình Cung cấp dữ liệu $\rightarrow$ AI Compile thành Wiki $\rightarrow$ Truy vấn dựa trên Wiki. Tri thức được kết nối và phát triển theo thời gian.
- **Kiến trúc hai lớp (The Two-Folder System)**:
    - **Lớp Raw (Raw Layer)**: Chứa dữ liệu nguồn không chỉnh sửa (articles, PDF, notes). Đảm bảo tính toàn vẹn của nguồn tin.
    - **Lớp Wiki (Wiki Layer)**: Chứa các bài viết concept, tóm tắt và index do AI tạo ra từ lớp Raw. Đây là nơi tri thức được "tiêu hóa" và tổ chức.
- **Giá trị mang lại**: Biến AI từ một công cụ tra cứu thành một đối tác tư duy, nơi AI có thể nhận diện các mẫu (patterns) và liên kết giữa các mảng kiến thức khác nhau trong kho lưu trữ cá nhân.

## Liên quan
- [[AI-Workflow-Automation]]
- [[Chiết xuất kiến thức thành đồ thị (Knowledge Graph Distillation)]]

## Nguồn tham khảo
- [[src_build-llm-knowledge-base]]
