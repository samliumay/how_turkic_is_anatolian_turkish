import sys, json; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
def A(*inc): return group(ANC, list(inc))[0]
byz = A(r"^Turkey_Anatolia_.*\(Byzantine\).*(East_Med-Anatolian|Anatolian_BA|Central_Anatolian_Greek)_Profile", r"^Turkey_Anatolia_Early-High_Medieval_Stratonikeia_\(East_Med-Anatolian")
tur = A(r"^Kazakhstan_Early_Medieval_Turk_\(", r"^Kyrgyzstan_Early_Medieval_Turk_\(", r"^Kazakhstan_Early-High_Medieval_Karakhanid", r"^Kazakhstan_High_Medieval_Kipchak")
kar = group(MOD, [r"^(Georgian|Mingrelian|Svan|Laz)"], [r"Jew"])[0]
CL = [
 ("West Anatolia", True, [r"^Turkish_(Aydin|Izmir|Manisa|Balikesir|Canakkale|Denizli|Mugla|Usak|Kutahya|Afyonkarahisar|Bursa|Bilecik|Eskisehir|Sakarya|Yalova|Kocaeli)", r"^Turkish_Istanbul_\(Anatolian_Turk_Profile"]),
 ("Central Anatolia", True, [r"^Turkish_(Ankara|Konya|Kayseri|Aksaray|Kirsehir|Nevsehir|Nigde|Karaman|Kirikkale|Yozgat|Cankiri|Corum|Sivas|Isparta|Burdur|Antalya)"]),
 ("North Anatolia (western Black Sea)", True, [r"^Turkish_(Kastamonu|Sinop|Samsun|Amasya|Tokat|Ordu|Bartin|Karabuk|Zonguldak|Bolu|Duzce)"]),
 ("South (Adana, Mersin, Gaziantep)", False, [r"^Turkish_(Adana|Mersin|Hatay|Gaziantep|Kahramanmaras|Osmaniye)"]),
 ("Trabzon, Rize, Artvin", False, [r"^Turkish_(Trabzon|Rize|Artvin)"]),
 ("Erzurum and the east", False, [r"^Turkish_(Erzurum|Erzincan|Kars|Ardahan|Bayburt)"]),
 ("Balkan Turks", False, [r"^Turkish_Balkans_\(Anatolian", r"^Turkish_(East_Thrace|Western_Thrace|Central_Macedonia|Eastern_Macedonia|Northern_Bulgaria|North_Macedonia)"]),
 ("Azerbaijani", False, [r"^Azeri_(Azerbaijan|Armenia|Georgia|Dagestan|Turkey)"]),
]
out = []
for name, core, inc in CL:
    t, sel = group(MOD, inc)
    w, d = mix(t, [byz, tur, kar], ["byz", "tur", "kar"]); w = dict(w)
    out.append({"cluster": name, "core": core, "n": sum(n for *_, n in sel), "byz": round(w["byz"]*100, 1), "tur": round(w["tur"]*100, 1), "kar": round(w["kar"]*100, 1), "fit": round(d, 2)})
    print(f'{name:36s} core={core!s:5} n={out[-1]["n"]:<4} byz {out[-1]["byz"]:5.1f} tur {out[-1]["tur"]:5.1f} kar {out[-1]["kar"]:5.1f} fit {d:.2f}')
json.dump(out, open(sys.argv[1] + "/clusters.json", "w"), ensure_ascii=False, indent=1)
