# Ad-Hoc Verification ("recheck")

Khi Julius nói **"recheck"** sau một tổng kết công việc, anh ấy muốn xác nhận các thay đổi được claim đã thực sự tồn tại trên repo. Đây là verification ad-hoc, khác với re-validation cycle (post-Fix Agent).

## Workflow

1. **Xác định scope** — đọc tổng kết của Julius, liệt kê các mục cần verify
2. **Tìm commit range** — dùng `git log --oneline` để xác định khoảng commit chứa thay đổi. Nếu git log toàn "vault backup", tìm commit gần nhất trước và sau thời điểm thay đổi
3. **Chạy git diff** giữa 2 commit để thấy chính xác những gì đã thay đổi:
   ```bash
   git diff <commit-before>..<commit-after> --stat
   ```
4. **Verify từng mục** — so sánh claim vs actual:
   - Đếm số lượng (files, sections, lines)
   - Kiểm tra nội dung (field values, section names)
   - Đối chiếu claim trong tổng kết

## Common Verification Checks

### Tag file sections
```bash
# Đếm sections mới được thêm
git diff <before>..<after> -- wiki/tag/ | grep '^+## ' | sort | uniq -c

# Đếm tổng sections trong tag files
grep -c '^## ' wiki/tag/*.md
```

### Raw reference updates
```bash
git diff <before>..<after> -- wiki/sources/ --stat
```

### Archive report moves
```bash
git diff <before>..<after> -- wiki/reviews/ --stat | grep rename
```

### Broken wikilinks count
```python
import os, re

wiki_dir = 'wiki'
broken = 0
for root, dirs, files in os.walk(wiki_dir):
    if 'archive' in root or 'reviews' in root:
        continue
    for f in files:
        if not f.endswith('.md'): continue
        content = open(os.path.join(root, f)).read()
        for link in re.findall(r'\[\[([^\]|#]+)(?:[|#][^\]]+)?\]\]', content):
            found = False
            for subdir in ['concepts','sources','tag','topic','meta','drafts']:
                if os.path.exists(f'wiki/{subdir}/{link}.md'):
                    found = True; break
            if not found:
                broken += 1
print(f'Broken: {broken}')
```

## Pitfalls

- **Claim vs actual mismatch**: Tổng kết có thể nói "23 files" nhưng thực tế là 24 (file index gốc có thể được tính khác). Luôn report cả 2 con số.
- **Broken wikilinks**: Unique count ≠ occurrence count. Julius thường đếm occurrences. Chênh lệch nhỏ là bình thường do phạm vi đếm khác nhau.
- **Archive path**: Reports được archive vào `wiki/reviews/archive/YYYY-MM/`, không phải `archive/` ở root.
