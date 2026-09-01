---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, hack]
topic: ai-cybersecurity-skills-library
sources:
  - "[[src_anthropic-cybersecurity-skills]]"
last_updated: 2026-08-31
---

# Cybersecurity Skills Library

## Definition

Cybersecurity skills library là tập hợp các skills có cấu trúc, mã hóa quy trình làm việc của senior security analyst để AI agents có thể thực thi — khác với wordlists, payloads hay exploit code. Anthropic Cybersecurity Skills là ví dụ lớn nhất: 818 skills, 34 domains, mapping 6 industry frameworks (MITRE ATT&CK, NIST CSF 2.0, ATLAS, D3FEND, NIST AI RMF, MITRE F3). Mỗi skill theo agentskills.io standard với frontmatter YAML, Markdown structured execution, và reference files, giúp agent scan nhanh và load sâu theo nhu cầu. Mục tiêu: thu hẹp khoảng trống 4.8M unfilled roles bằng cách cho AI agents structured domain knowledge thay vì chỉ khả năng viết code và tìm web.

## Key ideas

- **34 domains phủ rộng:** Cloud, SOC, Threat Hunting, Digital Forensics, Malware Analysis, Red Teaming, AI Security, Ransomware, Supply Chain...
- **6-framework mapping:** Mỗi skill map tới framework phù hợp — ATT&CK + CSF near-universal, ATLAS/AI RMF cho AI-security skills
- **MITRE F3 (2026):** Fight Fraud Framework — Positioning (FA0001) + Monetization (FA0002), lấp khoảng trống ATT&CK sau initial compromise
- **Progressive disclosure:** ~30 tokens scan frontmatter, 500–2000 tokens load full — scan 818 skills trong 1 pass
- **Skill anatomy:** SKILL.md + references/standards + references/workflows + scripts/ + assets/template
- **Workflow sections:** When to Use · Prerequisites · Workflow · Verification — playbook thực thi có thể kiểm chứng
- **Sử dụng hợp pháp:** Bao gồm kỹ thuật offensive/dual-use, chỉ dành cho authorized testing, research, defense, education
- **Community-driven:** Grows qua contribution, license Apache-2.0, không affiliated với Anthropic

## Related concepts

- [[ai-security-tools]]
- [[agent-skill-management]]
- [[progressive-disclosure]]
- [[responsible-ai-security-research]]

## Sources

- [[src_anthropic-cybersecurity-skills]]
