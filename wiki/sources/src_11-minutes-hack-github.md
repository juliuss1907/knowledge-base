---
type: source
original: "[[raw/posts/2026-05-20_the-smart-ape-11-minutes-hack-github.md]]"
main_tag: tech
sub_tags: [hack, tools, news]
topic: github-supply-chain-attack-vs-code
date_ingested: 2026-05-20
date_compiled: 2026-05-21
url: https://x.com/i/status/2056983617302122740
author: The Smart Ape (@the_smart_ape)
---

# 11 minutes was all it took to hack github

## Metadata

- **Author:** The Smart Ape (@the_smart_ape)
- **Published:** 2026-05-20
- **Source:** X / Twitter
- **URL:** https://x.com/i/status/2056983617302122740
- **Type:** post

## Summary

GitHub thông báo ~3,800 internal repos bị đánh cắp thông qua supply chain attack tinh vi qua VS Code extension "NX Console". Extension độc hại tồn tại chỉ 11 phút trên marketplace nhưng lây nhiễm vào laptop một GitHub employee, từ đó đánh cắp toàn bộ internal repos. Thủ phạm TeamPCP đang rao bán dữ liệu với giá $50,000. Đây là ví dụ điển hình cho rủi ro bảo mật nghiêm trọng của VS Code Marketplace — nơi malware tăng 4x trong năm 2025.

## Key points

- **3,800 internal repos** của GitHub bị đánh cắp qua VS Code extension độc hại
- Extension **"NX Console"** (nrwl.angular-console) bị compromise chỉ tồn tại **11 phút** trên marketplace
- **2.2 triệu lượt** cài đặt toàn cầu của extension gốc → attack surface khổng lồ
- TeamPCP sử dụng **orphan commit** (commit ẩn) để inject payload 498KB obfuscated code
- Payload đánh cắp: GitHub tokens, npm tokens, AWS credentials, HashiCorp Vault, Kubernetes secrets, 1Password vault
- Exfiltration qua 3 kênh: HTTPS, GitHub API, DNS tunneling
- **Persistent backdoor** trên macOS nhận lệnh qua GitHub Search API "dead drop"
- Malware VS Code tăng **4x trong 2025** (27 năm 2024 → 105 trong 10 tháng 2025)
- **550+ secrets plaintext** trong 500+ extensions — Microsoft không review updates của popular extensions
- **Thủ phạm TeamPCP:** 300+ GB dữ liệu, 500,000 credentials trong 6 tháng; mục tiêu security tools và developer infrastructure
- Các mục tiêu trước: Trivy, Kics, Fake Bitwarden/cli, SAP packages, TanStack

## Concepts referenced

- [[supply-chain-attack]]
- [[vs-code-marketplace-security]]
- [[team-pcp-hacker-group]]
- [[orphan-commit-attack]]
- [[dns-tunneling]]
- [[dead-drop-communication]]
- [[github-security]]

## Original excerpts

> *"Bạn click 'install' và trao cho người lạ quyền truy cập full máy: tokens, secrets, shell history, everything. Cài program unsigned năm 2005 còn có friction hơn thế này."*