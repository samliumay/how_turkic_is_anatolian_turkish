# how_turkic_is_anatolian_turkish

A small ancient-DNA modeling exercise: how much of the modern Anatolian Turkish genome traces back to
the medieval Turkic populations of the steppe, and how much to the people who were already living in
Anatolia when the Seljuks arrived?

This repository holds the model definitions, the analysis scripts, their results and a short IEEE-format
paper behind the write-up on [umaysamli.com](https://umaysamli.com/blog/how-turkic-is-anatolian-turkish).

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

More in [docs/results.md](docs/results.md).

## Quick start

```bash
export G25_DIR=/path/to/g25/      # folder with modern.csv and ancient.csv; keep the trailing slash
W=$(mktemp -d)
uv run --with numpy --with scipy python analysis/01_core_and_groups.py "$W"
uv run --with numpy --with scipy python analysis/02_models.py "$W"
cd paper && make pdf              # paper/main.pdf
```

> [!WARNING]
> `01_core_and_groups.py` also reads the group definitions from a hard-coded path into the Hanami DNA
> backend, which is not public. See [docs/reproducing.md](docs/reproducing.md) for the full pipeline and
> what it needs. The author's own coordinates are not in this repository.

## Layout

| Path | What it is |
| --- | --- |
| `models/core-anatolia.md` | The medieval model, all fits and the pre-Turkic split |
| `data/samples.md` | The ancient samples behind each source, with site, dating and uniparental markers |
| `analysis/` | Python scripts that produce every number, table and figure |
| `results/` | Their JSON output |
| `paper/` | Short IEEE-format paper (`paper/main.pdf`) |
| `bibliography.bib` | The verified bibliography the paper uses |

## Documentation

| Doc | What it answers |
| --- | --- |
| [docs/README.md](docs/README.md) | Index of the docs |
| [docs/methodology.md](docs/methodology.md) | How the populations are averaged, compared and fitted |
| [docs/data.md](docs/data.md) | Which data the analysis uses, and where it comes from |
| [docs/reproducing.md](docs/reproducing.md) | The commands, in order, from G25 files to the paper PDF |
| [docs/results.md](docs/results.md) | Where each result lives, and what the paper adds |
