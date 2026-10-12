# Lessons from cleanup-commit runs (2026-10-04)

A "cleanup commit" — someone adding `.gitignore` rules and `git rm -r --cached` for agent-home runtime
— is the single highest-value event a Hygiene run can encounter, and the single most likely event to
make yesterday's carry-forward claims **false**. Both facts were proven on the 2026-10-04 run.

## 1. Check HEAD FIRST, before writing anything

Sibling Output/Format validators write their reports at ~23:00–23:15 on the same day. A manual cleanup
commit lands at any hour. So the first commands of every run must be:

```bash
git log -1 --format='%h %ci %s'                 # local HEAD + when
git ls-remote --heads origin                   # remote master (read-only, no fetch)
git log -1 --format='%h' <LAST HYGIENE REPORT>  # what the previous report assumed
```

If HEAD moved since the last hygiene report, **every carry-forward claim in that report is stale**.
Re-probe all of them with `git ls-files -s` + `git check-ignore --no-index -v`. Never restate
"E1–E13 carry-forward, 0 resolved" from the prior report's text — measure it.

On 2026-10-04 this flipped the entire run: two manual commits (`3b891e34` 19:14, `68f644e7` 19:41)
meant **9 of 13** carry-forward ERROR groups were closed, **3 were RESOLVED**, and one **new** group
(38 tracked files with pre-existing-but-ineffective ignore rules) surfaced. Reporting "0 resolved"
would have been flatly wrong in both directions.

## 2. `.gitignore` rules do NOT untrack files — residue is the actionable number

A cleanup commit's own message lists what it removed. That list is **not** proof of completeness.
A file committed *before* its rule was added keeps a matching `.gitignore` rule (so
`check-ignore --no-index` exits 0 with output) while remaining in `git ls-files`. This is pitfall
#12b's "rule exists but is ineffective" class.

So the correct completeness check is a residue diff, not a rule check:

```bash
# what the cleanup touched
git show --name-status <cleanup-sha> | grep -E '^D' | cut -f2 | sed 's#/[^/]*$##' | sort -u

# what still matches the same patterns TODAY
git ls-files .hermes .openclaw \
  | grep -E '\.db|\.db-|\.lock|\.bak|curator_backups|checkpoints|state-snapshots|auth|MEMORY\.md|config\.yaml'
```

Report **the residue count** ("38 files remain tracked") rather than the rule count. On 10-04 the
residue was 38 files across 4 groups, and 3 of those 4 already had ignore rules — so the fix is a
single `git rm -r --cached` on those exact paths, with **no new `.gitignore` entry**. Telling
Julius to add rules he already has would waste the cycle.

## 3. Owner segments in `raw/repos/` may contain hyphens

`^\d{4}-\d{2}-\d{2}_[a-z0-9]+_[a-z0-9\-_]+\.md$` **fails** on a legitimate owner like `tt-a1i`,
because `[a-z0-9]+` excludes `-`. §6 requires two segments; §8's slug rule explicitly allows hyphens.

Use `[a-z0-9][a-z0-9-]*` per segment. Proven 10-04: the old pattern flagged 1 false positive; the
fixed pattern yields **7/8 valid, 0 violations** in `raw/repos/`.

Generalise: **before any per-file naming WARNING is published, run the regex over every file in the
zone.** If a correct file fails, the regex is wrong, not the file — same reflex as pitfall #17.
Record it in the run's self-audit block so the next run inherits the fix.

## 4. Verify "git repo" claims instead of inheriting them

`.hermes/checkpoints/` had been called a "nested git repo" by reports on 09-29, 10-01, 10-02 and
10-03. On 10-04 it was tested properly and the claim is **false**:

```bash
find . -maxdepth 5 -type d -name .git -not -path './.git'   # → ONLY .hermes/hermes-agent/.git
git -C .hermes/checkpoints rev-parse --git-dir              # → /home/julius/knowledge-base/.git
```

`store/HEAD` existing proves only that a git object store exists there — which is Hermes's own
store, misfiled. The whole KB has **exactly one** nested repo. Assert this per run rather than
trusting the previous report's word; an inherited misclassification survives for weeks because
nobody re-runs the probe.

## 5. Machine-finding counts can collapse when `.gitignore` starts working

10-03 reported **120 machine findings (4 ERROR + 116 WARNING)**. 10-04 reported **7 (4 ERROR +
1 WARNING)** with an identical KB. Nothing about the content changed — the 116 WARNINGs were all
`memory/` files hitting `classify_generic_path()`, and `memory/` became ignored+untracked in the
cleanup commit, so the scanner no longer walks into it.

This is the mirror image of pitfall #13 (a WARNING count *rising* on an index rebuild). Both are
scanner-behaviour artefacts, not KB health. Always state the delta's *cause* and say explicitly
when a finding-count change comes from the scanner's own reach rather than from data.

## 6. Cross-check against sibling reports, do not copy them

The 10-04 Output and Format validators had already run and both independently recorded
"backup cron recovered, HEAD `68f644e7`". That is a useful cross-check on E2 — but their reports
cannot know about *path* findings. Verify independently:

- `git ls-remote --heads origin` vs local HEAD (read-only; remote default branch may be a decoy —
  `main` was abandoned 2026-05-11 while `master` is live)
- `git status --porcelain -uall` split `??` vs `M` (a `find -newer` count is not a new-file count)
- re-run your own scan; never infer your section from a sibling's