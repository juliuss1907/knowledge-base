---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, tutorial, coding]
topic: ai-animation-ads-workflow
sources:
  - "[[src_how-to-create-ai-animation-ads-with-gemini]]"
last_updated: 2026-10-04
---

# Frame Chaining for Scene Continuity

## Definition

Frame chaining là kỹ thuật nối các scene animation AI liên tiếp bằng cách lấy chính frame cuối của clip vừa render làm frame đầu (starting frame) cho clip tiếp theo. Nhờ đó scene N+1 bắt đầu đúng tại nơi scene N kết thúc, loại bỏ điểm cắt gắt và hiện tượng đổi style giữa chừng.

## Key ideas

- **Nguyên lý:** scene tiếp theo không được sinh từ mô tả text thuần mà từ output thực của scene trước — cùng một nguồn pixel nên continuity là kết quả tự nhiên
- **Vì sao quan trọng:** animation AI tạo ra nhiều scene rời rạc sẽ lộ ra ngay ở dạng điểm cắt lạ và style drift, đây chính là dấu hiệu khiến nội dung AI trông nghiệp dư
- **Quy trình lặp:** tạo starting frame → animate với prompt mô tả chuyển động và camera → review → lấy frame cuối làm input của scene kế tiếp → lặp tới hết
- **Vai trò của starting frame:** frame đầu phải khớp chính xác look mong muốn trước khi animate; nếu muốn claymation thì frame đầu phải là claymation, không thể để model tự suy ra
- **Prompt vẫn cần, nhưng prompt không mang continuity:** prompt mô tả hành động và chuyển động camera cho scene mới; continuity đến từ frame, không đến từ mô tả
- **Phụ thuộc tool sinh starting frame:** Nano Banana Pro tạo được ảnh stylized theo yêu cầu nên phù hợp làm nguồn frame đầu cho phương pháp kiểm soát cao
- **Quan hệ với nhất quán style:** chaining giải quyết vấn đề khác với style lock — style lock giữ bảng màu và ngôn ngữ hình, chaining giữ vị trí và hình học nối tiếp; cần cả hai
- **Chi phí của kỹ thuật này thấp, giá trị cao:** chỉ tốn thêm một lượt generate nhưng quyết định toàn bộ cảm giác chất lượng của video dài

## Related concepts

- [[ai-animation-ad-pipeline]]
- [[closed-form-springs]]
- [[code2video-render-loop]]

## Sources

- [[src_how-to-create-ai-animation-ads-with-gemini]]

## Notes
