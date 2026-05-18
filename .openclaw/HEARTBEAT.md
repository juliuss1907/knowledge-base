# HEARTBEAT

## Agent health
- Status: healthy
- Last checked: 2026-05-18 21:00:00 Asia/Saigon
- Host: `julius-vps`
- Host uptime: `up 6 days, 5 hours, 47 minutes`
- Load average: healthy; `0.75, 0.56, 0.44` at current sample
- Memory: healthy; `5.6Gi` available of `13Gi`
- Swap: healthy; `4.0Gi` used of `17Gi`

## OpenClaw checks
- Runtime: responsive
- Workspace: `/home/julius/knowledge-base`
- Disk `/`: healthy; `17%` used, `182G` free
- Disk `/home/julius/knowledge-base`: healthy; `17%` used, `182G` free
- Raw backlog: 6 file(s) with `status: unprocessed`
- Inbox markers: 0 actionable markers found in `Tasks/`
- Pending Hermes reports: actionable entries remain in `wiki/reviews/_action-required.md`
- Approved Fix Agent actions pending: present in `wiki/reviews/_action-required.md`

## Spot checks
- Raw backlog scan: issues present
  - `raw/articles/2026-05-18_1-month-with-hermes-ive-been-using-wrong.md`
  - `raw/articles/2026-05-18_google-guide-optimizing-generative-ai-search.md`
  - `raw/articles/2026-05-18_hermes-as-a-real-time-analyst.md`
  - `raw/articles/2026-05-18_3-things-learnt-3-weeks-hermes-analyst.md`
  - `raw/articles/2026-05-18_hermes-200-30-skills-3-worth-it.md`
  - `raw/articles/2026-05-18_hermes-analyst-workflow-essentials.md`
- Concept source-link scan: issues present; 20 concept files still contain deprecated `[[wiki/sources/...]]` links
- Sample concept source-link check:
  - `wiki/concepts/philosopher-syndrome.md`: frontmatter canonical, body still deprecated
  - `wiki/concepts/shift-left-testing.md`: frontmatter and body still deprecated
  - `wiki/concepts/codified-taste.md`: frontmatter and body still deprecated
- Source frontmatter scan: issues present; 2 source files still contain legacy `date_ingested` fields:
  - `wiki/sources/src_how-ai-productivity-fails.md`
  - `wiki/sources/src_how-some-people-become-unrecognizable.md`
- Pending review scan: actionable entries remain in `wiki/reviews/_action-required.md`
- Git scan: working tree has existing changes outside heartbeat scope:
  - ` m .hermes/hermes-agent`
  - ` M raw/articles/articles.md`
  - `?? raw/articles/2026-05-18_google-guide-optimizing-generative-ai-search.md`

## Last result
HEARTBEAT_ISSUES_PRESENT
