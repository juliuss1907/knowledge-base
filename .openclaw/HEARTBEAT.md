# HEARTBEAT.md — OpenClaw System Status

**Last check:** 2026-05-31 15:30 (Asia/Saigon)  
**Agent:** Kara (OpenClaw AX400)  
**Status:** ⚠️ 3 pending Hermes reports

---

## Quick Status

| Zone | Status | Notes |
|------|--------|-------|
| raw/ | ✅ | 0 unprocessed files |
| wiki/ | ✅ | 172 concepts, 38 sources, 19 tags |
| Pending reviews | ⚠️ | 3 reports awaiting Julius approval |

---

## Issues Requiring Attention

**3 Hermes reports pending (since 2026-05-30):**
- Format: 16 issues (empty sub_tags + invalid tags + field order)
- Output: 18 issues (empty sources + invalid status:stub)
- Hygiene: 2 unauthorized folders (memory/, search/ — outside Kara's scope)

**Total:** 36 issues awaiting Julius approval  
**Details:** `wiki/reviews/_action-required.md`

---

## Commands

```
approve format    # Approve Format Validator report
approve output    # Approve Output Validator report
approve hygiene   # Approve Hygiene Inspector report
openclaw fix apply  # Apply approved fixes
```

---

## Resolved This Session

*None*

---

*Next heartbeat: 16:00 (30 min)*