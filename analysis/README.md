# Analysis

Python scripts behind the post's numbers. They read the published Global-25 reference data
(`modern.csv`, `ancient.csv`) used by Hanami DNA; set `G25_DIR` to the folder that holds them.
Distances are Euclidean on the 25 scaled coordinates, times 100. Group averages are weighted by
sample size and skip outlier (`_o`), low-resolution, contaminated and 47Tolkien rows, as in Hanami DNA.

Every script takes one argument, a work folder. `01_core_and_groups.py` writes `core.npy` (the
core-Anatolia average) there; later scripts read it. Scripts that compare against the author also
read `owner.npy` from the work folder. The author's row is private and not in this repository.

```bash
W=$(mktemp -d)   # plus owner.npy if you have your own row
for s in 01_core_and_groups 02_models 03_pre_turkic_split 04_clusters 05_kurdish_subgroups 06_closeness 07_pca; do
  uv run --with numpy --with scipy python analysis/$s.py "$W"
done
uv run --with numpy --with scipy python analysis/08_emit_site_data.py "$W" turkic-data.ts
```

| Script | Output |
| --- | --- |
| `01_core_and_groups.py` | core-Anatolia average (778 people), distance to every curated group |
| `02_models.py` | the three-way medieval model and variants (`results/models.json`) |
| `03_pre_turkic_split.py` | the pre-Turkic split over six source sets |
| `04_clusters.py` | the three-way model per Turkish region (`results/clusters.json`) |
| `05_kurdish_subgroups.py` | every Kurdish subgroup against core Anatolia, Azerbaijanis and eastern Turks |
| `06_closeness.py` | the closeness chart (`results/closeness.json`) |
| `07_pca.py` | the PCA (`results/pca.json`, without the author's point) |
| `08_emit_site_data.py` | the website's `turkic-data.ts` |
