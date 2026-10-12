# Common Non-Compliant Patterns

> Recurring hygiene violations observed in practice.
> Updated: 2026-10-02

---

## Review file naming (wiki/reviews/)

The canonical format is `YYYY-MM-DD_<type>-report.md` where `<type>` is `format`, `output`, or `hygiene`.

Observed bad patterns and their fixes:

| Bad | Good | Fix action |
|---|---|---|
| `format-report-2026-05-30.md` | `2026-05-30_format-report.md` | Rename |
| `output-report-2026-06-14.md` | `2026-06-14_output-report.md` | Rename |
| `hygiene-report-2026-06-14.md` | `2026-06-14_hygiene-report.md` | Rename |
| `2026-05-28_validation-check.md` | `2026-05-28_output-report.md` | Rename |
| `2026-06-01_format-report-v2.md` | `2026-06-01_format-report.md` | Merge or overwrite |

**Systemic note:** Multiple historical reports accumulate with wrong naming. A bulk rename or archive pass is recommended once per quarter.

---

## Draft file naming (wiki/drafts/)

Slugs must use lowercase and hyphens only. Underscores are the most common violation.

| Bad | Good |
|---|---|
| `analysis_2026-advice.md` | `analysis-2026-advice.md` |
| `my_draft_file.md` | `my-draft-file.md` |

---

## Root-level orphans

Files and folders that frequently appear at root but are not in the whitelist:

