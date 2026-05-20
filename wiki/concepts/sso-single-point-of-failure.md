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

# SSO Single Point of Failure

## Definition

Single Sign-On (SSO) cho phép người dùng đăng nhập một lần vào nhà cung cấp danh tính (identity provider) như Google, sau đó truy cập nhiều dịch vụ. Tuy nhiên, điều này tạo ra điểm chết tập trung — khi tài khoản identity provider bị mất, mất truy cập vào toàn bộ hệ sinh thái dịch vụ phụ thuộc.

## Key ideas

- **Concentrated risk:** Mất một tài khoản Google = mất Gmail, YouTube, Drive, và tất cả các dịch vụ liên kết (Notion, Figma, Linear, Vercel, Stripe, SaaS...)
- **No SLA or contract:** Không có hợp đồng, SLA, hay kênh pháp lý để kháng cáo — chỉ có form được xử lý bởi model
- **Recovery nightmare:** Không có người hỗ trợ thực sự, không có cách appeal hiệu quả khi account bị suspended
- **False security:** SSO không an toàn hơn password manager + unique alias + hardware 2FA — chỉ tiện hơn
- **The 30-day rule:** Nếu mất truy cập dịch vụ trong 30 ngày gây thiệt hại cho công việc hoặc tài chính → không nên dùng SSO

## Related concepts

- [[oauth-security-risks]]
- [[token-theft-attack]]

## Sources

- [[wiki/sources/src_dont-sign-in-with-google.md]]

## Notes

