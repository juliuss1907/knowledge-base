---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, research, tools]
topic: ai-motion-design-pipeline
sources:
  - "[[src_motion-design-studio-with-opus-5-5]]"
last_updated: 2026-10-04
---

# Critique Loop Self-Scoring

## Definition

Critique loop self-scoring là thực hành bắt model nhìn lại chính output của nó: render từng frame thành contact sheet, đưa ảnh đó về cho model, yêu cầu chấm điểm theo tiêu chí cụ thể, liệt kê vấn đề tệ nhất kèm timestamp, rồi sửa và render lại đúng những phần bị ảnh hưởng — lặp tới khi điểm mọi tiêu chí đều đạt ngưỡng.

## Key ideas

- **Điều kiện tiên quyết:** chỉ chạy được khi model đọc được ảnh — chat app chỉ viết được animation, cần agent có shell (Claude Code) mới render, nghe và soi frame được
- **Bốn công cụ soi tạo ra:** contact sheet (`fps=2, scale=270:-1, tile=6x5`), strip 12 frame liên tiếp quanh hành động nhanh để bắt lỗi pop và chồng chữ, bản thu nhỏ 360px kiểm tra khả năng đọc trên điện thoại, và loop check phát cắt liền mạch
- **Tiêu chí chấm điểm phải cụ thể và quan sát được:** hook trong 2 giây đầu, khả năng đọc ở kích thước điện thoại, chất lượng chuyển động (có spring, không frame chết), độ đa dạng (có gì mới mỗi 2–4 giây), bố cục, brand accuracy, sound sync
- **Ngưỡng điểm là điều kiện thoát:** đặt ngưỡng rõ ràng (mọi tiêu chí ≥ 8/10) và lặp tới khi đạt — không có ngưỡng thì "sửa thêm" là vô hạn
- **Sửa có mục tiêu, không sửa chung:** liệt kê 3 vấn đề lớn nhất kèm timestamp, sửa 3 đó, render lại đúng những giây bị ảnh hưởng, rồi xem contact sheet mới
- **Vai trò phản hồi thay đổi chất lượng phán đoán:** "hãy là một motion director khắc nghiệt chứ không phải một tác giả tự hào" — chỉ định vai trò đánh giá là điều kiện để phê bình thật
- **Danh sách lỗi thường gặp để săn:** chữ chồng nhau lúc swap, phần tử trượt thay vì ease, corner label và viền khung, shot canh giữa trên gradient, chữ mờ do bị scale, beat chết không có gì xảy ra, giật ở seam của loop
- **Kiểm tra determinism như một bài test:** render cùng một đoạn hai lần rồi so hash — frame render hai lần phải giống hệt
- **Iteration là phương pháp chứ không phải thất bại:** case watercolor công khai 163 lần gọi model, 62,7 triệu token (96% cache reads), ~34 USD, ~6¾ giờ — con số này là bằng chứng trung thực chứ không phải lời xin lỗi
- **Chi phí bị kiểm soát bởi gate trước render đầy đủ:** chỉ render contact sheet (một frame mỗi beat) trước khi làm full pass — sửa storyboard rẻ hơn sửa render hàng trăm lần

## Related concepts

- [[code2video-render-loop]]
- [[closed-form-springs]]
- [[llm-judge-loop]]
- [[ai-evals]]
- [[behavioral-evals]]

## Sources

- [[src_motion-design-studio-with-opus-5-5]]

## Notes
