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

# VS Code Marketplace Security

## Definition

VS Code Marketplace là nền tảng phân phối extensions cho VS Code — nhưng cũng là "Wild West" về bảo mật. Malware trong extensions tăng 4x trong 2025, Microsoft không review updates của popular extensions, và 550+ secrets tìm thấy plaintext trong 500+ extensions.

## Key ideas

- **Malware detections:**
  - 2024: 27 cases
  - First 10 months 2025: **105 cases** (4x increase)
- **Secrets exposure:** 550+ secrets tìm thấy plaintext trong 500+ extensions
- **No update review:** Microsoft không review updates của popular extensions
- **Attack vector:** Extension có auto-update bật → malicious update được cài tự động
- **Ví dụ GitHub breach:** Extension "NX Console" (nrwl.angular-console) bị compromise, tồn tại 11 phút trên marketplace, lây nhiễm vào laptop GitHub employee
- **Rủi ro:** Extensions có full access vào workspace: tokens, secrets, shell history, everything
- **Giải pháp đề xuất:** Audit extensions, disable auto-update, review permissions, rotate credentials regularly

## Related concepts

- [[supply-chain-attack]]
- [[team-pcp-hacker-group]]

## Sources

- [[wiki/sources/src_11-minutes-hack-github.md]]

## Notes