---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, coding]
topic: loop-engineering
sources:
  - "[[src_loop-engineering-14-step-roadmap]]"
last_updated: 2026-06-30
---

# Ralph Wiggum Loop

## Definition

Ralph Wiggum loop là một failure mode trong loop engineering, được đặt tên bởi engineer Geoffrey Huntley theo nhân vật Ralph Wiggum trong The Simpsons — người luôn tuyên bố "I'm done!" khi chưa thực sự hoàn thành. Trong ngữ cảnh loop, đây là tình huống agent phát ra completion token quá sớm, loop exit khi công việc mới làm một nửa, và tiếp tục đốt token mà không ai phát hiện vì không có objective gate.

## Key ideas

- Xảy ra khi loop không có real verifier — chỉ có một agent thứ hai "review" mà không có test/build/linter làm tín hiệu khách quan
- Soft completion conditions: "done" được định nghĩa bởi judgment của agent, không phải bởi test pass/fail
- Không có hard stop: loop tiếp tục chạy đến khi bị kill bởi yếu tố bên ngoài (rate limit, người dùng nhận ra)
- Cách fix: objective gate — test pass/fail, build compile/not, linter zero/non-zero, không phải opinion của verifier
- Liên quan đến self-preferential bias: agent viết code quá dễ dãi khi tự chấm bài

## Related concepts

- [[loop-engineering]]
- [[comprehension-debt]]
- [[cognitive-surrender]]

## Sources

- "[[src_loop-engineering-14-step-roadmap]]"

## Notes
