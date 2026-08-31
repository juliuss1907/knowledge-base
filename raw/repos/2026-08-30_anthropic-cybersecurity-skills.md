---
type: repo
title: Anthropic Cybersecurity Skills — 818 structured cybersecurity skills for AI agents
url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
author: mukul975
date_published: [unknown]
date_ingested: 2026-08-30
status: processed
compiled_at: 2026-08-31
compiled_to: "[[src_anthropic-cybersecurity-skills]]"
source: github.com
language: Python
stars: 31648
license: Apache-2.0
homepage: https://mahipal.engineer/Anthropic-Cybersecurity-Skills/
---

# Anthropic Cybersecurity Skills

The largest open-source cybersecurity skills library for AI agents.

**818 production-grade cybersecurity skills · 34 security domains · 6 framework mappings · 26+ AI platforms**

> ⚠️ **Community Project** — independent, community-created project. Not affiliated with Anthropic PBC.
>
> 🔐 **Authorized & lawful use only.** Includes offensive and dual-use techniques (red-team C2, phishing simulation, exploitation) intended for **authorized penetration testing, security research, defense, and education**. Use only against systems you own or have explicit written permission to test. See [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Give any AI agent the security skills of a senior analyst

A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't — unless you give it these skills.**

This repo contains **818 structured cybersecurity skills** spanning **34 security domains**, each following the [agentskills.io](https://agentskills.io) open standard. The library maps across **six industry frameworks** — MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, NIST AI RMF, and the MITRE Fight Fraud Framework (F3) — with each skill mapped to the frameworks relevant to its type (a forensics skill carries ATT&CK + CSF; an AI-security skill adds ATLAS and AI RMF). Clone it, point your agent at it, and your next security investigation gets expert-level guidance in seconds.

## Six frameworks, one skill library

Each skill maps to the frameworks that fit its subject — ATT&CK and NIST CSF are near-universal, while ATLAS, AI RMF, D3FEND, and F3 apply where they're relevant. **Framework coverage across the 817 skills:** MITRE ATT&CK **805** · NIST CSF 2.0 **804** · MITRE D3FEND **139** · NIST AI RMF **97** · MITRE F3 **94** · MITRE ATLAS **93**.

| Framework | Version | Framework scope | What it maps |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org) | v19.1 | 15 tactics · Enterprise/Mobile/ICS | Adversary behaviors and TTPs |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | 2.0 | 6 functions · 22 categories · 106 subcategories | Organizational security posture |
| [MITRE ATLAS](https://atlas.mitre.org) | 2026.07 | 101 techniques · 77 sub-techniques | AI/ML adversarial threats |
| [MITRE D3FEND](https://d3fend.mitre.org) | v1.4.0 | 270 techniques | Defensive countermeasures |
| [NIST AI RMF](https://airc.nist.gov/AI_RMF) | 1.0 | 4 functions (Govern/Map/Measure/Manage) | AI risk management |
| [MITRE F3 (Fight Fraud Framework)](https://ctid.mitre.org/fraud/) | v1.1 (2026-04-09) | 8 tactics · 123 techniques · 94 fraud-relevant skills | Cyber-enabled financial fraud TTPs |

### 🆕 MITRE Fight Fraud Framework (F3) — 94 fraud-relevant skills

The **MITRE Fight Fraud Framework (F3)** was released **April 9, 2026** by MITRE's Center for Threat-Informed Defense (CTID), co-developed with JPMorganChase, Citigroup, Lloyds Banking Group, Standard Chartered, CrowdStrike, Verizon Business, FS-ISAC, and others. It is an ATT&CK-compatible TTP catalog for **cyber-enabled financial fraud** — filling the gap ATT&CK leaves after initial compromise.

F3 v1.1 adds **two fraud-specific tactics** that ATT&CK does not enumerate:
- **Positioning** (`FA0001`) — actions taken after access to collect/manipulate data and prepare the fraud (synthetic-identity seeding, account warming, beneficiary setup, SIM-swap pre-positioning, banking-session hijack).
- **Monetization** (`FA0002`) — converting stolen assets into usable funds (money-mule layering, APP fraud, crypto off-ramping, card cash-out, refund/chargeback abuse).

Fraud-specific techniques use `F1XXX` IDs (e.g. `F1005.003` Add Beneficiary, `F1025.003` Wire Transfer, `F1007` Adversary-in-the-Browser); reused ATT&CK techniques keep their `T1XXX` IDs.

### MITRE ATT&CK v19.1 — 805/817 skills mapped

Every skill carries a `mitre_attack` frontmatter list validated against **MITRE ATT&CK v19.1** (latest release) using the official `mitreattack-python` library — 290 distinct techniques and sub-techniques (146 base + 144 sub) across Enterprise, ICS, and Mobile. Zero revoked or deprecated IDs. v19.1's restructured Defense Evasion (now split into **Stealth** and **Defense Impairment**) is reflected.

## Quick start

```bash
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

Works immediately with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any agentskills.io-compatible platform.

## Why this exists

The cybersecurity workforce gap hit **4.8 million unfilled roles** globally in 2024 (ISC2). AI agents can help close that gap — but only if they have structured domain knowledge to work from. Today's agents can write code and search the web, but they lack the practitioner playbooks that turn a generic LLM into a capable security analyst.

Existing security tool repos give you wordlists, payloads, or exploit code. None of them give an AI agent the structured decision-making workflow a senior analyst follows: when to use each technique, what prerequisites to check, how to execute step-by-step, and how to verify results. That is the gap this project fills.

**Anthropic Cybersecurity Skills** is not a collection of scripts or checklists. It is an **AI-native knowledge base** built from the ground up for the agentskills.io standard — YAML frontmatter for sub-second discovery, structured Markdown for step-by-step execution, and reference files for deep technical context. Every skill encodes real practitioner workflows, not generated summaries.

## What's inside — 34 security domains

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 66 | AWS, Azure, GCP hardening · CSPM · cloud attack emulation · cloud forensics |
| SOC Operations | 63 | Playbooks · escalation workflows · Graph-log detection · tabletop exercises |
| Threat Hunting | 58 | Hypothesis-driven hunts · LOTL detection · EVTX hunting · fleet hunting |
| Threat Intelligence | 52 | STIX/TAXII · MISP · OpenCTI · feed integration · actor profiling |
| Web Application Security | 46 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Network Security | 43 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Digital Forensics | 41 | Disk imaging · memory forensics · Hayabusa/KAPE/Plaso timelines |
| Identity & Access Management | 40 | Entra ID/ROADtools · device-code phishing · PAM · zero trust identity |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Red Teaming | 35 | ADCS/Certipy · BloodHound CE · Sliver/Havoc C2 · NTLM relay |
| Container Security | 33 | K8s RBAC · image scanning · Falco · container escape |
| OT/ICS Security | 29 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Incident Response | 26 | Breach containment · ransomware response · IR playbooks |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Penetration Testing | 23 | Network · web · cloud · mobile · NetExec lateral movement |
| DevSecOps | 18 | CI/CD security · Trivy IaC/image scanning · code signing |
| Zero Trust Architecture | 18 | BeyondCorp · CISA maturity model · microsegmentation |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |
| Cryptography | 16 | TLS · Ed25519 · post-quantum migration · key management |
| AI Security | 14 | LLM red-teaming (garak/PyRIT) · prompt injection · MCP/agentic security · guardrails |
| Mobile Security | 13 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 13 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 10 | NIST 800-30/RMF · CMMC · HIPAA · TPRM · CIS benchmarks |
| Supply Chain Security | 8 | SBOMs · dependency confusion · malicious-package triage · SLSA/Sigstore |
| Threat Detection | 7 | Credential dumping · golden-ticket forgery · pass-the-ticket · LOLBAS · UEBA insider signals |
| Hardware & Firmware Security | 6 | CHIPSEC/UEFI audit · Secure Boot bypass · TPM attestation · bootkit hunting |
| Deception Technology | 6 | Honeytokens · canarytokens · breach detection |
| Blockchain Security | 2 | Ethereum smart-contract vulnerabilities · Foundry audit workflows |
| Wireless Security | 2 | Bluetooth Low Energy attack detection · BLE security assessment |
| Privacy Compliance | 2 | GDPR data-subject access requests · privacy impact assessments |
| Data Protection | 1 | Data loss prevention with Microsoft Purview |
| Purple Team | 1 | Atomic Red Team purple-team testing |

*817 skills across 34 domains. Counts come from the `subdomain` field in each skill's frontmatter.*

## How AI agents use these skills

Each skill costs **~30 tokens to scan** (frontmatter only) and **500–2,000 tokens to fully load** (complete workflow). This progressive disclosure architecture lets agents search all 818 skills in a single pass without blowing context windows.

```
User prompt: "Analyze this memory dump for signs of credential theft"

Agent's internal process:

  1. Scans 818 skill frontmatters (~30 tokens each)
     → identifies 12 relevant skills by matching tags, description, domain

  2. Loads top 3 matches:
     • performing-memory-forensics-with-volatility3
     • hunting-for-credential-dumping-lsass
     • analyzing-windows-event-logs-for-credential-access

  3. Executes the structured Workflow section step-by-step
     → runs Volatility3 plugins, checks LSASS access patterns,
        correlates with event log evidence

  4. Validates results using the Verification section
     → confirms IOCs, maps findings to ATT&CK T1003 (Credential Dumping)
```

**Without these skills**, the agent guesses at tool commands and misses critical steps. **With them**, it follows the same playbook a senior DFIR analyst would use.

## Skill anatomy

Every skill follows a consistent directory structure:

```
skills/performing-memory-forensics-with-volatility3/
├── SKILL.md              ← Skill definition (YAML frontmatter + Markdown body)
├── references/
│   ├── standards.md      ← MITRE ATT&CK, ATLAS, D3FEND, NIST mappings
│   └── workflows.md      ← Deep technical procedure reference
├── scripts/
│   └── process.py        ← Working helper scripts
└── assets/
    └── template.md       ← Filled-in checklists and report templates
```

### YAML frontmatter (real example)

```yaml
---
name: performing-memory-forensics-with-volatility3
description: >-
  Analyze memory dumps to extract running processes, network connections,
  injected code, and malware artifacts using the Volatility3 framework.
domain: cybersecurity
subdomain: digital-forensics
tags: [forensics, memory-analysis, volatility3, incident-response, dfir]
atlas_techniques: [AML.T0047]
d3fend_techniques: [D3-MA, D3-PSMD]
nist_ai_rmf: [MEASURE-2.6]
nist_csf: [DE.CM-01, RS.AN-03]
version: "1.2"
author: mukul975
license: Apache-2.0
---
```

### Markdown body sections

```markdown
## When to Use
Trigger conditions — when should an AI agent activate this skill?

## Prerequisites
Required tools, access levels, and environment setup.

## Workflow
Step-by-step execution guide with specific commands and decision points.

## Verification
How to confirm the skill was executed successfully.
```

Frontmatter fields: `name` (kebab-case, 1–64 chars), `description` (keyword-rich for agent discovery), `domain`, `subdomain`, `tags`, `atlas_techniques` (MITRE ATLAS IDs), `d3fend_techniques` (MITRE D3FEND IDs), `nist_ai_rmf` (NIST AI RMF references), `nist_csf` (NIST CSF 2.0 categories). MITRE ATT&CK technique mappings are documented in each skill's `references/standards.md` file and in the ATT&CK Navigator layer included with releases.

## Compatible platforms

**AI code assistants:** Claude Code (Anthropic) · GitHub Copilot (Microsoft) · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · Tabnine · Sourcegraph Cody · JetBrains AI

**CLI agents:** OpenAI Codex CLI · Gemini CLI (Google)

**Autonomous agents:** Devin · Replit Agent · SWE-agent · OpenHands

**Agent frameworks & SDKs:** LangChain · CrewAI · AutoGen · Semantic Kernel · Haystack · Vercel AI SDK · Any MCP-compatible agent

All platforms that support the [agentskills.io](https://agentskills.io) standard can load these skills with zero configuration.

## Releases

| Version | Date | Highlights |
|---|---|---|
| [v1.0.0](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) | March 11, 2026 | 734 skills · 26 domains · MITRE ATT&CK + NIST CSF 2.0 mapping · ATT&CK Navigator layer |

Skills have continued to grow on `main` since v1.0.0 — the library now contains **818 skills** with **6-framework mapping** (MITRE ATLAS, D3FEND, NIST AI RMF, and the MITRE Fight Fraud Framework added post-release). Check [Releases](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases) for the latest tagged version.

## Contributing

This project grows through community contributions. Add a new skill (read SCOPE.md first, then the template in CONTRIBUTING.md) — the thinnest domains are the ones most worth adding to. Submit one skill per PR. Improve existing skills, report issues.

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/).
