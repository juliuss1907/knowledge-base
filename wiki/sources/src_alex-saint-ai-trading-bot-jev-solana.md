---
type: source
original: "[[2026-09-23_alex-saint-ai-trading-bot-jev-solana]]"
main_tag: ai
sub_tags: [automation, tools, hack]
topic: ai-trading-agent-safety
date_compiled: 2026-09-24
url: https://x.com/alexsssaint/status/2102420062023946602
author: alex saint (@alexsssaint)
---

# save it > run it tonight

## Metadata

- **Source type:** Post
- **Published:** 2026-09-23
- **Author:** alex saint (@alexsssaint)
- **Source:** x.com
- **URL:** https://x.com/alexsssaint/status/2102420062023946602

## Summary

Bài viết mô tả một AI trading bot chạy trên Solana với hai model ở hai tốc độ: Jev đưa quyết định có confidence mỗi 15 giây, còn Fable rà soát log mỗi đêm và đề xuất bản sửa cho decision rules. Tác giả chuyển phép tính số sang adjectives trong code, thu gọn state thành mười hai từ, dùng `noul` để veto chu kỳ và mặc định `hold` khi API lỗi. Mô hình đêm chỉ ghi proposal, không tự deploy; con người phải duyệt diff trước khi prompt mới được dùng, còn private key nằm ngoài tầm truy cập của cả hai model. Dù vốn hệ thống có guardrails nhiều lớp, kết quả mới chỉ kéo dài tám ngày nên chưa phải track record và không đủ chứng minh hiệu quả chiến lược.

## Key points

- **Decision model thay chat model:** Jev nhận typed state và trả structured decision cùng probability, loại bỏ bước parse văn bản tự do trước khi thực thi.
- **Ba loại câu hỏi:** `choice` chọn giá trị, `score` chấm điểm theo thang và `noul` trả xác suất yes/no; các câu hỏi cùng state có thể chạy song song.
- **Confidence dùng cho risk control:** Quy tắc “confidence cao thì hành động, thấp thì `hold`” biến calibration thành điều kiện vận hành có thể kiểm thử.
- **Không đưa số thập phân cho model:** Code tính slippage, fees, return và volatility rồi chuyển thành adjectives như `thin`, `bot_war`, `pumping`, `violent`.
- **State nhỏ giảm biến động quyết định:** Tác giả giới hạn toàn bộ state ở mười hai từ vì mỗi chiều thông tin thêm có thể làm decision flip và tạo thêm chi phí giao dịch.
- **Decision log tạo vật liệu cải thiện:** Mỗi quyết định lưu state, action, confidence và biến động giá sau 15 phút để tìm các lần high-confidence bị sai.
- **Night shift chỉ đề xuất:** Fable rút gọn log, tập trung vào disagreement, viết proposal riêng; human approval hoặc test gate mới cho phép phát hành prompt version mới.
- **Key và authority được tách khỏi model:** Bot wallet chỉ chứa stake, Phantom nhận lợi nhuận, private key nằm trong code mà Jev và Fable không đọc.
- **Bằng chứng còn hạn chế:** Tác giả nêu rõ tám ngày vận hành không phải track record; rủi ro chính có thể là rewrite sai âm thầm làm giảm hiệu suất dù confidence vẫn cao.

## Concepts referenced

- [[two-speed-agent-loop]]
- [[calibrated-decision-models]]
- [[wallet-isolation-for-ai-agents]]
- [[ai-trading-agent]]
- [[multi-agent-risk-review]]

## Original excerpts

> “Fast model decides, slow model rewrites the fast one's rules. Never one model doing both.”
> — alex saint

> “Anything that can change how money moves gets a human or a test between the idea and the execution.”
> — alex saint

> “The compute is lunch money. The risk is the stake.”
> — alex saint
