---
name: hermes-state-recovery
description: Recover Hermes state.db from snapshots when the database is corrupted or malformed.
---

# Hermes State Recovery

Restore `state.db` from snapshots when the active database becomes corrupted (malformed, page-level errors, "database disk image is malformed").

## Triggers

- `state.db` reports "database disk image is malformed"
- User asks to restore state.db from a specific date
- Hermes sessions / memory stop working due to DB corruption

## Snapshot location

Snapshots live under `.hermes/state-snapshots/<timestamp>-<label>/`. Each snapshot directory contains a full copy of the `.hermes/` state at that point: `state.db`, `config.yaml`, `auth.json`, `cron/`, `gateway_state.json`, `manifest.json`.

Identify the right snapshot:
```bash
ls -lt .hermes/state-snapshots/
```

## Recovery workflow

### Phase 1: Assess corruption

```bash
# Check integrity
sqlite3 .hermes/state.db "PRAGMA integrity_check;"

# Check snapshot
sqlite3 .hermes/state-snapshots/<timestamp>/state.db "PRAGMA integrity_check;"
```

If integrity_check returns errors about "btreeInitPage() returns error code 11", "never used" pages — the DB has page-level corruption. Python's built-in `sqlite3` module will also fail with "database disk image is malformed".

### Phase 2: Dump recoverable data

The `.dump` command wraps output in a transaction. If any table fails during dump, the entire transaction rolls back with `ROLLBACK; -- due to errors`. **Solution: dump each table individually.**

```bash
SNAPSHOT=".hermes/state-snapshots/<timestamp>/state.db"

# Start transaction manually
echo "PRAGMA foreign_keys=OFF;" > /tmp/state_recovered.sql
echo "BEGIN TRANSACTION;" >> /tmp/state_recovered.sql

# Schema first
sqlite3 "$SNAPSHOT" ".schema" >> /tmp/state_recovered.sql

# Dump each table separately — skip compression_locks (usually empty/corrupted)
for table in schema_version sessions messages state_meta; do
    sqlite3 "$SNAPSHOT" ".mode insert $table" "SELECT * FROM $table;" >> /tmp/state_recovered.sql 2>/tmp/dump_${table}_err.log
    echo "Table $table exit: $?"
done

echo "COMMIT;" >> /tmp/state_recovered.sql
```

### Phase 3: Clean and import

The `.schema` dump includes `CREATE TABLE sqlite_sequence(name,seq)` and `INSERT INTO sqlite_sequence` — these are reserved and will fail on import. Remove them:

```bash
# Force text mode — dump may contain null bytes from message content
grep -av "sqlite_sequence" /tmp/state_recovered.sql > /tmp/state_clean.sql

# Import into fresh database
rm -f /tmp/state_restored.db
sqlite3 /tmp/state_restored.db < /tmp/state_clean.sql
```

### Phase 4: Verify

```bash
sqlite3 /tmp/state_restored.db "PRAGMA integrity_check;"   # Must return 'ok'
sqlite3 /tmp/state_restored.db "SELECT COUNT(*) FROM sessions;"
sqlite3 /tmp/state_restored.db "SELECT COUNT(*) FROM messages;"
sqlite3 /tmp/state_restored.db "SELECT COUNT(DISTINCT session_id) FROM messages;"
```

### Phase 5: Deploy

```bash
cd .hermes
# Backup current (corrupted) DB
cp state.db state.db.backup-before-restore-$(date +%Y%m%d_%H%M%S)
# Deploy recovered DB
cp /tmp/state_restored.db state.db
```

## Pitfalls

1. **`.recover` needs `sqlite_dbpage`** — this virtual table is rarely available. The `.recover` command will fail with "no such table: sqlite_dbpage". Fall back to `.dump`.

2. **`.dump` can roll back silently** — check the last line of the dump for `ROLLBACK; -- due to errors`. If present, dump tables individually.

3. **Messages table is largest and most likely to crash** — `sqlite3` may segfault (exit code 11) during messages dump. The data dumped before the crash is still valid. Accept partial recovery.

4. **`grep` treats dump as binary** — message content may contain null bytes. Use `grep -a` (or `grep --text`) to force text mode when filtering the dump SQL.

5. **`sqlite_sequence` is reserved** — the `.schema` dump includes it. Must filter out or import will fail with "object name reserved for internal use: sqlite_sequence".

6. **Python sqlite3 can't open malformed DBs** — use the `sqlite3` CLI tool. Install if missing: `sudo apt-get install -y sqlite3`.

7. **Expect data loss** — corrupted pages mean some sessions/messages will be unrecoverable. The snapshot captures the DB state at a point in time; if it was already corrupted when the snapshot was taken, recovery is partial.

## Reference

- `references/recovery-log-20260627.md` — full session log from a real recovery: corruption pattern, approaches tried, exact exit codes, and outcome.

## Verification checklist

After restore, confirm:
- [ ] `PRAGMA integrity_check` returns `ok`
- [ ] Session count matches expectations (within ~1-2 of snapshot)
- [ ] Message count is reasonable
- [ ] `SELECT COUNT(DISTINCT session_id) FROM messages` ≤ session count
- [ ] Date range makes sense (no 1970-01-01 entries without reason)
