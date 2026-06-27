# Recovery Session Log — 2026-06-27

## Context

`state.db` was corrupted (4.1MB, "database disk image is malformed"). User requested restore from snapshot dated June 26.

## Snapshot used

```
/home/julius/knowledge-base/.hermes/state-snapshots/20260626-005403-pre-update/state.db
```

Snapshot name pattern: `<YYYYMMDD>-<HHMMSS>-<label>` — this one was `pre-update` (taken before a Hermes update).

## Corruption pattern

```
Integrity check: Tree 10 page 586: btreeInitPage() returns error code 11
Page 12: never used
Page 13: never used
... (many "never used" pages)
```

Page-level corruption in the sessions/messages B-tree. Schema was readable but data pages were damaged.

## What was tried

| Approach | Result |
|---|---|
| Python sqlite3 direct open | "database disk image is malformed" |
| `.recover` command | Failed — "no such table: sqlite_dbpage" |
| `.dump` (full) | Rolled back — "ROLLBACK; -- due to errors" |
| **Dump individual tables** | **Worked** ✅ |

## Recovery outcome

| Metric | Value |
|---|---|
| Sessions recovered | 50 / 51 (1 lost) |
| Messages recovered | 811 |
| Sessions with messages | 15 |
| Date range | through 2026-06-14 |
| Restored DB size | 3.1 MB |
| Integrity check | ok |

## Individual table dump exit codes

```
schema_version: exit 0
sessions:       exit 0
messages:       exit 11 (segfault — partial recovery)
state_meta:     exit 0
```

The messages table caused a segfault partway through, but the rows dumped before the crash were valid.

## grep binary issue

The dump file contained null bytes from message content, causing `grep` to treat it as binary:
```
grep: /tmp/state_recovered.sql: tập tin nhị phân khớp mẫu tìm kiếm
```
Fix: use `grep -a` to force text mode. Without this, `sqlite_sequence` lines were not filtered out, causing import failure.

## Final deploy

```bash
# Backup
cp state.db state.db.backup-before-restore-20260627_095729

# Deploy
cp /tmp/state_restored.db state.db
```
