# how_turkic_is_anatolian_turkish

A small ancient-DNA modeling exercise: how much of the modern Anatolian Turkish genome traces back to
the medieval Turkic populations of the steppe, and how much to the people who were already living in
Anatolia when the Seljuks arrived?

This repository holds the model definitions, the analysis scripts and their results behind the write-up
on [umaysamli.com](https://umaysamli.com/blog/how-turkic-is-anatolian-turkish).

## Results in short

- **The author's kit** (Illustrative DNA, medieval model): 56.2% Byzantine Anatolia, 23.0% Turkic,
  18.8% Kartvelian, 2.0% Iranian Plateau, fit 1.779.
- **Core Anatolia** (778 Turks from western, central and northern Anatolia, Hanami DNA reference data):
  54.9% Byzantine Anatolia, 23.1% medieval Turkic, 21.9% Kartvelian, fit 2.06. Per region the Turkic share
  runs from 20.6% (Central) to 28.2% (West).
- **The pre-Turkic layer** is mostly Bronze Age Anatolian and Caucasian; Greek sources get 0% and Celtic
  (Galatian proxy) at most a few percent.
- **Closest populations** to core Anatolia: Azerbaijanis (3.5), then western and Alevi Kurds (4.7) and
  eastern Turks (5.1), who sit in the Azerbaijani cluster themselves. Greeks (7.0 to 8.3), Armenians
  (7.2) and the North Caucasus (7.2) come next; Uzbeks (20.5), Kazakhs (32.2) and Kyrgyz (35.7) are far
  away. Distances are G25 × 100.

## Layout

| Path | What it is |
| --- | --- |
| `models/core-anatolia.md` | The medieval model, all fits and the pre-Turkic split |
| `data/samples.md` | The ancient samples behind each source, with site, dating and uniparental markers |
| `analysis/` | Python scripts that produce every number and figure (see `analysis/README.md`) |
| `results/` | Their JSON output |
| `paper/` | Short IEEE-format paper (to be updated to these results) |

## Reproduce

See `analysis/README.md`. The scripts need the published Global-25 `modern.csv` and `ancient.csv`
(set `G25_DIR`), numpy and scipy. The author's own coordinates are not in this repository.

## Sources

- Lazaridis et al. (2022),
  [The genetic history of the Southern Arc: A bridge between West Asia and Europe](https://doi.org/10.1126/science.abm4247),
  *Science*: the Çapalıbağ (post-Seljuk southwestern Türkiye) and Gyumri (Black Fortress) samples.
- Damgaard et al. (2018),
  [137 ancient human genomes from across the Eurasian steppes](https://doi.org/10.1038/s41586-018-0094-2),
  *Nature*.
- Damgaard et al. (2018),
  [The first horse herders and the impact of early Bronze Age steppe expansions into Asia](https://doi.org/10.1126/science.aar7711),
  *Science*.
- Jeong et al. (2020),
  [A Dynamic 6,000-Year Genetic History of Eurasia's Eastern Steppe](https://doi.org/10.1016/j.cell.2020.10.015),
  *Cell*.
