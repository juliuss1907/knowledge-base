---
type: concept
status: draft
main_tag: tech
sub_tags: [hack, news]
topic: github-supply-chain-attack-vs-code
sources:
  - [[wiki/sources/src_11-minutes-hack-github.md]]
last_updated: 2026-05-21
---

# TeamPCP (Hacker Group)

## Definition

TeamPCP là nhóm hacker chuyên supply chain compromise với các alias: deadcatx3, pcpcat, shellforce, cipherforce. Trong 6 tháng đã đánh cắp 300+ GB dữ liệu, 500,000 credentials, và liên tục tấn công security tools và developer infrastructure.

## Key ideas

- **Các alias:** deadcatx3, pcpcat, shellforce, cipherforce
- **Thành tích 6 tháng:** 300+ GB dữ liệu, 500,000 credentials
- **Mô hình:** Bán credential & supply chain compromise (thay vì ransomware)
- **Mục tiêu:** Security tools và developer infrastructure — compromise 1 tool millions dev tin → inherit access to everything
- **Timeline các vụ:**
  - **March:** Trivy, Kics (security scanners)
  - **April:** Fake Bitwarden/cli; SAP developer packages (570k weekly downloads)
  - **May 11:** TanStack (84 malicious versions, 42 npm packages)
  - **May 20:** GitHub trực tiếp (~3,800 internal repos)
- **Kỹ thuật:** Orphan commits, obfuscated payloads, multi-channel exfiltration, persistent backdoors, RSA-4096 signed commands

## Related concepts

- [[supply-chain-attack]]
- [[vs-code-marketplace-security]]
- [[orphan-commit-attack]]

## Sources

- [[wiki/sources/src_11-minutes-hack-github.md]]

## Notes