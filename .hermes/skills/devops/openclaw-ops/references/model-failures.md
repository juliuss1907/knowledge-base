# Model Routing Failures

Use when OpenClaw cannot call a model or falls back across providers. Diagnose evidence before changing routing or limits.

## Classify before probing

| Evidence | Class | First action |
|---|---|---|
| HTTP 401 / model not supported | auth or model ID | Verify provider credential and exact model ID. |
| HTTP 403 quota exhausted | quota | Check account quota; do not treat as context failure. |
| HTTP 403 subscription required | entitlement | Choose a model covered by current subscription. |
| HTTP 410 retired | dead model | Remove from primary and fallback chains. |
| HTTP 429 / rate limit | transient | Respect retry timing; keep healthy fallbacks. |
| OAuth refresh failed | credential lifecycle | Re-authenticate OAuth profile. |
| `Context overflow: prompt too large` | context budget | Inspect prompt estimate, context metadata, and compaction. |
| `non_deliverable_terminal_turn` with `stopReason=length` and tiny output | output-budget clamp | Follow `empty-response-diagnostics.md`; do not first blame auth. |
| `FallbackSummaryError: All models failed` | aggregate failure | Expand nested error per model, then classify each separately. |

A successful gateway health check does not prove model health. A successful small model probe does not prove a large conversation can generate output.

## Safe liveness probe

1. Load secret from configured profile or provider entry without printing it.
2. Probe exact provider/model pair with a tiny prompt and explicit output limit.
3. Record HTTP status, model actually served, finish reason, content, and usage.
4. Repeat with a realistic output limit if first response is empty.
5. Stop after evidence separates transport, auth, quota, model availability, and context budget.

For a local OpenAI-compatible gateway, include its configured API key. An unauthenticated direct probe can return 401 before reaching the selected model and proves nothing about model health.

## Routing metadata rules

- Put real `contextWindow` and `maxTokens` in `models.providers.<provider>.models[]`.
- A combo/router alias is not one backend model. Resolve its route list and use conservative limits shared by every possible backend.
- `maxTokens` is requested output capacity, not additional context. It does not bypass remaining-context clamps.
- On current OpenClaw, read compaction reserve from `~/.openclaw/agents/<id>/agent/settings.json`; do not restore retired `reserveTokensFloor` in `openclaw.json`.
- Effective compaction reserve can be capped relative to context budget. Verify the effective runtime value before blaming reserve size.

## Configuration gate

1. Back up `openclaw.json` and per-agent settings.
2. Verify each route independently; record status and reason.
3. Choose limits from verified backend capabilities, never model names or optimistic suffixes.
4. Patch only supported schema.
5. Restart gateway and verify health.
6. Run one fresh representative turn, not only a small liveness probe.
7. Inspect trajectory usage and final status.

Never run `openclaw configure` after manual tuning. It rewrites routing and limit fields. Treat `openclaw doctor --fix` as mutating: back up first and diff config afterward.
