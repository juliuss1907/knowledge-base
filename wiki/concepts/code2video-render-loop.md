---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools, system]
topic: ai-motion-design-pipeline
sources:
  - "[[src_motion-design-studio-with-opus-5-5]]"
last_updated: 2026-10-04
---

# Code2Video Render Loop

## Definition

Code2Video render loop là pipeline tạo video bằng cách bắt model viết một chương trình vẽ frame thay vì xuất video trực tiếp. Model viết một hàm thuần `seek(t)` vẽ đúng frame tại mọi thời điểm, headless browser gọi hàm đó hàng trăm lần chụp từng frame, ffmpeg ghép lại thành MP4. Vì không phụ thuộc timer, render giống hệt nhau mọi lần chạy và một thay đổi chỉ là sửa một dòng rồi render lại.

## Key ideas

- **Model không xuất được MP4:** Opus 5.5 nhận text và ảnh vào, trả text ra — mọi video trong làn sóng motion design là *chương trình do model viết*, còn thứ khác biến chương trình đó thành frame
- **Tính quyết định là mẹo cốt lõi:** không dùng timer, CSS transition hay requestAnimationFrame ở render mode; noise phải seeded (mulberry32) chứ không dùng Math.random — nếu không thì mỗi lần render cho kết quả khác nhau và không sửa được từng giây
- **Cơ chế render chuẩn:** headless browser (Playwright) gọi `window.seek(t)` ở 60fps (900 lần cho 15 giây), chụp canvas từng frame, đẩu vào ffmpeg qua pipe; dùng subframe trung gian và trộn bằng `tmix` để có motion blur
- **Render chậm hơn nhưng sửa được từng phần:** đổi công cụ xuất video trực tiếp thì sửa một cảnh phải làm lại toàn bộ; ở đây sửa một dòng rồi render lại đúng những giây bị ảnh hưởng
- **Model tự chọn route không dependency:** khi bỏ qua Remotion và HyperFrames dù có sẵn, Opus dựng `index.html` + Playwright + ffmpeg từ đầu — muốn model dùng framework thì phải nói rõ trong prompt
- **Route B cho nghiệp dụng:** Remotion (React) hợp với series, template, video data-driven; HyperFrames (HTML + GSAP) hợp khi bạn nghĩ bằng web page — cả hai đều cho khả năng sửa một dòng rồi render lại
- **Một số chi tiết quyết định chất lượng:** phải đợi `document.fonts.ready` trước khi chụp vì canvas text cần font đã tải; tuyệt đối không dùng `will-change` trên phần bị camera scale (chữ sẽ mờ); giữ thống nhất DPR giữa browser và canvas
- **Đây là cùng nguyên tắc với render deterministic trong kỹ thuật đồ họa:** state phải suy ra được từ thời gian, không tích luỹ theo thứ tự khung hình

## Related concepts

- [[closed-form-springs]]
- [[critique-loop-self-scoring]]
- [[html-as-agent-output-format]]
- [[harness-engineering]]

## Sources

- [[src_motion-design-studio-with-opus-5-5]]

## Notes
