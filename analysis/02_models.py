import sys, json; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
import os
core = np.load(sys.argv[1] + "/core.npy"); U = np.load(sys.argv[1] + "/owner.npy") if os.path.exists(sys.argv[1] + "/owner.npy") else None
def A(*inc, exc=()): return group(ANC, list(inc), list(exc))
def M(*inc, exc=()): return group(MOD, list(inc), list(exc))
SRC = {}
SRC["Byzantine Anatolia"], byz_sel = A(r"^Turkey_Anatolia_.*\(Byzantine\).*(East_Med-Anatolian|Anatolian_BA|Central_Anatolian_Greek)_Profile", r"^Turkey_Anatolia_Early-High_Medieval_Stratonikeia_\(East_Med-Anatolian")
SRC["Medieval Turkic (Kazakhstan, Kyrgyzstan)"], tur_sel = A(r"^Kazakhstan_Early_Medieval_Turk_\(", r"^Kyrgyzstan_Early_Medieval_Turk_\(", r"^Kazakhstan_Early-High_Medieval_Karakhanid", r"^Kazakhstan_High_Medieval_Kipchak")
SRC["Göktürk-era Mongolia"], _ = A(r"^Mongolia_Early_Medieval_Turkic_Period_\(n=")
SRC["Kartvelian (Georgian, Laz)"], _ = M(r"^(Georgian|Mingrelian|Svan|Laz)", exc=[r"Jew"])
SRC["Anatolia BA"], aba_sel = A(r"^Turkey_Anatolia_(EBA|MBA|MLBA)_")
SRC["Mycenaean Greek"], _ = A(r"^Greece_LBA_Mycenaean_")
SRC["Celtic (La Tène, Galatian proxy)"], _ = A(r"^Czechia_IA_La_Tene_\(Intermediate", r"^Austria_IA_La_Tene")
SRC["Caucasus LBA (Armenia)"], _ = A(r"^Armenia_LBA_Lchashen-Metsamor_")
SRC["Levant IA"], _ = A(r"^Israel_IA_|^Lebanon_IA_|^Israel_LBA_")
SRC["Iran IA"], _ = A(r"^Iran_IA_")
out = {}
def run(key, target, names):
    w, d = mix(target, [SRC[n] for n in names], names)
    out[key] = {"weights": [(n, round(x * 100, 1)) for n, x in w], "fit": round(d, 3)}
    print(f"\n{key}  fit {d:.3f}"); [print(f"   {x*100:5.1f}  {n}") for n, x in w]
for tname, t in [("core", core)] + ([("owner", U)] if U is not None else []):
    run(f"{tname}: original 3-way", t, ["Byzantine Anatolia", "Medieval Turkic (Kazakhstan, Kyrgyzstan)", "Kartvelian (Georgian, Laz)"])
    run(f"{tname}: 3-way, Mongolia Turkic", t, ["Byzantine Anatolia", "Göktürk-era Mongolia", "Kartvelian (Georgian, Laz)"])
    run(f"{tname}: 2-way", t, ["Byzantine Anatolia", "Medieval Turkic (Kazakhstan, Kyrgyzstan)"])
    run(f"{tname}: pre-Turkic split", t, ["Anatolia BA", "Mycenaean Greek", "Celtic (La Tène, Galatian proxy)", "Caucasus LBA (Armenia)", "Levant IA", "Iran IA", "Medieval Turkic (Kazakhstan, Kyrgyzstan)"])
# what Byzantine Anatolia itself is made of
run("Byzantine Anatolia: split", SRC["Byzantine Anatolia"], ["Anatolia BA", "Mycenaean Greek", "Celtic (La Tène, Galatian proxy)", "Caucasus LBA (Armenia)", "Levant IA", "Iran IA"])
print("\nsizes: byz", len(byz_sel), sum(n for *_, n in byz_sel), "| turkic", len(tur_sel), sum(n for *_, n in tur_sel), "| ABA", len(aba_sel))
for l, _, n in tur_sel: print("  T", l)
json.dump(out, open(sys.argv[1] + "/models.json", "w"), indent=1, ensure_ascii=False)
