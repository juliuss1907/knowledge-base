---
type: source
original: "[[2026-09-25_how-to-make-infinite-ads-with-claude-code]]"
main_tag: ai
sub_tags: [tools, automation, tutorial]
topic: ai-ad-creative-system
date_compiled: 2026-10-04
url: https://x.com/shivsakhuja/status/2103379767311691891
author: Shiv (@shivsakhuja)
---

# How to make infinite ads with Claude Code (Full Guide)

## Metadata

- **Author:** Shiv (@shivsakhuja)
- **Published:** 2026-09-25
- **Source:** x.com (X Article long-form)
- **URL:** https://x.com/shivsakhuja/status/2103379767311691891
- **Type:** post
- **Engagement at ingest:** 33 likes · 6 reposts · 19 replies · 71 bookmarks · 5.304 views
- **Yêu cầu:** Claude Code + API key Fal hoặc OpenAI

## Summary

Shiv (@shivsakhuja) mô tả hệ thống dùng Claude Code sinh hàng loạt quảng cáo tĩnh cho DTC brand, tuyên bố nhóm của ông đã tạo hơn 30.000 creative trong 2 tháng bằng đúng workflow này. Luận điểm trung tâm: dùng AI image tool hay nhờ ChatGPT làm quảng cáo thường thất bại vì output chậm, thiếu nhất quán và không giống brand — thứ model thiếu không phải intelligence mà là hệ thống xung quanh nó. Hệ thống gồm 5 bước: (1) brand brain là một folder chứa toàn bộ thông tin thương hiệu mà Claude đọc lại mỗi lần, không bao giờ bắt đầu từ số 0; (2) một skill `.claude/skills/make-static-ads/SKILL.md` biết đọc brief, chọn sản phẩm và template, viết prompt rồi gửi sang GPT Image 2.5; (3) viết creative brief trước khi tạo bất kỳ ảnh nào; (4) thêm một judge — Claude Opus 5.5 chấm điểm pass/fail theo rubric trước khi người dùng kịp nhìn ảnh, ảnh fail thì quay lại model edit với prompt chỉ sửa đúng lỗi đó; (5) biến phản hồi thành rule trong `rules.md` để lần sau không lặp lại sai lầm. Chi phí mỗi creative hoàn chỉnh khoảng 10–20 cent, thấp hơn nhiều so với designer làm thủ công, và chiến lược là làm thật nhiều rồi chọn — chấp nhận phần lớn output sẽ bị loại.

## Key points

- **Vấn đề gốc:** Meta cần lượng creative lớn và tốc độ đẩy lớn; designer không kịp volume, nên team chuyển sang AI — nhưng kết quả thường disappointing: chậm, thiếu nhất quán, copy tệ, hoặc nói những điều brand không bao giờ nói
- **Chẩn đoán chính xác:** vấn đề không phải model yếu mà là thiếu hệ thống xung quanh model — agent cần knowledge (hiểu brand), skill (biết làm việc), tools (làm được việc), và loop (tốt hơn sau mỗi lần dùng)
- **Brand brain là folder, không phải prompt:** `brand-brain/` gồm `brand-overview.md`, `visual-language.md`, `rules.md`, `judge-rubric.md`, `product-catalog/<product>/` (notes + images) và `creative-templates/` (product-hero, ugc-testimonial, before-after) — Claude đọc lại mỗi lần nên không khởi động từ số 0
- **Cấu trúc thư mục:** `brand-brain/` + `campaigns/<campaign>/{brief.md, ads/}` + `.claude/skills/make-static-ads/SKILL.md` — campaign brief tách khỏi brand knowledge để mỗi campaign có không gian riêng
- **Skill làm đúng 5 việc:** hiểu campaign → lấy sản phẩm liên quan từ product catalog → lấy 1 creative template → viết prompt → gửi prompt + ảnh sản phẩm + template vào GPT Image 2.5 Flare ở mức medium hoặc high effort
- **Brief trước, ảnh sau:** brief gồm goal, đối tượng, sản phẩm, offer, angles/concept — bỏ bước này thì phần lớn batch sẽ không có nghĩa hoặc có angle tệ
- **Hai nguồn đa dạng:** templates tạo đa dạng hình ảnh, angles tạo đa dạng ý tưởng — dùng cả hai, đừng chỉ một
- **Judge chặn output trước khi người dùng thấy:** Claude Opus 5.5 chấm pass/fail theo `judge-rubric.md` với các tiêu chí hallucinations, product accuracy, logo fidelity, brand identity — ảnh fail thì nhận edit prompt chỉ sửa đúng vấn đề đó rồi chấm lại
- **Sửa cục bộ bằng model khác:** ảnh fail gửi sang GPT Image 2.5 Sunburst với edit prompt của judge — Sunburst mạnh hơn về sửa lỗi chính xác nên không phải làm lại cả quảng cáo; mặc định loop 1–2 lần rồi bỏ
- **Điều kiện dừng loop:** nếu judge fail quá nhiều chiều, đừng cứ loop tiếp — có thể bản thân ý tưởng không đáng sửa
- **Feedback → rule là vòng đóng:** mỗi lần duyệt batch thấy điều sai thì ghi vào `rules.md` ("không dùng font này", "luôn có logo", "ưu tiên logo góc dưới trái") — skill đọc rule mỗi lần chạy nên không lặp lại lỗi cũ
- **Anti-pattern được liệt kê:** không template (GPT Image 2.5 làm tốt khi có template, text-to-image đơn thuần cho kết quả kém), để LLM tự chọn toàn bộ angles (ý tưởng generic), bỏ qua brief, kỳ vọng mọi ảnh đều đẹp, và sửa cùng một lỗi hai lần thay vì biến nó thành rule
- **Con số:** ~10–20 cent mỗi creative hoàn chỉnh, trên 30.000 creative trong 2 tháng — đủ rẻ để chấp nhận làm nhiều và chọn
- **Đường cài nhanh:** `npx gooseworks install --all` rồi `/gooseworks onboard me` và `/gooseworks plan my campaign and make me a batch of ad creatives` — thay vì tự dựng

## Concepts referenced

- [[brand-brain]]
- [[llm-judge-loop]]
- [[harness-engineering]]

## Original excerpts

> "What you actually need is a system around the model. The agent needs knowledge so it understands your brand. It needs a skill so it knows how to do the work. It needs tools so it can actually do the work. And it needs a loop so it gets better every time you use it."

> "When an image comes back, don't look at it yet. Let a judge look at it first."

> "If the judge fails on too many dimensions, don't keep looping, it might not be worth it."

> "It works out to about 10 to 20 cents per finished creative, so you can afford to [make lots of variants and pick the ones you like]."
