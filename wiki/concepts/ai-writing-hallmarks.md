---
type: concept
status: draft
main_tag: ai
sub_tags: [opinion]
topic: ai-writing-habits
sources:
  - "[[src_habits-of-ai-writing-a16z-crypto]]"
last_updated: 2026-08-26
---

# AI Writing Hallmarks

## Definition

Bộ đặc điểm văn phong thường gặp trong machine-generated prose, chia thành bốn nhóm: rhetorical (câu nghe hay nhưng rỗng nghĩa), voice (từ vựng generic, tính fungible cao), structural (over-organization), và punctuation (colon/em dash clustering). Điểm mấu chốt: đây là taxonomy các vấn đề viết đã tồn tại từ trước AI, nên giá trị của việc nhận diện nằm ở sửa văn chứ không phải truy tìm nguồn.

## Key ideas

- Rhetorical tells: "insight-shaped writing" — câu plausible nhưng semantic-vacant ("Something real is happening"), empty contrasts, hedges làm câu không thể sai, in-summation phrases; trước AI người ta gọi loại ngôn ngữ này là "corporate"
- Voice tells: fungibility test — câu có thể transplant sang bài khác topic mà không ai nhận ra; low-friction vocabulary, abstract nouns 3+ âm tiết nói về điều không có gì ("efficiency", "innovation"), insipid dynamism ("navigate", "unlock", "empower")
- Structure tells: over-organization, mọi thứ come in threes, formulaic openings, signposting thừa, ending bằng restatement thay vì mở hướng mới
- Punctuation tells: colon-heavy phrasing kèm grocery lists, em dash clustering (dấu dash tự nó vô tội, density mới là vấn đề), sameness — mọi câu cùng nhịp
- Khi embrace: Alexa voice hợp với support docs/ToS/error messages; cấu trúc rõ hợp với explainer/documentation/content cho skimmers và tối ưu SEO/LLM
- Edit strategy dùng chính LLM ở chế độ detection: flag jargon và hedges, yêu cầu "boring version" để chạy paraphrase test, viết ở reading level thấp hơn làm blunt instrument
- Hệ quả meta: khi AI né tells (ví dụ bỏ em dash quay sang colons), bộ tells liên tục dịch chuyển — detection theo danh sách đặc trưng là cuộc đua không hồi kết

## Related concepts

- [[paraphrase-test]]
- [[ai-text-watermarking]]
- [[non-commodity-content]]

## Sources

- [[src_habits-of-ai-writing-a16z-crypto]]