- `openclaw-workspace-state.json` — **recurring since 2026-08-22; 3rd consecutive run flagged 08-24.** OpenClaw runtime workspace state (`version 1, setupCompletedAt 2026-05-12`), 69 bytes. Applied inline 08-23 morning (git rm → ~/.openclaw/) — runtime recreated <12h and ~10-min git auto-commit (`vault backup`) re-tracked it. Applied again 08-24 morning (removal commit `b568979f` 09:52 + `.gitignore` guard lines 88–89) — runtime recreated **10:00 SAME DAY: recycle < 1h, accelerating**. Gitignore guard now holds the REPO clean (file untracked + ignored; `git ls-files --error-unmatch` fails, `git check-ignore` hits) — only the disk-level orphan persists, and history retains pre-09:52 committed copies (cosmetic only; do NOT rewrite history). Writer still active on OpenClaw 2026.7.1-2; expected to end with the SQLite workspace-state refactor update. **08-24 verdict: STOP re-deleting (4th deletion changes nothing) — fix is either redirect the writer output path OR wait for the update.** **08-25: 4th consecutive run flagged (1E, only issue; 55,860 paths). Root cause CONFIRMED in vendor source (SKILL.md v1.21 pitfall #9: any dir containing AGENTS.md = workspace; state path CWD-relative by design, `dist/workspace-DkQ7irPD.js`). Disk file persisted all day (mtime 08-24 10:00, no fresh write on 08-25); git-level clean (untracked + `.gitignore:88` guard verified via `git check-ignore -v`). Per-run ERROR listing of this file remains correct and expected; do NOT re-escalate [SYSTEMATIC VIOLATION], do NOT recommend deletion-only fixes — reference SKILL.md pitfall #9 instead.**

- `RAW_BACKLOG.md` — leftover from manual tracking; should move to `wiki/drafts/` or `raw/articles/`
- `MEMORY.md` — agent memory file that leaked from `.hermes/` or `.openclaw/`
- `search/` — temporary search index; should be gitignored or removed
- `state/` — empty directory, **resolved since 07-20** (absent 07-20 through 07-22). Was recurring since 06-25. If it reappears, move inside `.hermes/` or `.openclaw/`; otherwise `rmdir`.
- `memory/` — old folder migrated to `.openclaw/memory/` in v1.2. **Resolved since 07-21** — absent 07-21 and 07-22 after Fix Agent bulk apply removed the folder and moved contents. Previously recurred 10 times (07-03 through 07-20). If it reappears, the writing process targets `memory/` instead of `.openclaw/memory/` — fix the process output path.
- `temp_content/` — scratch folder; should be removed after use

**Update 2026-07-22 — `memory/` and `state/` resolution confirmed:** Second consecutive clean run (51,944 paths) with zero root orphans. Both folders absent from 07-21 and 07-22 hygiene runs. Resolution appears permanent after Fix Agent bulk apply (07-20). If either reappears, escalate to process-level fix — do not treat as another file deletion.

**Update 2026-08-14 — `memory/` and `state/` RESURFACED after 4 clean runs (08-11 -> 08-13).** Hygiene 08-14 run (53,559 paths) found `memory/` (containing `memory/2026-08-14-0153.md`, an OpenClaw session log created 08:54) and an empty `state/`. The session-log file confirms the memory-log writer is emitting to KB root `memory/` instead of `.openclaw/memory/`. This is a process-level leak — file deletion is a stopgap; the writing process output path must be corrected. Escalated as [SYSTEMATIC VIOLATION] in the 08-14 report. 3-consecutive-clean streak broken.

**Update 2026-08-17 — `memory/` AND `state/` both resurfaced (4th consecutive run, 08-14→08-17).** Hygiene 08-17 run (53,578 paths) found `memory/` holding **6 files, all created 08-17**: 3 OpenClaw session logs (`2026-08-17-1325/1327/1329.md`, agent:main:main), `heartbeat-ok.md`, `heartbeat-poll.md`, and `fetch-status.md`. All 6 are **git-tracked** (`git ls-files memory/` confirmed) — they reach commits via the ~10-min auto `vault backup`, so filesystem deletion only removes the working copy and the committed copy resurrects on next checkout/sync. The writer runs multiple times daily. Fix MUST be root-cause (redirect the session/heartbeat/fetch writer output path from `memory/` → `.openclaw/memory/`) plus a committable removal (`git rm -r memory/` + commit). `state/` persists as an empty untracked phantom dir. Escalated as [SYSTEMATIC VIOLATION] in the 08-17 report. 08-11→08-13 clean streak remains broken.

**Update 2026-08-29 — `openclaw-workspace-state.json` 8th consecutive run flagged (08-22 → 08-29).** Hygiene 08-29 run (55,940 paths) — same status as 08-28: disk orphan persists (69 bytes, mtime 08-24 10:00, NO fresh write in 5 days), git-level clean (untracked + `.gitignore` guard via `git check-ignore`). Root cause CONFIRMED (SKILL.md v1.21 pitfall #9: OpenClaw treats any dir with AGENTS.md as workspace; state path CWD-relative by design). Per-pitfall ERROR listing remains correct; do NOT re-escalate [SYSTEMATIC VIOLATION], do NOT recommend deletion-only fixes. `wiki/HEARTBEAT.md` symlink also flagged 4th consecutive run (08-26 → 08-29, created 08-26 17:01); untracked + gitignored, same process-level leak — some sync tool mirrors the root `HEARTBEAT.md → .openclaw/HEARTBEAT.md` symlink into `wiki/`. `memory/` + `state/` clean 7th consecutive run.

**Update 2026-09-02 — `openclaw-workspace-state.json` 11th consecutive run flagged (08-22 → 09-02).** Status unchanged: 69 bytes, mtime 08-24 10:00, no fresh write in 9 days. Git-level clean (untracked + `.gitignore` guard). `wiki/HEARTBEAT.md` 7th consecutive run (08-26 → 09-02). **Major process-level fix:** [SYSTEMATIC VIOLATION] repos naming from 08-31 is now **RESOLVED** — all 6 raw/repos files from the 08-30 ingest batch were renamed with owner segments on 09-01 by Fix Agent (git commit `2ba955d1`, 09:57). 4/6 fully compliant; 2 residual (`MengTo_threeui`, `PostHog_posthog`) have uppercase owner — violates lowercase slug rule (folder-structure.md §8). **NEW pattern:** 8 `*-backup-2026-09-01.md` files in `wiki/drafts/` created by Fix Agent at 09:57 on 09-01 as pre-rename backups — all violate draft naming convention (date-prefix + underscore + `-backup-` suffix; 2 use `src_` prefix). Escalated as [SYSTEMATIC VIOLATION] in 09-02 report. `memory/` + `state/` clean 10th consecutive run.

**Update 2026-09-08 — both 09-02 escalations still outstanding after 6 days (12th run for root json, 8th for HEARTBEAT).** Hygiene 09-08 run (56,020 paths): 2 repos casing files (`MengTo_threeui`, `PostHog_posthog`) và 8 `*-backup-2026-09-01.md` drafts vẫn nguyên — Fix Agent chưa action trên report 09-02 (đã approved/applied với 2 items này DEFERRED). Carried forward per carry-forward rule — không re-escalation. Ghi nhận: hygiene runs bị skip 09-03→09-07 (không report nào), vault auto-commit cũng tạm dừng 09-05→09-07, resumed 09-08. `memory/` + `state/` clean 11th consecutive run.

**Update 2026-09-08 23:31 (evening re-scan) — ROOT JSON MIGRATED BY RUNTIME; NEW `.migrated.*` MARKER PATTERN.** Sự kiện 20:42: OpenClaw runtime tự migrate root `openclaw-workspace-state.json` → `~/.openclaw/workspace-state.json` (đích tồn tại từ 08-23) — kết thúc streak 12 run mà KHÔNG cần ai xóa (đúng dự báo pitfall #9: home restructure `/home/julius/.openclaw/` mtime 20:43). Hệ quả: (1) **MỚI — migration marker** `openclaw-workspace-state.json.migrated.<sha256>.<uuid>` (69 bytes, same content) nằm lại root, KHÔNG được .gitignore (pattern cũ chỉ cover tên gốc), và **đã bị commit** vào vault backup `b5e519fc` 20:45 → git-level đã pollute; fix = `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached`. (2) Root `HEARTBEAT.md` symlink biến mất cùng sự kiện — absence là compliant, không flag. (3) `wiki/HEARTBEAT.md` symlink giờ **DANGLING** (target `~/.openclaw/HEARTBEAT.md` không còn tồn tại) — lần 9 liên tiếp nhưng xóa giờ an toàn. Lesson: khi một leak được "resolved" bởi writer tự thay đổi hành vi, KIỂM TRA ARTIFACT MỚI nó để lại (marker/rename) — resolution hiếm khi sạch hoàn toàn; và `.gitignore` guards cần wildcard cho các biến thể (`*.migrated.*`) chứ không chỉ tên gốc.

---

## Heartbeat artifacts

Agent heartbeat files that sometimes leak outside their home:

- `raw/.last_heartbeat` — should be in `.hermes/` or `.openclaw/`, not `raw/`
- `wiki/HEARTBEAT.md` — **new variant (2026-08-10):** leaked to wiki/ root level, distinct from the wiki/reviews/ leak. Caught by wiki-root-level check before 08-10; now has dedicated HEARTBEAT_LEAK_PATHS classification.
- `wiki/reviews/HEARTBEAT.md` — should be in `.hermes/` or root (if symlink), not `wiki/reviews/`

**Recurring note (2026-08-10):** `wiki/HEARTBEAT.md` has been flagged every run since 08-07 (4th consecutive). This is a **process-level leak** — a runtime process writes HEARTBEAT.md to `wiki/` root instead of the agent home. The scan script now detects this specifically (added to `HEARTBEAT_LEAK_PATHS` 2026-08-10).

**Recurring note (2026-06-27):** `wiki/reviews/HEARTBEAT.md` has been flagged every run since 06-25. Fix Agent deleted it 2026-06-27 09:34 but it reappeared by 23:30. This is a **process-level leak** — a runtime process writes HEARTBEAT.md to `wiki/reviews/` instead of the agent home. File deletion alone will not resolve it; the writing process must be identified and its output path corrected.

**Resolution (2026-06-28):** The HEARTBEAT leak was resolved. The 2026-06-28 hygiene run (23:30) scanned 51,528 paths and found zero HEARTBEAT artifacts in `wiki/reviews/` or `raw/`. The root-level symlink `HEARTBEAT.md → .openclaw/HEARTBEAT.md` is correctly placed. If the leak recurs, flag as ERROR and escalate to process-level fix.

---

## Raw content naming — papers vs standard types

`raw/papers/` uses a different naming convention from other raw types:

| Type | Pattern | Example |
|---|---|---|
| Standard (`articles`, `posts`, etc.) | `YYYY-MM-DD_<slug>.md` | `2026-05-07_anthropic-claude-code.md` |
| Papers | `YYYY-MM-DD_<author>_<title>.md` | `2026-05-22_ning-et-al_code-as-agent-harness.md` |

**Pitfall:** A single `RE_RAW_CONTENT` regex that matches `YYYY-MM-DD_<slug>.md` will false-positive on papers. The scan script must check for `RE_RAW_PAPERS` before falling through to `RE_RAW_CONTENT` when processing `raw/papers/`.

---

## Scan script false-positive traps

Three patterns that caused false positives in the 2026-06-27 run:

1. **Archive regex prefix** — `RE_REVIEW_ARCHIVE` must use `^wiki/reviews/archive/` not `^archive/`. `os.walk` relative paths start from the repo root, so the full `wiki/reviews/archive/` prefix is needed.

2. **Papers naming** — `raw/papers/` uses `YYYY-MM-DD_<author>_<title>.md` (two slug segments separated by underscore). A single `RE_RAW_CONTENT` will flag every paper as non-compliant. Must add `RE_RAW_PAPERS` and check it first.

3. **Whitelisted files with uppercase** — `context/USER.md` is explicitly whitelisted by name but fails a generic lowercase-hyphen naming check. Skip the naming check for files that appear by name in an explicit whitelist (`CONTEXT_FILES`, `WIKI_META_FILES`). Only apply naming rules to content files (concepts, sources, tags, topics, drafts).

---

## Agent home content confusion

`.hermes/` and `.openclaw/` contain agent runtime files. The Hygiene Inspector should NOT flag deep internals as orphans. However, user content (e.g., `src_*.md`, `YYYY-MM-DD_*.md`, or article-like files) placed at the first level inside these agent homes IS a real orphan.

**Example real orphan:**
- `.openclaw/memory/2026-05-26.md` — user content inside agent home

**Example false positive (do NOT flag):**
- `.hermes/hermes-agent/agent/tool_executor.py` — runtime code
- `.hermes/cron/output/284427e7c7fa/2026-05-12_23-30-01.md` — cron output
- `.hermes/skills/creative/touchdesigner-mcp/references/particles.md` — skill reference

**Rule:** Skip `.hermes/` and `.openclaw/` at depth > 1 for orphan checks.

---

## 2026-09-30 — `git check-ignore` SKIPS tracked files (false evidence for many runs)

**The trap.** `git check-ignore` (plain form) **does not report tracked files**. Git docs: tracked files are not shown. So for a file that is already committed, plain `check-ignore` returns **exit 1 with no output** — indistinguishable from "no rule exists".

Every run up to and including 2026-09-29 used the plain form. That produced two different wrong claims:

- "`.gitignore:37` CÓ rule" — inferred from a plain-`check-ignore` rc that actually proved nothing.
- "`check-ignore` exit 1 ⇒ NOT ignored" — used on the two `.migrated.*` markers (2026-09-29 E9) to call them untracked-and-not-ignored.

**The rule.** For every hit, run **both**:

```bash
git ls-files -s -- <path>              # empty  => untracked (definitive)
git check-ignore --no-index -v -- <path>   # rule in isolation, ignores index state
git check-ignore -v -- <path>           # only meaningful for UNTRACKED files
```

Then classify: tracked + rule exists = **RULE-EXISTS-BUT-INEFFECTIVE**; tracked + no rule = **TRACKED-NO-RULE**; untracked + rule = correctly ignored; untracked + no rule = real leak.

Proven 2026-09-30 on `.hermes/auth.json`: plain → `rc=1` no output; `--no-index` → `.gitignore:37:.hermes/auth.json` `rc=0`. Re-probed 21 files.

**Corollary:** the same "plain exit code on a tracked file" error applies to `git ls-files` (see pitfall #7) — never infer state from an exit code alone; assert on **output emptiness**.

## 2026-09-30 — Grep filenames, not key names, to inventory secret exposure

2026-09-29 found `.hermes/auth.json` by grepping key names (`access_token`/`api_key`) inside that one file, and reported "at least 4 ERRORs". Grepping **filenames** in HEAD across both agent homes found **7 auth-named tracked files** — 4 of them in `.openclaw/` and 1 in `.hermes/state-snapshots/` were missed entirely. Two of those had *no* key names at all, so a key-name grep can never reach them.

**Rule:** inventory exposure by `git ls-tree -r HEAD --name-only | grep -Ei '(auth|token|secret|credential|apikey|\.env)'` **excluding `skills/`** (skill docs legitimately mention auth). Then per-file `ls-files` + `check-ignore --no-index` + commit count. Only then report. Never read values.

**Also probe by EXTENSION, not by name.** A name-grep misses runtime DBs that carry the same blast radius: `.hermes/kanban.db`, `-shm`, `-wal` (141 commits each), `projects.db`, `verification_evidence.db` (345 commits), `.hermes/state-snapshots/` (7 files), `config.yaml.bak.*` (18/18). 9 of 9 runtime patterns had **no `.gitignore` rule**, while `.openclaw/*.bak` and `.hermes/state.db*` did — the `.hermes/` zone is unprotected.

## 2026-09-30 — Publish dir counts with an explicit, reproducible shape

The 2026-09-29 headline "1,735 files + 70 dirs" was not reproducible for the dir half: today 9 root + 23 content-zone (recursive) + 42 agent-home L1 = **74**, and no subset yields 70. Never carry a dir total forward without stating its composition inline, or the next run reads the delta as structural growth.

Counting shape used from 2026-09-30 on (all with `find -type f -o -type l` / `find -type d`, sockets excluded):

- **files** = content zones (recursive) + root regular files/symlinks + agent-home level-1 files
- **dirs** = root dirs + content-zone dirs (recursive) + agent-home level-1 dirs

Corroborate any file delta with `git status --porcelain -uall` split `??` vs `M` (pitfall #13) — a `find -newer` delta is not evidence on its own.

## 2026-09-30 — agent-home level-1 count is VOLATILE, not just socket-prone

Removing sockets (pitfall 09-29) is **not sufficient** for a reproducible scope total. The agent homes' first level churn on their own: on 2026-09-30 the count went **99 at 23:30 → 98 at 23:55** within one run. `.hermes/.skills_prompt_snapshot.json` (per-session artifact, mtime 23:15) was deleted by the runtime, while three `state.db.malformed-backup-20260617_082024{,-shm,-wal}` files appeared. Of the 98, **46 look volatile** (`.db*`, `-shm`, `-wal`, `.lock`, `.pid`, `.sock`, `*cache*`, `.etag`, `.log`, `spawn-ledger`, `gateway_state`, `channel_directory`, `processes.json`).

**Rule:** a published scope total containing agent-home L1 is **not reproducible** even with the correct socket filter. Either exclude agent-home L1 from the published total, or publish it separately and label it volatile. When both a pre-write and post-write figure are needed, state which component is stable:

> "1.751 files total — **only 1.653 stable** (1.641 content zones + 11 root); 98 agent-home L1 files are **volatile** (99 at scan → 98 at verify)."

Also: a **transient per-session file must never be counted as KB growth**, and its disappearance must not be reported as a resolved issue. Verify volatility empirically before blaming the counting method — sample the same count 5× over ~30s; if it is stable *now*, the change came from a runtime event during the run, which is itself the finding.

## 2026-10-02 — `find -o` precedence silently narrows the scope test

`find .hermes/checkpoints -type f -o -type l | wc -l` looked correct but reported **6.814** where the grouped form
`find .hermes/checkpoints \( -type f -o -type l \) | wc -l` also gives 6.814 — *identical here*, which is exactly why the trap survives: the un-grouped form works only when the `-print` binds to the whole expression, and `find` implies `-print` on the **last** branch only. In practice a command like

```bash
find . -path ./.git -prune -o -newerct <ref> -print
```

returned **0** for the whole tree because `-print` bound to the `-newerct` branch alone and every non-matching path was pruned away silently. The `-newerct` form also fails outright when given a **file** reference: `find <file> -newerct <file>` errors with *"Không thể tìm biết cách giải thích … dạng ngày hay giờ"*.

**Rule:** group the type test explicitly — `\( -type f -o -type l \) -print` — and prefer a Python `stat.S_ISREG/S_ISLNK` filter when you need the same definition in two places (scan + verify). A one-liner that returns `0` for a tree you just measured non-zero is a scoping bug, not an empty tree.

## 2026-10-02 — The dir-count shape differs between `os.walk` and `find -type d`

Reporting 74 dirs while the verify recomputed 70 was **not** KB drift: `os.walk("raw")` yields `("raw", [subdirs], [files])` for the zone itself, so `len(dn)` counts only *children*. Summing `len(dn)` across four zones gives **19** (23 minus the 4 zone roots). `find raw wiki context scripts -type d` gives **23**, because each zone root is a directory too.

**Rule:** the content-zone dir term must include the zone root (`if dp == zone: n += 1`), and the published label must say so — "23 vùng nội dung (**bao gồm thư mục gốc vùng**)". Same trap for the root-files term: `cnt(".")` walks the **entire tree** (243K files here), while the intended root term is only top-level entries — use a listdir-based count and assert it (11) or the verify fails for a reason that has nothing to do with the KB.

## 2026-10-02 — `wiki/wiki.md` is whitelisted; a "file at wiki/ root" check must not flag it

§7's tree lists `wiki.md ✓ required (level 1 index)` on the same lines that also say *"No files at `wiki/` root level"*. A scanner that treats every top-level file in `wiki/` as an orphan therefore emits a **false ERROR on a file the spec requires**. Proven: the 10-02 run reported `ERROR Path wiki/wiki.md` and a phantom 6th ERROR group.

**Rule:** in the `wiki/` root check, `continue` on the whitelisted index names before falling through to the generic orphan error. Same applies to `raw/raw.md` in `raw/`. When a scanner ERROR survives to the report, **grep the spec for the exact name first** — the spec tree and the spec Rules section can disagree (see W3), and the tree's explicit `✓ required` line wins for a file's existence. Record the correction as a *script* defect in the report, not as a KB finding.
