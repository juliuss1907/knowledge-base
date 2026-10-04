---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, strategy, tools]
topic: ai-motion-design-pipeline
sources:
  - "[[src_motion-design-studio-with-opus-5-5]]"
last_updated: 2026-10-04
---

# Director's Brief

## Definition

Director's brief là dạng đặc tả cấp cao dành cho tác phẩm dài, trong đó agent được thuê làm director, animator, sound designer và render engineer cùng lúc thay vì được ra lệnh làm một việc. Điểm khác biệt cốt lõi: brief không *mô tả* video mà *thuê một ê-kíp* — nó cung cấp đủ bối cảnh để agent tự quyết định trong lúc chạy nhiều giờ.

## Key ideas

- **Bằng chứng về quy mô:** các brief được chia sẻ công khai dài 9.500 ký tự (một nhân vật nói với máy 5 phút, agent chạy 12 giờ, ra video 142 giây) và 19.000 ký t cho một tác phẩm khác — thang này hoàn toàn khác một prompt một dòng
- **Tám thành phần của một brief hoàn chỉnh:** logline một dòng (để mọi quyết định sau đều kiểm được với nó), references và inputs, tools & keys kèm ngân sách, character bible (tỉ lệ, palette, biểu cảm, identity lock sống sót qua mọi đổi style), beat sheet (mốc thời gian, visual payoff mỗi 3–5 giây, hook trong 2 giây đầu), text on screen, workflow có gate, critique loop, deliverables
- **Identity lock quan trọng với character:** một mô tả nhận diện phải sống sót qua mọi lần đổi phong cách, nếu không nhân vật sẽ đổi mặt giữa các cảnh
- **Generate-then-trace là kỹ thuật then chốt:** video model (Seedance 2.5) render base shot có nhân vật và vật lý, rồi agent vẽ lại toàn bộ video bằng JavaScript đè lên để người xem chỉ thấy lớp code — video model giải quyết chuyển động khó viết tay, lớp JS mang lại look nhất quán và sở hữu được
- **Workflow phải có gate, không được bỏ qua:** plan → rig → stills → animatic → full pass → polish → audio → render; animatic với audio giả ở 960x540 là chốt nhịp trước khi lao vào polish
- **Chia subagent theo chapter có điều kiện tiên quyết:** agent viết `ANIMATION_GUIDE.md` trước để các subagent chạy song song cùng một style, và `STORYBOARD.md` sau pass đầu — không có tài liệu chuẩn style thì mỗi subagent tự chế ra một phong cách
- **Deliverables phải chứa cả file kiểm chứng:** video cuối, bản loop check, poster frame, contact sheet, và source sạch kèm README — không phải chỉ một file MP4
- **Bí mật nằm ở chỗ agent có thể tự dừng chờ:** brief cho phép "hiện shot list rồi tiếp tục nếu tôi không trả lời trong 10 phút" — biến bài toán tương tác thành tác vụ chạy không giám sát
- **Brief cần giả định bảo thủ về khả năng của chính agent:** yêu cầu agent tự đánh giá cái gì thực sự làm được với ngân sách API hiện có, thay vì hứa hẹn rồi bỏ dở

## Related concepts

- [[code2video-render-loop]]
- [[critique-loop-self-scoring]]
- [[multi-agent-taxonomy]]
- [[harness-engineering]]

## Sources

- [[src_motion-design-studio-with-opus-5-5]]

## Notes
