# Process Recheck Report

Khi Julius gửi một báo cáo recheck có sẵn (dạng table: Issue | Trước | Sau | Trạng thái), xử lý từng dòng:

## Các loại trạng thái và cách xử lý

| Trạng thái | Ý nghĩa | Hành động |
|---|---|---|
| ✅ Đã fix | Fix Agent đã sửa đúng | Xác nhận, không làm gì |
| ❌ Chưa fix | Fix Agent báo fix nhưng chưa sửa | **Sửa trực tiếp** nếu là lỗi nhỏ (typo, phrasing) |
| ⚠️ Cần check | File biến mất hoặc trạng thái không rõ | Hỏi Julius xác nhận intentional hay accidental |
| ⏭️ Bỏ qua | Systemic issue, không verify được | Ghi nhận, không action |

## File biến mất — quy trình xác nhận

Khi recheck report flag một file "đã biến mất":
1. Kiểm tra file có trong git history không: `git log --all --full-history --name-only -- '*filename*'`
2. Kiểm tra commit gần nhất liên quan: `git log --oneline -1 -- path/to/file`
3. Nếu file đã được commit delete → có thể intentional (Obsidian Git sync)
4. **Hỏi Julius xác nhận** trước khi kết luận
5. Nếu Julius xác nhận intentional → update skill nếu skill document file đó

## Sửa trực tiếp các lỗi nhỏ

Khi recheck report chỉ ra instance cụ thể chưa fix (VD: "dòng 28 vẫn còn mental models"):
- Đọc chính xác dòng đó
- Patch: `old_string` phải khớp chính xác nội dung hiện tại
- Verify bằng grep sau khi patch
- Việc này là fix lỗi bỏ sót của Fix Agent, không phải validation work bình thường
