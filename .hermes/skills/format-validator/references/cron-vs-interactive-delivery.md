# Cron vs interactive — where delivery lives

Cron runs and interactive runs look the same in SKILL.md ("send Telegram") but
behave differently at runtime. Getting this wrong wastes a turn.

## What actually happens

- **Cron mode**: the post-turn harness auto-delivers your *final response*
  to the job's configured destination (Telegram home channel in this repo).
  `hermes send --to telegram` to that same target exits 0 but is *skipped*:

  `Skipped send_message to telegram:1370258715. This cron job will already
  auto-deliver its final response… Put the intended content in your final
  response instead.`

  Observed 2026-08-21 — correct workaround: write the notification text as
  your final response; don't burn a tool call on `hermes send` to the home
  channel.

- **Interactive / on-demand** (`validate format` from Julius): no auto-delivery.
  You must call `hermes send` yourself, or the user never sees the result.

## Recipe

1. After validation, check whether you're in cron (system prompt says
   "You are running as a scheduled cron job").
2. If cron → skip `hermes send --to telegram` on the home channel; embed
   the message in your final response. Only use `hermes send` if targeting
   a *different* channel.
3. If interactive → call `hermes send --to telegram` as the spec says.
4. Keep the message body identical in both paths; only the delivery channel
   changes.
