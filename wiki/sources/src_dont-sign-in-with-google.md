---
type: source
original: "[[raw/posts/2026-05-19_dont-sign-in-with-google.md]]"
main_tag: tech
sub_tags: [hack, tools, opinion]
topic: sso-security-risks
date_ingested: 2026-05-19
date_compiled: 2026-05-20
url: https://x.com/the_smart_ape/status/2055941633179283523
author: The Smart Ape (@the_smart_ape)
---

# Don't Sign In With Google

## Metadata

- **Author:** The Smart Ape (@the_smart_ape)
- **Published:** 2026-05-19
- **Source:** X/Twitter
- **URL:** https://x.com/the_smart_ape/status/2055941633179283523
- **Type:** post

## Summary

Bài viết cảnh báo về rủi ro của việc sử dụng "Sign in with Google" cho các dịch vụ quan trọng. Một người bạn của tác giả đã mất toàn bộ SaaS 3 năm tuổi chỉ vì tài khoản Google bị suspended mà không rõ lý do, không thể đăng nhập vào Notion, Figma, Linear, Vercel, Stripe. Tác giả phân tích 7 vấn đề chính của SSO và đưa ra khuyến nghị: nếu mất truy cập dịch vụ trong 30 ngày sẽ gây thiệt hại cho công việc hoặc tài chính, không nên dùng SSO.

## Key points

- **Single point of failure:** Khi tài khoản Google bị suspended, mất truy cập vào tất cả các dịch vụ liên kết (Gmail 8 năm, YouTube, Drive, SaaS 3 năm tuổi, Notion, Figma, Vercel, Stripe...)
- **Không có kênh appeal:** Không có hợp đồng, SLA, hay tòa án để kháng cáo — chỉ có form được xử lý bởi model
- **SSO không an toàn hơn password:** Risk tập trung (mất là mất tất cả) thay vì phân tán
- **Domain ownership change vulnerability:** Attacker mua domain startup đã chết, recreate email cũ, vào được Slack/Notion với data cũ — Google response "won't fix"
- **Token theft bypass password reset:** Malware dùng `multilogin` OAuth endpoint để steal refresh token, reset password không stop được
- **Consent phishing bypasses 2FA:** Attacker không authenticate mà ask for authorization qua real Google consent screen, token valid for months
- **Tracking:** "Sign in with Google" button là Google-hosted script, Google thấy page load, referrer, user agent, identity — không cần click
- **No email alias:** Không có tính năng Hide My Email như Apple, email chính đi đến mọi app
- **Recommendation:** Nếu mất truy cập 30 ngày gây thiệt hại → tạo account riêng, dùng password manager + alias email + hardware 2FA

## Concepts referenced

- [[oauth-security-risks]]
- [[sso-single-point-of-failure]]
- [[token-theft-attack]]
- [[consent-phishing]]
- [[domain-takeover-vulnerability]]

## Original excerpts

> *"If losing access to this service for 30 days would damage your work or your money, do not use SSO."*

**Domain takeover:**
> *"Startup chết → domain bán $12 → attacker mua, tạo Google Workspace → Recreate old employee emails → click 'Sign in with Google' → vào được Slack, Notion với data cũ"*

**Consent phishing:**
> *"Attacker không authenticate — mà ask for authorization. Real Google consent screen → user tap 'Allow' → attacker có token valid months."*
