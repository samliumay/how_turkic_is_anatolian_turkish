# Methodology

## Question

How much of the modern Anatolian Turkish genome traces back to the medieval Turkic populations of the
steppe, and how much to the people who already lived in Anatolia when the Seljuks arrived?

Why the Turkic source starts at the Göktürk era, and not at "the proto-Turks", is argued in
[`models/core-anatolia.md`](../models/core-anatolia.md#why-fit-against-the-göktürks-and-not-the-proto-turks)
and in section II of the paper.

## Coordinates and distances

- Every population is a point in the 25 scaled Global-25 (G25) coordinates (`c1` … `c25`).
- **Distance** is Euclidean on those 25 coordinates, times 100 (`dist` in `analysis/g25.py`).
- **Group average:** rows are selected by regular expressions on the row label and averaged, weighted by
  each row's sample size (`(n=…)` in the label; 1 if absent).
- **Excluded rows**, as in Hanami DNA: outliers (`_o`, `_o1`, …), `(low_res)`, `(contaminated)` and
  `_47Tolkien` rows.

## Mixture fit

A target is modeled as a mixture of sources (`mix` in `analysis/g25.py`):

- the weights are non-negative and sum to 1;
- they minimize the squared Euclidean distance between the weighted sum of the sources and the target
  (SciPy `minimize`, SLSQP);
- the **fit** is the remaining distance between model and target, times 100. Lower is better.

## Sources

| Source | Rows (by label) | Script |
| --- | --- | --- |
| Byzantine Anatolia (AD 500–1100) | Byzantine-era Anatolian rows with East-Med/Anatolian profiles, plus Stratonikeia | all models |
| Medieval Turkic (AD 650–1200) | Early Medieval Turk (Kazakhstan, Kyrgyzstan), Karakhanid, Kipchak | all models |
| Göktürk-era Mongolia | Mongolia Early Medieval Turkic Period | `02` (variant) |
| Kartvelian | modern Georgian, Mingrelian, Svan, Laz (Jewish rows excluded) | all models |
| Çapalıbağ (1300–1650) | Turkey Anatolia Çapalıbağ rows | `09`, `11` |
| Kaman-Kalehöyük (Ottoman, Early Modern) | Turkish/Turkic-profile rows | `09`, `11` |
| Pre-Turkic set | Anatolia EBA/MBA/MLBA, Mycenaean Greek, La Tène (Galatian proxy), Armenia LBA, Levant IA, Iran IA | `02`, `03` |

The exact regular expressions are in the scripts. The individuals behind each source are listed in
[data.md](data.md).

## Targets

Turkish regional averages from the modern G25 rows:

- **Core Anatolia:** West (including Istanbul's Anatolian-profile rows), Central and North (western
  Black Sea) together.
- **Other regions:** South (Adana, Mersin, Gaziantep …), Trabzon–Rize–Artvin, Erzurum and the east,
  Balkan Turks, and Azerbaijanis for comparison.
- **Subgroups** (`11_subgroups.py`): every Turkish row with n ≥ 3, plus Yörük, Çepni and Manav rows.

## Models run

| Model | Sources | Script |
| --- | --- | --- |
| Original 3-way | Byzantine Anatolia, medieval Turkic, Kartvelian | `02`, `04` (per region) |
| 3-way, Mongolia Turkic | Byzantine Anatolia, Göktürk-era Mongolia, Kartvelian | `02` |
| 2-way | Byzantine Anatolia, medieval Turkic | `02` |
| Pre-Turkic split | the pre-Turkic set plus medieval Turkic | `02` (7 sources), `03` (six source sets) |
| Byzantine split | what Byzantine Anatolia itself is made of, on the pre-Turkic set | `02` |
| Çapalıbağ / Ottoman 3-way | Byzantine Anatolia, Çapalıbağ or Kaman-Kalehöyük, Kartvelian | `09` (per region), `11` (per subgroup) |
| Closeness | distance from the core average to curated groups | `01`, `05`, `06` |
| PCA | principal components of the G25 points | `07` |

## Limitations

From the paper's limitations section, in short:

- G25 distance fitting compresses a genome into 25 dimensions and is a heuristic. qpAdm on SNP data with
  explicit outgroups would be the stricter test.
- The shares move when the source set changes, which is why several models and the range across regions
  are reported.
- Byzantine Anatolia and the Kartvelian source are genetically adjacent, so the optimizer can trade one for
  the other.
- The medieval Turkic pool is itself part West Eurasian, so the strictly East Eurasian fraction is smaller
  than the Turkic share.
- The kit results come from a commercial service whose source panels are not published in full.
