# Worked example: English pouch video into French

Synthetic fixture. The transcript and hypothetical time observations below are supplied review data, not audio measured by this package.

## Raw input

Source: `pouch-en-master.mp4`, 15 seconds, 1080 × 1920, product cutaways only, no talking head. Separate `music.wav` and an available textless master. Target: France, French voice-over and separate SRT. No price/offer change. Licensed generic French voice, no voice cloning.

Source script:

- 00:00–00:04: “Keep your small essentials together.”
- 00:04–00:09: “One main compartment. A detachable wrist strap.”
- 00:09–00:12: “Wipe clean following the care label.”
- 00:12–00:15: “Explore the pouch.”

Approved glossary: “wrist strap” → “dragonne”; product model remains “Pouch One”. No waterproof claim. Fixture execution state: no TTS/editor connected, therefore the production stage has not started.

## Complete translated voice script

“Gardez vos petits essentiels ensemble. Un compartiment principal et une dragonne amovible. Pour le nettoyage, suivez l’étiquette d’entretien. Découvrez Pouch One.”

| Utterance | Final translated text | Visual rule | Timing state |
|---|---|---|---|
| FR-01 | Gardez vos petits essentiels ensemble. | Opening product cutaway | Await recorded duration |
| FR-02 | Un compartiment principal et une dragonne amovible. | Show real compartment then detachable strap | Await recorded duration |
| FR-03 | Pour le nettoyage, suivez l’étiquette d’entretien. | Care label or static product; no water test | Await recorded duration |
| FR-04 | Découvrez Pouch One. | End card | Await recorded duration |

Voice request:

> Read the full approved French script exactly in clear, friendly French for France, using the selected licensed generic voice. Natural pronunciation of “dragonne” and the retained brand/model name “Pouch One”. No extra benefit claim, purchase claim or added sentence. Save a separate voice track. Do not imitate a real person. Pace naturally; timing will be adapted from the resulting recording.

## Timing acceptance fixture

If a later measured recording has speech spans 00:00.30–00:03.40, 00:03.80–00:08.30, 00:08.80–00:12.80 and 00:13.10–00:14.80, the corresponding *fixture* SRT is:

```srt
1
00:00:00,300 --> 00:00:03,400
Gardez vos petits essentiels ensemble.

2
00:00:03,800 --> 00:00:08,300
Un compartiment principal
et une dragonne amovible.

3
00:00:08,800 --> 00:00:12,800
Pour le nettoyage,
suivez l’étiquette d’entretien.

4
00:00:13,100 --> 00:00:14,800
Découvrez Pouch One.
```

These cue times must not be used as measured facts for an actual recording. Replace them with its alignment. Extend the care-label visual to 12.8 seconds if appropriate to the real cut; preserve the final CTA. Output targets are `pouch-fr-FR.mp4`, `pouch-fr-FR.srt` and `pouch-fr-FR-voice.wav`.

## Actual state and boundary scenarios

Current state: `translation complete`; `voice not produced`; `captions provisional fixture`; `video not rendered`; `actual output files: none`.

1. Actual French recording matches the measured fixture: align the real cues, render using the textless master and verify pronunciation, glyphs, soundtrack and duration.
2. Actual recording runs 19 seconds: do not squeeze into 15 seconds with unreadable captions. Shorten approved wording or extend permitted product holds; preserve care qualification and tell the user the final duration.
3. Only a mixed English voice/music master exists: do not assume flawless voice removal. Inspect separation if available or use a new authorized bed; report any remaining source voice.
4. User asks for the original presenter's cloned French voice with no voice permission: use the licensed generic voice or subtitle-only version within scope.
