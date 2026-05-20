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

# Consent Phishing

## Definition

Consent phishing là kỹ thuật tấn công trong đó attacker không cố gắng authenticate (đánh cắp credentials) mà thay vào đó ask for authorization — yêu cầu người dùng cấp quyền truy cập cho ứng dụng độc hại thông qua real OAuth consent screen của nhà cung cấp dịch vụ (Google, Microsoft).

## Key ideas

- **Authorization vs Authentication:** Attacker không cần biết password — chỉ cần user tap "Allow" trên real consent screen
- **Real Google consent screen:** Attacker tạo app OAuth hợp lệ, consent screen là thật từ Google
- **Bypasses 2FA:** Vì đây là authorization flow hợp lệ, 2FA không ngăn được
- **Long-lived access:** Token valid for months, attacker có persistent access
- **31% Microsoft 365 breaches 2025** là do token theft/consent phishing
- **Social engineering:** App có tên giả mạo dịch vụ hợp lệ, yêu cầu quyền hợp lý-sounding

## Related concepts

- [[oauth-security-risks]]
- [[token-theft-attack]]

## Sources

- [[wiki/sources/src_dont-sign-in-with-google.md]]

## Notes

