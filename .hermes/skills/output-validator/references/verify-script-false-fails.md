# Verify-script false-FAIL classes — consolidated 2026-09-30 + 2026-10-01

Across two runs, 13 checks FAILed. **Every one was a bug in the ad-hoc verification script. All three output files were correct throughout.** Five distinct classes, all recurring in new clothing from classes already documented in SKILL.md.

Standing rule, load-bearing: **when a verify script FAILs, run every component standalone against its file before touching any file.** Every case below was diagnosed by printing, per FAIL, the real value, the real phrasing, and the real line contents.

---

## Class 1 — Literal the file phrases differently

**Symptom:** `checkf "Unpatched count 78" '78 (unpatched) -> 77' "$R"` → FAIL. The report is prose: *"quick-scan reported **78** under-5 concepts at run start. An independent re-implementation of the corrected pattern returns **77**."* Both numbers present, substring invented.

**Rule:** before embedding any cross-file literal, run it standalone:
```bash
grep -qF '<pat>' <file>; echo $?
```
Assert a phrase you **copied from** the report, not a shape you imagined. Reports are prose; a check that demands a hyphenated arrow sequence will fail against a correctly-worded sentence forever.

---

## Class 2 — Threshold where the truth is a specific count

**Symptom:** `grep -c '| ✅ APPLIED |' "$A" -gt 100` → FAIL at **85**. The bound was a guess dressed as a safety margin.

**Rule:** measure the value first, then assert **equality**:
```bash
N=$(grep -c '| ✅ APPLIED |' "$A"); echo "$N"    # 85
check "applied rows preserved" bash -c 'test "$(grep -c "| ✅ APPLIED |" "$1")" -eq 85' _ "$A"
```
Pair it with a corroborating total so a later sibling append doesn't turn a true equality into a false FAIL:
```bash
check "all status rows intact" bash -c 'test "$(grep -cE "\| (✅ APPLIED|🔍 PENDING|✅ APPROVED) \|" "$1")" -eq 130' _ "$A"
```

---

## Class 3 — Whole-file grep where the assertion is about one entry

**Symptom:** `check "not a SILENT run" bash -c '! grep -q "Result.*\[SILENT\]" "$M"'` → FAIL. MEMORY.md contains **19** `[SILENT]` markers — all in *older* entries (09-17, 09-18 …). This run was a reportable audit day and correctly carries none.

**Rule:** scope the check to this run's block:
```bash
sed -n '/^## <TODAY>/,/^## <PREV>/p' "$M" > /tmp/block.txt
check "not a SILENT run" bash -c 'test "$(grep -c SILENT "$1")" -eq 0' _ /tmp/block.txt
```
Same root cause as the 2026-08-14 `tail -1` pitfall: assert about *your* block, never about the whole file.

---

## Class 4 — Double-backslash in an ERE literal

**Symptom:** `checkf "section 4 patched" "grep -cE '^- |^[0-9]+\\.\\.|^\\|'" "$S"` → FAIL against a file whose line 118 contains **single** backslashes.

**Root cause:** inside `grep -E`, `\\.` is not the same as `\.` — single `\.` is the correct ERE escape for a literal dot. The patch tool had written the single-backslash form correctly; the *check* was wrong.

**Rule:** when verifying that a script line was patched, extract the real line first and embed that exact string:
```bash
sed -n '118p' "$S" | grep -oF "grep -cE '^- |^[0-9]+\.|^\|'"   # confirm literal present
```
Then embed the single-backslash form in the check. Note that in bash double quotes, `\.` survives as `\.`; in single quotes it also survives — but a *literal double* backslash typed into a double-quoted string becomes `\\`, which is the wrong pattern. Prefer extracting over hand-typing regexes.

---

## Class 5 — Siblings changed the number under you: assert the invariant

**Symptom (the documented 07-13 sibling race, recurring):** report written with pending **37**. Format Validator ran at 23:15 during this run's verification pass and added its own entry. Three checks then FAILed:
- `Header says 37` → header now **38**
- `entry count == 37` → count now **38**
- `EN+VI == 37` → EN **29** + VI **9** = 38

None of the three indicates a file defect. All three hardcoded a number that a concurrent writer legitimately changed.

