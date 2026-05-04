---
type: raw
source_type: article
source_url: https://open.substack.com/pub/davidwsilva/p/ai-learned-to-write-like-you-detection
date_ingested: 2026-05-03
tags: [#ai, #research]
status: processed
processed_date: 2026-05-04
---

# AI Đã Học Viết Như Bạn. Phát Hiện Về Mặt Toán Học Là Bất Khả Thi

**Tác giả:** David W. Silva  
**Nguồn:** Substack  
**Ngày:** 2026-02-20  
**Link gốc:** https://open.substack.com/pub/davidwsilva/p/ai-learned-to-write-like-you-detection

---

## Tóm tắt

Các AI detector (công cụ phát hiện văn bản do AI viết) **không hoạt động**. Đây không phải vấn đề công nghệ — mà là **ràng buộc toán học**.

---

## Bằng chứng thực tế

| Trường hợp | Kết quả |
|---|---|
| US Constitution được ZeroGPT đánh giá | **96.21% AI-generated** |
| OpenAI detection tool | Đóng cửa sau accuracy rate **26%** |
| Vụ kiện năm 1993 (trước ChatGPT) | ZeroGPT đánh giá **100% AI** |
| Kinh Thánh | **98.9% AI** theo detector |

→ Nhiều trường đại học đã **dừng sử dụng AI detectors** vì gây hại nhiều hơn lợi.

---

## Tại sao không thể phát hiện? — Toán học

**Vấn đề cốt lõi:**
- LLMs được train **với mục tiêu duy nhất**: tạo ra văn bản không thể phân biệt với văn bản con người
- AI detector được yêu cầu tìm sự khác biệt giữa AI text và human text
- **Nhưng model được train để loại bỏ những khác biệt đó**

**Chuỗi toán học:**

```
Training giảm KL divergence
    ↓
KL divergence giới hạn Total Variation
    ↓
Total Variation giới hạn detection accuracy
    ↓
Training càng tốt → KL divergence càng nhỏ → Detection accuracy → 50% (như tung đồng xu)
```

→ **Không có detector nào, dù tinh vi đến đâu, có thể vượt qua giới hạn này.**

---

## Scaling Laws

Mỗi khi model tăng gấp đôi kích thước:
- KL divergence giảm theo power law
- Độ chính xác tốt nhất của detector giảm theo một lượng có thể dự đoán
- Khoảng cách giữa detector tốt nhất và tung đồng xu **đang thu hẹp**

---

## Về "Phong cách viết"

Một người có thể nói: "Tôi có thể phát hiện qua phong cách."

Nhưng: **Phong cách cũng chỉ là feature thống kê.** Nếu phân phối của model gần với phân phối human → phong cách cũng gần. Stylometric analysis, zero-shot tests, perplexity methods — tất cả đều chạm cùng một trần.

---

## Watermarking — Giải pháp DUY NHẤT

Có cách phát hiện AI text thực sự? **Có.** Nhưng chỉ khi **AI company hợp tác** — watermarking (model nhúng tín hiệu ẩn vào output). Đây không phải điều detector có thể làm sau sự kiện.

---

## Lời khuyên

> Bạn không muốn nghe như AI? Bạn sẽ hoặc nghe robotic hơn AI (vì AI ngày càng giỏi nghe như người), hoặc kìm nén mọi đặc điểm của writing competent (syntax, nuance, cadence, argumentation) → kết quả: văn phạm nghèo nàn, rhetoric dull, không thể phân biệt với chính sự tầm thường bạn đang cố tránh.

**Hãy là người nổi loạn.** Viết đúng tiếng Anh. Dùng em-dashes, nhiều linguistic constructions, rich adjectives — như một công cụ để giao tiếp. Đừng hạ thấp để "không nghe như AI."
