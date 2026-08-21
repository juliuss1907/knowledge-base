# Gateway Config Schema — Valid vs Invalid Paths

## Valid

```json
{
  "agents": {
    "defaults": {
      "compaction": { "reserveTokensFloor": 50000 },
      "model": { "primary": "9router/oc/mimo-v2.5-free", "fallbacks": ["google/gemma-4-31b-it"] }
    }
  },
  "models": {
    "providers": {
      "9router": {
        "baseUrl": "http://localhost:20128/v1",
        "api": "openai-completions",
        "models": [{ "id": "oc/mimo-v2.5-free", "contextWindow": 128000, "maxTokens": 8192 }]
      },
      "ollama": {
        "baseUrl": "https://ollama.com",
        "models": [{ "id": "nemotron-3-nano:30b", "contextWindow": 128000, "maxTokens": 8192 }]
      }
    }
  }
}
```

## Invalid (rejected by gateway)

```json
{
  "agents": {
    "defaults": {
      "models": {
        "opencode/minimax-m2.5-free": { "contextWindow": 200000 },
        "9router/oc/mimo-v2.5-free": { "contextWindow": 128000 }
      }
    }
  }
}
```

### Error emitted

```
[reload] config reload skipped (invalid config): agents.defaults.models.google/gemma-4-31b-it: Unrecognized keys: "contextWindow", "maxTokens" (x5)
```

### Why

`agents.defaults.models` is not a free-form map of `modelRef → {contextWindow}`. The gateway validates it strictly and rejects unknown keys. Per-model window belongs in `models.providers.<provider>.models[]`. Plugin models like `opencode/*` are not represented there at all — their catalog comes from the plugin at runtime.

### Rule

- **Never** write `agents.defaults.models.<ref> = {contextWindow}`.
- **Never** run `openclaw configure` wizard after manual tuning — it resets `reserveTokensFloor` to 20000 and drops custom provider windows.
- Always `cp openclaw.json openclaw.json.bak-*` before editing.
- After editing, `systemctl --user restart openclaw-gateway` and wait 6–8s before `openclaw cron run`.

## Cron payload schema

```json
{
  "payload": {
    "kind": "agentTurn",
    "message": "Chạy ...",
    "model": "9router/oc/mimo-v2.5-free",
    "fallbacks": ["ollama/nemotron-3-nano:30b", "ollama/nemotron-3-super", "google/gemma-4-31b-it"],
    "timeoutSeconds": 600
  }
}
```

`fallbacks` order matters — free, live models first; rate-limited `google/gemma` last.
