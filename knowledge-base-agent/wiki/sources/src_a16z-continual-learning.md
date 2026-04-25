---
type: source
source_url: https://www.a16z.news/p/why-we-need-continual-learning
date_ingested: 2026-04-23
tags: [#ai, #llm]
---
# Tại Sao Chúng Ta Cần Continual Learning — a16z

Bài viết phân tích về sự cần thiết của việc cho phép LLMs học liên tục sau khi triển khai.

## Key Points
- **Hạn chế của LLMs hiện nay**: Hoạt động như nhân vật trong phim Memento, sống trong "hiện tại vĩnh cửu", không thể tạo ký ức mới vào parameters mà phải dùng "hỗ trợ" (context, RAG).
- **In-Context Learning (ICL)**: Hiệu quả với kiến thức đã tồn tại, nhưng không đủ cho những đột phá khái niệm mới hoặc kiến thức ngầm không thể diễn đạt.
- **Bản chất của LLM**: Là thuật toán nén lossy. Chính khả năng nén giúp model khái quát hóa. Việc cấm cập nhật weights sau deploy là một nghịch lý.
- **Phân cấp tiếp cận**:
    - *Context (Non-parametric)*: RAG, agent harnesses (hạn chế bởi context window).
    - *Modules*: Adapters, nén KV caches (chuyên môn hóa model mà không retrain).
    - *Weight Updates (Parametric)*: Sparse memory, RL loops, Test-time training (cho phép internalize kiến thức).
- **Khác biệt giữa Memory và Learning**: Memory là recall lại lịch sử; Learning là hiểu patterns để dự đoán và khái quát hóa.
- **Hướng nghiên cứu**: EWC, Test-time training (TTT), Meta-learning.
