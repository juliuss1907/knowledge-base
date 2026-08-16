---
type: source
original: "[[2026-08-15_how-ai-text-watermarking-works]]"
main_tag: ai
sub_tags: [research, tools, hack]
topic: ai-text-watermarking
date_compiled: 2026-08-16
url: https://declaude.org/watermarking/
author: James Padolsey
---

# How AI text watermarking works: a visual guide

## Metadata

- **Tác giả:** James Padolsey (NOPE, declaude)
- **URL:** https://declaude.org/watermarking/
- **Nguồn:** declaude.org — visual guide kèm interactive figures
- **Nền tảng:** Website / article

## Summary

Bài viết giải thích cách AI text watermarking hoạt động mà không cần giấu dữ liệu trong ký tự — dấu vân tay nằm trong *lựa chọn giữa các từ*, không phải trong chính các từ. Mô hình viết bằng cách "tung xúc xắc có trọng số" giữa nhiều từ đều hợp lý, và một secret key có thể bí mật nghiêng các lựa chọn đó về phía "green words". Người giữ key có thể tái-tô màu bất kỳ văn bản nào và đếm tỷ lệ green — nếu cao hơn ngẫu nhiên thì văn bản đã qua xử lý của mô hình. Điểm yếu của phương pháp này là editing: dấu chỉ tồn tại trong những chuỗi từ nguyên vẹn, nên rewrite từ nghĩa (không dùng chung chuỗi từ) mới thực sự xoá được mark, còn paraphrase nhẹ chỉ làm loãng nó. Bài nhấn mạnh watermarking là một phép kiểm tra thống kê có key — khác hẳn các "AI detector" kiểu GPTZero đoán theo phong cách — và một dấu tìm thấy chỉ chứng minh "đã qua xử lý", không phải "do AI viết".

## Key points

- Watermark không nằm trong ký tự hay metadata — nằm trong *các lựa chọn giữa các từ* khi model sinh text.
- Model viết bằng cách chọn từ giữa một shortlist các ứng viên đều hợp lý (weighted dice roll) — slack này là nguyên liệu để giấu mark.
- Cơ chế kinh điển (Kirchenbauer et al. 2023): secret key chia từ thành green/red, rồi nghiêng nhẹ xúc xắc về green; nudge đủ nhẹ để text vẫn đọc bình thường.
- Colour của một từ không cố định — key tính từ một chuỗi ngắn các từ phía trước, nên cùng một từ có thể green sau prefix này, red sau prefix khác.
- Two variants: Google SynthID (tournament-style, giữ nguyên odds từng từ đúng model dự định) và Aaronson's scheme tại OpenAI (derive trực tiếp dice-roll từ key).
- Detection không đọc nội dung hay phán xét phong cách — chỉ replay key-l colouring và đếm tỷ lệ green; gần 50% nghĩa là không có mark (hoặc sai key).
- Mark sống trong các chuỗi từ nguyên vẹn; editing xoá mark đúng ở nơi chuỗi bị phá vỡ. Rewrite từ nghĩa (không chung chuỗi từ) là cách thực sự xoá mark.
- Trên MarkLLM (KGW/EXP chạy open model), full-rewrite để lại ~0.5% window sống sót, detector rơi từ chắc chắn xuống coin flip; light paraphrase chỉ làm loãng, recover được sau ~800 tokens.
- Detection là private (chỉ key-holder mới check được), probabilistic, và nói về *processing* chứ không phải *authorship*.
- Giới hạn: Anthropic's production scheme chưa công bố, nên chưa ai bên ngoài test được trên chính model Claude; text ngắn và ít lựa chọn (code, trích dẫn) mang rất ít mark.

## Concepts referenced

- [[ai-text-watermarking]]

## Original excerpts

> "They work because they don't live in the characters at all. They live in the choices between words."
>
> "A watermark check is not an 'AI detector.' A watermark is the opposite: a deliberate, key-gated statistical test."
>
> "A found mark means 'processed by', not 'written by'."