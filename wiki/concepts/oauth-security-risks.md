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

# OAuth Security Risks

## Definition

OAuth là giao thức ủy quyền phổ biến cho phép người dùng đăng nhập vào ứng dụng thứ ba thông qua tài khoản của nhà cung cấp dịch vụ (như Google, Microsoft) mà không cần chia sẻ mật khẩu. Tuy nhiên, việc lạm dụng OAuth tạo ra nhiều vector tấn công và rủi ro tập trung (single point of failure) cho cả người dùng và doanh nghiệp.

## Key ideas

- **Authorization ≠ Authentication:** OAuth ủy quyền truy cập, không xác thực danh tính — attacker có thể lợi dụng sự nhầm lẫn này
- **Refresh token persistence:** Token có thể valid for months, reset password không revoke được
- **Token theft:** Malware (Lumma, Rhadamanthys) sử dụng `multilogin` endpoint để steal refresh token và regenerate session cookies
- **Consent phishing:** Attacker tạo app OAuth hợp lệ, hiển thị real Google consent screen — user tap "Allow" là attacker có token
- **31% Microsoft 365 breaches 2025** là do token theft, Salesforce/Google Workspace tokens cũng bị harvest

## Related concepts

- [[token-theft-attack]]
- [[consent-phishing]]
- [[sso-single-point-of-failure]]

## Sources

- [[wiki/sources/src_dont-sign-in-with-google.md]]

## Notes

