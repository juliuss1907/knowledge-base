---
type: source
original: "[[2026-07-02_how-to-create-ai-animation-ads-with-gemini]]"
main_tag: ai
sub_tags: [tools, tutorial, automation]
topic: ai-animation-ads-workflow
date_compiled: 2026-10-04
url: https://x.com/Mho_23/status/2072764968399667330
author: Miko (@Mho_23)
---

# How To Create AI Animation Ads With Gemini Omni + Fable 5 (Full Guide)

## Metadata

- **Author:** Miko (@Mho_23) — https://t.me/mikoslab
- **Published:** 2026-07-02
- **Source:** x.com (X Article long-form: https://x.com/i/article/2072755339905110016)
- **URL:** https://x.com/Mho_23/status/2072764968399667330
- **Type:** post
- **Engagement at ingest:** 286 likes · 26 reposts · 671 bookmarks · 26.117 views

## Summary

Miko (@Mho_23) trình bày pipeline sản xuất quảng cáo animation bằng AI với chi phí khoảng 12 cent mỗi video, nhắm vào hai nỗi đau phổ biến nhất của dân làm quảng cáo: thời gian chỉnh hình hàng giờ cho mỗi video và chi phí freelancer quá cao. Toàn bộ quy trình chạy trên Gemini Omni (Google AI Ultra, 25.000 credit/tháng giá 200 USD, mỗi video ~15 credit → khoảng 1.666 video/tháng), với Claude Fable 5 làm não chiến lược, Nano Banana Pro tạo frame nền, ElevenLabs đọc voiceover, TikTok/Suno làm nhạc nền và CapCut để ghép và phụ đề. Bài viết chia làm hai phương pháp: phương pháp 1 import SOP vào Claude để Claude tự sinh prompt từng scene theo brand (nhanh, 10–15 phút cho một quảng cáo hoàn chỉnh), phương pháp 2 tạo frame đầu bằng Nano Banana Pro rồi nối tiếp scene bằng frame cuối của scene trước (kiểm soát sáng tạo cao hơn, lâu hơn). Kỹ thuật đáng chú ý nhất và tác giả nói "đa số không biết" chính là cơ chế lấy frame cuối của scene N làm frame đầu của scene N+1 — khớp liền không có điểm cắt hay đổi style giữa các scene. Tác giả nhấn mạnh Gemini Omni giữ được style ổn định xuyên suốt nếu style được khai báo ngay từ đầu, và một prompt Omni tinh chỉnh có thể gánh luôn phần editing thay vì chỉ tạo clip.

## Key points

- **Bài toán kinh tế:** Google AI Ultra 200 USD/tháng = 25.000 credit, mỗi video ~15 credit → ~1.666 video/tháng → khoảng **12 cent/video**, thay thế hoàn toàn phí editor và thời gian chờ turnaround nhiều ngày
- **Nỗi đau được nêu đích danh:** làm thủ công mất trên 1 giờ mỗi video khi cần test nhiều concept → cộng dồn giết chết biên lợi nhuận; đường thuê editor thì gửi brief, chờ 3 ngày, nhận lại sản phẩm lệch yêu cầu, round revision thêm 2 ngày nữa
- **Vai trò mỗi tool trong stack:** Claude Fable 5 = phân tích SOP + sinh prompt từng scene (chiến lược sáng tạo); Gemini Omni = render scene thành clip; Nano Banana Pro = tạo frame đầu phong cách; ElevenLabs = voiceover; TikTok hoặc Suno = nhạc nền; CapCut = ghép + phụ đề + export
- **Phương pháp 1 (nhanh):** dán nguyên SOP vào Claude, yêu cầu Claude phân tích và hiểu cấu trúc trước, sau đó nhập brand details (sản phẩm, tệp khách hàng mục tiêu, style, selling points) → Claude đề xuất concept và trả về prompt theo từng scene, viết sao cho feed thẳng vào Gemini Omni, không phải dịch qua công cụ trung gian
- **Phương pháp 2 (kiểm soát cao):** tạo frame đầu bằng Nano Banana Pro (phải đúng style — muốn claymation thì tạo ảnh claymation), đưa frame + prompt mô tả chuyển động và camera vào Gemini Omni, review rồi mới đi tiếp
- **Kỹ thuật nối frame:** lấy chính frame cuối của clip vừa render làm starting frame cho scene tiếp theo → hai scene chảy liền mạch, không có điểm cắt gắt, không đổi style, lặp lại cho tới hết → đây là cách làm quảng cáo animation dài liên tục mà trông không amateur
- **Tính nhất quán của style:** Gemini Omni khóa style nếu style được nói rõ ngay từ đầu — quảng cáo claymation trông ra claymation xuyên suốt thay vì đổi phong cách giữa chừng
- **Các style khả dụng:** claymation (stop motion), pixar-style 3D, anime, paper cutout, lego, wes-anderson (đối xứng pastel) — chỉ cần chỉ định trong prompt và giữ nhất quán
- **Chọn phương pháp theo nhu cầu:** cần tốc độ và sản lượng lớn → phương pháp 1; có tầm nhìn hình ảnh cụ thể và cần kiểm soát từng frame → phương pháp 2
- **Điểm mấu chốt:** "một prompt Omni tinh chỉnh có thể gánh phần lớn công việc, kể cả phần editing video"
- **Lưu đường dẫn SOP:** tác giả dùng bán kèm SOP đầy đủ trong Free AI Content Starter Kit (whop.com) — phần thuật toán cốt lõi mới là frame-chaining, còn lại là cấu hình tool

## Concepts referenced

- [[ai-animation-ad-pipeline]]
- [[frame-chaining-continuity]]
- [[content-generation-workflow]]

## Original excerpts

> "each animation ad video costs about 15 credits to generate. so if you take your 25,000 credits and divide that by 15 credits per video you get roughly 1,666 full animation videos per month. $200 divided by 1,666 videos comes out to about 12 cents per video."

> "take the last frame of the video you just generated. use that exact frame as the starting frame for your next scene. add your prompt describing what should happen in the next part of the storyline."

> "now you have two scenes that flow together seamlessly because the second scene literally starts where the first one ended. there's no jarring cut or style shift because you're using the actual output from the previous scene as the input for the next one."

> "you just specify the style you want in your prompts and stay consistent with that style throughout every scene. Gemini Omni does a good job of maintaining that consistency as long as you're clear about what you want from the start."
