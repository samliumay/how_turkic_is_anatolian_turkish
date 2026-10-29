# Humanizer pass and IEEE paper, 2026-10-29

## Ownership decision

The researcher asked for the humanizer on this side project's blog post and for the paper in IEEE format (2026-10-29). This is a blog side project, and the post was agent-drafted, so edits are allowed in every section.

## Paper (new)

There was no paper before this pass. `paper/main.tex` (IEEEtran, `conference,a4paper`, same setup as `is_hypergamy_real/paper`) was written from the blog post, `../models/core-anatolia.md` and `../data/samples.md`. It adds no new numbers. Two TikZ figures (`figures/timeline.tex`, `figures/model.tex`), Okabe-Ito colours plus patterns for greyscale.

- Build: `make pdf` (latexmk, pdflatex; BibTeX reads `../bibliography.bib`). 3 pages, no warnings, BibTeX 0 warnings.
- `../bibliography.bib`: 4 entries, each fetched from doi.org (Crossref BibTeX) on 2026-10-29; keys renamed; `month` fields removed (IEEEtran has no "june" macro).
- The acknowledgment discloses AI assistance (IEEE recommends disclosure there). Edit or remove it as you see fit.
- **Open:** the Kartvelian share (20.8%) was inferred as 100 - 56.2 - 23.0. A `%%` comment at the top of `main.tex` lists every place to update once the model output is checked.
- Scan of the new text: 1688 words, ; 0.07, : 0.05, ( 0.14 per sentence, nominalizations 0.55. The one summary opener ("In short") was removed.

## Blog post

Glossary: Göktürk-era / medieval Turkic (source), Byzantine Anatolia, Kartvelian, core Anatolia, cluster, band, fit distance. American spelling (the post's own). No em dashes.

| | words | sentences | ; /sent | : /sent | ( /sent | nominal./sent | longest |
|---|---|---|---|---|---|---|---|
| before | 1603 | 91 | 0.07 | 0.25 | 0.14 | 0.52 | 55 |
| after | 1591 | 96 | 0.03 | 0.22 | 0.14 | 0.49 | 46 |

Changes: the two em dashes rewritten; the Çapalıbağ uniparental sentence split; "In words: on the Göktürk side, ...; the rest ..." made two sentences; two of four "rather than" removed (one restated "their own cluster", one tail about a screenshot); "ultimately" deleted; the conclusion's point 3 split.

Fidelity: facts unchanged. Kept review items: "modeled separately rather than blended into Anatolia proper" -> "modeled separately" (restates the bold label); "rather than a hand-picked pair" -> "instead of a hand-picked pair" (same contrast), with the screenshot tail dropped.

Blind check (seed 1, N = 6): after preferred in 4/6. Pair 6 was an unchanged paragraph (the post had only five changed paragraphs). In pair 4 the reader preferred the original "can actually answer", so "actually" was restored. Light pass on text that was already fairly clean.

This pass changes style, not authorship; disclose AI assistance per the venue's policy.

# Second version and humanizer pass, 2026-10-30

## What changed (content, by the researcher's corrections)

- Rebuilt on the Hanami DNA G25 reference data (`../analysis/`, results in `../results/`) and the author's Illustrative DNA results.
- Kartvelian corrected: the kit is 56.2% Byzantine Anatolia, 23.0% Turkic, 18.8% Kartvelian, 2.0% Iranian Plateau (fit 1.779). The earlier 20.8% was an inference and was wrong.
- Three models per target: medieval Turkic, Çapalıbağ (early Anatolian Turkic, 12 people) and Kaman-Kalehöyük (Ottoman-era, 3 people). All three put core Anatolia at about 23% medieval Turkic.
- All regions including Trabzon, Erzurum and the Balkan Turks; appendix with 89 Turkish subgroups.
- Corrected claims: Azerbaijanis are the closest population; Kurds are split (west/Alevi vs southeast/Iraq/Iran) because the closest Kurds belong to the Azerbaijani/eastern cluster; Greeks are no closer than Armenians; Anatolian is not Greek.
- Title shortened to "How Turkic Is Anatolian Turkish?". Before copy: `old_versions/main_2026-10-29_first_version.tex`.

## Humanizer pass

Before copy: `old_versions/main_2026-10-30_before_humanizer.tex`. Edits allowed everywhere (side project, agent-drafted).

| | words | ; /sent | : /sent | ( /sent | nominal./sent | longest |
|---|---|---|---|---|---|---|
| before | 1900 | 0.17 | 0.11 | 0.45 | 0.44 | 46 |
| after (with the later Ottoman and subgroup paragraphs) | 2180 | 0.08 | 0.12 | 0.45 | 0.37 | 45 |

- Seven semicolon-joined sentences split (abstract, method, results, limitations, conclusion, data availability). Fidelity on the humanizer edits alone: exit 0, no review items.
- Parentheses stay above 0.30: almost all hold numbers next to their claim (distances, shares, n), which a results paper needs.
- The repeated "Anatolian, not Greek" sentence in Results and Conclusion is intended (conclusion restates the finding).
- Blind reader check skipped: seven punctuation-level edits give pairs too similar to judge (the skill's own note on similarity above 0.95).
- Blog post (written fresh in this session): colons 0.33 per sentence come from the bold region labels in the two lists, a site convention; no em dashes; two rhetorical questions are the post's framing.

This pass changes style, not authorship; disclose AI assistance per the venue's policy.
