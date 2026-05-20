---
type: raw
source_type: post
source_url: https://x.com/the_smart_ape/status/2055941633179283523
date_ingested: 2026-05-19
status: processed
compiled_at: 2026-05-20
compiled_to: [[wiki/sources/src_dont-sign-in-with-google.md]]
---

# Don't Sign In With Google

**Tác giả:** The Smart Ape (@the_smart_ape)  
**Nguồn:** X/Twitter  
**Ngày đăng:** 2026-05-19

---

## Tóm tắt

Bài viết cảnh báo về rủi ro của "Sign in with Google" — một người bạn mất toàn bộ SaaS 3 năm tuổi chỉ vì tài khoản Google bị suspended mà không rõ lý do.

## Câu chuyện

**Người bạn bị mất:**
- 8 năm Gmail
- YouTube, Google Drive
- Play Store purchases
- SaaS 3 năm tuổi — vì mọi thứ dựa vào Google account
- Không thể đăng nhập Notion, Figma, Linear, Vercel, Stripe...
- Không rõ lý do, không có người hỗ trợ, không có cách appeal

## Vấn đề với "Sign in with Google"

### 1. Không phải tạo account — là "Google vouch for me"

- Không có contract, SLA, hay court để appeal
- Chỉ có form, và form được đọc bởi model

### 2. SSO không secure hơn password

**So sánh:**
| | Sign in with Google | Password manager + unique alias + hardware 2FA |
|---|---|---|
| Risk | Concentrated (lose everything) | Distributed (lose 1/20) |
| Security | ❌ | ✅ |
| Convenience | ✅ | ❌ |

### 3. Domain ownership change vulnerability

- Startup chết → domain bán $12 → attacker mua, tạo Google Workspace
- Recreate old employee emails → click "Sign in with Google" → vào được Slack, Notion với data cũ
- Google response: "won't fix" → chỉ reopen sau khi viral → bounty: $1,337

### 4. Token theft bypass password reset

- Malware (Lumma, Rhadamanthys) dùng `multilogin` OAuth endpoint
- Steal refresh token → regenerate session cookies
- Reset password không stop được

### 5. Consent phishing bypasses 2FA

- Attacker không authenticate — mà ask for authorization
- Real Google consent screen → user tap "Allow" → attacker có token valid months
- 31% Microsoft 365 breaches 2025 là token theft
- Salesforce/Google Workspace tokens cũng bị harvest

### 6. Tracking

- "Sign in with Google" button là Google-hosted script
- Google sees page load, referrer, user agent, identity
- Không cần click — chỉ cần load page

### 7. No email alias

- Apple "Sign in with Apple" có Hide My Email relay
- Google: real primary email đi đến mọi app
- Email là master key cho mọi password reset

## Recommendation

**Không phải "never use SSO" — mà là:**

> *"If losing access to this service for 30 days would damage your work or your money, do not use SSO."*

**Thay vào đó:**
- Create real account
- Use password manager
- Use alias email (Fastmail, Proton, Apple Relay)
- Set up 2FA với hardware key

**Audit ngay:**
- Mở myaccount.google.com/connections
- Revoke mọi app không nhận ra hoặc không dùng 6 tháng

---

## Tags gợi ý

- #security
- #business
- #opinion
