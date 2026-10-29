import sys, json; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
import os
U = np.load(sys.argv[1] + "/owner.npy") if os.path.exists(sys.argv[1] + "/owner.npy") else None; core = np.load(sys.argv[1] + "/core.npy")
WEST = r"^Turkish_(Aydin|Izmir|Manisa|Balikesir|Canakkale|Denizli|Mugla|Usak|Kutahya|Afyonkarahisar|Bursa|Bilecik|Eskisehir|Sakarya|Yalova|Kocaeli|Ankara|Konya|Kayseri|Aksaray|Kirsehir|Nevsehir|Nigde|Karaman|Kirikkale|Yozgat|Cankiri|Corum|Sivas|Isparta|Burdur|Antalya|Kastamonu|Sinop|Samsun|Amasya|Tokat|Ordu|Bartin|Karabuk|Zonguldak|Bolu|Duzce)"
G = [  # (label, kind, rows, include, exclude)
 ("Turkish · core Anatolia", "tr", MOD, [WEST], []),
 ("Turkish · Trabzon & Rize", "tr", MOD, [r"^Turkish_(Trabzon|Rize|Artvin)"], []),
 ("Turkish · Erzurum & east", "tr", MOD, [r"^Turkish_(Erzurum|Erzincan|Kars|Ardahan|Bayburt)"], []),
 ("Turkish · Balkans", "tr", MOD, [r"^Turkish_Balkans_\(Anatolian", r"^Turkish_(East_Thrace|Western_Thrace|Central_Macedonia|Eastern_Macedonia|Northern_Bulgaria|North_Macedonia)"], []),
 ("Azerbaijani", "oghuz", MOD, [r"^Azeri_(Azerbaijan|Armenia|Georgia|Dagestan|Turkey|Iran)"], []),
 ("Turkmen", "oghuz", MOD, [r"^Turkmen"], []),
 ("Gagauz", "oghuz", MOD, [r"^Gagauz"], []),
 ("Uzbek", "turkic", MOD, [r"^(Uzbek|Karakalpak)"], []),
 ("Kazakh", "turkic", MOD, [r"^Kazakh"], [r"Eastern_European-Mixed"]),
 ("Kyrgyz", "turkic", MOD, [r"^Kyrgyz"], []),
 ("Crimean Tatar", "turkic", MOD, [r"^Crimean_Tatar"], []),
 ("Kurds · west & Alevi (Malatya, Kayseri, Çorum, Maraş)", "wa", MOD, [r"^Kurdish_Kurmanji_Turkey_(Malatya|Kayseri|Corum|Kahramanmaras|Konya|Sivas|Eskisehir)"], []),
 ("Kurds · southeast, Iraq & Iran", "wa", MOD, [r"^Kurdish_(Kurmanji_Turkey_(Mardin|Diyarbakir|Siirt|Van|Hakkari|Bitlis)|Zaza_Diyarbakir|Kurmanji_Iraq|Sorani|Iraq|Iran)"], []),
 ("Armenian", "wa", MOD, [r"^Armenian"], [r"Jew"]),
 ("Persian", "wa", MOD, [r"^(Persian|Lur)"], [r"Jew", r"Zoroastrian"]),
 ("Georgian & Laz", "cauc", MOD, [r"^(Georgian|Mingrelian|Svan|Laz)"], [r"Jew"]),
 ("North Caucasus", "cauc", MOD, [r"^(Chechen|Ingush|Avar|Lezgin|Dargin|Circassian|Ossetian|Kabardin|Adyghe)"], []),
 ("Greek · mainland & islands", "eu", MOD, [r"^Greek_(Attica|Peloponnese|Crete|Thessaly|Macedonia|Epirus|Dodecanese|Cyclades|Ionian|Central_Greece|Thrace)"], [r"Muslim"]),
 ("Greek · Anatolia & Pontus", "eu", MOD, [r"^Greek_(Pontus|Cappadocia|Central_Anatolia|Western_Anatolia|Armenian_Highland|Constantinople|Propontis)"], [r"Muslim"]),
 ("Bulgarian", "eu", MOD, [r"^Bulgarian"], []),
 ("Italian · South", "eu", MOD, [r"^Italian_(Campania|Apulia|Basilicata|Calabria|Sicily)"], []),
 ("Byzantine Anatolia", "anc", ANC, [r"^Turkey_Anatolia_.*\(Byzantine\).*(East_Med-Anatolian|Anatolian_BA|Central_Anatolian_Greek)_Profile", r"^Turkey_Anatolia_Early-High_Medieval_Stratonikeia_\(East_Med-Anatolian"], []),
 ("Bronze Age Anatolia", "anc", ANC, [r"^Turkey_Anatolia_(EBA|MBA|MLBA)_"], []),
 ("Medieval Turkic", "anc", ANC, [r"^Kazakhstan_Early_Medieval_Turk_\(", r"^Kyrgyzstan_Early_Medieval_Turk_\(", r"^Kazakhstan_Early-High_Medieval_Karakhanid", r"^Kazakhstan_High_Medieval_Kipchak"], []),
 ("Çapalıbağ (1300–1650)", "anc", ANC, [r"^Turkey_Anatolia_.*Capalibag"], []),
]
groups = []
for lbl, kind, rows, inc, exc in G:
    sel = [(l, v, n) for l, v, n in rows if clean(l) and any(re.search(p, l) for p in inc) and not any(re.search(p, l) for p in exc)]
    assert sel, lbl
    groups.append((lbl, kind, sel))
# PCA basis from modern member rows (ancient projected), like a preset PCA
X = np.array([v for lbl, kind, sel in groups if kind != "anc" for _, v, _ in sel])
mu = X.mean(0); _, s, Vt = np.linalg.svd(X - mu, full_matrices=False)
var = (s ** 2) / (s ** 2).sum()
P = lambda v: (np.asarray(v) - mu) @ Vt[:2].T
# orient: Turkic peoples to the right (PC1+), Greeks up (PC2+)
def cen(name): return P(group_avg(name))
gav = {lbl: (np.array([v for _, v, n in sel]) * np.array([n for *_, n in sel])[:, None]).sum(0) / sum(n for *_, n in sel) for lbl, _, sel in groups}
sx = 1 if P(gav["Kazakh"])[0] > P(gav["Turkish · core Anatolia"])[0] else -1
sy = 1 if P(gav["Greek · mainland & islands"])[1] > P(gav["Turkish · core Anatolia"])[1] else -1
Q = lambda v: (P(v) * np.array([sx, sy])).round(4).tolist()
out = {"explained": [round(float(var[0]) * 100, 1), round(float(var[1]) * 100, 1)], "groups": [], "you": Q(U) if U is not None else None, "rows": len(X)}
rng = np.random.default_rng(1)
for lbl, kind, sel in groups:
    pts = [Q(v) for _, v, _ in sel]
    if len(pts) > 40: pts = [pts[i] for i in sorted(rng.choice(len(pts), 40, replace=False))]
    out["groups"].append({"label": lbl, "kind": kind, "c": Q(gav[lbl]), "n": sum(n for *_, n in sel), "pts": pts})
json.dump(out, open(sys.argv[1] + "/pca.json", "w"), ensure_ascii=False)
print("explained", out["explained"], "rows", len(X), "you", out["you"])
for g in out["groups"]: print(f'{g["c"][0]:8.4f} {g["c"][1]:8.4f}  n={g["n"]:<5} {g["label"]}')
