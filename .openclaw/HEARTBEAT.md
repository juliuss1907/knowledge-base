# HEARTBEAT

## Agent health
- Status: healthy
- Last checked: 2026-05-18 08:30:00 Asia/Saigon
- Host: `julius-vps`
- Host uptime: `up 5 days, 17 hours, 17 minutes`
- Load average: healthy; `0.96, 0.69, 0.57`
- Memory: healthy; available capacity OK
- Swap: healthy

## OpenClaw checks
- Runtime: responsive
- Workspace: `/home/julius/knowledge-base`
- Disk `/`: healthy; 16% used, ~181G free
- Disk `/home/julius/knowledge-base`: healthy; 16% used, ~181G free
- Raw backlog: 0 file(s) with `status: unprocessed`
- Inbox markers: active marker count needs rescan; previous marker references are in heartbeat/runtime files
- Pending Hermes reports: tracked in `wiki/reviews/_action-required.md`
- Approved Fix Agent actions pending: present in `wiki/reviews/_action-required.md`

## Spot checks
- Raw backlog scan: clean; `raw/articles/2026-05-17_aaron-wright-ai-agents-legal-body.md` is now `status: processed`
- Concept source-link spot check: issues present; concept files still include deprecated `[[wiki/sources/...]]` source-link patterns
- Deprecated wikilinks: issues present; files still contain `[[wiki/sources/...]]` patterns in `wiki/concepts/`
- Source frontmatter scan: issues present; source files still contain legacy `date_ingested` fields, including `wiki/sources/src_how-ai-productivity-fails.md` and `wiki/sources/src_how-some-people-become-unrecognizable.md`
- Pending review scan: approved fixes and pending reports still tracked in `wiki/reviews/_action-required.md`
- Git scan: working tree has existing changes; no cleanup performed by heartbeat

## Last result
HEARTBEAT_ISSUES_PRESENT
