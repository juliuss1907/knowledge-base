---
type: source
original: "[[2026-05-20_unreasonable-effectiveness-of-html]]"
main_tag: ai
sub_tags: [tools, opinion, coding]
topic: html-as-agent-output
date_compiled: 2026-10-03
url: https://claude.dev/blog/using-claude-code-the-unreasonable-effectiveness-of-html/
author: Thariq Shihipar
---

# Using Claude Code: The unreasonable effectiveness of HTML

## Metadata

- **Author:** Thariq Shihipar (member of technical staff, Anthropic)
- **Published:** 2026-05-20
- **Source:** claude.dev
- **URL:** https://claude.dev/blog/using-claude-code-the-unreasonable-effectiveness-of-html/
- **Type:** article
- **Example gallery:** https://thariqs.github.io/html-effectiveness/
- **Code gallery:** https://github.com/anthropics/html-effectiveness

## Summary

Thariq Shihipar (Anthropic) lập luận rằng Markdown — định dạng phổ biến nhất để agent giao tiếp với con người — đã trở thành ràng buộc ngay khi Claude Code đủ mạnh để viết spec, plan và báo cáo dài hơn một trang. Ông chuyển sang dùng HTML làm output format mặc định, vì HTML gánh được mật độ thông tin mà Markdown không có: bảng dữ liệu, CSS, SVG, canvas, tương tác JavaScript, workflow và dữ liệu không gian. Lý do không chỉ ở "đẹp hơn": người đọc dừng lại ở khoảng 100 dòng Markdown và không ai trong tổ chức chịu đọc, trong khi HTML dễ đọc hơn, dễ chia sẻ hơn (mở bằng browser thay vì đính kèm), và mở ra tương tác hai chiều — slider, knob, editor throwaway — với nút export để đưa thay đổi ngược lại thành prompt. Phần token tăng thêm gần như không đáng kể khi context window của Opus 4.7 đã lên 1 triệu token. Điều thật sự nằm sau toàn bộ là muốn giữ bản thân ở trong vòng lặp với Claude, thay vì bàn giao plan rồi chỉ đọc lướt.

## Key points

- **Markdown thành giới hạn:** tác giả không đọc nổi file Markdown quá 100 dòng, và cũng không thuyết phục được ai khác trong tổ chức đọc — trong khi Claude càng mạnh thì spec và plan nó viết càng dài
- **Lợi thế lớn nhất của Markdown đã mất:** ngày càng ít khi tác giả tự edit các file này, chúng được dùng làm spec và reference; khi cần sửa thì prompt Claude sửa — tức là mất đúng cái lợi thế lớn nhất (dễ edit bằng tay) của Markdown
- **Information density của HTML:** table cho tabular data, CSS cho design, SVG cho illustration và workflow, script tags cho code snippet, JavaScript + CSS cho interaction, absolute positioning + canvas cho spatial data, image tags cho ảnh — gần như không có loại thông tin nào model đọc được mà HTML không biểu diễn hiệu quả
- **Model biểu diễn kém trong Markdown:** khi bị giới hạn ở Markdown, model phải làm những việc kém hiệu quả — ASCII diagram, hoặc ước lượng màu sắc bằng unicode
- **Ba lý do thực dụng:** visual clarity (Claude tự tổ chức cấu trúc bằng tab, illustration, link, mobile responsive), ease of sharing (upload HTML rồi gửi link, đồng nghiệp mở ở bất kỳ đâu — tỉ lệ thật sự đọc spec/report/PR writeup tăng rõ), và two-way interaction
- **Custom editing interface:** khi không mô tả được ý mình bằng text box, tác giả bảo Claude build một editor throwaway cho đúng piece of data đó — không phải product, không phải tool tái sử dụng, chỉ một file HTML — và luôn kết thúc bằng export ("copy as JSON", "copy as prompt") để quay lại Claude Code
- **Dữ liệu là lợi thế lớn nhất của Claude Code so với Claude.ai:** ngoài filesystem còn có MCP (Slack, Linear), web browser (Claude in Chrome) và git history — chính bài viết này được viết bằng cách bảo Claude Code đọc folder code, tìm mọi file HTML đã sinh, gom nhóm và dựng diagram cho từng loại
- **Workflow nhiều file thay cho một plan:** brainstorm nhiều hướng khác nhau → mở rộng hướng đó thành mockup → viết implementation plan → mở session mới và đưa toàn bộ file này vào để implement; các file được giữ lại làm reference cho verification
- **Không cần kỹ thuật gì để bắt đầu:** chỉ cần prompt "make an HTML file" hoặc "make an HTML artifact"; điều cần biết là artifact đó phải làm gì và dùng ra sao — chuyển thành skill sau khi thấy pattern lặp
- **Token cost không phải rào cản:** Markdown dùng ít token hơn, nhưng với context window 1MM của Opus 4.7 thì phần tăng thêm gần như không thấy, còn khả năng thật sự đọc lại tài liệu tăng lên — nên tổng output tốt hơn
- **Tác giả gần như bỏ Markdown hoàn toàn** (thừa nhận mình ở thành HTML maximalist), và không còn dùng một plan duy nhất mà tách theo từng stage
- **Động cơ sâu nhất là giữ mình trong loop:** khi Claude gánh nhiều việc hơn, tác giả nhận ra mình đọc plan kỹ hơn trước, nên cần một cách để vẫn gắn với các lựa chọn của Claude thay vì bàn giao rồi bỏ qua

## Concepts referenced

- [[html-as-agent-output-format]]
- [[throwaway-editing-interface]]
- [[multi-file-artifact-workflow]]
- [[code-visualization]]
- [[long-context-models]]
- [[human-judgment-ai]]
- [[frontend-design-agent]]

## Original excerpts

> "I've found that I tend to not actually read more than a 100-line Markdown file, and I certainly am not able to get anyone else in my organization to read it."

> "In my opinion, there is almost no set of information that Claude can read that you cannot efficiently represent with HTML."

> "Not a product, or a reusable tool, but a single HTML file, purpose-built for this one piece of data. The trick is always to end with an export: a 'copy as JSON' or 'copy as prompt' button that turns whatever I did in the UI back into something I can paste into Claude Code or commit to a file. You stay in the loop, but the loop gets much tighter."

> "While Markdown often uses fewer tokens, I've found that the added expressiveness of HTML and the much higher likelihood of me reading it means I get overall better output. With the 1MM context window in Opus 4.7, the increased token usage is not really noticeable in the context window."

> "The real reason I use HTML instead of Markdown is that it helps me feel much more in the loop with Claude. As Claude takes on more, I'd noticed I was reading plans less closely, and I wanted a way to stay engaged with its choices rather than just hand them off."

## Notes
