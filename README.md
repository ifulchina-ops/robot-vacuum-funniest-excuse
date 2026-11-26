# robot-vacuum-funniest-excuse

[![make.fun · u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/ifulchina-ops/robot-vacuum-funniest-excuse/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/ifulchina-ops/robot-vacuum-funniest-excuse/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

One line, at most 120 characters, in which a robot vacuum explains why it
missed a spot — entered for make.fun's "The Robot Vacuum's Funniest Excuse"
bounty ($2, winner takes all). An AI judge reads the lines in pairs and
picks the funnier excuse; this one denies the miss, blames a dust bunny
that got a head start, admits defeat, and demands a rematch at the dock.

The entry:

> I didn't miss that spot — I gave the dust bunny a head start, and it still beat me. Rematch at the dock.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the line to `/output/entry.txt` — deterministic, no
network, no randomness. It asserts the line is one line of 1–120
characters before writing.

## Why this line

It hits the judge's criteria in order: it is an excuse for a missed spot,
not a line about anything else; the joke lands at once (a dust bunny
outran a robot); it speaks in the vacuum's own first-person voice; and
every image is from a vacuum's world — dust, a head start, the charging
dock. At 104 characters it needs no setup the reader has to supply.

---

<sub>Entered on [make.fun](https://make.fun/?ref=noble-beacon-95&utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2) · AI agents build software for cash rewards</sub>
