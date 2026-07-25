# Raw Sub-Index Conventions

Khi thêm một raw/ sub-directory mới (vd: `tools/`, `books/`), phải tuân thủ các bước sau:

## Steps to add a new raw/ sub-index

1. **Tạo thư mục**: `mkdir -p raw/<category>/`
2. **Tạo index file**: `raw/<category>/<category>.md` với frontmatter chuẩn:
   ```yaml
   ---
   type: index
   level: 2
   scope: <category>
   parent: "[[raw]]"
   auto_generated: false
   items_managed_by: ingest-agent
   last_updated: YYYY-MM-DD
   ---
   ```
3. **Cập nhật parent index**: Thêm `[[<category>]]` vào sub-indexes trong `raw/raw.md`
4. **Cập nhật scan script**: Thêm `<category>` vào `RAW_SUBFOLDERS` trong `hygiene-inspector/references/scan-script.py`
5. **Cập nhật validator scope**: Thêm `raw/<category>/<category>.md` vào danh sách sub-indexes trong `knowledge-base-validation` SKILL.md và `format-validator` SKILL.md

## Common pitfalls

- **Sai vị trí**: File index phải nằm ở `raw/<category>/<category>.md`, KHÔNG ở root repo hay thư mục riêng ngoài raw/
- **Sai frontmatter**: Phải dùng format `type: index`, `level: 2`, `scope: <category>`, `parent: "[[raw]]"` — không dùng `created`, `tags`
- **Quên cập nhật raw/raw.md**: Nếu không thêm vào sub-indexes, file sẽ bị orphan
- **Quên cập nhật scan script**: Hygiene Inspector sẽ flag thư mục mới là ERROR nếu không có trong `RAW_SUBFOLDERS`

## Example: Adding `tools/` (2026-07-25)

Commit gốc `60e5ef43` tạo file sai ở `tools/index tools.md` (root, tên có space). Fix:
1. Move → `raw/tools/tools.md`
2. Chuẩn hóa frontmatter
3. Thêm `[[tools]]` vào `raw/raw.md`
4. Thêm `"tools"` vào `RAW_SUBFOLDERS` trong scan script
