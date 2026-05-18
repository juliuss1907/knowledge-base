# HEARTBEAT

## Agent health
- Status: healthy
- Last checked: 2026-05-18 19:30:00 Asia/Saigon
- Host: `julius-vps`
- Host uptime: `up 6 days, 4 hours, 17 minutes`
- Load average: healthy; `0.55, 0.33, 0.31` at current sample
- Memory: healthy; 5.7Gi available
- Swap: healthy; 13Gi free / 17Gi total

## OpenClaw checks
- Runtime: responsive
- Workspace: `/home/julius/knowledge-base`
- Disk `/`: healthy; 17% used, 182G free
- Disk `/home/julius/knowledge-base`: healthy; 17% used, 182G free
- Raw backlog: 1 file(s) with `status: unprocessed`
- Inbox markers: 0 actionable markers found in `Tasks/`
- Pending Hermes reports: actionable entries remain in `wiki/reviews/_action-required.md`
- Approved Fix Agent actions pending: present in `wiki/reviews/_action-required.md`

## Spot checks
- Raw backlog scan: issues present
  - `raw/articles/2026-05-18_hermes-analyst-workflow-essentials.md`
- Concept source-link scan: issues present; 20 concept files still contain deprecated `[[wiki/sources/...]]` links
- Source frontmatter scan: issues present; 2 source files still contain legacy `date_ingested` fields:
  - `wiki/sources/src_how-ai-productivity-fails.md`
  - `wiki/sources/src_how-some-people-become-unrecognizable.md`
- Pending review scan: actionable entries remain in `wiki/reviews/_action-required.md`
- Git scan: working tree has existing changes outside heartbeat scope:
  - ` m .hermes/hermes-agent`

## Last result
HEARTBEAT_ISSUES_PRESENT
