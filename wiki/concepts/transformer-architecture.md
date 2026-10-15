---
type: concept
status: draft
main_tag: ai
sub_tags: [research, coding]
topic: attention-mechanism-foundation
sources:
  - "[[src_is-attention-the-essence-of-intelligence]]"
last_updated: 2026-10-15
---

# Transformer Architecture

## Definition

Transformer là kiến trúc mạng neural được nhóm nghiên cứu tại Google giới thiệu vào năm 2017 qua bài báo "Attention Is All You Need", loại bỏ hoàn toàn các lớp mạng tái hồi (RNN) và tích chập (CNN) để xây dựng hệ thống hoàn toàn dựa trên cơ chế self-attention. Kiến trúc này trở thành nền tảng cốt lõi cho hầu hết các mô hình ngôn ngữ lớn (LLM) và các mô hình tạo sinh đa phương thức hiện đại.

## Key ideas

- **Cấu trúc Encoder - Decoder:** Transformer chia thành hai khối chính: Encoder xử lý và làm giàu biểu diễn ngữ cảnh của chuỗi đầu vào thông qua các lớp self-attention xếp chồng; Decoder sử dụng cả self-attention và cross-attention để sinh chuỗi đầu ra từng phần tử một.
- **Tính toán song song:** Khác với RNN phải xử lý tuần tự từng từ một theo thời gian, Transformer cho phép tính toán toàn bộ các từ trong câu cùng một lúc, khai thác tối đa sức mạnh tính toán song song của phần cứng GPU/TPU.
- **Multi-Head Attention:** Việc sử dụng song song nhiều attention head giúp mô hình đồng thời nắm bắt nhiều loại mối quan hệ ngữ nghĩa và cú pháp khác nhau (như quan hệ chủ ngữ - vị ngữ, đại từ thay thế, hay liên kết cảm xúc).
- **Vấn đề chi phí bậc hai O(n²):** Cơ chế self-attention chuẩn đòi hỏi mỗi từ phải tính tích vô hướng với tất cả các từ khác trong ngữ cảnh, tạo ra chi phí tính toán và bộ nhớ tăng theo hàm bậc hai của độ dài chuỗi đầu vào.
- **Thách thức về hiệu suất năng lượng:** Dù đạt năng lực mô hình hóa ngôn ngữ vượt trội, Transformer tiêu tốn tài nguyên huấn luyện và năng lượng rất lớn so với khả năng học tập và tư duy hiệu quả của não bộ sinh học.

## Related concepts

- [[attention-mechanism]]
- [[language-modeling-ai-complete]]
- [[long-context-models]]

## Sources

- [[src_is-attention-the-essence-of-intelligence]]

## Notes
