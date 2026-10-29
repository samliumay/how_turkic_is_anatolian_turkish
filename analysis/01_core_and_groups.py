import sys, re; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
import os
sql = open("/home/umaysamli/Desktop/projects/hanami/platform/hanamidna/hanami_dna_backend/src/main/resources/db/migration/V3__groups_presets_and_panel.sql", encoding="utf-8").read()
names = dict(re.findall(r"\('([a-z0-9-]+)', '([^']+)', 'modern'\)", sql))
rules = {}
for g, p, e in re.findall(r"\('([a-z0-9-]+)', '((?:[^']|'')+)', (true|false)\)", sql):
    rules.setdefault(g, ([], []))[1 if e == "true" else 0].append(p.replace("''", "'").replace("\\(", "\\(").replace("\\)", "\\)"))
G = {}
for g, (inc, exc) in rules.items():
    if g in names and inc:
        try: G[g] = group(MOD, inc, exc)[0]
        except ValueError: pass
WEST = r"^Turkish_(Aydin|Izmir|Manisa|Balikesir|Canakkale|Denizli|Mugla|Usak|Kutahya|Afyonkarahisar|Bursa|Bilecik|Eskisehir|Sakarya|Yalova|Kocaeli)"
CENT = r"^Turkish_(Ankara|Konya|Kayseri|Aksaray|Kirsehir|Nevsehir|Nigde|Karaman|Kirikkale|Yozgat|Cankiri|Corum|Sivas|Isparta|Burdur|Antalya)"
NORTH = r"^Turkish_(Kastamonu|Sinop|Samsun|Amasya|Tokat|Ordu|Bartin|Karabuk|Zonguldak|Bolu|Duzce)"
core, sel = group(MOD, [WEST, CENT, NORTH, r"^Turkish_Istanbul_\(Anatolian_Turk_Profile"])
np.save(sys.argv[1] + "/core.npy", core)
print("core rows", len(sel), "individuals", sum(n for *_, n in sel))
U = np.load(sys.argv[1] + "/owner.npy") if os.path.exists(sys.argv[1] + "/owner.npy") else None
if U is not None: print("owner->core", round(dist(U, core), 2))
rows = sorted(((dist(core, v), names[g], g) for g, v in G.items()), key=lambda t: t[0])
import json; json.dump([(g, n, round(d, 2)) for d, n, g in rows], open(sys.argv[1] + "/core_to_groups.json", "w"), indent=0)
for d, n, g in rows[:60]: print(f"{d:6.2f}  {n}  [{g}]")
