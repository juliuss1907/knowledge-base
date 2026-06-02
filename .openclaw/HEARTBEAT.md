# HEARTBEAT.md — OpenClaw System Status

> Automated health check every 30 minutes
> Last check: 2026-06-02 14:00 (Asia/Saigon)

---

## Status: ⚠️ ATTENTION NEEDED

## Quick Checks

| Check | Result | Notes |
|---|---|---|
| **Inbox** | ✅ Clean | No #agent/inbox files |
| **Raw backlog** | ✅ Clean | 0 unprocessed files |
| **Concept backlinks** | ⚠️ Weak | Sample: concepts still with 0 links |
| **Pending reviews** | ⚠️ 1 pending | Fix Agent #2 partially applied |

---

## Raw Inventory

| Folder | Files |
|---|---|
| articles | 25 |
| papers | 4 |
| posts | 8 |
| repos | 1 |
| videos | 5 |
| websites | 4 |
| **Total** | **47** |

---

## Wiki Inventory

| Folder | Count |
|---|---|
| sources | 41 |
| concepts | 186 |

---

## Pending Reviews

**1 report** — `wiki/reviews/_action-required.md`

Format Validator (2026-06-01-v2): **PARTIALLY APPLIED**
- 10 invalid sub_tags + 6 empty remaining after Fix Agent #2
- Output Validator (2026-06-01-v2): 4 systemic issues requiring re-compile

**Action required by:** Julius

---

## Concept Backlinks — Systemic Issue

Sample check shows **all sampled concepts have 0 backlinks**:
- `ashbys-law.md`: 0 links in sample
- Other recent concepts: no cross-references

**This suggests a systemic compilation problem** — concepts created without back-references to sources. Requires re-compile of affected files after Format Validator issues are resolved.

---

## Next Scheduled Actions

- **Index Agent**: 21:00 (daily index update)
- **Readwise sync**: 07:00 tomorrow

---

*Next heartbeat: 14:30*