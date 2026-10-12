# Typo variant 4 — capital-I after Vietnamese diacritic

Original scope (2026-07-16, 5 instances): `ngườI` → `người`.
Expanded scope (2026-07-18): **ALL** Vietnamese words where lowercase-i follows a vowel with any diacritic — 237+ instances across 14 files.

## Affected categories

| Category | Examples | Count (07-18) |
|---|---|---|
| à + I → ài | BàI → Bài, tàI → tài | ~20 |
| ạ + I → ại | lạI → lại, ngoạI → ngoại | ~15 |
| ớ + I → ới | mớI → mới, giớI → giới, VớI → Với | ~30 |
| ả + I → ải | phảI → phải, GiảI → Giải | ~25 |
| ổ + I → ổi | đổI → đổi | ~15 |
| ờ + I → ời | thờI → thời, lờI → lời, ngườI → người | ~50 |
| ơ + I → ơi | nơI → nơi | ~15 |
| ộ + I → ội | hộI → hội | ~10 |
| ố + I → ối | MốI → Mối, cuốI → cuối | ~15 |
| ọ + I → ọi | mọI → mọi | ~10 |
| ổ + I → ổi | đuổI → đuổi | ~10 |
| đ + I → đi | đI → đi | ~5 |

## Detection

`quick-scan.sh` section 2d detects `ngườI` specifically. For a full sweep:

```bash
grep -rPn '[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]I\b' wiki/sources/ wiki/concepts/
```

Any Vietnamese diacritic character followed by capital I at a word boundary.

## Fix — character-level sed (42 combinations)

```bash
for f in <file-list>; do
  sed -i 's/àI/ài/g; s/áI/ái/g; s/ảI/ải/g; s/ãI/ãi/g; s/ạI/ại/g
          s/èI/èi/g; s/éI/éi/g; s/ẻI/ẻi/g; s/ẽI/ẽi/g; s/ẹI/ẹi/g
          s/ềI/ềi/g; s/ếI/ếi/g; s/ểI/ểi/g; s/ễI/ễi/g; s/ệI/ệi/g
          s/ìI/ìi/g; s/íI/íí/g; s/ỉI/ỉi/g; s/ĩI/ĩi/g; s/ịI/ịi/g
          s/òI/òi/g; s/óI/ói/g; s/ỏI/ỏi/g; s/õI/õi/g; s/ọI/ọi/g
          s/ồI/ồi/g; s/ốI/ối/g; s/ổI/ổi/g; s/ỗI/ỗi/g; s/ộI/ội/g
          s/ờI/ời/g; s/ớI/ới/g; s/ởI/ởi/g; s/ỡI/ỡi/g; s/ợI/ợi/g
          s/ùI/ùi/g; s/úI/úi/g; s/ủI/ủi/g; s/ũI/ũi/g; s/ụI/ụi/g
          s/ừI/ừi/g; s/ứI/ứi/g; s/ửI/ửi/g; s/ữI/ữi/g; s/ựI/ựi/g
          s/ỳI/ỳi/g; s/ýI/ýi/g; s/ỷI/ỷi/g; s/ỹI/ỹi/g
          s/đI/đi/g' "$f"
done
```

No need to enumerate specific words — the sed is character-level.

## Escalation threshold

When a single batch contains 237+ instances across 14/14 files, this is a Compile Agent prompt defect, not a patch-each-batch problem. Escalate with `[SYSTEMATIC ISSUE]` and recommend prompt review. The validator should check: if capital-I appears in >50% of new files AND >50 total instances, escalate rather than listing individually.

## Symptom

Unlike the double-i variant, the capital-I variant passes basic spell-check (the letter 'I' is valid ASCII) but breaks Vietnamese readability because capital letters don't appear mid-word in Vietnamese. The capital 'I' is visually close to lowercase 'i' in monospace/code fonts, making it easy to miss in code review.

## Shared root cause

All five Compile Agent tokenization variants share one origin: the LLM mishandles the character following a Vietnamese diacritic. Five variants observed:

1. "ngưởi" (hook-above 'ỉ' instead of grave 'ời') — original
2. "ngườii" (doubled lowercase 'i') — 2026-06-23
3. "ngườitrong" etc. (spacing merge, space dropped) — 2026-07-02
4. "ngườI" and ALL [vowel+diacritic]I — this variant, 2026-07-16
5. "ngườ" (the 'i' deleted entirely) — 2026-07-21, see SKILL.md

Each "fix" to the Compile Agent prompt shifts the error rather than eliminating it. The tokenization boundary between the diacritic character and the following 'i' remains unstable.
