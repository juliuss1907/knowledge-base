---
type: concept
status: draft
main_tag: system
sub_tags: [tools, hack]
topic: isolation-spectrum
sources:
  - "[[src_google-cloud-agent-sandbox-runtimes]]"
last_updated: 2026-09-02
---

# Isolation Spectrum

## Definition

Isolation spectrum là khung phân loại các tầng cô lập phần mềm (software isolation tiers) cho agent sandbox runtimes, được định nghĩa bởi câu hỏi: "lớp phần mềm nào được dùng chung giữa untrusted code và host?" — từ shared-process đến hardware VM. Mỗi tầng có trade-off giữa startup speed, density, và isolation strength.

## Key ideas

- **Tầng 1 — V8 Isolates (Cloudflare Workers, Deno Core):** Code chạy trong cùng OS process, mỗi isolate có memory heap riêng. Startup sub-5 ms, density cực cao, nhưng giới hạn ở JavaScript, TypeScript, WebAssembly — không chạy arbitrary Linux binaries hay C-extension Python packages.
- **Tầng 2 — Standard OCI Containers (Docker, runc):** Native execution speed, full OS compatibility, nhưng shared host kernel qua cgroups/namespaces/seccomp. Không phải multi-tenant boundary — kernel exploit (Dirty Pipe, Leaky Vessels) có thể chiếm toàn bộ host. Chỉ dùng cho trusted single-tenant workloads.
- **Tầng 3 — User-Space Kernels (gVisor/runsc, GKE Sandbox, Cloud Run Sandbox):** Intercept system calls trong Go-based user-space plane (Sentry), filter host access qua strict seccomp jail. Container-level density, không expose host kernel. Syscall-heavy operations có overhead, nhưng CPU-bound code chạy near-native. Không có escape công khai từ Sentry đến host.
- **Tầng 4 — MicroVMs (Firecracker, Cloud Hypervisor, Kata Containers):** Dedicated minimal Linux guest kernel trong hardware-assisted KVM virtualization boundary. Gold standard cho hard tenant isolation, nhưng mỗi microVM có dedicated guest memory overhead.
- **Bài học thực tế:** Gán nhãn "sandboxed" không đồng nghĩa với an toàn. Cần xác định đúng tầng isolation dựa trên threat model. Running LLM-generated bash commands trong rootless Docker tương đương "betting your cluster on the hope that the model never generates a C snippet that hits a zero-day kernel race condition."

## Related concepts

- [[agent-sandbox-runtimes]] — overall sandbox runtime landscape
- [[sandbox-state-forking]] — memory checkpointing
- [[network-egress-default-deny]] — network security
- [[agent-defense-in-depth]] — multi-layer security approach

## Sources

- "[[src_google-cloud-agent-sandbox-runtimes]]"