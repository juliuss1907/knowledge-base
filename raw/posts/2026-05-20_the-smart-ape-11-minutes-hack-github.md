---
type: post
title: "11 minutes was all it took to hack github"
url: https://x.com/i/status/2056983617302122740
author: The Smart Ape (@the_smart_ape)
date_published: 2026-05-20
date_ingested: 2026-05-20
status: unprocessed
source: X / Twitter
---

# 11 minutes was all it took to hack github

**Tác giả:** The Smart Ape (@the_smart_ape)  
**Nguồn:** X / Twitter  
**Ngày đăng:** 2026-05-20

---

## Sự kiện chính

GitHub thông báo **~3,800 internal repos** bị đánh cắp. Source code của công ty lưu trữ source code cả thế giới vừa bị compromise.

Toàn bộ files đang được rao bán trên diễn đàn cybercrime với giá **$50,000** — nhiều đối thủ sẵn sàng trả.

## Entry point: Vô cùng "bình thường"

| Yếu tố | Chi tiết |
|--------|----------|
| **Công cụ** | VS Code extension "NX Console" (nrwl.angular-console) |
| **Thời gian tồn tại** | Chỉ **11 phút** trên marketplace |
| **Lây nhiễm** | Một GitHub employee có auto-update bật |
| **Cài đặt toàn cầu** | 2.2 triệu lượt |

**Timeline:**
- **May 18:** Update độc hại lên marketplace
- **May 19:** GitHub phát hiện → cô lập laptop, gỡ extension
- **May 20 1:48 AM:** GitHub thông báo

## Cơ chế tấn công (rất tinh vi)

### 1. Lấy token

TeamPCP đánh cắp token của một nx contributor → dùng push **orphan commit** (commit ẩn, không gắn branch) lên nrwl/nx repo.

### 2. Payload

- `package.json` + `index.js` **498KB obfuscated code**
- Chạy trên Bun (JavaScript runtime nhanh)

### 3. Steal credentials

Ngay khi dev mở workspace, extension đánh cắp:
- **GitHub tokens** → mở mọi repo dev có quyền
- **npm tokens** → publish package độc dưới tên nạn nhân
- **AWS credentials** → server access
- **HashiCorp Vault & Kubernetes secrets** → production keys
- **1Password vault** (nếu đang unlock)

### 4. Exfiltration

Dữ liệu chảy ra qua **3 kênh**:
- HTTPS thông thường
- GitHub API (qua firewall whitelist)
- DNS tunneling

### 5. Backdoor (macOS)

- Python backdoor **persistent**
- Nhận lệnh qua GitHub Search API "dead drop"
- Commands signed với **RSA-4096** — professional grade

## Thủ phạm: TeamPCP

| | |
|---|---|
| **Alias** | deadcatx3, pcpcat, shellforce, cipherforce |
| **Thành tích 6 tháng** | 300+ GB dữ liệu, 500,000 credentials |
| **Mô hình** | Bán credential & supply chain compromise (thay vì ransomware) |

**Các mục tiêu trước:**
- **March:** Trivy, Kics (security scanners)
- **April:** Fake Bitwarden/cli; SAP developer packages (570k weekly downloads)
- **May 11:** TanStack (84 malicious versions, 42 npm packages)
- **Now:** GitHub trực tiếp

**Pattern:** Tấn công **security tools và developer infrastructure** — compromise 1 tool millions dev tin → inherit access to everything.

## Vấn đề hệ thống

**VS Code Marketplace = Wild West**

| Năm | Malware detections |
|-----|-------------------|
| 2024 | 27 |
| First 10 months 2025 | **105** (4x more) |

- 550+ secrets tìm thấy plaintext trong 500+ extensions
- **Microsoft không review updates** của popular extensions

> *"Bạn click 'install' và trao cho người lạ quyền truy cập full máy: tokens, secrets, shell history, everything. Cài program unsigned năm 2005 còn có friction hơn thế này."*

## Rủi ro thực sự: 3,800 internal repos

GitHub nói **no customer data** bị ảnh hưởng, chỉ internal repos.

**Nhưng 3,800 repos đó chứa gì?**
- Moderation tooling
- Code cho security features chưa release
- Scripts chạy production infra
- Secrets vô tình commit (xảy ra với mọi người, kể cả GitHub)

GitHub đã rotate critical credentials — đúng việc. Nhưng khi attacker có **24 giờ head start** và **3,800 repos** để tìm kiếm:

> *"Cuộc đua đã thua. Chúng ta chỉ sẽ biết thiệt hại khi breach tiếp theo ở đâu đó hóa ra được enable bởi thứ leak từ đây."*

## Lời khuyên ngay lập tức

Nếu bạn có **API keys, tokens, .env files**, hoặc bất kỳ thông tin nhạy cảm nào trong GitHub repos (kể cả private):

1. **Rotate chúng ngay hôm nay**
2. **Pull chúng ra** khỏi repos
