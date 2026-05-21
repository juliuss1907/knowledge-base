---
type: concept
status: draft
main_tag: tech
sub_tags: [hack, tools]
topic: github-supply-chain-attack-vs-code
sources:
  - [[wiki/sources/src_11-minutes-hack-github.md]]
last_updated: 2026-05-21
---

# Supply Chain Attack

## Definition

Supply chain attack là hình thức tấn công mà kẻ xâm nhập target không trực tiếp, mà thông qua các bên thứ ba đáng tin cậy trong chuỗi cung ứng — như software vendors, package repositories, hoặc development tools. Thay vì hack 1,000 targets, attacker chỉ cần compromise 1 tool mà millions dev tin dùng.

## Key ideas

- **Nguyên lý:** Compromise 1 node trong supply chain → inherit access to everything downstream
- **Mục tiêu phổ biến:** Package managers (npm, PyPI), IDE extensions (VS Code), security scanners, CI/CD pipelines
- **Ví dụ điển hình:**
  - GitHub breach qua VS Code NX Console extension (May 2026)
  - TeamPCP: Trivy, Kics, Bitwarden/cli, SAP packages, TanStack
- **Tại sao nguy hiểm:**
  - Trusted by default: Dev không audit code của tools họ dùng hàng ngày
  - Wide blast radius: 1 compromise → millions affected
  - Hard to detect: Payload nằm trong trusted tool
- **Defense:** Pin dependencies, audit suppliers, zero-trust architecture, rapid rotation

## Related concepts

- [[vs-code-marketplace-security]]
- [[team-pcp-hacker-group]]

## Sources

- [[wiki/sources/src_11-minutes-hack-github.md]]

## Notes