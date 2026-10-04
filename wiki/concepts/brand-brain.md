---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, strategy]
topic: ai-ad-creative-system
sources:
  - "[[src_how-to-make-infinite-ads-with-claude-code]]"
last_updated: 2026-10-04
---

# Brand Brain

## Definition

Brand brain là một folder chứa toàn bộ kiến thức về thương hiệu (mô tả, ngôn ngữ hình ảnh, luật cấm, catalog sản phẩm, template sáng tạo) được agent đọc lại ở mỗi lần sinh output, thay vì để mỗi phiên làm việc bắt đầu từ trang giấy trắng. Mục tiêu là đảm bảo output AI "nói đúng giọng thương hiệu" thay vì trông như sản phẩm của bất kỳ startup nào.

## Key ideas

- **Định nghĩa vấn đề:** phần lớn quảng cáo do AI tạo trông không giống brand vì agent không có nguồn sự thật nào về brand — nó chỉ đoán màu, font và giọng
- **Bốn thành phần:** `brand-overview.md` (bản chất thương hiệu), `visual-language.md` (màu, font, cách dùng logo), `rules.md` (danh sách always/never), `judge-rubric.md` (tiêu chí chấm điểm)
- **Catalog sản phẩm là tài sản lớn nhất:** `product-catalog/<product>/` chứa notes + ảnh thật — đây là thứ chặn hallucination (ảnh sai sản phẩm) và chặn logo/UI bịa đặt
- **Creative templates tạo đa dạng hình ảnh:** `creative-templates/` lưu các layout tái sử dụng (product-hero, ugc-testimonial, before-after) — template là biến thể của visual, angles là biến thể của ý tưởng, cần cả hai
- **`rules.md` phải bắt đầu nhỏ và lớn dần:** ban đầu vài dòng, mỗi vòng review phát hiện lỗi thì thêm một dòng — rule sinh ra từ feedback thực tế thay vì rule viết trước để đẹp cho form
- **Luật phải cụ thể đến mức kiểm chứng:** "không dùng font này", "luôn có logo", "ưu tiên logo góc dưới trái" — mỗi luật chặn được một nhóm lỗi lặp lại
- **Tách brand khỏi campaign:** brand knowledge và brief theo campaign nằm ở hai thư mục riêng (`brand-brain/` và `campaigns/<campaign>/`) để một brief không làm bẩn kiến thức dài hạn
- **Đây là context engineering dạng file:** cùng nguyên tắc với context window management — đưa kiến thức vào artifact tái sử dụng đọc mỗi run, thay vì nhồi vào từng prompt

## Related concepts

- [[llm-judge-loop]]
- [[harness-engineering]]
- [[context-engineering]]
- [[codified-taste]]

## Sources

- [[src_how-to-make-infinite-ads-with-claude-code]]

## Notes
