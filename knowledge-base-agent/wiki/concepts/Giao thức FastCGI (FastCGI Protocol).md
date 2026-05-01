---
type: concept
status: draft
tags: [#tech, #coding]
---
# Giao thức FastCGI (FastCGI Protocol)

## Mô tả
FastCGI là một giao thức truyền thông giữa web server (như Nginx, Apache) và một ứng dụng backend (như PHP, Python, Ruby). Nó được thiết kế để cải thiện hiệu suất so với CGI truyền thống bằng cách duy trì các tiến trình ứng dụng chạy ngầm, thay vì khởi tạo lại cho mỗi yêu cầu.

### Ưu điểm so với HTTP trong Reverse Proxy
- **Thiết kế Binary:** Truyền tải dữ liệu hiệu quả hơn so với định dạng văn bản của HTTP.
- **Quản lý kết nối:** Hỗ trợ đa luồng và duy trì kết nối bền vững, giảm chi phí thiết lập TCP/TLS cho mỗi request.
- **Phân tách vai trò:** Tách biệt rõ ràng giữa tầng điều phối (web server) và tầng thực thi (application server).

## Liên quan
- [[Reverse Proxy]]
- [[HTTP Protocol]]

## Nguồn tham khảo
- [FastCGI vẫn là giao thức tốt hơn cho Reverse Proxy sau 30 năm](https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies)
