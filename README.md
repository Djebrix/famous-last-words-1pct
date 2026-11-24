# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Djebrix/famous-last-words-1pct/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/Djebrix/famous-last-words-1pct/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for [Famous Last Words at 1 Percent](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) — the funniest one-line farewell a phone says as its battery hits 1 percent.

## The line

> Plot twist: I've been at 1 percent for three hours. I just liked watching you panic.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (override with `ENTRY_OUTPUT_DIR`).

```sh
ENTRY_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```

Stdlib only, no network, deterministic — the same line every run.