**Rule: never hardcode the pending count the way you hardcode the report filename.** Assert the invariants SKILL.md already identifies as load-bearing, plus a floor:

```bash
sed -n '/^## Pending Reports/,/^## Báo cáo đã duyệt/p' "$A" > /tmp/pend.txt
P=$(grep -c '^### ' /tmp/pend.txt)
HN=$(grep -o '\*\*Pending reports awaiting review:\*\* [0-9]*' "$A" | head -1 | grep -o '[0-9]*$')
EN=$(grep -c '^- \*\*Status:\*\*' /tmp/pend.txt)
VI=$(grep -c '^- \*\*Trạng thái:\*\*' /tmp/pend.txt)
check "entry count == header" test "$P" -eq "$HN"
check "EN+VI == entry count"   test "$((EN+VI))" -eq "$P"
check "count >= my write"      test "$P" -ge 37
```

At 10-01 verification time: `entry_count=38, header=38, EN=29, VI=9` — all three invariants exactly true. Also add a positive check that the **sibling's** entry is present, so a clean run proves coexistence rather than absence:
```bash
check "10-01 sibling Format entry present" bash -c 'grep -q "^### 🔍 Format Validation — 2026-10-01" "$1"' _ "$A"
```

**Corollary — MEMORY.md line numbers shift too.** The top-insertion ordering check (`new_line < prev_line`) still held, but the absolute numbers moved: this run's heading went **line 7 → line 15** because a sibling entry landed above it. Any check hardcoding a line number, or asserting "no `## ` heading above my entry" against a fixed `head -6` window, will break. Assert **relative** ordering only, and widen the window defensively.

## Class 6 — a check pattern that also matches the comment explaining the fix

**Symptom (10-01, second verification pass):** `check "no stale 'grep -c .^- .' in section 4" bash -c '! sed -n "/─── 4\./,/─── 5\./p" "$1" | grep -q "grep -c .\^-"'` → FAIL, on a script that is correctly patched.

**Root cause:** the patch I had just applied contains a *comment* quoting the old pattern verbatim:

```bash
# Previously this counter used `grep -c '^- '` only, so concepts whose Key ideas are…
```

The grep pattern `grep -c .\^-` has a wildcard before `^-`, so it matches `grep -cE '^- …'` **and** the prose in the comment. The check was asking "is the old pattern gone?" while the file legitimately documents what it replaced.

**Rule:** when asserting that something was *removed* or *replaced*, exclude comments. A comment quoting the old value is documentation, not a defect.
```bash
! sed -n '/<section>/,/<\/section>/p' "$1" | grep -v '^ *#' | grep -q '<old pattern>'
```
Corollary: any "is X gone?" check must be written against code lines only, or it will fail every time someone documents the fix.

## Class 7 — fallback-OR check with no primary branch matching

**Symptom (same pass):** `check "baseline 77" bash -c 'grep -q "Baseline is \*\*77\*\*" "$1" || grep -q "re-baseline.*77\|baseline.*77" "$1"'` → FAIL, though the baseline is recorded in SKILL.md.

**Root cause:** I guessed the wording. SKILL.md actually reads `- **77** concepts in the 1–4 key-ideas range (what quick-scan flags)`. Neither guessed pattern matched; the `||` fallback just made the check *look* defensive while both branches were wrong.

**Rule:** an `A || B` fallback in a verify script is a smell — it hides the fact that neither branch was tested against the real text. This is Class 1 in disguise. Use `checkf` with the phrase copied verbatim from the file, and prove it standalone first.

---

## Checklist before shipping a verify script

1. Every cross-file literal tested standalone with `grep -qF '<pat>' <file>; echo $?`
2. No invented prose substrings — copy real phrases from the file
3. Thresholds replaced by measured equality + a corroborating total
4. Scoped greps (`sed -n '/entry/,/entry/p' > /tmp/block`) instead of whole-file greps
5. Regex literals extracted from the target, not hand-typed
6. Pending counts asserted as invariants (`P == header`, `EN+VI == P`), never literals
7. `set -e` absent, or every `grep -q` inside an `if`/`|| true`
8. No emoji in the script body (security scanner)
9. Sibling entries positively checked for coexistence
10. Re-run after the sibling cron window closes; if a count moved, confirm it is the sibling's entry and not a corruption
