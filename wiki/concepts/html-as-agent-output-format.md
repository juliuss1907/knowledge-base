---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, opinion, coding]
topic: html-as-agent-output
sources:
  - "[[src_unreasonable-effectiveness-of-html]]"
  - "[[src_motion-design-studio-with-opus-5-5]]"
last_updated: 2026-10-04
---

# HTML as Agent Output Format

## Definition

HTML as agent output format là thực hành để agent sinh tài liệu dưới dạng file HTML thay vì Markdown, nhằm tăng mật độ thông tin và khả năng đọc của output so với một tài liệu text thuần. Thariq Shihipar (Anthropic) lập luận rằng Markdown đã thành định dạng giới hạn khi agent viết được spec, plan và báo cáo dài hơn một trang, và ông chuyển sang HTML làm format mặc định cho gần như mọi output.

## Key ideas

- **Markdown mất lợi thế cốt lõi:** lợi thế lớn nhất của Markdown là dễ edit bằng tay, nhưng khi file được dùng làm spec/reference và mọi chỉnh sửa đều thông qua prompt, lợi thế đó biến mất
- **Information density là lý do chính:** HTML gánh được table (tabular data), CSS (design), SVG (illustration, workflow), script tags (code snippet), JavaScript + CSS (interaction), absolute positioning + canvas (spatial data), image tags (ảnh) — gần như không có loại thông tin nào model đọc được mà HTML không biểu diễn hiệu quả
- **Model biểu diễn kém khi bị ép dùng Markdown:** buộc dùng Markdown, model phải làm ASCII diagram hoặc ước lượng màu sắc bằng unicode — dấu hiệu format đang chặn khả năng thật của model, không phải lỗi của model
- **Giới hạn đọc thực tế ~100 dòng Markdown:** tác giả không đọc nổi file Markdown dài hơn 100 dòng và cũng không thuyết phục được đồng nghiệp đọc; Claude tốt hơn thì tài liệu càng dài, tệ lặp càng rõ
- **Dễ đọc là do Claude tổ chức cấu trúc, không chỉ do định dạng:** tab, illustration, link, mobile responsive — model chủ động bố trí để tối ưu điều hướng, thứ mà Markdown không có khái niệm tương đương
- **Dễ chia sẻ là lợi thế thực dụng nhất:** Markdown gần như không render được trong browser nên phải đính kèm; upload HTML rồi gửi link, đồng nghiệp mở ở bất kỳ đâu — tỉ lệ thật sự đọc spec, report, PR writeup tăng rõ rệt
- **Token cost không còn là rào cản:** Markdown dùng ít token hơn, nhưng với context window 1 triệu token của Opus 4.7 thì phần tăng thêm gần như không thấy trong context, còn khả năng thật sự đọc lại tài liệu lại tăng lên — nên tổng output tốt hơn, xem [[long-context-models]]
- **Bắt đầu không cần kỹ thuật gì:** chỉ cần prompt "make an HTML file" hoặc "make an HTML artifact"; yếu tố quyết định là biết artifact cần làm gì và dùng ra sao, không phải biết HTML
- **Skill hoá sau khi thấy pattern:** tác giả để prompt from scratch trước để cảm nhận, rồi mới gom các pattern lặp thành skill — xem [[agent-skill-management]]
- **Claude Code có lợi thế dữ liệu mà Claude.ai không có:** filesystem, MCP (Slack, Linear), web browser (Claude in Chrome), git history — nhờ đó HTML artifact có thể dựng từ dữ liệu thật của codebase thay vì mô tả suông
- **HTML như output format của agent tự sinh code:** trong pipeline code2video, agent xuất ra `index.html` + `render.mjs` chứ không xuất video — HTML là định dạng trung gian mà browser đọc và chụp từng frame, xem [[code2video-render-loop]]
- **Một canvas, một hàm thuần là ranh giới giữa demo và sản phẩm:** khi agent được yêu cầu dựng "trang mô tả video", nó sẽ xuất HTML tĩnh; yêu cầu `window.seek(t)` biết vẽ mọi thời điểm mới là đưa nó về phía artifact có thể dùng
- **Tác giả tự nhận ở thành HTML maximalist:** đã gần như bỏ Markdown, không phải luận điểm khách quan mà là lựa chọn cá nhân của một người viết spec hàng ngày

## Related concepts

- [[throwaway-editing-interface]]
- [[multi-file-artifact-workflow]]
- [[code-visualization]]
- [[frontend-design-agent]]
- [[long-context-models]]
- [[human-judgment-ai]]
- [[context-window-management]]
- [[code2video-render-loop]]

## Sources

- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)
- [[src_motion-design-studio-with-opus-5-5]]

## Notes
