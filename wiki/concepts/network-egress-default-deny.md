---
type: concept
status: draft
main_tag: system
sub_tags: [automation, hack]
topic: network-egress-default-deny
sources:
  - "[[src_google-cloud-agent-sandbox-runtimes]]"
last_updated: 2026-09-02
---

# Network Egress Default Deny

## Definition

Network egress default deny là nguyên tắc bảo mật cho agent sandbox runtimes: mọi outbound network traffic từ sandbox execution environment phải bị chặn mặc định, chỉ cho phép qua explicit domain/IP allowlist. Đây là biện pháp phòng thủ quan trọng nhất với autonomous agents vì prompt injection attack không cần kernel escape — chỉ cần unrestricted HTTP requests là đủ để exfiltrate data hoặc đánh cắp credentials.

## Key ideas

- **Egress lớn hơn hypervisor như attack surface:** Security engineers thường dành 90% thời gian audit hypervisor boundaries và 10% cho networking — với AI agents, tỷ lệ này cần đảo ngược. Một attacker chỉ cần prompt injection + unrestricted outbound, không cần hypervisor escape.
- **Các nguy cơ cụ thể khi egress không được kiểm soát:** Exfiltrate sensitive files, query internal cloud metadata services (169.254.169.254), steal ambient IAM credentials — tất cả bằng standard HTTP requests không cần exploit nào.
- **Ambient credentials phải bị strip:** Sandbox process không được inherit parent environment variables, secret tokens, hoặc access đến instance metadata endpoints. Nếu agent cần call external APIs, requests phải route qua identity-aware gateway (Agent Gateway) xác minh token bên ngoài sandbox boundary.
- **Implementations cụ thể:** Apply default-deny firewall rule trên mọi sandbox network bridge. Block link-local addresses (169.254.0.0/16). Yêu cầu explicit domain allowlists cho mọi tool call cần package downloads hoặc external API calls.
- **Defense-in-depth:** Hypervisor escape vẫn cần được phòng thủ, nhưng network controls cung cấp additional defense-in-depth layer ngăn lateral movement nếu escape xảy ra.

## Related concepts

- [[agent-sandbox-runtimes]] — sandbox environment where this applies
- [[isolation-spectrum]] — isolation tiers
- [[agent-defense-in-depth]] — multi-layer security
- [[prompt-injection]] — attack vector that exploits unrestricted egress

## Sources

- "[[src_google-cloud-agent-sandbox-runtimes]]"