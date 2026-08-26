---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools, hack]
topic: ai-text-watermarking
sources:
  - "[[src_how-ai-text-watermarking-works]]"
  - "[[src_this-essay-is-10-percent-ai-generated]]"
last_updated: 2026-08-26
---

# AI Text Watermarking

## Definition

AI text watermarking là kỹ thuật nhúng một dấu hiệu không nhìn thấy vào văn bản do mô hình sinh ra, bằng cách tác động lên *các lựa chọn giữa các từ* chứ không phải lên chính ký tự hay metadata. Một secret key làm nghiêng nhẹ xác suất chọn từ giữa một shortlist các ứng viên đều hợp lý; người giữ key có thể tái-tô màu văn bản và đếm tỷ lệ để phát hiện xem nó có qua xử lý của mô hình hay không.

## Key ideas

- Dấu nằm trong "lựa chọn giữa các từ" (choices between words) — vì text không có pixels để giấu và metadata không sống sót qua copy-paste, mark phải nằm ở thứ tồn tại sau mọi thao tác: chính lựa chọn từ.
- Secret key chia các ứng viên thành green/red mỗi lần fork, rồi nghiêng nhẹ xúc xắc về green; nudge đủ nhẹ nên văn bản vẫn đọc bình thường và một từ red vẫn có thể thắng.
- Colour không cố định theo từ — được tính từ chuỗi ngắn các từ phía trước, nên cùng từ có thể green/red tuỳ context; chỉ có lean tổng thể về green là tích luỹ.
- Có nhiều scheme cùng nguyên lý: Kirchenbauer et al. (nudge green/red), Google SynthID-Text (secret tournament giữ nguyên odds từng từ), Aaronson's scheme (derive dice-roll từ key).
- Detection là phép kiểm tra thống kê có key: replay màu và đếm tỷ lệ green; ~50% nghĩa là không mark hoặc sai key. Không đọc nội dung, không phán xét phong cách.
- Mark sống trong các chuỗi từ nguyên vẹn → editing phá chuỗi là xoá mark. Paraphrase nhẹ chỉ loãng (recover sau ~800 tokens); chỉ rewrite từ nghĩa không chung chuỗi từ mới xoá được.
- Dấu chứng minh "đã qua xử lý" chứ không phải "do AI viết" — text chỉ được proofread/dịch bởi model cũng nhiễm mark; text ngắn và ít slack (code, trích dẫn) gần như không mang mark.
- Khác biệt quan trọng với "AI detector" kiểu GPTZero: watermark là phép kiểm tra key-gated có nguyên tắc, không phải phán đoán theo style.
- Alex Danco (2026): các model company đồng loạt công bố watermarking khi dư luận về AI writing đạt đỉnh — theo historical pattern "peak reaction to the thing is the moment when the thing stops mattering"; arms race giữa detector và avoider có thể đã đóng cửa sổ reliable detection ở frontier models
- Trong thực tiễn xã hội, watermark/detector (Pangram) được dùng như category authorship để dunk "100% AI generated" — phục vụ author-function chứ không hẳn phán xét chất lượng văn bản (xem [[author-function]])

## Related concepts

- [[llm-output-detection]]
- [[synthid]]
- [[author-function]]
- [[ai-writing-hallmarks]]

## Sources

- [[src_how-ai-text-watermarking-works]]
- [[src_this-essay-is-10-percent-ai-generated]]

## Notes