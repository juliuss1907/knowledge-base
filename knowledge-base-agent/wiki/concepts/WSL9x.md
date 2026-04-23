---
type: concept
status: draft
tags: [#coding, #research]
---
# Windows 9x Subsystem for Linux (WSL9x)

## Mô tả
Một dự án thử nghiệm cho phép chạy Linux kernel hiện đại (6.19) song song và hợp tác với Windows 9x kernel mà không cần reboot.

## Chi tiết
- **Cơ chế:** Linux kernel chạy "cooperatively" bên trong Windows 9x, tận dụng paging và memory protection.
- **Kỹ thuật:** Sử dụng cross toolchain `i386-linux-musl` và Open Watcom v2.
- **Mục đích:** Thể hiện khả năng tương thích ngược và khả năng chạy đa nhiệm giữa hai hệ điều hành khác thời đại trên cùng một máy.

## Liên quan
- [[OS-Kernel]]
- [[Linux-Kernel]]
- [[Virtualization]]

## Nguồn tham khảo
- [[wiki/sources/src_wsl9x-linux-win9x.md]]
