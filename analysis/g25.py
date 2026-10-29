"""G25 helpers mirroring hanami_dna_backend (Euclidean distance, n-weighted group averages, GLOBAL_EXCLUDE)."""
import csv, re, numpy as np
import os
R = os.environ.get("G25_DIR", "/home/umaysamli/Desktop/projects/hanami/platform/hanamidna/hanami_dna_backend/src/main/resources/reference/g25/")
EXCL = [re.compile(p) for p in (r"_o[0-9]*(_|$)", r"\(low_res\)", r"\(contaminated\)", r"_47Tolkien$")]
def load(name):
    rows = []
    with open(R + name + ".csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            m = re.search(r"\(n=(\d+)\)$", r["Name"])
            rows.append((r["Name"], np.array([float(r[f"c{i}"]) for i in range(1, 26)]), int(m.group(1)) if m else 1))
    return rows
MOD, ANC = load("modern"), load("ancient")
def clean(lbl): return not any(p.search(lbl) for p in EXCL)
def group(rows, inc, exc=()):
    sel = [(l, v, n) for l, v, n in rows if clean(l) and any(re.search(p, l) for p in inc) and not any(re.search(p, l) for p in exc)]
    if not sel: raise ValueError(f"empty group {inc}")
    w = np.array([n for _, _, n in sel], float)
    return (np.array([v for _, v, _ in sel]) * w[:, None]).sum(0) / w.sum(), sel
def dist(a, b): return float(np.linalg.norm(a - b)) * 100
def mix(target, sources, names):
    """non-negative weights summing to 1, minimising Euclidean distance (SLSQP)."""
    from scipy.optimize import minimize
    A = np.array(sources); k = len(A)
    f = lambda w: np.sum((w @ A - target) ** 2)
    res = minimize(f, np.ones(k) / k, bounds=[(0, 1)] * k, constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}], method="SLSQP", options={"ftol": 1e-14, "maxiter": 2000})
    return sorted(zip(names, res.x), key=lambda t: -t[1]), np.sqrt(res.fun) * 100
