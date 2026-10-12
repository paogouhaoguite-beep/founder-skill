# Synthetic worked example

Input verified spoken phrase from 1.0 to3.0 sec: “Hand wash only.” SRT cue:
```srt
1
00:00:01,000 --> 00:00:03,000
Hand wash only.
```

Duration 2 sec, positive and ordered. This synthetic timing is supplied, not inferred. The real player still requires placement/readability verification.

Boundary scenario 1: The script says “dishwasher-safe” but audio says “not dishwasher-safe.” Captions follow the actual audio and flag the script discrepancy.
Boundary scenario 2: No audio or timing exists. Deliver text segments and request timing evidence; do not invent an SRT that appears synchronized.
