---
type: concept
status: draft
main_tag: tech
sub_tags: [hack, tools]
topic: sso-security-risks
sources:
  - [[wiki/sources/src_dont-sign-in-with-google.md]]
last_updated: 2026-05-20
---

# Token Theft Attack

## Definition

Token theft là kỹ thuật tấn công trong đó malware đánh cắp OAuth refresh token từ thiết bị nạn nhân. Attacker sau đó dùng token này để regenerate session cookies và duy trì truy cập vào tài khoản — ngay cả khi nạn nhân reset password.

## Key ideas

- **Multilogin endpoint:** Malware (Lumma, Rhadamanthys) sử dụng `multilogin` OAuth endpoint để steal refresh token
- **Bypass password reset:** Reset password không stop được attacker vì token vẫn valid
- **Session regeneration:** Attacker dùng stolen refresh token để tạo session cookies mới
- **Long-lived tokens:** Token có thể valid for months, tạo persistence cho attacker
- **31% Microsoft 365 breaches 2025** là do token theft
- **Salesforce/Google Workspace tokens** cũng bị harvest tương tự

## Related concepts

- [[oauth-security-risks]]
- [[consent-phishing]]

## Sources

- [[wiki/sources/src_dont-sign-in-with-google.md]]

## Notes

