# Data

## What the analysis reads

| Input | What it is | In the repo? |
| --- | --- | --- |
| `modern.csv`, `ancient.csv` | The published Global-25 (G25) reference coordinates, as used by Hanami DNA. The paper counts 3,227 modern and 5,071 ancient rows. Columns: `Name`, `c1` … `c25`. | No. Point `G25_DIR` at the folder that holds them. |
| `V3__groups_presets_and_panel.sql` | Hanami DNA's curated group definitions (name, include and exclude patterns). Only `01_core_and_groups.py` reads it, for the distance to every curated group. | No. The path is hard-coded to the Hanami DNA backend. |
| `owner.npy` | The author's own G25 row, used for the "owner" models and the PCA point. | No. Private and git-ignored (`*.npy`). Every script skips it if it is missing. |
| Illustrative DNA result | The author's kit on Illustrative DNA's medieval model (2026-10-30), quoted in `models/core-anatolia.md`. | Only the published shares. |

## Ancient samples

[`data/samples.md`](../data/samples.md) lists the individuals behind each source and control, with site,
dating and uniparental markers:

- the **medieval Turkic reference pool** (AD 650–1200), Central Steppe and Tian Shan;
- the **Çapalıbağ** individuals, southwestern Türkiye, 1300–1650 CE;
- **Gyumri** (Black Fortress cemetery), Armenia, 1665–1950 CE, a control for the Caucasus-side profile.

## Sources

The ancient individuals are published in these papers (full entries in
[`bibliography.bib`](../bibliography.bib)):

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
