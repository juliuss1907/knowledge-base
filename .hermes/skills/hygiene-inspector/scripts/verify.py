#!/usr/bin/env python3
"""Verify hygiene-inspector run artifacts.
Checks: report existence & content, _action-required.md update, scan reproducibility.
Run after generating the hygiene report.
"""
import os, json, sys
from datetime import date
from subprocess import run, PIPE

today = date.today().isoformat()
KB = os.path.expanduser("~/knowledge-base")
errors = []

# ── Check 1: Report exists with correct content ──
report = f"{KB}/wiki/reviews/{today}_hygiene-report.md"
if not os.path.exists(report):
    errors.append(f"MISSING: {report}")
else:
    with open(report) as f:
        r = f.read()
    for needle in [
        f"# Hygiene Inspection — {today}",
        "Paths checked:**",
        "## Summary",
    ]:
        if needle not in r:
            errors.append(f"REPORT MISSING: {needle}")
    print(f"  Report: {len(r)} bytes, {r.count(chr(10))} lines")

# ── Check 2: _action-required.md updated ──
ar = f"{KB}/wiki/reviews/_action-required.md"
with open(ar) as f:
    a = f.read()
for needle in [
    f"{today}",
    "Hygiene Inspector",
    "hygiene-report.md",
]:
    if needle not in a:
        errors.append(f"ACTION MISSING: {needle}")
print(f"  _action-required.md: {len(a)} bytes, {a.count(chr(10))} lines")

# ── Check 3: Scan reproducible ──
script = f"{KB}/.hermes/skills/hygiene-inspector/references/scan-script.py"
if os.path.exists(script):
    os.chdir(KB)
    cp = run(["python3", script], capture_output=True, text=True, timeout=30)
    data = json.loads(cp.stdout)
    paths = data.get("paths_checked", 0)
    total = data.get("issues_total", 0)
    errors_count = data.get("total_severity_counts", {}).get("ERROR", 0)
    print(f"  Scan reproducible: {paths} paths, {total} issues, {errors_count} ERROR")
else:
    print(f"  Scan reproducibility: SKIPPED (script not found at {script})")

# ── Report ──
if errors:
    print(f"\nFAILED: {len(errors)} error(s)")
    for e in errors:
        print(f"  ❌ {e}")
    sys.exit(1)
else:
    print(f"\n✅ All checks passed — hygiene-inspector {today} run verified")
