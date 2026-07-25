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
5. **Cập nhật format-validator/scripts/validate.py** — ⚠️ CÓ 5 VỊ TRÍ hardcode list raw types, tất cả đều phải thêm `<category>`:
   - **Line ~215**: `for rd in ['articles', 'posts', 'videos', 'papers', 'websites', 'repos']:` — broken wikilink lookup trong concept body
   - **Line ~277**: `for d in ['articles', 'posts', 'videos', 'papers', 'websites', 'repos']:` — `original` field lookup trong source validation
   - **Line ~349**: `for rd in ['articles', 'posts', 'videos', 'papers', 'websites', 'repos']:` — broken wikilink lookup trong source body
   - **Line ~452**: `valid_scopes = ['articles', 'posts', 'websites', 'videos', 'papers', 'repos', 'tags']` — L2 index scope validation
   - **Line ~564**: `for rd in ['articles', 'posts', 'websites', 'videos', 'papers', 'repos']:` — main scan loop auto-discovery raw sub-indexes
6. **Cập nhật ingest-agent files** (3-4 files trong `.openclaw/skills/ingest-agent/`):
   - `SKILL.md` — tất cả references đến "6 types" → "7 types", thêm `tool` vào valid type values
   - `workflow.md` — type table thêm row mới, Step 6/7 thêm folder name
   - `reference.md` — valid values cho `type` field thêm `<category>`
   - `examples.md` — (optional) thêm example mới cho type mới

## Common pitfalls

- **Sai vị trí**: File index phải nằm ở `raw/<category>/<category>.md`, KHÔNG ở root repo hay thư mục riêng ngoài raw/
- **Sai frontmatter**: Phải dùng format `type: index`, `level: 2`, `scope: <category>`, `parent: "[[raw]]"` — không dùng `created`, `tags`
- **Quên cập nhật raw/raw.md**: Nếu không thêm vào sub-indexes, file sẽ bị orphan
- **Quên cập nhật scan script**: Hygiene Inspector sẽ flag thư mục mới là ERROR nếu không có trong `RAW_SUBFOLDERS`
- **⚠️ Quên cập nhật validate.py — 5 vị trí**: Mỗi vị trí hardcode một list raw types riêng. Nếu chỉ sửa 4/5 vị trí, validator sẽ bỏ sót file mới trong một số code path (vd: `original` field validation pass nhưng broken wikilink lookup sẽ miss). Luôn grep toàn bộ file sau khi sửa để xác nhận không còn list nào thiếu
- **⚠️ Quên cập nhật ingest-agent**: Compile Agent dùng ingest-agent config làm reference. Nếu ingest-agent không biết về type mới, nó sẽ từ chối ingest content với type đó

## Example: Adding `tools/` (2026-07-25)

Commit gốc `60e5ef43` tạo file sai ở `tools/index tools.md` (root, tên có space). Fix:
1. Move → `raw/tools/tools.md`
2. Chuẩn hóa frontmatter
3. Thêm `[[tools]]` vào `raw/raw.md`
4. Thêm `"tools"` vào `RAW_SUBFOLDERS` trong scan script
