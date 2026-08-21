# Model Failures — 2026-08-21 Session Transcript

Source: live `KB Compile Daily` (b91792a8) + `openclaw cron runs` + direct probe of `https://ollama.com/v1/chat/completions` and `http://localhost:20128/v1/models`.

## Failure modes seen (exact strings)

```
Context overflow: prompt too large for the model. Try /reset (or /new) to start a fresh session, or use a larger-context model.
Context overflow: estimated context size exceeds safe threshold during tool loop.
FallbackSummaryError: All models failed (3): api-ai-box-vn/deepseek-v4-flash-0731: 403 insufficient user quota, remaining: đ0.000000 (request id: 202608180313251203089498268d9d6yfJKd54Y) (auth)
FallbackSummaryError: All models failed (3): custom-api-ai-box-vn-2/deepseek-v4-pro[1m]: HTTP 403 new_api_error: Token này không có quyền truy cập model deepseek-v4-pro[1m] (request id: 20260816011333918019278268d9d66J8YB70l) (auth)
FallbackSummaryError: All models failed (3): custom-api-ai-box-vn-4/deepseek-v4-flash[1m]: 403 Token này không có quyền truy cập model deepseek-v4-flash[1m] (request id: 202608150118461487350118268d9d61XPdfHx4) (auth)
FallbackSummaryError: All models failed (2): opencode/minimax-m2.5-free: HTTP 401 ModelError: Model minimax-m2.5-free is not supported (auth)
FallbackSummaryError: All models failed (3): openai-codex/gpt-5.4: OAuth token refresh failed for openai-codex: Failed to refresh OpenAI Codex token. Please try again or re-authenticate.
ollama/kimi-k2.5:cloud: 410 {"error":"kimi-k2.5 was retired at 2026-07-31 00:00:00 -0700 PDT (ref: 96024fa1-a526-412c-a1e5-dcef4eed90a7)"} (timeout)
ollama/minimax-m2.7:cloud: 403 {"error":"this model requires a subscription, upgrade for access: https://ollama.com/upgrade (ref: a3e403d6-b3bb-4233-ba4c-e9fdafd7c5d6)"} (auth)
google/gemma-4-31b-it: ⚠️ API rate limit reached. Please try again later. (rate_limit)
9router/oc/mimo-v2.5-free: ⚠️ API rate limit reached. Please try again later. (rate_limit)
openclaw-gateway: [context-overflow-precheck] estimatedPromptTokens=14226 promptBudgetBeforeReserve=8000 overflowTokens=6226 reserveTokens=16384 effectiveReserveTokens=8000 sessionFile=.../7e5e3825-...jsonl
openclaw-gateway: config reload skipped (invalid config): agents.defaults.models.google/gemma-4-31b-it: Unrecognized keys: "contextWindow", "maxTokens" (x5)
```

## Liveness matrix (probed 2026-08-21 09:14–09:22 +07)

| Model ID | Provider path | Result | Note |
|---|---|---|---|
| `ollama/nemotron-3-nano:30b` | `ollama` | ✅ free | keep as fallback |
| `ollama/nemotron-3-super` | `ollama` | ✅ free | keep as fallback |
| `ollama/gpt-oss:120b` | `ollama` | ✅ free | alt fallback |
| `ollama/gpt-oss:20b` | `ollama` | (not probed, likely free) |  |
| `ollama/minimax-m2.7:cloud` | `ollama` | ❌ 403 subscription | `Upgrade for access` |
| `ollama/kimi-k2.6:cloud` | `ollama` | ❌ 403 subscription / cooldown |  |
| `ollama/kimi-k3:cloud` | `ollama` | ❌ Pro+extra usage |  |
| `ollama/kimi-k2.5:cloud` | `ollama` | ❌ 410 retired 2026-07-31 |  |
| `ollama/qwen3.5:397b` | `ollama` | ❌ 403 subscription |  |
| `ollama/glm-5.2:cloud` | `ollama` | ❌ 403 subscription |  |
| `ollama/deepseek-v4-flash:0731` | `ollama` | ❌ 403 subscription |  |
| `opencode/minimax-m2.5-free` | `opencode` plugin | ❌ 401 not supported | removed upstream |
| `api-box/deepseek-v4-flash[1m]` | `api-box` | ❌ 403 no quyền | current ai-box token lacks [1m] |
| `api-box/deepseek-v4-flash` | `api-box` | ❌ context 16k overflow |  |
| `ai-box-vn/deepseek-v4-pro` | `ai-box-vn` | ❌ 403 quota 0.000000 |  |
| `9router/oc/mimo-v2.5-free` | `9router` | ⚠️ 429 rate limit (transient) | requested primary — keep |
| `google/gemma-4-31b-it` | `google` | ⚠️ 429 rate limit (transient) | keep as last fallback |
| `openai-codex/gpt-5.4` | `openai-codex` | ❌ OAuth refresh failed | token expired, needs re-auth |

## Final working routing (applied)

```json
// KB Compile Daily b91792a8
{ "model": "9router/oc/mimo-v2.5-free", "fallbacks": ["ollama/nemotron-3-nano:30b", "ollama/nemotron-3-super", "google/gemma-4-31b-it"], "timeoutSeconds": 600 }
// KB Index Daily 5de7b598
{ "model": "ollama/nemotron-3-nano:30b", "fallbacks": ["ollama/nemotron-3-super", "google/gemma-4-31b-it"], "timeoutSeconds": 600 }
```

`compaction.reserveTokensFloor`: 20000 → 50000; `9router/oc/mimo-v2.5-free` contextWindow: 16000 → 128000 via `models.providers.9router.models[]`.
