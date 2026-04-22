---
type: concept
status: draft
tags: [#coding, #ai]
updated: 2026-04-22
---
# Spec-Driven Development (SDD)

## Mô tả
Phương pháp phát triển phần mềm tập trung vào việc xác định rõ ràng ý định (intent) thông qua specification trước khi triển khai code, đặc biệt hiệu quả khi làm việc với AI coding agents.

## Nội dung
SDD đối lập với "vibe coding" (lập trình dựa trên cảm tính/prompt mơ hồ). Trong SDD, **intent là source of truth**, không phải code.

**Quy trình chuẩn (ví dụ Spec Kit của GitHub):**
1. **Specify:** Tạo mô tả chi tiết về user journeys và outcomes (không bàn về tech stack).
2. **Plan:** Thiết kế kiến trúc, chọn tech stack và ràng buộc.
3. **Tasks:** Chia nhỏ plan thành các task độc lập, có thể test được.
4. **Implement:** Triển khai từng task và review tập trung.

**Các cấp độ áp dụng:**
- **Spec-first:** Viết spec kỹ trước khi code.
- **Spec-anchored:** Sử dụng spec làm mỏ neo để bảo trì và phát triển.
- **Spec-as-source:** Chỉ chỉnh sửa spec, AI tự động update code.

**Lợi ích:**
- Giảm thiểu tech debt.
- Hạn chế việc AI phải "đoán" yêu cầu, từ đó giảm lỗi và tăng độ tin cậy.
- Dễ dàng review các thay đổi nhỏ thay vì khối lượng code khổng lồ.

## Liên quan
- [[AI Coding Agents]]
- [[Vibe Coding]]

## Nguồn tham khảo
- [[wiki/sources/src_spec-driven-development-github.md]]
- [[wiki/sources/src_spec-driven-development-claude-code.md]]
