---
type: concept
status: draft
main_tag: tech
sub_tags: [coding, research]
topic: ai-motion-design-pipeline
sources:
  - "[[src_motion-design-studio-with-opus-5-5]]"
last_updated: 2026-10-04
---

# Closed-Form Springs

## Definition

Closed-form spring là cách biểu diễn chuyển động bằng một hàm giải tích theo thời gian, thay vì tích luỹ trạng thái qua từng frame. Chuyển động kết quả có khối lượng — tăng tốc, vượt qua đích một chút rồi settle — đồng thời vẫn là hàm thuần của `t`, nên có thể render bất kỳ frame nào mà không cần mô phỏng những frame trước đó.

## Key ideas

- **Chuyển động rẻ vs chuyển động đắt:** motion rẻ ease từ A sang B trên một curve cố định; motion đắt có khối lượng — nó tăng tốc, overshoot nhẹ, rồi settle
- **Điều kiện để deterministic:** spring phải là closed-form step response, tức hàm của `t` chứ không phải tích phân của trạng thái hiện tại — đây là điều kiện để `seek(t)` render frame 812 không cần frame 0→811
- **Mẹo bị nhiều người bỏ qua — cộng spring thay vì restart:** khi một giá trị đổi target nhiều lần (cursor, chiều rộng container), không restart spring mà **cộng** một spring cho mỗi lần đổi, mỗi cái bắt đầu ở thời điểm riêng; chuyển động vẫn liên tục và vẫn render được frame bất kỳ
- **Thư viện chuyển động theo loại:** snappy cho button/toggle/leading edge, default cho card/container/camera, heavy cho chữ lớn, vật thể 3D, logo lockup, playful (overshoot rõ) cho mascot và sticker
- **Tab indicator co giãn bằng hai spring khác độ cứng:** cạnh dẫn cứng hơn cạnh theo, để nó bám trước và giãn ra — thao tác kéo trực tiếp tính giá trị từ vị trí con trỏ, thả ra thì spring về từ chỗ vừa thả
- **Text trong container đang morph cần thời điểm vào/ra riêng:** text vào sau khi morph bắt đầu và ra trước khi morph kế tiếp, nếu không sẽ chồng chữ
- **Text trong box morph đòi hỏi alpha tách riêng:** công thức alpha cắt bằng cả hai phía (fade-in sau start, fade-out trước end) thay vì một hệ số đơn
- **Loop liền mạch bằng cách ghim frame cuối về frame đầu:** kể cả vị trí và vận tốc con trỏ, nếu không vòng lặp sẽ giật ở đường seam
- **Cấm:** bouncy easing, glow, gradient trên UI chrome, particle burst, và mọi thứ trông như template — danh sách "banned look" ngăn model rơi về mặc định

## Related concepts

- [[code2video-render-loop]]
- [[critique-loop-self-scoring]]
- [[frame-chaining-continuity]]

## Sources

- [[src_motion-design-studio-with-opus-5-5]]

## Notes
