"""Cross-file integrity check for Format Validator output.

Validates that today's format report, _action-required.md, and MEMORY.md
are all internally consistent — matching file counts, issue counts, and
correct structure.

Usage (from KB root):
    python3 .hermes/skills/format-validator/scripts/verify_integrity.py [YYYY-MM-DD]

If no date given, uses today's date.

Exit 0 on all checks pass, 1 on any failure.
"""
import sys
import os
import re
from datetime import date as dt_date

KB = os.getcwd()
# Allow explicit date override, default to today
if len(sys.argv) > 1:
    today = sys.argv[1]
else:
    today = dt_date.today().isoformat()

REPORT = os.path.join(KB, f"wiki/reviews/{today}_format-report.md")
ACTION = os.path.join(KB, "wiki/reviews/_action-required.md")
MEMORY = os.path.join(KB, ".hermes/MEMORY.md")

errors = []

# ── 1. Report file existence & key fields ──────────────────────────

if not os.path.isfile(REPORT):
    errors.append(f"MISSING: {REPORT}")
else:
    with open(REPORT) as f:
        content = f.read()

    checks = [
        ("Status header", '**Status:** pending'),
        ("Issues found label", '**Issues found:**'),
        ("Date in title", f"# Format Validation — {today}"),
        ("Validator field", '**Validator:** format-validator'),
        ("ERRORs line present", '**ERRORs**'),
        ("WARNINGs line present", '**WARNINGS**'),
        ("Delta section present", 'Δ from'),
        ("Files checked table", 'Files checked |'),
        ("Escalations section", '## Escalations'),
        ("Verification section", '## Verification'),
    ]
    for label, pattern in checks:
        if pattern not in content:
            errors.append(f"REPORT: {label} — missing '{pattern[:40]}'")

    # Extract counts for cross-check
    m_files = re.search(r'Files checked[:\s]+(\d+)', content)
    m_total = re.search(r'\*\*Total issues\*\*[:\s]+(\d+)', content)
    files_checked = int(m_files.group(1)) if m_files else None
    total_issues = int(m_total.group(1)) if m_total else None

    if files_checked is None:
        errors.append("REPORT: cannot parse Files checked count")
    if total_issues is None:
        errors.append("REPORT: cannot parse Total issues count")

    print(f"✅ Report: {len(content)} chars, files={files_checked}, issues={total_issues}")

# ── 2. _action-required.md ─────────────────────────────────────────

with open(ACTION) as f:
    ar = f.read()

ar_checks = [
    ("Has today's row", f"| 🔍 PENDING | {today[5:]} | Format |" in ar),
    ("Has today's entry", f"### 🔍 Format Validation — {today}" in ar),
    ("Has report link", f"wiki/reviews/{today}_format-report.md" in ar),
    ("Last updated today", f"**Last updated:** {today}" in ar),
    ("Approved entries preserved", '✅ APPROVED' in ar),
]
for label, ok in ar_checks:
    if not ok:
        errors.append(f"ACTION-REQUIRED: {label}")

# Cross-check: does _action-required mention the right issue count?
if total_issues is not None:
    short_date = today[5:]  # MM-DD
    # Capture the first number in the Issues column — works for both
    # WARNING-only format (e.g. "318W") and mixed ERROR+WARNING format
    # (e.g. "337 (1E+336W)"), where the first number is total issues.
    pat = re.compile(rf'\|\s*🔍\s*PENDING\s*\|\s*{re.escape(short_date)}\s*\|\s*Format\s*\|\s*(\d+)')
    m = pat.search(ar)
    if m:
        ar_count = int(m.group(1))
        if ar_count != total_issues:
            errors.append(f"ACTION-REQUIRED: issue count mismatch — report has {total_issues}, _action-required has {ar_count}")
    else:
        errors.append("ACTION-REQUIRED: cannot find Format row for today")

print(f"✅ _action-required.md: {len(ar)} chars, {sum(1 for _, ok in ar_checks if ok)}/{len(ar_checks)} checks pass")

# ── 3. MEMORY.md ───────────────────────────────────────────────────

with open(MEMORY) as f:
    mem = f.read()

today_entry = f"## {today}"
mem_checks = [
    ("Today entry exists", today_entry in mem),
    ("Above yesterday entry (prepended)", today_entry in mem.split("\n---")[0] if "\n---" in mem else True),
]
for label, ok in mem_checks:
    if not ok:
        errors.append(f"MEMORY.md: {label}")

# Cross-check: MEMORY.md counts match report
if files_checked is not None:
    ck = f"Files checked: {files_checked}" in mem
    if not ck:
        errors.append(f"MEMORY.md: file count mismatch — expected {files_checked}")
if total_issues is not None:
    ck = str(total_issues) in mem
    if not ck:
        errors.append(f"MEMORY.md: issue count mismatch — expected {total_issues}")

print(f"✅ MEMORY.md: {sum(1 for _, ok in mem_checks if ok)}/{len(mem_checks)} checks pass")

# ── 4. Final ───────────────────────────────────────────────────────

print(f"\n{'='*50}")
if errors:
    print(f"❌ VERIFICATION FAILED — {len(errors)} error(s):")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("✅ ALL CHECKS PASSED — Format validator output integrity verified")
    sys.exit(0)
