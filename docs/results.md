# Results

The headline numbers are in the [README](../README.md#results-in-short). The full tables are in
[`models/core-anatolia.md`](../models/core-anatolia.md); this page says where each result lives.

## Files

| File | Written by | What it holds |
| --- | --- | --- |
| `results/core_to_groups.json` | `01` | Distance (G25 × 100) from the core-Anatolia average to every Hanami DNA curated group: `[id, name, distance]` |
| `results/models.json` | `02` | Every model on core Anatolia and on the author's row: `weights` (source, %) and `fit` |
| `results/clusters.json` | `04` | The original 3-way model per region: `n`, `byz`, `tur`, `kar` (%), `fit`, and whether the region is in the core |
| `results/closeness.json` | `06` | The closeness chart: `label`, `kind` (colour group), `d` (distance), `n` |
| `results/pca.json` | `07` | PCA points per group, without the author's point |
| `results/capalibag.json` | `09` | Per region: Byzantine / Çapalıbağ / Kartvelian and Byzantine / Kaman-Kalehöyük / Kartvelian shares and fits |
| `results/subgroups.json` | `11` | Per Turkish subgroup row: the Turkic, Çapalıbağ and Kaman-Kalehöyük share and fit of each 3-way model |

`03_pre_turkic_split.py` and `05_kurdish_subgroups.py` print their results and save nothing.

## In the paper

[`paper/main.pdf`](../paper/main.pdf) (IEEE conference format; source `paper/main.tex`) reports the
results above and adds two models that are not in the README:

- **Çapalıbağ (1300–1650) as the Turkic source**, per region (Table in `paper/tables/regions.tex`, figure in
  `paper/figures/regions.tex`).
- **Ottoman-era Kaman-Kalehöyük as the Turkic source**, per region and per subgroup
  (`paper/tables/subgroups.tex`).

The paper's second version (2026-10-30) is built on the Hanami DNA reference data and the author's
Illustrative DNA results. Earlier versions are kept in `paper/old_versions/`.

## Blog post

The write-up is on [umaysamli.com](https://umaysamli.com/blog/how-turkic-is-anatolian-turkish). Its data
file comes from `08_emit_site_data.py`.
