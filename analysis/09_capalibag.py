"""Çapalıbağ (1300–1650) as an early Anatolian Turkic source, fitted for every Turkish region."""
import sys, json, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
def A(*inc): return group(ANC, list(inc))[0]
byz = A(r"^Turkey_Anatolia_.*\(Byzantine\).*(East_Med-Anatolian|Anatolian_BA|Central_Anatolian_Greek)_Profile", r"^Turkey_Anatolia_Early-High_Medieval_Stratonikeia_\(East_Med-Anatolian")
cap = A(r"^Turkey_Anatolia_.*Capalibag")
otm = A(r"^Turkey_Anatolia_Early_Modern_Kaman-Kalehoyuk_\((Turkish|Turkic)_Profile")
tur = A(r"^Kazakhstan_Early_Medieval_Turk_\(", r"^Kyrgyzstan_Early_Medieval_Turk_\(", r"^Kazakhstan_Early-High_Medieval_Karakhanid", r"^Kazakhstan_High_Medieval_Kipchak")
kar = group(MOD, [r"^(Georgian|Mingrelian|Svan|Laz)"], [r"Jew"])[0]
# what Çapalıbağ itself is, on the medieval sources
w, d = mix(cap, [byz, tur, kar], ["byz", "tur", "kar"]); print("Çapalıbağ itself:", {k: round(v * 100, 1) for k, v in w}, "fit", round(d, 2))
CL = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "clusters.json")))
REG = {
 "West Anatolia": [r"^Turkish_(Aydin|Izmir|Manisa|Balikesir|Canakkale|Denizli|Mugla|Usak|Kutahya|Afyonkarahisar|Bursa|Bilecik|Eskisehir|Sakarya|Yalova|Kocaeli)", r"^Turkish_Istanbul_\(Anatolian_Turk_Profile"],
 "Central Anatolia": [r"^Turkish_(Ankara|Konya|Kayseri|Aksaray|Kirsehir|Nevsehir|Nigde|Karaman|Kirikkale|Yozgat|Cankiri|Corum|Sivas|Isparta|Burdur|Antalya)"],
 "North Anatolia (western Black Sea)": [r"^Turkish_(Kastamonu|Sinop|Samsun|Amasya|Tokat|Ordu|Bartin|Karabuk|Zonguldak|Bolu|Duzce)"],
 "South (Adana, Mersin, Gaziantep)": [r"^Turkish_(Adana|Mersin|Hatay|Gaziantep|Kahramanmaras|Osmaniye)"],
 "Trabzon, Rize, Artvin": [r"^Turkish_(Trabzon|Rize|Artvin)"],
 "Erzurum and the east": [r"^Turkish_(Erzurum|Erzincan|Kars|Ardahan|Bayburt)"],
 "Balkan Turks": [r"^Turkish_Balkans_\(Anatolian", r"^Turkish_(East_Thrace|Western_Thrace|Central_Macedonia|Eastern_Macedonia|Northern_Bulgaria|North_Macedonia)"],
 "Azerbaijani": [r"^Azeri_(Azerbaijan|Armenia|Georgia|Dagestan|Turkey)"],
}
core = group(MOD, REG["West Anatolia"] + REG["Central Anatolia"] + REG["North Anatolia (western Black Sea)"])[0]
out = []
for name, inc in [("Core Anatolia", None)] + list(REG.items()):
    t = core if inc is None else group(MOD, inc)[0]
    w, d = mix(t, [byz, cap, kar], ["byz", "cap", "kar"]); w = dict(w)
    w2, d2 = mix(t, [byz, otm, kar], ["byz", "otm", "kar"]); w2 = dict(w2)
    out.append({"cluster": name, "byz": round(w["byz"] * 100, 1), "cap": round(w["cap"] * 100, 1), "kar": round(w["kar"] * 100, 1), "fit": round(d, 2),
                "otm_byz": round(w2["byz"] * 100, 1), "otm": round(w2["otm"] * 100, 1), "otm_kar": round(w2["kar"] * 100, 1), "otm_fit": round(d2, 2)})
    print(f'{name:36s} byz {out[-1]["byz"]:5.1f}  Çapalıbağ {out[-1]["cap"]:5.1f}  kar {out[-1]["kar"]:5.1f}  fit {d:.2f} | Ottoman {out[-1]["otm"]:5.1f} (byz {out[-1]["otm_byz"]}, kar {out[-1]["otm_kar"]}) fit {d2:.2f}')
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "capalibag.json"), "w"), ensure_ascii=False, indent=1)
