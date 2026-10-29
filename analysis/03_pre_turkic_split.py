import sys, json, itertools; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
core = np.load(sys.argv[1] + "/core.npy")
def A(*inc): return group(ANC, list(inc))[0]
S = {
 "Anatolia BA": A(r"^Turkey_Anatolia_(EBA|MBA|MLBA)_"),
 "Mycenaean Greek": A(r"^Greece_LBA_Mycenaean_"),
 "Celtic (La Tène)": A(r"^Czechia_IA_La_Tene_\(Intermediate", r"^Austria_IA_La_Tene"),
 "Caucasus (Armenia LBA)": A(r"^Armenia_LBA_Lchashen-Metsamor_"),
 "Levant IA": A(r"^Israel_IA_|^Lebanon_IA_|^Israel_LBA_"),
 "Iran IA": A(r"^Iran_IA_"),
 "Medieval Turkic": A(r"^Kazakhstan_Early_Medieval_Turk_\(", r"^Kyrgyzstan_Early_Medieval_Turk_\(", r"^Kazakhstan_Early-High_Medieval_Karakhanid", r"^Kazakhstan_High_Medieval_Kipchak"),
}
base = ["Anatolia BA", "Mycenaean Greek", "Celtic (La Tène)", "Medieval Turkic"]
res = []
for extra in [(), ("Caucasus (Armenia LBA)",), ("Levant IA",), ("Iran IA",), ("Caucasus (Armenia LBA)", "Levant IA"), ("Caucasus (Armenia LBA)", "Iran IA")]:
    names = base + list(extra); w, d = mix(core, [S[n] for n in names], names)
    res.append((d, names, w)); print(f"fit {d:.3f}: " + ", ".join(f"{n} {x*100:.1f}" for n, x in w))
