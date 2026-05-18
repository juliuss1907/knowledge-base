# HEARTBEAT

## Agent health
- Status: healthy
- Last checked: 2026-05-18 11:00:00 Asia/Saigon
- Host: `julius-vps`
- Host uptime: `up 5 days, 19 hours, 47 minutes`
- Load average: healthy; `0.84, 0.48, 0.40`
- Memory: healthy; 6.3Gi available
- Swap: healthy; 13Gi free

## OpenClaw checks
- Runtime: responsive
- Workspace: `/home/julius/knowledge-base`
- Disk `/`: healthy; 17% used, ~182G free
- Disk `/home/julius/knowledge-base`: healthy; 17% used, ~182G free
- Raw backlog: 0 file(s) with `status: unprocessed`
- Inbox markers: 0 actionable markers found; existing matches are identity/session references
- Pending Hermes reports: 5 pending reports in `wiki/reviews/_action-required.md`
- Approved Fix Agent actions pending: present in `wiki/reviews/_action-required.md`
- Cron health: `Compile Daily` and `Index Update` enabled; Compile Daily next run scheduled

## Spot checks
- Raw backlog scan: clean
- Concept source-link spot check: issues present; 20 files still include deprecated `[[wiki/sources/...]]` source-link patterns in `wiki/concepts/`
- Deprecated wikilinks: issues present; concept files still contain `[[wiki/sources/...]]` patterns
- Source frontmatter scan: issues present; 2 source files still contain legacy `date_ingested` fields:
  - `wiki/sources/src_how-ai-productivity-fails.md`
  - `wiki/sources/src_how-some-people-become-unrecognizable.md`
- Pending review scan: 5 pending reports in `wiki/reviews/_action-required.md`; approved Fix Agent actions still pending
- Git scan: working tree has existing change outside heartbeat scope: `.hermes/hermes-agent`

## Last result
HEARTBEAT_ISSUES_PRESENT
