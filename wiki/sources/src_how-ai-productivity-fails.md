---
type: source
original: raw/articles/2026-05-14_how-ai-productivity-fails.md
main_tag: ai
sub_tags: [tools, automation, opinion]
topic: ai-productivity
author: Shrivu
url: https://open.substack.com/pub/shrivu/p/how-ai-productivity-fails
date_ingested: 2026-05-14
date_compiled: 2026-05-15
---

# How AI Productivity Fails

## Metadata

- **Author:** Shrivu
- **Published:** 2026-05-14
- **Source:** Substack
- **URL:** https://open.substack.com/pub/shrivu/p/how-ai-productivity-fails
- **Type:** article

## Summary

Hầu hết người dùng AI chỉ tăng năng suất 10-20% dù họ tuyên bố AI "thay đổi cuộc chơi". Tác giả cho rằng mức tăng 2x hoặc 10x+ là hoàn toàn có thể đạt được, nhưng đòi hỏi đồng thời **thay đổi cá nhân** (personal practice) và **tái cấu trúc tổ chức** (organizational refactoring). Vấn đề hiện tại là sản lượng tăng theo cấp số nhưng tác động thực tế chỉ tăng tuyến tính.

## Key points

- **Không lập kế hoạch, chỉ generate:** AI loại bỏ ma sát buộc phải lập kế hoạch, dẫn đến hệ thống không thể debug hoặc mở rộng. Giải pháp: Outline trước (headers, structure, audience, plan, principles, what-done-looks-like), sau đó mới để AI điền nội dung.
- **Task quá nhỏ:** Context overhead không giảm theo kích thước task. Với AI, một fix 2 dòng code trả cùng chi phí setup như một feature đầy đủ. Giải pháp: Nâng mức tham vọng task đến khi context cost được justify.
- **Giới hạn cognitive với parallel agents:** AI mở rộng generation, không phải working memory của con người. Giới hạn khoảng 3 agents active trong cognitive window. Giải pháp: Closed loops - để agent tự kiểm tra output mà không cần người.
- **1% cuối cùng vẫn cần bạn:** Verification infrastructure và định nghĩa rõ ràng về "done" là kỷ luật khác với generation. Giải pháp: Closed loops end-to-end với tests, queries, sandboxes, browser tools.
- **Không codify taste:** Chat interface coi mỗi session như ephemeral, nhưng taste là reusable artifact. Giải pháp: Xây dựng skills cho class of task, không phải instance. Refuse to edit AI output manually nếu không feed vào learnings.
- **Skill atrophy:** Kỹ năng đến từ cognitive struggle, AI loại bỏ struggle này. Juniors bị ảnh hưởng nặng nhất vì offload cognition trước khi xây dựng capacity đánh giá output.
- **Organization pitfalls - Rewarding usage, not impact:** Usage dễ đo; impact khó đo. Giải pháp: Reward what shipped, weight outcomes by reusable leverage (closed loops, codified skills).
- **No curator after build cost fell:** AI loại bỏ filter "chỉ worthwhile tools mới được build". Giải pháp: Architect-owner accountable cho taxonomy; pilots nhỏ với retirement criteria rõ ràng.
- **Skills without taste-holders:** AI phá vỡ coupling giữa authoring và expertise. Giải pháp: Domain-expert quyết định core skill set; taste-holders build shared skills với quality bar.
- **Review as bottleneck:** Generation vượt review capacity. Giải pháp: Hold people accountable for artifact dù AI generated; reviewers refuse là debugger of last resort.
- **Handoffs, not loops:** AI nén 20% coding nhưng để lại 80% approvals/reviews/syncs làm bottleneck. Giải pháp: Loop ownership thay cho function ownership - một người đóng chuỗi từ problem đến deployment.
- **Mandates without taste:** Mandate truyền behavior, không truyền taste/judgment. Giải pháp: Clarity về expectations, role-definitions, và why behind AI adoption.
- **No shared target:** Bottom-up energy cần target để compound. Giải pháp: ROI legible cho mỗi team; wire working behaviors vào career pathways.

## Concepts referenced

- [[shift-left-testing]]
- [[closed-loop-system]]
- [[codified-taste]]
- [[skill-atrophy]]
- [[loop-ownership]]
- [[taste-holders]]
- [[transposed-organization]]

## Original excerpts

> "If you find it taxing to review your own AI generated output, you didn't shift left."

> "The easy review at the end is only easy because the hard review at the start was good."

> "Any time you find yourself editing or 'bullying' the output for a better answer, that's a rule you can codify once and stop bullying forever."

> "Refuse to edit an AI output manually or in a way that doesn't feed into learnings for next time."

> "AI multiplies what you already do well and whatever your org already enables. If your practice is loose, AI compounds the looseness. If your org runs on handoffs, AI accelerates the frequency of handoffs."
