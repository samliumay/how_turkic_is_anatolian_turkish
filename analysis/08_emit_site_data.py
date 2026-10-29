import sys, json; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
D = sys.argv[1]
close = json.load(open(D + "/closeness.json")); pca = json.load(open(D + "/pca.json")); cl = json.load(open(D + "/clusters.json")); mo = json.load(open(D + "/models.json"))
wk = group(MOD, [r"^Kurdish_Kurmanji_Turkey_(Malatya|Kayseri|Corum|Kahramanmaras|Konya|Sivas|Eskisehir)"])[0]
az = group(MOD, [r"^Azeri_(Azerbaijan|Armenia|Georgia|Dagestan|Turkey)"])[0]
east = group(MOD, [r"^Turkish_(Erzurum|Erzincan|Kars|Ardahan|Igdir|Agri|Van|Malatya|Elazig|Bitlis|Tunceli|Mus)"])[0]
print("west Kurds -> Azeri", round(dist(wk, az), 2), "| west Kurds -> TR east", round(dist(wk, east), 2))
rng = np.random.default_rng(2)
for g in pca["groups"]:
    if len(g["pts"]) > 14: g["pts"] = [g["pts"][i] for i in sorted(rng.choice(len(g["pts"]), 14, replace=False))]
r = lambda v: [round(x, 4) for x in v]
ts = ["/**", " * Data for the \"How Turkic Is Anatolian Turkish?\" figures. Generated from the Hanami DNA G25",
      " * reference data (modern.csv, ancient.csv) by the analysis scripts kept in the project repo",
      " * (how_turkic_is_anatolian_turkish/analysis). Distances are Euclidean x 100; edit the scripts, not this file.", " */", "",
      "export type Kind = 'tr' | 'oghuz' | 'kipchak' | 'turkic' | 'wa' | 'cauc' | 'eu' | 'anc';", "",
      "/** Distance from the core-Anatolia Turkish average (778 people) to each group. */",
      "export const CLOSENESS: readonly { label: string; kind: Kind; d: number; n: number }[] = ["]
ts += [f"  {{ label: {json.dumps(x['label'], ensure_ascii=False)}, kind: '{x['kind']}', d: {x['d']}, n: {x['n']} }}," for x in close] + ["];", ""]
ts += ["/** Three-source fit per Turkish cluster (Byzantine Anatolia, medieval Turkic, Kartvelian). */",
       "export const CLUSTERS: readonly { cluster: string; core: boolean; n: number; byz: number; tur: number; kar: number; fit: number }[] = ["]
ts += [f"  {{ cluster: {json.dumps(x['cluster'], ensure_ascii=False)}, core: {str(x['core']).lower()}, n: {x['n']}, byz: {x['byz']}, tur: {x['tur']}, kar: {x['kar']}, fit: {x['fit']} }}," for x in cl] + ["];", ""]
ts += [f"/** PCA of {pca['rows']} modern reference rows (PC1 {pca['explained'][0]}%, PC2 {pca['explained'][1]}%); ancient groups and the author are projected. */",
       f"export const PCA_EXPLAINED = [{pca['explained'][0]}, {pca['explained'][1]}] as const;",
       f"export const PCA_YOU: readonly [number, number] = [{r(pca['you'])[0]}, {r(pca['you'])[1]}];",
       "export const PCA_GROUPS: readonly { label: string; kind: Kind; n: number; c: readonly [number, number]; pts: readonly (readonly [number, number])[] }[] = ["]
for g in pca["groups"]:
    pts = ", ".join(f"[{p[0]}, {p[1]}]" for p in g["pts"])
    ts.append(f"  {{ label: {json.dumps(g['label'], ensure_ascii=False)}, kind: '{g['kind']}', n: {g['n']}, c: [{g['c'][0]}, {g['c'][1]}], pts: [{pts}] }},")
ts += ["];", ""]
cap = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "capalibag.json")))
ts += ["/** Byzantine Anatolia + Çapalıbağ (1300–1650, early Anatolian Turkic) + Kartvelian, per region. */",
       "export const CAPALIBAG: readonly { cluster: string; byz: number; cap: number; kar: number; fit: number }[] = ["]
ts += [f"  {{ cluster: {json.dumps(x['cluster'], ensure_ascii=False)}, byz: {x['byz']}, cap: {x['cap']}, kar: {x['kar']}, fit: {x['fit']} }}," for x in cap] + ["];", ""]
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(ts))
print("core model", mo["core: original 3-way"], "| split", mo["core: pre-Turkic split"]["fit"])
