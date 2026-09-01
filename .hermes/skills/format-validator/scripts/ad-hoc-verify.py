#!/usr/bin/env python3
"""Reusable ad-hoc verification for the format-validator cron run.

Replaces the hand-written /tmp/hermes-verify-format-<DATE>.py pattern. The recurring
regex bug (doubled backslashes 08-26/08-27, stray `:` in negated class 08-30/08-31)
is eliminated by hardcoding the SINGLE known-good pattern `[^\d]*` here and deriving
all expected counts from the report's own header — nothing to hand-type, nothing to
re-derive, no raw-string escaping traps.

Usage (run from KB root):
    python3 .hermes/skills/format-validator/scripts/ad-hoc-verify.py [YYYY-MM-DD]

Default date: today. Returns exit 0 (PASS) or 1 (FAIL) and prints one-line verdicts.

This is AD-HOC verification of the three changed files (report, _action-required.md,
MEMORY.md) — distinct from canonical verify_integrity.py (suite green). Run BOTH after
writing all three files.
"""
import os
import re
import sys
from datetime import date

KB = "/home/julius/knowledge-base"
today = sys.argv[1] if len(sys.argv) > 1 else date.today().isoformat()

report_path = os.path.join(KB, f"wiki/reviews/{today}_format-report.md")
ar_path = os.path.join(KB, "wiki/reviews/_action-required.md")
mem_path = os.path.join(KB, ".hermes/MEMORY.md")

# Report doesn't exist yet -> caller is too early; that's expected mid-run, not a failure
if not os.path.exists(report_path):
    print(f"⚠️  {today}_format-report.md not found — run after writing the report")
    sys.exit(0)

report = open(report_path, encoding="utf-8").read()
ar = open(ar_path, encoding="utf-8").read()
mem = open(mem_path, encoding="utf-8").read()

# Derive expected counts from the report header so nothing is hardcoded/manual
def num(report, label):
    # [^\d]* = the ONLY safe pattern: any non-digit between label and the number.
    # Do NOT use \s or \d inside a raw string (recurring trap) and do NOT put a
    # stray char (colon/space) inside the negated class before ^.
    m = re.search(re.escape(label) + r"[^\d]*(\d+)", report)
    return int(m.group(1)) if m else None

total = num(report, "Total issues") or num(report, "Issues found")
errors_n = num(report, "ERRORs")
warnings_n = num(report, "WARNINGS")
files_n = num(report, "Files checked")
if files_n is None:
    # fall back to bold display line
    files_n = num(report, "**Files checked**")

errors = []

# --- Report header fields (literal substrings verify_integrity.py requires) ---
for label, needle in [
    ("Status pending", "**Status:** pending"),
    ("Validator", "**Validator:** format-validator"),
    ("INFOS", "**INFOS:** 0"),
    ("Files checked table", "Files checked |"),
    ("Escalations section", "## Escalations"),
    ("Verification section", "## Verification"),
    ("Delta marker", "Δ from"),
]:
    if needle not in report:
        errors.append(f"report missing: {label}")
# bold forms require space-before-colon (space keeps **WARNINGS** a substring)
if f"**ERRORs**: {errors_n}" not in report:
    errors.append(f"report missing bold **ERRORs**: {errors_n}")
if f"**WARNINGS**: {warnings_n}" not in report:
    errors.append(f"report missing bold **WARNINGS**: {warnings_n}")
if total is None:
    errors.append("report: cannot parse total issues count")

# --- _action-required.md: today's Format row + sibling rows survive rewrite ---
row_re = re.compile(r"\|\s*🔍\s*PENDING\s*\|\s*" + today[5:] + r"\s*\|\s*Format\s*\|\s*(\d+)")
m = row_re.search(ar)
if not m:
    errors.append(f"AR missing 🔍 PENDING {today[5:]} Format row")
elif int(m.group(1)) != total:
    errors.append(f"AR Format issues cell {m.group(1)} != report total {total}")
if f"wiki/reviews/{today}_format-report.md" not in ar:
    errors.append("AR missing full report path link")
# any OTHER validator's same-day row (Output/Hygiene) must also survive the rewrite.
# Sibling row can be 🔍 PENDING or ✅ APPLIED (e.g. Hygiene applied earlier the same day,
# observed 2026-09-01); if neither form exists, only allow it when that sibling produced
# NO report today (SILENT run, e.g. Output with 0 new files — observed 2026-09-01).
for sib in ("Output", "Hygiene"):
    sib_pending = re.search(r"🔍\s*PENDING\s*\|\s*" + today[5:] + r"\s*\|\s*" + sib, ar)
    sib_applied = re.search(r"✅\s*APPLIED\s*\|\s*" + today[5:] + r"\s*\|\s*" + sib, ar)
    sib_report = os.path.join(KB, f"wiki/reviews/{today}_{sib.lower()}-report.md")
    if not sib_pending and not sib_applied and os.path.exists(sib_report):
        errors.append(f"AR missing {sib} {today[5:]} row (report exists but row dropped)")
# pending count — tolerant of ** wrapper and any non-digit gap
m = re.search(r"awaiting review:[^\d]*(\d+)", ar)
if not m:
    errors.append("AR cannot parse 'Pending reports awaiting review' count")
if "✅ APPROVED" not in ar:
    errors.append("AR missing ✅ APPROVED marker")
if f"**Last updated:** {today}" not in ar:
    errors.append("AR Last updated not today")

# --- MEMORY.md ---
if f"## {today} " not in mem:
    errors.append("MEMORY missing today's entry")
if f"Files checked: {files_n}" not in mem:
    errors.append(f"MEMORY missing plain 'Files checked: {files_n}' line")
m = re.search(r"Issues found[^\d]*(\d+)", mem)
if not m or int(m.group(1)) != total:
    errors.append(f"MEMORY issues count {m.group(1) if m else None} != report total {total}")

if errors:
    print("❌ AD-HOC VERIFICATION FAILED")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print(f"✅ AD-HOC VERIFICATION PASSED — {today}: {total} issues "
      f"({errors_n}E+{warnings_n}W), {files_n} files, AR+MEMORY consistent")
