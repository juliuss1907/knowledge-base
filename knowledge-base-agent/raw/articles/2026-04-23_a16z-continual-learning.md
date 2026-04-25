---
type: raw
source_type: article
source_url: https://www.a16z.news/p/why-we-need-continual-learning
date_ingested: 2026-04-23
tags: [#ai, #llm]
status: processed
processed_date: 2026-04-25
---
# Tại Sao Chúng Ta Cần Continual Learning — a16z

## Tóm tắt

Bài viết từ a16z về **continual learning** — lĩnh vực nghiên cứu cách để AI models học liên tục sau khi deploy, không chỉ dựa vào in-context learning.

## Mở đầu: So sánh với phim Memento

LLMs giống như nhân vật Leonard Shelby trong phim Memento — sống trong "hiện tại vĩnh cửu." Chúng có kiến thức khổng lồ nhưng không thể tạo ký ức mới. Để bù đắp, ta bao quanh chúng bằng các "đồ dùng hỗ trợ": lịch sử chat như sticky notes, hệ thống retrieval như sổ ghi chú, system prompts như hình xăm hướng dẫn.

## In-Context Learning đủ cho đến đâu?

ICL đủ với những vấn đề mà câu trả lời đã tồn tại ở đâu đó trên thế giới. Nhưng với những vấn đề đòi hỏi khám phá thực sự mới (như toán học mới), tình huống đối kháng (bảo mật), hoặc kiến thức quá ngầm không thể diễn đạt bằng ngôn ngữ — có lập luận mạnh rằng models cần cách cập nhật kiến thức **trực tiếp vào trong parameters** sau khi deploy.

## Trích dẫn Ilya Sutskever

> "Con người không phải AGI. Đúng, có một nền tảng nhất định về kỹ năng, nhưng con người thiếu rất nhiều kiến thức. Thay vào đó, chúng ta dựa vào continual learning. Nếu tôi tạo ra một đứa trẻ 15 tuổi siêu thông minh, chúng biết rất ít. Một học sinh giỏi, rất nhiệt tình. Quá trình deployment sẽ bao gồm một giai đoạn học hỏi, thử nghiệm và sai sót. Đó là một quá trình, không phải thả một thứ đã hoàn chỉnh ra."

## Nghịch lý

- LLMs là **thuật toán nén** — chúng nén internet vào trong parameters
- Nén có mất mát (lossy compression) là thứ làm chúng mạnh — buộc model tìm cấu trúc, khái quát hóa, xây dựng representations có thể chuyển giao
- **Nghịch lý:** chính cơ chế làm LLM mạnh trong training, ta lại không cho phép chúng làm sau deployment

## Ví dụ: Định lý cuối cùng của Fermat

350 năm không ai chứng minh được — không phải vì thiếu tài liệu, mà vì lời giải đòi hỏi bước đột phá khái niệm hoàn toàn mới. Khi Andrew Wiles cuối cùng giải được (thập niên 1990s), ông phải phát minh các kỹ thuật mới hoàn toàn, kết nối hai nhánh toán học khác biệt.

→ Câu hỏi: Liệu ví dụ này proves rằng có gì đó còn thiếu ở LLMs? Hay chúng proves rằng mọi kiến thức con người chỉ là data để training/recombination?

## Các hướng tiếp cận cho continual learning

Phổ từ **không nén** (pure retrieval, weights frozen) → **nén hoàn toàn bên trong** (weight-level learning) → **modules** (vùng trung gian):

| Hướng tiếp cận | Mô tả |
|---|---|
| **Context (non-parametric)** | Retrieval pipelines thông minh hơn, agent harnesses, prompt orchestration. Hạn chế: độ dài context |
| **Modules** | Các module kiến thức gắn được (đã nén KV caches, adapter layers) — chuyên môn hóa model mà không cần retrain. Model 8B + đúng module = hiệu năng 109B trên các tác vụ cụ thể |
| **Cập nhật weights (parametric)** | Sparse memory layers, RL loops, test-time training. Hướng sâu nhất, khó deploy nhất, nhưng cho phép models thực sự internalize thông tin/kỹ năng mới |

## Tại sao "memory features" như ChatGPT Memory không thỏa mãn?

Users không muốn khả năng nhớ thuần túy. Họ muốn năng lực.
- Model đã internalize các patterns → có thể khái quát hóa ra tình huống mới
- Model chỉ recall lại lịch sử → không khái quát hóa được

Khác biệt: "Đây là điều bạn đã phản hồi trước đó" (sao chép nguyên) vs. "Tôi hiểu cách bạn suy nghĩ đủ để dự đoán điều bạn cần" (học được)

## Các hướng nghiên cứu

- **Regularization/weight-space:** EWC, weight interpolation — nhưng dễ gãy ở quy mô lớn
- **Test-time training (TTT):** Chạy gradient descent trên test-time data, nén thông tin mới vào parameters tại thời điểm cần thiết
- **Meta-learning:** Train models để biết cách học

## Nguồn

- a16z: https://www.a16z.news/p/why-we-need-continual-learning