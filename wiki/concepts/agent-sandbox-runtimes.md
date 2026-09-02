---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, hack, system]
topic: agent-sandbox-runtimes
sources:
  - "[[src_google-cloud-agent-sandbox-runtimes]]"
last_updated: 2026-09-02
---

# Agent Sandbox Runtimes

## Definition

Agent sandbox runtimes là môi trường thực thi cô lập (isolated execution environment) cho LLM-generated code — nơi mã do AI sinh ra được chạy an toàn mà không gây hại cho hệ thống chủ. Khác với microservice hay batch job, agent sandbox phải xử lý đặc thù: agent dành ~95% thời gian chờ model reasoning, rồi bùng nổ trong micro-bursts thực thi, và cần giữ state giữa các interaction turns.

## Key ideas

- **Cold-start thực tế khác xa marketing:** Vendor benchmark đo trên empty loops (VMM boot stripped kernel ~150 ms), nhưng bootstrap real runtime (overlay filesystem + Python/Node + network + data libraries) mất 610 ms-2.3s tùy cấu hình, cộng thêm ~10s cho headless Chromium. Giải pháp là pre-warmed template pools.
- **Isolation spectrum là câu hỏi "code nào dùng chung với neighbor":** Từ shared-process (V8 isolates) đến shared-kernel (OCI containers) đến user-space kernel intercept (gVisor) đến hardware VM (Firecracker). Mỗi tầng đánh đổi giữa density, speed, và isolation strength.
- **Standard OCI container không an toàn multi-tenant:** Docker/Kubernetes Pod dùng chung host kernel — một kernel exploit (Dirty Pipe, Leaky Vessels) là đủ để chiếm toàn bộ host. Kubernetes documentation xác nhận: standard Pod không phải hard multi-tenant boundary.
- **Network egress > hypervisor security:** Prompt injection không cần kernel escape. Nếu sandbox có unrestricted outbound, agent có thể exfiltrate file, query cloud metadata (169.254.169.254), đánh cắp ambient IAM credentials — tất cả bằng HTTP requests thông thường.
- **State forking và memory checkpointing quan trọng hơn raw boot time:** Agent session spans multiple turns, nếu destroy state mỗi turn thì mất workspace context. Giải pháp: snapshot memory xuống object storage khi idle, restore từ warm worker trong 250 ms-3s, đạt p50 ~50 ms per-call latency trên warm pool.
- **Decision rubric 4 câu hỏi:** JS/WASM → V8 isolates; trusted single-tenant → hardened OCI containers; multi-tenant untrusted Linux → gVisor; custom kernel/hardware isolation → microVMs.

## Related concepts

- [[isolation-spectrum]] — 4-tier isolation architecture
- [[sandbox-state-forking]] — memory checkpointing and snapshot restore
- [[network-egress-default-deny]] — deny-by-default egress security
- [[agent-harness]] — software layer wrapping LLM for execution
- [[autonomous-agents]] — agents that operate independently
- [[prompt-injection]] — attack vector that bypasses hypervisor

## Sources

- "[[src_google-cloud-agent-sandbox-runtimes]]"