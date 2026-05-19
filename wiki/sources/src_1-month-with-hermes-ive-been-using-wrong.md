---
type: source
original: raw/articles/2026-05-18_1-month-with-hermes-ive-been-using-wrong.md
main_tag: ai
sub_tags: [tools, automation, opinion]
topic: hermes-operator-builder-pattern
date_compiled: 2026-05-19
url: https://defi0xjeff.substack.com/p/1-month-with-hermes-ive-been-using
author: defi0xjeff
---

# 1 Month with Hermes — I've Been Using Hermes Wrong All Along

## Metadata

- **Source type:** Article
- **Published:** 2026-05-18
- **Author:** defi0xjeff
- **URL:** https://defi0xjeff.substack.com/p/1-month-with-hermes-ive-been-using
- **Type:** Article

## Summary

Sau 1 tháng sử dụng Hermes, tác giả nhận ra đã dùng sai cách — Hermes không phải "builder" mà là "operator". Bài viết chia sẻ cách phân chia vai trò giữa Claude (builder) và Hermes (operator) để tối ưu workflow, cùng các ví dụ thực tế như PolyBond prediction market dashboard và Bangkok activities tracker.

## Key points

- **Hermes là Operator, không phải Builder**: Hermes phù hợp cho recurring tasks, automated reports, và analysis — không phải building UI/dashboard
- **Phân chia vai trò rõ ràng**: Claude = Builder (xây dựng dashboard, UI, features one-time), Hermes = Operator (deliver reports, analyze data, recurring jobs)
- **Hermes có persistent memory + self-learning loop**: Tự động setup skills nếu thấy cần, giảm thời gian task lần sau
- **Ví dụ thực tế PolyBond**: Claude xây prediction market dashboard nhanh gấp 10x, Hermes chạy định kỳ analyze và deliver brief report
- **Health check quan trọng**: Implement health check để detect bugs trước cron jobs
- **Phải specific khi delegate**: "remember", "make sure to adjust [x] cron job" cần instruction rõ ràng
- **Dashboard building vẫn cần human oversight**: Data "premium"/hữu ích thường tốn tiền, không phải AI-only

## Concepts referenced

- [[hermes-operator-role]]
- [[claude-builder-role]]
- [[ai-tool-role-separation]]
- [[prediction-market-dashboard]]
- [[persistent-memory-ai]]

## Original excerpts

> "You have to steer the AI. Not let it steer you."
> "Use the AI to augment learning. Not the other way around."
