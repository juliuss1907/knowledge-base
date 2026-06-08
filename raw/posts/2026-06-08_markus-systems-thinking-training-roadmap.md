---
type: raw
source_type: post
source_url: https://t.me/markus_rk_200_bot
date_ingested: 2026-06-08
tags: []
status: unprocessed
---

# Markus — Lộ trình luyện tập Systems Thinking (4 mức độ)

Source: [Markus](https://t.me/markus_rk_200_bot)

---

Dựa trên bài viết, kết hợp kinh nghiệm từ thực tế — đây là lộ trình luyện tập theo 4 mức, từ thấp đến cao. Tập trung vào 3 nguyên tắc kỷ luật trước khi vào kỹ thuật.

---

## 3 nguyên tắc kỷ luật (bắt buộc trước khi học technique)

### 1. Pause trước action ⏸️

Phản xạ số một khi gặp vấn đề là nhảy vào giải quyết. Tư duy hệ thống đòi hỏi ngược lại: dừng lại đủ lâu để hỏi "vấn đề này nằm trong hệ thống nào?" trước khi xử lý.

**Thực tế:** 10 phút pause thường tiết kiệm 2 giờ sửa về sau.

### 2. Chịu được "chưa biết" 🫧

Hệ thống phức tạp sẽ không cho bạn câu trả lời ngay. Bạn phải chấp nhận: "Tôi chưa hiểu cấu trúc — và cần thêm thời gian/việc để hiểu." Không có ảo tưởng mình sẽ có insight ngay lập tức.

### 3. Câu hỏi tốt hơn câu trả lời nhanh ❓

Đặt câu hỏi đúng sẽ dẫn đến đáp án đúng. Câu trả lời nhanh thường dẫn đến sửa nhiều lần.

---

## 4 mức luyện tập (từ dễ đến khó)

### Mức 1: Quan sát cấu trúc 👀

**Phù hợp:** bắt đầu từ cuộc sống cá nhân, không cần tài liệu

**Bài tập hàng ngày:**

#### ① Before/After Comparison

Khi sự cố xảy ra, trước khi sửa, viết ra:
- Điều gì thay đổi 1–2 tuần trước khi sự cố xuất hiện?
- Có ai đổi cách làm việc không?
- Có biến động nào trong input/output (lượng khách, deadline, ngân sách, scope)?

**Ví dụ:** Pipeline Coin68 bị fail OAuth — nếu chỉ nhìn "auth fail", bạn sửa bằng re-login token. Nếu pause và hỏi "thay đổi gì trước đó?" → có thể phát hiện Google cập nhật policy OAuth, hoặc scheduler chạy job sau khi token refresh window đã đóng. Cùng một triệu chứng, hai cách hiểu dẫn đến hai cách sửa khác hệ thống.

#### ② The "What Stays the Same" Question

Khi muốn đổi thứ gì, hỏi: "Nếu ta đổi X, cái gì vẫn giữ nguyên?" Cái không đổi thường là cấu trúc nền — chính là phần bạn cần hiểu.

**Ví dụ:** Đổi từ cron 8:30 AM sang 7:30 AM. Nếu hỏi "cái gì vẫn vậy?" → múi giờ user, rằng vẫn phải research trước khi viết, rằng sáng sớm user chưa dậy đọc. Cái không đổi = constraint bạn phải làm việc quanh nó.

#### ③ Notice Repetition

Ghi lại cùng một vấn đề xuất hiện 2–3 lần trong tháng. Đây là dấu hiệu cấu trúc, không phải sự cố ngẫu nhiên.

---

### Mức 2: Vẽ quan hệ 🕸️

**Phù hợp:** khi đã có vấn đề cụ thể muốn hiểu sâu

**Bài tập:** System Map (mỗi lần gặp vấn đề mới)

**4 bước vẽ bản đồ trong 10–15 phút:**

1. **Liệt kê nodes** — các thực thể tham gia (con người, hệ thống, quy trình, khách hàng, công cụ...)
2. **Vẽ arrows** — mỗi arrow phải có nhãn (làm gì với cái kia? tạo áp lực, cung cấp input, kích hoạt, ràng buộc...)
3. **Tìm loops** — mũi tên khép kín (A → B → C → A) là feedback loop — thường là cốt lõi của hành vi lặp lại
4. **Tô màu mức ảnh hưởng** — đậm = yếu tố bạn có thể can thiệp, nhạt = bên ngoài tầm kiểm soát

**Câu hỏi quan trọng sau khi vẽ:**
- **Biên nào?** — Cái gì trong hệ thống, cái gì nằm ngoài?
- **Then chốt nào?** — Nếu thay đổi 1 yếu tố duy nhất, hệ thống sẽ phản ứng thế nào?
- **Feedback loop nào đang lái hành vi?**

**Template nhanh** (giấy trắng / Miro / Excalidraw):

```
 [A] ──ràng buộc──> [B]
  │                     │
tạo áp lực         cung cấp
  │                     │
 [C] <──kích hoạt──── [D]
  ↑
  └────feedback loop────┘
```

**Ví dụ áp dụng cho Coin68 pipeline:**

| Node | Vai trò |
|------|---------|
| **Cron job** | Trigger 8:30 AM |
| **Sheet** | Source of truth, ưu tiên task |
| **Subagent** | Nghiên cứu + viết |
| **Drafts folder** | Output |
| **Telegram notify** | Loop back với Julius để duyệt |
| **Lessons learned** | Feedback loop cập nhật knowledge |

**Feedback loop chính:** Julius review → self-reflect → lessons learned → subagent đọc → bài sau tốt hơn. Nếu một trong các node này vắng mặt, hệ thống dừng tiến hóa.

---

### Mức 3: Tìm can thiệp có tác động cao 🎯

**Phù hợp:** khi đã hiểu cấu trúc, muốn tìm chỗ nên tác động

**Khái niệm:** **Leverage Points** (theo Donella Meadows) — không phải mọi chỗ trong hệ thống đều có giá trị can thiệp ngang nhau. 12 leverage points từ thấp → cao:

**Cao** (thay đổi hệ thống tận gốc — khó):
1. **Paradigms** — thay đổi cách mọi người nghĩ về hệ thống
2. **Goals** — thay đổi mục đích hệ thống
3. **Power to change structure** — phân quyền

**Trung bình** (thay đổi cấu trúc):
4. **Feedback loops** — tạo/ngắt vòng lặp
5. **Information flows** — ai thấy cái gì, khi nào
6. **Rules** — thay đổi luật chơi

**Thấp** (tác động tại chỗ):
7. **Constants/parameters** — số liệu
8. **Buffers** — dự trữ
9. **Material flows** — dòng chảy vật chất

**Câu hỏi then chốt:** "Nếu tôi có một đòn bẩy, tôi nên đặt nó ở đâu để tạo thay đổi tốt nhất?"

**Bài tập:** Với hệ thống bạn đang vận hành, đặt câu hỏi:
- Nếu được thay 1 thứ duy nhất, tôi nên thay cái gì?
- Nếu tôi thay đổi ở đây, hệ thống tự cân bằng có trả lại về cũ không?

---

### Mức 4: Practice với "thinking tools" 🧰

**Phù hợp:** khi đã quen với tư duy hệ thống cơ bản, muốn nâng cao

**5 thinking tools hay dùng:**

#### ① Iceberg Model (tầng sâu của sự kiện)

```
        Sự kiện ← "Cái tôi thấy"
           ↓
       Pattern ← "Cái này đã xảy ra bao nhiêu lần"
           ↓
  Systemic Structure ← "Cấu trúc nào sinh ra pattern này"
           ↓
    Mental Models ← "Niềm tin/thế giới quan nào sinh ra cấu trúc"
```

**Khi dùng:** Lần đầu tiên gặp vấn đề, đào xuống. Lần thứ 2, đã thấy pattern. Lần thứ 3+, hỏi "cấu trúc nào sinh ra chuyện này?".

#### ② Feedback Loop Analysis (tìm vòng lặp)

- **Balancing loop** (cân bằng) — kéo hệ thống về trạng thái cũ. VD: nhiệt độ phòng tăng → A/C bật → hạ nhiệt → tắt.
- **Reinforcing loop** (khuếch đại) — đẩy hệ thống đi xa hơn. VD: người dùng tăng → network effect mạnh → thu hút thêm người dùng → tăng mạnh hơn.

**Câu hỏi:** "Loop nào đang khuếch đại vấn đề? Loop nào đang kìm hãm?"

#### ③ Stock and Flow (tồn kho & dòng chảy)

- **Stock** — lượng tích lũy tại một thời điểm (tồn kho, dân số, tiền trong tài khoản, số dự án active)
- **Flow** — tốc độ thay đổi (sinh/đẻ mới, chết/tiêu hao)

**Câu hỏi:** "Stock này tăng/giảm nhanh hay chậm? Có bottleneck ở flow nào không?"

#### ④ Causal Loop Diagram (mở rộng System Map)

- Vẽ các vòng lặp nhân–quả có hướng
- Gắn dấu (+) = đồng biến, (–) = nghịch biến
- Đếm vòng lặp dương (khuếch đại) hay âm (cân bằng) để hiểu hành vi

#### ⑤ Behavior Over Time (BOT) (đồ thị)

- Vẽ biến số theo trục thời gian
- Hỏi: "Tăng/giảm ổn định hay có inflection point? Có oscillation không? Driver nào?"

---

## Lộ trình 30 ngày đề xuất

| Tuần | Trọng tâm | Bài tập |
|------|-----------|---------|
| **1** | Quan sát | Trước khi sửa bất cứ thứ gì, viết 3 dòng: "thay đổi gì trước đó? cái này xảy ra lần mấy? constraint nào tôi đang bỏ qua?" |
| **2** | Vẽ | Mỗi khi gặp vấn đề, dành 10 phút vẽ system map bằng tay. Không cần đẹp, cần rõ quan hệ. |
| **3** | Tìm leverage | Với 1 hệ thống cụ thể (vd: Coin68 pipeline), thử 12 leverage points — chọn ra 1 nơi bạn nghĩ có thể tác động hiệu quả nhất. |
| **4** | Thực hành nâng cao | Dùng Iceberg Model + Feedback Loop Analysis cho 1 vấn đề quan trọng trong tuần. Viết 1 trang phân tích. |

---

## Sai lầm thường gặp

### ❌ "Tôi thấy nhiều quan hệ → tôi hiểu hệ thống"

Thấy nhiều quan hệ không có nghĩa hiểu hệ thống. Hệ thống cần có biên, cấu trúc, mục đích. Nếu bạn thấy "mọi thứ liên quan đến mọi thứ" mà không thể chỉ ra đâu là then chốt — bạn đang ở holistic, không phải systems.

### ❌ "Tôi có system map → tôi sẵn sàng can thiệp"

Bản đồ là bước đầu, không phải kết luận. Sau khi vẽ xong, phải test giả thuyết: "Nếu tôi tác động vào A, hệ thống sẽ phản ứng thế nào?" — và theo dõi thực tế.

### ❌ "Tư duy hệ thống thay thế được phân tích"

Tác giả nhấn mạnh: "Systems thinking không thay thế phân tích. Nó cải thiện chất lượng phân tích." Bạn vẫn cần data, vẫn cần phân tích từng phần. Tư duy hệ thống giúp bạn biết phân tích cái nào trước và đặt nó trong bối cảnh nào.

### ❌ "Cần phải giỏi tự nhiên mới học được"

Tác giả khẳng định: tư duy hệ thống là **capability**, không phải **trait**. Người giỏi bẩm sinh thấy quan hệ nhanh hơn. Người giỏi kỷ luật biết cách test quan hệ đó, xác định biên, tìm feedback, hỏi "thay đổi từ đâu?". Cả hai đều đến đích — chỉ khác tốc độ.

---

## 1 dặn dò cuối

> **"Some people may see the system sooner. But seeing the system clearly still takes work."**

Nếu anh đang vận hành 1 hệ thống nào đó (Coin68 pipeline, X content, knowledge base) — bắt đầu từ tuần 1, quan sát 1 vấn đề thực. Đừng học framework trước, hãy để framework phục vụ vấn đề thực. Mỗi bài viết Catena, mỗi cron fail, mỗi token expired — đều là dịp để luyện tập. 🛠️