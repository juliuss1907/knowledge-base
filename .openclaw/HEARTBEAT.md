# HEARTBEAT

## Agent health
- Status: healthy
- Last checked: 2026-05-18 07:30:00 Asia/Saigon
- Host: `julius-vps`
- Host uptime: `up 5 days, 16 hours, 17 minutes`
- Load average: healthy; `0.90, 0.97, 0.69`
- Memory: healthy; 13Gi total, available capacity OK
- Swap: healthy

## OpenClaw checks
- Runtime: responsive
- Workspace: `/home/julius/knowledge-base`
- Disk `/`: healthy; 17% used, 182G free
- Disk `/home/julius/knowledge-base`: healthy; 17% used, 182G free
- Raw backlog: 1 file(s) with `status: unprocessed`
- Inbox markers: 1 active marker outside identity/reference/runtime files
- Pending Hermes reports: tracked in `wiki/reviews/_action-required.md`
- Approved Fix Agent actions pending: present in `wiki/reviews/_action-required.md`

## Spot checks
- Raw backlog scan: issues present; 1 raw file(s) unprocessed: `raw/articles/2026-05-17_aaron-wright-ai-agents-legal-body.md`
- Concept source-link spot check: issues present; concept files still include deprecated `[[wiki/sources/...]]` source-link patterns
- Deprecated wikilinks: issues present; files still contain `[[wiki/sources/...]]` patterns in `wiki/concepts/`
- Source frontmatter scan: issues present; source files still contain legacy `date_ingested` fields, including `wiki/sources/src_how-ai-productivity-fails.md` and `wiki/sources/src_how-some-people-become-unrecognizable.md`
- Pending review scan: approved fixes and pending reports still tracked in `wiki/reviews/_action-required.md`
- Inbox scan: 1 active `#agent/inbox` marker found outside identity/reference/runtime files
- Git scan: working tree has existing changes: `m .hermes/hermes-agent`

## Last result
HEARTBEAT_ISSUES_PRESENT
