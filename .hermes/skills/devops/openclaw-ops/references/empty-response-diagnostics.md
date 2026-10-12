# Empty or Non-Deliverable Agent Responses

Use when gateway/provider transport is reachable but user sees a generic empty-response warning.

## Evidence chain

1. **Identify exact run.** From `openclaw sessions --json`, record `sessionKey`, `sessionId`, timestamp, `agentId`, model, provider, and `contextTokens`. Display identity need not equal OpenClaw agent ID; never assume a named persona maps to a directory name.
2. **Read OpenClaw trajectory.** Query `trajectory_runtime_events` by `session_id` and `run_id`. Parse `event_json`; `type` is inside JSON, not a SQL column. Focus on `model.completed` and `trace.artifacts`: `stopReason`, usage output, `compactionCount`, timeout flags, `terminalError`, and `timedOutByRunBudget`.
3. **Check gateway and provider.** Verify gateway health, then run a cheap authenticated model probe with an explicit output limit. HTTP success plus full content rules out a dead gateway/provider for that probe.
4. **Correlate provider request.** Match timestamp and served backend model in provider request database. Inspect `max_tokens`, finish reason, output usage, and whether request storage is truncated.
5. **Check live model metadata.** Run `openclaw models list --json` and `openclaw infer model inspect --model <provider/model> --json`. Compare with session `contextTokens`; a hot-reloaded config can differ from stale session metadata until session reset.
6. **Inspect transport only after correlation.** Locate current OpenClaw bundle and search for `clamp_max_tokens`, `usesExplicitProxyLikeEndpoint`, and `resolveOpenAICompletionsEffectiveContextTokens`. Enable `OPENCLAW_DEBUG_MODEL_TRANSPORT=1` for one bounded run when exact wire evidence is still needed.

## Managed OpenAI-completions clamp mechanism

For an explicit proxy-like endpoint, OpenClaw estimates input tokens from outgoing messages and tools, then limits requested output to remaining context:

```text
remaining = max(1, effective_context - estimated_input - 1)
output_limit = min(requested_output, remaining)
```

Consequences:

- Near-full context can send `max_tokens=1` or `max_completion_tokens=1`.
- Provider may return `finish_reason=length`, empty/`null` content, and one completion token.
- OpenClaw marks turn `non_deliverable_terminal_turn`; surface layer may show generic “agent couldn't generate a response”.
- Setting model `maxTokens` does not bypass this remaining-context clamp.
- `compaction.reserveTokens` does not create capacity above the model context window; it controls compaction headroom.

## Evidence discipline

- **Confirmed wire claim:** only claim the original request contained `max_tokens=1` when full request payload is stored and directly readable.
- **Truncated payload:** treat `request`/`providerRequest` containing `_truncated=true` and `_preview` as incomplete. State that exact original field cannot be recovered from that row.
- **Strong mechanism evidence:** large prompt, tiny output, length stop, healthy provider, matching clamp code, and controlled probe reproducing same signature. Describe this as high-confidence mechanism, not fabricated wire capture.
- Do not attribute blame to provider, auth, or rate limit when correlated request succeeded and has no auth/quota error.

## Combo aliases

`/v1/models` may expose only a combo alias. Resolve router combo definition to concrete backends before choosing context or output metadata. Treat context capability as conservative minimum across every route; aliases can switch backends between calls.

## Recovery and durable fix

1. Start a fresh session immediately to remove stale context and restore responsiveness. `/new` or equivalent session reset is a recovery action, not a substitute for metadata repair.
2. Correct `contextWindow` to verified conservative backend limit. Do not inflate to session-cached value or optimistic model name.
3. Ensure runtime and live model metadata agree; reset session after changing them when needed.
4. Keep compaction reserve that leaves useful prompt headroom; do not reduce it blindly based on this symptom.
5. Run a fresh representative turn with output larger than one token and verify final assistant content, finish reason, and usage.
6. Capture `OPENCLAW_DEBUG_MODEL_TRANSPORT=1` only for bounded diagnosis; remove or disable afterward according to service configuration.
