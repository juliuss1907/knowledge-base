---
type: concept
status: draft
tags: [#ai, #coding]
---
# Lỗi định tuyến tính phí trong Claude Code (Claude Code Billing Bug)

## Mô tả
Lỗi định tuyến tính phí là sự cố kỹ thuật xảy ra khi một hệ thống tự động phân loại yêu cầu (routing) dựa trên nội dung văn bản, dẫn đến việc áp dụng sai mô hình tính phí cho người dùng.

### Chi tiết sự cố (Trường hợp Claude Code)
- **Nguyên nhân:** Hệ thống định tuyến nhận diện chuỗi ký tự cụ thể ("HERMES.md") trong commit của người dùng và hiểu nhầm đây là một loại yêu cầu đặc biệt.
- **Hậu quả:** Người dùng đang sử dụng gói thuê bao (subscription) bị chuyển sang chế độ tính phí theo lượt dùng (pay-as-you-go), dẫn đến việc bị trừ tiền không chính xác.
- **Bài học:** Cảnh báo về việc sử dụng các "magic strings" hoặc chuỗi ký tự đặc biệt để điều phối logic hệ thống mà không có cơ chế xác thực chặt chẽ.

## Liên quan
- [[AI Agent Coordination]]
- [[Software Billing Systems]]

## Nguồn tham khảo
- [Lỗi HERMES.md trong Claude Code gây tính phí sai](https://github.com/anthropics/claude-code/issues/53262)
