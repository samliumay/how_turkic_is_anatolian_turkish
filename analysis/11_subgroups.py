"""Every Turkish subgroup row on three models: medieval Turkic, Çapalıbağ (1300–1650) and Ottoman-era
Kaman-Kalehöyük (Early Modern), each with Byzantine Anatolia and Kartvelian."""
import sys, json, os, re; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
def A(*inc): return group(ANC, list(inc))
byz = A(r"^Turkey_Anatolia_.*\(Byzantine\).*(East_Med-Anatolian|Anatolian_BA|Central_Anatolian_Greek)_Profile", r"^Turkey_Anatolia_Early-High_Medieval_Stratonikeia_\(East_Med-Anatolian")[0]
tur = A(r"^Kazakhstan_Early_Medieval_Turk_\(", r"^Kyrgyzstan_Early_Medieval_Turk_\(", r"^Kazakhstan_Early-High_Medieval_Karakhanid", r"^Kazakhstan_High_Medieval_Kipchak")[0]
cap = A(r"^Turkey_Anatolia_.*Capalibag")[0]
otm, otm_sel = A(r"^Turkey_Anatolia_Early_Modern_Kaman-Kalehoyuk_\((Turkish|Turkic)_Profile")
kar = group(MOD, [r"^(Georgian|Mingrelian|Svan|Laz)"], [r"Jew"])[0]
w, d = mix(otm, [byz, tur, kar], ["byz", "tur", "kar"]); print("Kaman-Kalehöyük (Ottoman) itself:", {k: round(v * 100, 1) for k, v in w}, "fit", round(d, 2), "n", sum(n for *_, n in otm_sel))
w, d = mix(cap, [byz, otm, kar], ["byz", "otm", "kar"]); print("Çapalıbağ on Ottoman source:", {k: round(v * 100, 1) for k, v in w}, "fit", round(d, 2))
rows = [(l, v, n) for l, v, n in MOD if clean(l) and re.match(r"^Turkish_", l) and n >= 3 and "Mixed" not in l and "Profile)" not in l or (clean(l) and re.match(r"^Turkish_(Istanbul_\(Anatolian|Balkans_\(Anatolian)", l))]
rows += [(l, v, n) for l, v, n in MOD if clean(l) and re.search(r"_(Yoruk|Cepni|Manav)_", l)]
seen, out = set(), []
for l, v, n in rows:
    if l in seen: continue
    seen.add(l)
    r = {"label": re.sub(r"_\(n=\d+\)$", "", l).replace("Turkish_", "").replace("_", " "), "n": n}
    for key, src in (("tur", tur), ("cap", cap), ("otm", otm)):
        w, d = mix(v, [byz, src, kar], ["byz", key, "kar"]); w = dict(w)
        r[key] = round(w[key] * 100, 1); r[key + "_fit"] = round(d, 2)
    out.append(r)
out.sort(key=lambda r: r["label"])
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "subgroups.json"), "w"), ensure_ascii=False, indent=0)
print(len(out), "rows")
for r in out: print(f'{r["label"][:40]:40s} n={r["n"]:<3} tur {r["tur"]:5.1f} ({r["tur_fit"]:.2f})  cap {r["cap"]:5.1f} ({r["cap_fit"]:.2f})  otm {r["otm"]:5.1f} ({r["otm_fit"]:.2f})')
