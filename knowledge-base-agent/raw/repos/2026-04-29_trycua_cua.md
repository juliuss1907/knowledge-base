---
type: raw
source_type: repo
source_url: https://github.com/trycua/cua
date_ingested: 2026-04-29
tags: [#ai, #coding]
status: processed
processed_date: 2026-05-01
---
# CUA — Computer-Use Agents Infrastructure
## trycua

**Link:** https://github.com/trycua/cua
**Stars:** 14.9k
**Commits:** 3,199
**Website:** cua.ai

---

## Tóm tắt

Open-source infrastructure cho Computer-Use Agents — sandbox environments, SDKs, và benchmarks để train/evaluate AI agents có thể điều khiển toàn bộ desktop (macOS, Linux, Windows).

---

## Các thành phần chính

### SDK Interfaces
Standardized interfaces cho agent tương tác với desktop:
- **Shell** — execute commands
- **Mouse** — control cursor, click
- **Keyboard** — type, shortcuts
- **Screen** — capture/analyze screen
- **Clipboard** — copy/paste
- **Tunnel** — network tunneling
- **Terminal** — terminal access
- **Window** — window management
- **Mobile** — mobile device control

### Sandbox Runtimes
- **DockerRuntime** — Linux containers
- **QEMURuntime** — VMs (Linux, Windows, macOS)
- **LumeRuntime**
- **AndroidEmulatorRuntime**
- **HyperVRuntime** — Windows Hyper-V

### Hardware Acceleration
- **macOS:** HVF (Intel), TCG (Apple Silicon)
- **Linux:** KVM, HVF
- **Windows:** Hyper-V

### Image Builder
Agent install packages trên guest OS:
- Linux: apt, apk
- macOS: brew
- Windows: choco, winget
- Python: pip, uv
- PWA install

### Benchmark
- **WinArena** — benchmark cho Windows agents
- 117 integration tests cho interfaces
- 37 tests cho image builder

---

## Đáng chú ý

- Cross-platform: macOS + Linux + Windows
- Tự detect hardware acceleration phù hợp
- Maintain bởi Anthropic (nhiều commits từ Claude Sonnet 4.6)
- GitHub Copilot CLI MCP integration
- Auto-generate interface docs từ pydocstrings

---

## Công nghệ

- Python (SDK chính)
- Swift (cua-driver cho macOS)
- Rust (performance-critical components)
- Pytest cho tests

---

## Liên quan

- Claude Computer Use (tương tự nhưng closed source)
- Computer Use benchmarks (WinArena)
- Agent sandboxing infrastructure