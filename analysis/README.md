# Analysis

Python scripts behind the post's and the paper's numbers. They read the published Global-25 reference data
(`modern.csv`, `ancient.csv`) used by Hanami DNA; set `G25_DIR` to the folder that holds them (with a
trailing `/`). Distances are Euclidean on the 25 scaled coordinates, times 100. Group averages are weighted
by sample size and skip outlier (`_o`), low-resolution, contaminated and 47Tolkien rows, as in Hanami DNA.

Scripts `01` to `07` take one argument, a work folder. `01_core_and_groups.py` writes `core.npy` (the
core-Anatolia average) there; later scripts read it. Scripts that compare against the author also read
`owner.npy` from the work folder. The author's row is private and not in this repository.

The commands, in order, are in [`../docs/reproducing.md`](../docs/reproducing.md); the method is in
[`../docs/methodology.md`](../docs/methodology.md).

| Script | Output |
| --- | --- |
| `g25.py` | shared helpers: loading, group averages, distance, mixture fit |
| `01_core_and_groups.py` | core-Anatolia average (778 people), distance to every curated group (`core_to_groups.json`) |
| `02_models.py` | the three-way medieval model and variants (`models.json`) |
| `03_pre_turkic_split.py` | the pre-Turkic split over six source sets (printed) |
| `04_clusters.py` | the three-way model per Turkish region (`clusters.json`) |
| `05_kurdish_subgroups.py` | every Kurdish subgroup against core Anatolia, Azerbaijanis and eastern Turks (printed) |
| `06_closeness.py` | the closeness chart (`closeness.json`) |
| `07_pca.py` | the PCA (`pca.json`) |
| `08_emit_site_data.py` | the website's `turkic-data.ts` |
| `09_capalibag.py` | Çapalıbağ and Kaman-Kalehöyük as Turkic sources, per region (`results/capalibag.json`) |
| `10_paper_figures.py` | `paper/figures/regions.tex`, `closeness.tex`, `pca.tex` |
| `11_subgroups.py` | every Turkish subgroup on the three models (`results/subgroups.json`) |
| `12_paper_tables.py` | `paper/tables/regions.tex`, `subgroups.tex` |
