---
type: concept
status: draft
main_tag: system
sub_tags: [automation, tools]
topic: sandbox-state-forking
sources:
  - "[[src_google-cloud-agent-sandbox-runtimes]]"
last_updated: 2026-09-02
---

# Sandbox State Forking

## Definition

Sandbox state forking là kỹ thuật quản lý trạng thái (state management) cho agent sandbox runtimes, nơi memory state của sandbox được snapshot xuống object storage khi agent idle và restore nhanh chóng từ warm worker pools khi agent cần thực thi tiếp. Giải pháp này giải quyết bài toán: agent session spans multiple interactive turns (inspect files → run test → fail → edit code → retry), nhưng nếu destroy state mỗi turn thì mất workspace context, còn maintain VMs liên tục thì tốn kém.

## Key ideas

- **Bài toán kiến trúc trung tâm:** Agent dành ~95% thời gian chờ model reasoning/tools, rồi bùng nổ thực thi. Nếu destroy sandbox state mỗi turn, agent mất workspace context. Nếu keep VMs chạy liên tục, lãng phí resources trong idle periods.
- **Giải pháp memory checkpointing:** Khi agent idle → pause runtime → write incremental snapshot xuống object storage (Cloud Storage). Khi next tool call đến → warm worker restore snapshot trong 250 ms-3s. Workspace state được bảo toàn mà không đốt VM budget lúc idle.
- **Warm multiplexed worker pools:** Trên optimized pool, warm per-call execution latency đạt p50 ~50 ms dưới concurrent load, so với 500 ms+ trên unpooled serialized execution backends.
- **Decouple ephemeral execution từ persistent data:** Agent artifacts durable lưu trong cloud object storage; local filesystem operations trên active turns dùng copy-on-write scratchpads. Đây là built-in capability nên có trong chosen sandbox service/platform.
- **Không chỉ snapshots, mà cả pre-warmed templates:** Pre-warmed template pools (SandboxWarmPool từ kubernetes-sigs/agent-sandbox) giải quyết cold-start ở tầng runtime provisioning, state forking giải quyết ở tầng session continuity — hai lớp này kết hợp cho interactive agent experience.

## Related concepts

- [[agent-sandbox-runtimes]] — overall sandbox runtime landscape
- [[isolation-spectrum]] — isolation tiers cho sandbox environment
- [[network-egress-default-deny]] — network security cho sandbox

## Sources

- "[[src_google-cloud-agent-sandbox-runtimes]]"