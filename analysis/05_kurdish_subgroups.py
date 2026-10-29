import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from g25 import *
core = np.load(sys.argv[1] + "/core.npy")
az = group(MOD, [r"^Azeri_(Azerbaijan|Armenia|Georgia|Dagestan|Turkey)"])[0]
east = group(MOD, [r"^Turkish_(Erzurum|Erzincan|Kars|Ardahan|Igdir|Agri|Van|Malatya|Elazig|Bitlis|Tunceli|Mus)"])[0]
rows = [(l, v, n) for l, v, n in MOD if clean(l) and l.startswith("Kurd") and "Jew" not in l]
print(f"{'label':62s} {'n':>3}  core   azeri  TR-east")
for l, v, n in sorted(rows, key=lambda r: dist(core, r[1])):
    print(f"{l[:62]:62s} {n:>3}  {dist(core, v):5.2f}  {dist(az, v):5.2f}  {dist(east, v):5.2f}")
print("azeri->core", round(dist(az, core), 2), " TR-east->core", round(dist(east, core), 2), " TR-east->azeri", round(dist(east, az), 2))
