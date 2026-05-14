#!/usr/bin/env bash
# =============================================================================
# Knowledge Base V2 — Skeleton Setup Script
# =============================================================================
# Purpose: In-place rewrite KB V1 → V2 structure
# Strategy: Backup wiki/ V1 → wipe → create V2 skeleton with placeholder files
# Pre-flight: Requires git tag v1.0-final + branch v1-archive (created BEFORE running)
#
# Usage:
#   cd /path/to/knowledge-base
#   bash setup-skeleton-kb-v2.sh
#
# Author: Julius
# Version: 1.0
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
readonly SCRIPT_NAME="setup-skeleton-kb-v2.sh"
readonly REQUIRED_TAG="v1.0-final"
readonly REQUIRED_BRANCH="v1-archive"
readonly BACKUP_DIR="wiki-v1-archive"
readonly TODAY="$(date +%Y-%m-%d)"

# Colors for output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m' # No Color

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------
log_info()    { echo -e "${BLUE}[INFO]${NC} $*"; }
log_ok()      { echo -e "${GREEN}[ OK ]${NC} $*"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_error()   { echo -e "${RED}[FAIL]${NC} $*" >&2; }

abort() {
    log_error "$1"
    log_error "Aborting. No changes made."
    exit 1
}

confirm() {
    local prompt="$1"
    read -r -p "$(echo -e "${YELLOW}${prompt}${NC} [y/N]: ")" reply
    [[ "$reply" =~ ^[Yy]$ ]]
}

# -----------------------------------------------------------------------------
# Pre-flight checks
# -----------------------------------------------------------------------------
preflight() {
    log_info "Running pre-flight checks..."

    # 1. Check we're in a git repo
    if [[ ! -d ".git" ]]; then
        abort "Not a git repository. Run from knowledge-base/ root."
    fi
    log_ok "Git repository detected"

    # 2. Check working tree clean
    if ! git diff-index --quiet HEAD --; then
        abort "Working tree has uncommitted changes. Commit or stash first."
    fi
    log_ok "Working tree clean"

    # 3. Check tag v1.0-final exists
    if ! git rev-parse "$REQUIRED_TAG" >/dev/null 2>&1; then
        abort "Required tag '$REQUIRED_TAG' not found. Run: git tag $REQUIRED_TAG && git push origin $REQUIRED_TAG"
    fi
    log_ok "Tag '$REQUIRED_TAG' exists"

    # 4. Check branch v1-archive exists
    if ! git show-ref --verify --quiet "refs/heads/$REQUIRED_BRANCH"; then
        abort "Required branch '$REQUIRED_BRANCH' not found. Run: git branch $REQUIRED_BRANCH && git push origin $REQUIRED_BRANCH"
    fi
    log_ok "Branch '$REQUIRED_BRANCH' exists"

    # 5. Check we're NOT on v1-archive branch
    local current_branch
    current_branch="$(git rev-parse --abbrev-ref HEAD)"
    if [[ "$current_branch" == "$REQUIRED_BRANCH" ]]; then
        abort "Currently on '$REQUIRED_BRANCH'. Switch to main: git checkout main"
    fi
    log_ok "Current branch: $current_branch (not v1-archive)"

    # 6. Check raw/ exists (we need to preserve it)
    if [[ ! -d "raw" ]]; then
        log_warn "raw/ folder not found — will be created (empty)"
    else
        local raw_count
        raw_count=$(find raw -type f -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
        log_ok "raw/ folder exists with $raw_count markdown files (will be preserved)"
    fi

    # 7. Check backup target doesn't already exist
    if [[ -d "$BACKUP_DIR" ]]; then
        abort "Backup folder '$BACKUP_DIR' already exists. Remove or rename it first."
    fi
    log_ok "Backup folder name available: $BACKUP_DIR/"

    echo ""
    log_info "All pre-flight checks passed."
    echo ""
}

# -----------------------------------------------------------------------------
# Show plan
# -----------------------------------------------------------------------------
show_plan() {
    cat <<EOF
${BLUE}═══════════════════════════════════════════════════════════════${NC}
  KB V2 SKELETON SETUP — EXECUTION PLAN
${BLUE}═══════════════════════════════════════════════════════════════${NC}

This script will perform the following actions:

  1. Backup existing wiki/ → ${BACKUP_DIR}/
     (preserves V1 wiki content as untracked folder)

  2. Remove V1 agent folders (if exist):
     - .openclaw/  (will be re-created with V2 structure)
     - .hermes/    (will be re-created with V2 structure)
     - agents/     (V1 location, no longer used)

  3. Create V2 folder structure:
     - .openclaw/{skills/}, .hermes/{skills/}
     - context/, raw/{6 subfolders}, wiki/{8 subfolders}

  4. Create placeholder files (Wave 2-6 will fill content):
     - SKILL.md stubs with progressive disclosure template
     - IDENTITY.md, SOUL.md, MEMORY.md, HEARTBEAT.md stubs
     - meta/format-spec.md, meta/folder-structure.md stubs
     - knowledge-base.md, README.md, context/USER.md stubs

  5. Print verify checklist

${YELLOW}NOT touched by this script:${NC}
  - raw/ content (preserved as-is)
  - AGENTS.md, TAGS.md (will be written by separate Wave 1 deliverables)
  - .git/ (untouched)

${YELLOW}Rollback if needed:${NC}
  git checkout $REQUIRED_TAG -- .
  rm -rf $BACKUP_DIR

EOF

    if ! confirm "Proceed with skeleton setup?"; then
        abort "User cancelled."
    fi
    echo ""
}

# -----------------------------------------------------------------------------
# Step 1: Backup wiki/ V1
# -----------------------------------------------------------------------------
backup_v1() {
    log_info "Step 1/4: Backing up V1 content..."

    if [[ -d "wiki" ]]; then
        mv wiki "$BACKUP_DIR"
        log_ok "Moved wiki/ → $BACKUP_DIR/ (untracked, add to .gitignore if needed)"
    else
        log_warn "No wiki/ folder to backup"
    fi

    # Remove V1 agent folders if they exist
    for legacy in ".openclaw" ".hermes" "agents"; do
        if [[ -d "$legacy" ]]; then
            rm -rf "$legacy"
            log_ok "Removed legacy: $legacy/"
        fi
    done

    echo ""
}

# -----------------------------------------------------------------------------
# Step 2: Create folder structure
# -----------------------------------------------------------------------------
create_folders() {
    log_info "Step 2/4: Creating V2 folder structure..."

    # Root-level agent folders
    mkdir -p .openclaw/skills/{ingest-agent,compile-agent,index-agent,fix-agent}
    mkdir -p .hermes/skills/{output-validator,format-validator,hygiene-inspector}

    # Context
    mkdir -p context

    # Raw layer (preserve if exists, create subfolders if missing)
    mkdir -p raw/{articles,posts,websites,videos,papers,repos}

    # Wiki layer
    mkdir -p wiki/{meta,sources,concepts,tag,topic,drafts}
    mkdir -p wiki/reviews/archive

    log_ok "Folder structure created"
    echo ""
}

# -----------------------------------------------------------------------------
# Step 3: Create placeholder files
# -----------------------------------------------------------------------------

# Generate SKILL.md stub with progressive disclosure template
write_skill_stub() {
    local path="$1"
    local agent_name="$2"
    local job_name="$3"
    local wave="$4"

    cat > "$path" <<EOF
# ${agent_name} — ${job_name}

> **Status:** Placeholder — Wave ${wave}
> **Scheduled:** TBD
> **Last updated:** ${TODAY}

---

## Role

<!-- TODO Wave ${wave}: 1-2 sentences defining what this skill does -->

---

## When to use

<!-- TODO Wave ${wave}: Trigger conditions — when this skill should be loaded -->

- Trigger 1: TBD
- Trigger 2: TBD

---

## Quick start

<!-- TODO Wave ${wave}: First steps the agent must take when invoked -->

1. TBD
2. TBD
3. TBD

---

## Details

For complete instructions, see supporting files in this folder:

- \`workflow.md\` — step-by-step process (TODO Wave ${wave})
- \`examples.md\` — sample inputs/outputs (TODO Wave ${wave})
- \`reference.md\` — detailed specs (TODO Wave ${wave}, optional)

---

## Escalation

<!-- TODO Wave ${wave}: When to ask Julius vs when to proceed autonomously -->

- Condition X → propose via channel
- Condition Y → save to \`wiki/drafts/\`
- Condition Z → ask Julius directly

---

## Constraints

<!-- TODO Wave ${wave}: Hard limits this skill must respect -->

- Read-only zones: TBD
- Write zones: TBD
- Forbidden actions: TBD
EOF
}

# Generate IDENTITY.md stub
write_identity_stub() {
    local path="$1"
    local agent_name="$2"
    local wave="$3"

    cat > "$path" <<EOF
# ${agent_name} — IDENTITY

> **Status:** Placeholder — Wave ${wave}
> **Last updated:** ${TODAY}

---

## Name

${agent_name}

## Purpose

<!-- TODO Wave ${wave}: 2-3 sentences defining who this agent is and what it exists for -->

## Skills

<!-- TODO Wave ${wave}: List of skills this agent has, with paths -->

## Boundaries

<!-- TODO Wave ${wave}: What this agent must never do -->
EOF
}

# Generate SOUL.md stub
write_soul_stub() {
    local path="$1"
    local agent_name="$2"
    local wave="$3"

    cat > "$path" <<EOF
# ${agent_name} — SOUL

> **Status:** Placeholder — Wave ${wave}
> **Last updated:** ${TODAY}

---

## Operating principles

<!-- TODO Wave ${wave}: How this agent thinks, decides, communicates -->

## Tone & style

<!-- TODO Wave ${wave}: Communication style with Julius -->

## Decision heuristics

<!-- TODO Wave ${wave}: Default behaviors when ambiguous -->
EOF
}

# Generate MEMORY.md stub
write_memory_stub() {
    local path="$1"
    local agent_name="$2"
    local wave="$3"

    cat > "$path" <<EOF
# ${agent_name} — MEMORY

> **Status:** Placeholder — Wave ${wave}
> **Format:** Append-only log
> **Last updated:** ${TODAY}

---

<!-- Append entries below. Never delete or rewrite past entries. -->
<!-- Format: YYYY-MM-DD HH:MM | event-type | summary -->

## ${TODAY} — Initial setup

- Skeleton created by setup-skeleton-kb-v2.sh
- Awaiting Wave ${wave} content fill
EOF
}

# Generate HEARTBEAT.md stub
write_heartbeat_stub() {
    local path="$1"
    local agent_name="$2"
    local wave="$3"

    cat > "$path" <<EOF
# ${agent_name} — HEARTBEAT

> **Status:** Placeholder — Wave ${wave}
> **Purpose:** Last-known liveness signal
> **Last updated:** ${TODAY}

---

last_run: never
last_run_status: not_started
last_run_duration_sec: 0
next_scheduled: TBD
EOF
}

# Generate meta file stub
write_meta_stub() {
    local path="$1"
    local title="$2"
    local consumer="$3"
    local wave="$4"

    cat > "$path" <<EOF
# ${title}

> **Status:** Placeholder — Wave ${wave}
> **Consumed by:** ${consumer}
> **Last updated:** ${TODAY}

---

<!-- TODO Wave ${wave}: Fill ground-truth specification. -->
<!-- This file is the source of truth for ${consumer}. -->
<!-- Changes here directly affect validator behavior. -->

## Section 1: TBD

## Section 2: TBD

## Section 3: TBD
EOF
}

# Generate generic placeholder
write_placeholder() {
    local path="$1"
    local title="$2"
    local wave="$3"

    cat > "$path" <<EOF
# ${title}

> **Status:** Placeholder — Wave ${wave}
> **Last updated:** ${TODAY}

---

<!-- TODO Wave ${wave}: Fill content -->
EOF
}

# Generate index file (for raw/ subfolders)
write_index_stub() {
    local path="$1"
    local folder_name="$2"

    cat > "$path" <<EOF
# ${folder_name} — Index

> Auto-generated index for raw/${folder_name}/
> Last updated: ${TODAY}

---

## Files

<!-- This file is maintained by OpenClaw Ingest Agent -->
<!-- Format: - [[YYYY-MM-DD_slug]] — short description -->
EOF
}

create_placeholders() {
    log_info "Step 3/4: Creating placeholder files..."

    # ----- OpenClaw skills (Wave 3) -----
    write_skill_stub ".openclaw/skills/ingest-agent/SKILL.md"  "OpenClaw" "Ingest Agent"  "3"
    write_skill_stub ".openclaw/skills/compile-agent/SKILL.md" "OpenClaw" "Compile Agent" "3"
    write_skill_stub ".openclaw/skills/index-agent/SKILL.md"   "OpenClaw" "Index Agent"   "3"
    write_skill_stub ".openclaw/skills/fix-agent/SKILL.md"     "OpenClaw" "Fix Agent"     "3"
    log_ok "OpenClaw skills (4 stubs)"

    # ----- Hermes skills (Wave 4) -----
    write_skill_stub ".hermes/skills/output-validator/SKILL.md"   "Hermes-VPS" "Output Validator"   "4"
    write_skill_stub ".hermes/skills/format-validator/SKILL.md"   "Hermes-VPS" "Format Validator"   "4"
    write_skill_stub ".hermes/skills/hygiene-inspector/SKILL.md"  "Hermes-VPS" "Hygiene Inspector"  "4"
    log_ok "Hermes skills (3 stubs)"

    # ----- OpenClaw identity files (Wave 5) -----
    write_identity_stub  ".openclaw/IDENTITY.md"  "OpenClaw" "5"
    write_soul_stub      ".openclaw/SOUL.md"      "OpenClaw" "5"
    write_memory_stub    ".openclaw/MEMORY.md"    "OpenClaw" "5"
    write_heartbeat_stub ".openclaw/HEARTBEAT.md" "OpenClaw" "5"
    log_ok "OpenClaw identity (4 stubs)"

    # ----- Hermes identity files (Wave 5) -----
    write_identity_stub  ".hermes/IDENTITY.md"  "Hermes-VPS" "5"
    write_soul_stub      ".hermes/SOUL.md"      "Hermes-VPS" "5"
    write_memory_stub    ".hermes/MEMORY.md"    "Hermes-VPS" "5"
    write_heartbeat_stub ".hermes/HEARTBEAT.md" "Hermes-VPS" "5"
    log_ok "Hermes identity (4 stubs)"

    # ----- Wiki meta files (Wave 2 — ground truth) -----
    write_meta_stub "wiki/meta/format-spec.md"      "Format Specification"     "Hermes Format Validator + OpenClaw Compile Agent" "2"
    write_meta_stub "wiki/meta/folder-structure.md" "Folder Structure Whitelist" "Hermes Hygiene Inspector"                          "2"
    log_ok "Wiki meta (2 stubs)"

    # ----- Wiki review entry point -----
    cat > "wiki/reviews/_action-required.md" <<EOF
# Action Required

> Single entry point for Julius to see all pending Hermes findings.
> Auto-maintained by Hermes after each validator run.
> Last updated: ${TODAY}

---

## Pending issues

<!-- Hermes appends here. Cleared when Julius marks resolved. -->

_No issues yet — KB V2 freshly initialized._
EOF
    log_ok "Reviews entry point"

    # ----- Context (Wave 6) -----
    write_placeholder "context/context.md" "Context — Index"      "6"
    write_placeholder "context/USER.md"    "Julius — User Profile" "6"
    log_ok "Context (2 stubs)"

    # ----- Raw index files (only if missing — preserve existing) -----
    for folder in articles posts websites videos papers repos; do
        local idx="raw/${folder}/${folder}.md"
        if [[ ! -f "$idx" ]]; then
            write_index_stub "$idx" "$folder"
        fi
    done
    log_ok "Raw indexes (created if missing, existing preserved)"

    # ----- Root-level files (Wave 6, except AGENTS.md + TAGS.md) -----
    if [[ ! -f "knowledge-base.md" ]]; then
        write_placeholder "knowledge-base.md" "Knowledge Base — Dashboard" "6"
    fi
    if [[ ! -f "README.md" ]]; then
        write_placeholder "README.md" "Knowledge Base — README" "6"
    fi
    log_ok "Root dashboards (knowledge-base.md, README.md)"

    log_warn "AGENTS.md and TAGS.md NOT created — written by separate Wave 1 deliverables"

    echo ""
}

# -----------------------------------------------------------------------------
# Step 4: Verify
# -----------------------------------------------------------------------------
verify() {
    log_info "Step 4/4: Verification..."
    echo ""

    local errors=0

    # Required folders
    local required_dirs=(
        ".openclaw/skills/ingest-agent"
        ".openclaw/skills/compile-agent"
        ".openclaw/skills/index-agent"
        ".openclaw/skills/fix-agent"
        ".hermes/skills/output-validator"
        ".hermes/skills/format-validator"
        ".hermes/skills/hygiene-inspector"
        "context"
        "raw/articles" "raw/posts" "raw/websites"
        "raw/videos" "raw/papers" "raw/repos"
        "wiki/meta" "wiki/sources" "wiki/concepts"
        "wiki/tag" "wiki/topic" "wiki/drafts"
        "wiki/reviews/archive"
    )

    for dir in "${required_dirs[@]}"; do
        if [[ -d "$dir" ]]; then
            echo "  ✓ $dir/"
        else
            echo "  ✗ $dir/ MISSING"
            ((errors++))
        fi
    done

    echo ""

    # Required placeholder files
    local required_files=(
        ".openclaw/IDENTITY.md" ".openclaw/SOUL.md"
        ".openclaw/MEMORY.md" ".openclaw/HEARTBEAT.md"
        ".openclaw/skills/ingest-agent/SKILL.md"
        ".openclaw/skills/compile-agent/SKILL.md"
        ".openclaw/skills/index-agent/SKILL.md"
        ".openclaw/skills/fix-agent/SKILL.md"
        ".hermes/IDENTITY.md" ".hermes/SOUL.md"
        ".hermes/MEMORY.md" ".hermes/HEARTBEAT.md"
        ".hermes/skills/output-validator/SKILL.md"
        ".hermes/skills/format-validator/SKILL.md"
        ".hermes/skills/hygiene-inspector/SKILL.md"
        "wiki/meta/format-spec.md"
        "wiki/meta/folder-structure.md"
        "wiki/reviews/_action-required.md"
        "context/context.md" "context/USER.md"
    )

    for file in "${required_files[@]}"; do
        if [[ -f "$file" ]]; then
            echo "  ✓ $file"
        else
            echo "  ✗ $file MISSING"
            ((errors++))
        fi
    done

    echo ""

    if [[ $errors -eq 0 ]]; then
        log_ok "Verification passed — all expected paths present"
    else
        log_error "Verification found $errors missing paths"
        return 1
    fi
}

# -----------------------------------------------------------------------------
# Final checklist
# -----------------------------------------------------------------------------
print_next_steps() {
    cat <<EOF

${GREEN}═══════════════════════════════════════════════════════════════${NC}
  SKELETON SETUP COMPLETE
${GREEN}═══════════════════════════════════════════════════════════════${NC}

${BLUE}Next steps:${NC}

  1. Add the two remaining Wave 1 files manually:
     - knowledge-base/AGENTS.md   (provided in Wave 1 deliverable 2/3)
     - knowledge-base/TAGS.md     (provided in Wave 1 deliverable 3/3)

  2. Add to .gitignore (if not already):
     ${BACKUP_DIR}/

  3. Review structure:
     tree -L 2 -a -I '.git|node_modules' .

  4. Stage and commit:
     git add .openclaw/ .hermes/ context/ raw/ wiki/
     git add AGENTS.md TAGS.md knowledge-base.md README.md
     git commit -m "feat: KB v2 skeleton + Wave 1 foundation"
     git push origin main

  5. From workspace repo, bump submodule pointer:
     cd ..
     git add knowledge-base
     git commit -m "bump: kb pointer to v2 skeleton"
     git push

  6. On VPS, pull and verify (Phase B in migration plan):
     ssh vps
     cd knowledge-base && git pull

${YELLOW}Rollback if needed:${NC}
     git checkout ${REQUIRED_TAG} -- .
     rm -rf ${BACKUP_DIR}

${YELLOW}Wave 2 unlocks after this commit:${NC}
     - wiki/meta/format-spec.md
     - wiki/meta/folder-structure.md

EOF
}

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
main() {
    echo ""
    log_info "Starting $SCRIPT_NAME"
    echo ""

    preflight
    show_plan
    backup_v1
    create_folders
    create_placeholders
    verify
    print_next_steps
}

main "$@"
