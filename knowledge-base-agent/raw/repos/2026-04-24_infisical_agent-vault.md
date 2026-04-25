---
type: raw
source_type: repo
source_url: https://github.com/Infisical/agent-vault
date_ingested: 2026-04-24
tags: [#coding, #security]
status: processed
processed_date: 2026-04-25
---
# Infisical/agent-vault

## Tóm tắt

**Agent Vault** là một **HTTP credential proxy và vault** mã nguồn mở từ Infisical — đóng vai trò trung gian giữa AI agents và các API chúng gọi.

**Vấn đề:** AI agents là hệ thống non-deterministic, dễ bị prompt injection lừa đảo → có thể leak secrets. Cách quản lý secrets truyền thống (trả credentials về cho caller) không an toàn với agents.

**Giải pháp:** Agent Vault **không bao giờ reveal credentials cho agents**. Thay vào đó, agents route HTTP requests qua local proxy → proxy inject credentials ở network layer → credentials không bao giờ được trả về cho agent.

## Tính năng chính

- **Brokered access, not retrieval** — agent được scoped session + `HTTPS_PROXY`, gọi API bình thường, vault inject credential ngầm
- **Works with any agent** — Claude Code, Cursor, Codex, OpenClaw, v.v.
- **Encrypted at rest** — AES-256-GCM, optional master password với Argon2id, passwordless mode cho PaaS
- **Request logs** — log mọi request với method, host, path, status, latency, credential key names

## Cài đặt

```bash
# Script (macOS/Linux)
curl -fsSL https://get.agent-vault.dev | sh
agent-vault server -d

# Docker
docker run -it -p 14321:14321 -p 14322:14322 -v agent-vault-data:/data infisical/agent-vault
```

Server chạy HTTP API port `14321` + TLS-encrypted HTTPS proxy port `14322`.

## Cách hoạt động với agents

**CLI cho local agents:**
```bash
agent-vault run -- claude
agent-vault run --sandbox=container --share-agent-dir -- claude
```

**SDK cho sandboxed agents (Docker, Daytona, E2B):**
```bash
npm install @infisical/agent-vault-sdk
```

Agent bên trong container chỉ cần gọi `fetch("https://api.github.com/...")` — không cần SDK, không cần credentials. Vault inject tự động.

## Bảo mật

- MIT license, `ee/` directory chứa enterprise features riêng
- Đang active development, API có thể thay đổi
- Nên đọc security docs trước khi deploy

## Tech stack

- Go backend
- Node.js + TypeScript SDK
- Vite frontend
- MIT License