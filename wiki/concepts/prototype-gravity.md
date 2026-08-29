---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, vibecode]
topic: ai-design-workflow
sources:
  - "[[src_how-i-design-with-ai]]"
last_updated: 2026-08-29
---

# Prototype Gravity

## Definition

Prototype Gravity là hiện tượng khi AI đã build version đầu tiên của thiết kế trong codebase thực, khiến bạn có cảm giác dễ refine bản đó hơn là khám phá các option thiết kế khác. Đây là "silent killer" của thiết kế AI: nó khóa bạn vào một hướng ngay từ đầu, ngăn bạn thử nghiệm và cản trở chất lượng thiết kế tổng thể. Lực hút này mạnh đến mức bạn từ bỏ việc so sánh với các phương án thay thế tốt hơn.

## Key ideas

- **Nguyên nhân:** agent build version đầu trong codebase → có cảm giác như đầu tư đã bỏ ra, nên refine thay vì thử lại từ đầu
- **Hệ quả:** thiết kế bị gắn vào một hướng duy nhất, không được khám phá
- **Thiết kế trong codebase cũng ép agent build version "graft" lên codebase thực,** giới hạn không gian thiết kế
- **Giải pháp:** iterate trong design tool (Figma, Cursor Design Mode, Claude Design, HTML prototypes) thay vì trong product
- **Dùng tool có fine control** và iterate nhanh với minimal extra context
- **AI generate 3-4 variants của mọi thứ** trước khi chọn

## Related concepts

- [[design-process]]
- [[product-vs-prototype]]
- [[vibe-coding]]

## Sources

- [[src_how-i-design-with-ai]]
