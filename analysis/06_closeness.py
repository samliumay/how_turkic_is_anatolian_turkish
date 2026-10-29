import sys, json; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
core = np.load(sys.argv[1] + "/core.npy")
def g(*inc, exc=()): return group(MOD, list(inc), list(exc))
B = [  # label, kind
 ("Azerbaijani · Caucasus", "oghuz", g(r"^Azeri_(Azerbaijan|Armenia|Georgia|Dagestan|Turkey)")),
 ("Azerbaijani · Iran", "oghuz", g(r"^Azeri_Iran")),
 ("Kurds · west & Alevi (Malatya, Kayseri, Çorum, Maraş)", "wa", g(r"^Kurdish_Kurmanji_Turkey_(Malatya|Kayseri|Corum|Kahramanmaras|Konya|Sivas|Eskisehir)")),
 ("Turkish · Erzurum & the east", "tr", g(r"^Turkish_(Erzurum|Erzincan|Kars|Ardahan|Igdir|Agri|Van|Malatya|Elazig|Bitlis|Tunceli|Mus)")),
 ("Kurds · southeast, Iraq & Iran", "wa", g(r"^Kurdish_(Kurmanji_Turkey_(Mardin|Diyarbakir|Siirt|Van|Hakkari|Bitlis)|Zaza_Diyarbakir|Kurmanji_Iraq|Sorani|Iraq|Iran)")),
 ("Nogai & Karachay-Balkar", "kipchak", g(r"^(Nogai|Karachay|Balkar|Kumyk)")),
 ("Persian & Lur", "wa", g(r"^(Persian|Lur)", exc=[r"Jew", r"Zoroastrian"])),
 ("Greek · Anatolia & Pontus", "eu", g(r"^Greek_(Pontus|Cappadocia|Central_Anatolia|Western_Anatolia|Lycaonia|Sebasteia|Armenian_Highland|Constantinople|Propontis)", exc=[r"Muslim"])),
 ("Armenian", "wa", g(r"^Armenian", exc=[r"Jew"])),
 ("North Caucasus", "wa", g(r"^(Chechen|Ingush|Avar|Lezgin|Dargin|Lak|Circassian|Ossetian|Kabardin|Adyghe|Tabasaran)")),
 ("Greek · mainland & islands", "eu", g(r"^Greek_", exc=[r"Muslim", r"Italy", r"^Greek_(Pontus|Cappadocia|Central_Anatolia|Western_Anatolia|Lycaonia|Sebasteia|Armenian_Highland|Constantinople|Propontis)"])),
 ("Italian · Centre & South", "eu", g(r"^Italian_(Lazio|Umbria|Marche|Abruzzo|Molise|Campania|Apulia|Basilicata|Calabria|Sicily)")),
 ("Georgian & Laz", "wa", g(r"^(Georgian|Mingrelian|Svan|Laz)", exc=[r"Jew"])),
 ("Turkmen", "oghuz", g(r"^Turkmen")),
 ("Bulgarian", "eu", g(r"^Bulgarian")),
 ("Crimean Tatar", "kipchak", g(r"^Crimean_Tatar")),
 ("Uzbek", "turkic", g(r"^(Uzbek|Karakalpak)")),
 ("Kazakh", "turkic", g(r"^Kazakh", exc=[r"Eastern_European-Mixed"])),
 ("Kyrgyz", "turkic", g(r"^Kyrgyz")),
]
out = [{"label": l, "kind": k, "d": round(dist(core, v), 2), "n": sum(x[2] for x in sel)} for l, k, (v, sel) in B]
out.sort(key=lambda r: r["d"]); json.dump(out, open(sys.argv[1] + "/closeness.json", "w"), ensure_ascii=False, indent=0)
for r in out: print(f'{r["d"]:6.2f}  n={r["n"]:<4} {r["kind"]:8s} {r["label"]}')
