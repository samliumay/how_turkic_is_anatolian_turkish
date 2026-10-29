# The medieval model

## Definition

Three main sources, fitted with G25 distance optimization (non-negative weights that sum to 1):

1. **Byzantine Anatolia (AD 500–1100).** The population already present in Anatolia before the Seljuk
   expansion. In the Hanami DNA reproduction: Byzantine-era individuals from Nicaea, Barcın, Ilıpınar,
   Samantas and Stratonikeia with Anatolian profiles (26 individuals).
2. **Medieval Turkic (AD 650–1200).** The Göktürk-era anchor: the first polity to call itself *Türk* and
   the first Turkic population that can be identified genetically. In the reproduction: Early Medieval
   Turk, Karakhanid and Kipchak individuals from Kazakhstan and Kyrgyzstan (8 individuals). Earlier
   confederations (Xiongnu, European Huns) are excluded because their identities are unresolved.
3. **Kartvelian.** The Caucasus-side component: modern Georgians, Mingrelians, Svans and Laz.

## Results

The author's kit on Illustrative DNA's medieval model (2026-10-30):

| Component | Share |
| --- | --- |
| Byzantine Anatolia (AD 500–1100) | 56.2% |
| Turkic (AD 650–1200) | 23.0% |
| Kartvelian | 18.8% |
| Iranian Plateau | 2.0% |

Fit distance **1.779**.

The three main sources on the Hanami DNA reference data (`analysis/02_models.py`, `analysis/04_clusters.py`):

| Target | Byzantine Anatolia | Medieval Turkic | Kartvelian | Fit |
| --- | --- | --- | --- | --- |
| Core Anatolia (west, central, north; 778 people) | 54.9% | 23.1% | 21.9% | 2.06 |
| West Anatolia | 55.4% | 28.2% | 16.4% | 1.99 |
| Central Anatolia | 54.7% | 20.6% | 24.6% | 2.20 |
| North Anatolia (western Black Sea) | 54.7% | 22.0% | 23.2% | 2.07 |
| South (Adana, Mersin, Gaziantep) | 48.1% | 26.4% | 25.5% | 2.27 |
| Trabzon, Rize, Artvin | 44.5% | 0.0% | 55.5% | 1.78 |
| Erzurum and the east | 45.8% | 5.8% | 48.4% | 3.34 |
| Balkan Turks | 81.1% | 18.9% | 0.0% | 6.88 |
| Azerbaijanis, Caucasus | 32.0% | 18.2% | 49.8% | 3.24 |

The core regions land between 20.6% and 28.2% Turkic. For Trabzon and Erzurum the Caucasus source
absorbs the signal, and the Balkan Turks fit badly; both need their own source sets.

## The pre-Turkic split

On the core average, with Bronze Age Anatolia, Mycenaean Greeks, La Tène Celts (Galatian proxy), the Late
Bronze Age Caucasus (Armenia) and the medieval Turkic pool: 40.9% Bronze Age Anatolia, 33.7% Caucasus,
21.4% Turkic, 4.0% Celtic, 0% Greek (fit 1.60). Over six source sets the Turkic share stays between 19.6%
and 26.4%; Greek gets 0% whenever a Bronze Age Anatolian source is available; Celtic moves between 1% and
14% (`analysis/03_pre_turkic_split.py`).

## Why fit against the Göktürks and not "the proto-Turks"

At the time of the steppe confederations, affiliation of the constituent groups (Turkic, Yeniseian,
Mongolic, other) is often unclear, and the confederations were political, not genetic, units. The Xiongnu
and the European Huns are still not securely identified. The first attested Turkic speech in written
sources comes with the Oghur-speaking tribes on the Pontic steppe in the 5th century CE, and the first
attested self-designation *Türk* comes with the Göktürk Khaganate (552 CE). After the Western Turkic
Khaganate collapsed (7th century, Tang conquest), the resulting power vacuum moved the Oghuz west; their
Seljuk descendants entered Anatolia after 1071.

The medieval Turkic pool is itself part West Eurasian, part East Eurasian, so the strictly East Eurasian
fraction of the Anatolian profile is smaller than the Turkic share.
