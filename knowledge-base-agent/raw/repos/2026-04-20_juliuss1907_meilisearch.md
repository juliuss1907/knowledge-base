---
type: raw
source_type: repo
source_url: https://github.com/juliuss1907/meilisearch
date_ingested: 2026-04-20
tags: [#ai, #coding, #research]
status: unprocessed
---
# Meilisearch — Lightning-fast Search Engine

## Tóm tắt

Meilisearch là search engine RESTful API, mã nguồn mở, hỗ trợ AI-powered hybrid search. Tốc độ tìm kiếm dưới 50ms. Có thể tích hợp vào app/website chỉ trong vài dòng code.

## Tính năng chính

**Tìm kiếm:**
- Hybrid search — kết hợp semantic + full-text search
- Search-as-you-type: kết quả dưới 50ms
- Typo tolerance: chấp nhận lỗi chính tả
- Synonym support
- Filtering & faceted search
- Sorting theo price, date, hoặc bất kỳ field nào
- Geosearch: lọc theo vị trí địa lý
- Hỗ trợ đa ngôn ngữ (Chinese, Japanese, Hebrew, Latin alphabet...)

**AI:**
- Conversational search: hỏi bằng ngôn ngữ tự nhiên, nhận câu trả lời AI
- Personalization: cá nhân hoá kết quả theo từng user
- Vector search (semantic search)
- Tích hợp LangChain và MCP

**Quản lý:**
- API keys với fine-grained permissions
- Multi-tenancy: nhiều tenant dùng chung
- Document relations: link documents giữa các indexes
- Replication & sharding: scale ngang

**Triển khai:**
- Dễ cài đặt, deploy, maintain
- Cloud option (Meilisearch Cloud)
- RESTful API, nhiều SDK cho Python, JavaScript, Go, Ruby...

## License

- **MIT license** cho core search engine
- **BSL 1.1** cho các tính năng enterprise (sharding, S3 snapshots...)
- Không được dùng enterprise features trong production nếu không có commercial agreement

## Links

- Website: https://meilisearch.com
- Docs: https://meilisearch.com/docs
- Cloud: https://meilisearch.com/cloud
