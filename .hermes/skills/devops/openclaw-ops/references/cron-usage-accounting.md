# Cron Usage Accounting — Baseline (2026-09-09)

Real measured data from the 2026-09-09 session. Use as reference points; re-query before reusing.

## Job inventory (6 active)

| System | Job | Schedule | Primary model |
|---|---|---|---|
| Hermes | Output Validator (d48e30a9a963) | 23:00 | session model (glm-5.3-flash on 09-08) |
| Hermes | Format Validator (d14687442111) | 23:15 | session model |
| Hermes | Hygiene Inspector (f1ff44c008e2) | 23:30 | session model |
| OpenClaw | KB Compile Daily (Kara) | 08:00 | 9router/oc/mimo-v2.5-free → ollama nemotron fallbacks |
| OpenClaw | KB Index Daily (Kara) | 21:00 | ollama/nemotron-3-nano:30b |
| OpenClaw | Heartbeat Check | every 30 min | default (b-ai — in cooldown, runs cost 0) |

X News jobs (3× daily) disabled since 2026-05-23 — excluded.

## Averages (Hermes validators, 73 runs each ≈ 2.5 months)

| Job | avg in/run | avg out/run | avg cache-read/run |
|---|---|---|---|
| Format Validator | 149.7k (heaviest) | 13.7k | 1.04M |
| Output Validator | 117.6k | 11.0k | 1.02M |
| Hygiene Inspector | 99.2k | 11.9k | 673k |
| **Total/day (3 jobs)** | **~366k** | **~36.6k** | **~2.73M** |

## Worst case (measured)

Single run: Format 2026-05-17 = 1.66M in / 43.2k out; Hygiene same day = 1.63M in. Peak cache-read in one run = 4.0M (Format 2026-07-17).

Worst day (validators, 2026-08-31): 1.94M in + 90.8k out + 4.65M cache-read ≈ 6.7M tokens processed.

Worst day incl. Kara: + Compile 913k (nemotron, 2026-08-26) + Index full-rebuild est. 0.5–1M + Heartbeat 48×~5k ≈ **~8.9M tokens/day ceiling**.

Month at worst every day ≈ 267M tokens (theory; actual free-tier providers → cost ≈ 0).

## Observations

- Cache-read ≈ 65% of total — bills differently (cheaper) than fresh input; always split the two in reports.
- 2026-09-03: all 3 validators = 0 tokens (provider failed before any call) — zero-cost failure days happen.
- Heartbeat failing on b-ai cooldown = 48 free but useless runs/day.
- OpenClaw sessions older than usage logging show all-zero usage — unmeasurable, not zero.
