# Typo variant 6 — dropped `ự` in "ký tự" (2026-10-04)

A sixth manifestation of the same root cause as variants 1-5: Compile Agent drops the
final character of Vietnamese words carrying diacritics. This time the victim is `ự`,
not `i`.

## Observed

`wiki/concepts/directors-brief.md:20`

```
- **Bằng chứng về quy mô:** các brief được chia sẻ công khai dài 9.500 ký tự
  (một nhân vật nói với máy 5 phút, agent chạy 12 giờ, ra video 142 giây)
  và 19.000 ký t cho một tác phẩm khác — thang này hoàn toàn khác một prompt một dòng
```

The file writes `ký tự` correctly in the first half of the sentence and drops the `ự`
in the second half. **A same-sentence inconsistency is the tell** — grep for the word
and read the whole sentence, don't just check the match exists.

Raw confirms the intent: `raw/posts/2026-09-27_...:915` → `@pradeepXkapoor's "Pip"
robot film used a 19,000-character brief`.

## Detection

```bash
grep -rPl 'ký t[^ự]' wiki/sources/ wiki/concepts/
```

**WHITELIST — REQUIRED.** The pattern also matches the perfectly valid word `ký tên`
("to sign"). Measured 2026-10-04: 4 files matched, 3 of them legitimate `ký tên`
(`ai-legal-personhood.md:23`, `saudi-pakistan-defense-agreement.md:16`,
`src_aaron-wright-ai-agents-legal-body.md:28`). A naive count overstates the defect
4x. Filter:

```bash
grep -rPl 'ký t[^ựt]' wiki/sources/ wiki/concepts/   # exclude ký tên
```

## Sibling sweeps

Any final-vowel drop on a diacritic-bearing word is worth checking:

```bash
grep -rPn 'chất lượ[^\n]{0,3}[^n]|qu[ảa]n tr[ìi]nh|s[ưu] d[ụ]ng|nghi[ệe]m|th[ực] t[ế]|k[ỳ] v[ọ]ng' \
  wiki/sources/ wiki/concepts/
```

Validate each hit by reading the line — words like `chất lượng` are only defective when
a character is genuinely missing. Do not report a regex hit without confirming the
character is absent.

## Fix

```bash
sed -i 's/19\.000 ký t /19.000 ký tự /' wiki/concepts/directors-brief.md
```

Context-specific sed, not a bare `s/ký t /ký tự /g` — the latter would not help anyway
here (the truncated form has no trailing space match to anchor on) and could damage
`ký tên` if the pattern were written carelessly.

## Suggested quick-scan addition

Add `grep -rPl 'ký t[^ựt]'` as a new pass with a label naming it variant 6, and note
the `ký tên` whitelist in a comment so the next run does not "fix" valid text.