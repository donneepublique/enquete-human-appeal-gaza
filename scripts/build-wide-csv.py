"""
Construit dashboard-scrape/partners_wide.csv :
un partenaire par ligne, valeurs numériques parsées, métriques agrégées + rangs.

Entrée : dashboard-scrape/partners_raw.json (sortie du scraper)
Sortie : dashboard-scrape/partners_wide.csv
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = ROOT / "dashboard-scrape" / "partners_raw.json"
OUT_PATH = ROOT / "dashboard-scrape" / "partners_wide.csv"

GOVS = ["Middle Area", "Khan Younis", "Gaza", "North Gaza", "Rafah"]


def parse_value(s: str) -> float:
    """Parse une valeur PowerBI : '2,92K' → 2920, '21,715000...' → 21.715, '' → 0."""
    if not s:
        return 0.0
    s = s.strip().replace("…", "").replace("...", "")
    mult = 1.0
    if s.endswith("K"):
        s = s[:-1].strip()
        mult = 1_000.0
    elif s.endswith("M"):
        s = s[:-1].strip()
        mult = 1_000_000.0
    s = s.replace(",", ".").replace(" ", "")
    try:
        return float(s) * mult
    except ValueError:
        return 0.0


def parse_int(s: str) -> int:
    if not s:
        return 0
    return int(s.replace(",", "").strip())


def main():
    raw = json.loads(RAW_PATH.read_text())

    # Baseline cluster séparée
    baseline = raw.get("__baseline_cluster__", {})
    baseline_pie = baseline.get("pie") or {}
    cluster_m3_total = sum(parse_value(v["value_raw"]) for v in baseline_pie.values())
    cluster_max = parse_int((baseline.get("scale") or [""])[-1])

    # Build partner rows
    rows = []
    for label, entry in raw.items():
        if label == "__baseline_cluster__":
            continue
        if not isinstance(entry, dict) or "error" in entry:
            # On note l'erreur quand même
            rows.append({
                "partner": label,
                "max_people": None,
                "total_m3": None,
                "error": entry.get("error", "") if isinstance(entry, dict) else "invalid",
                **{f"m3_{g.lower().replace(' ', '_')}": None for g in GOVS},
                **{f"pct_{g.lower().replace(' ', '_')}": None for g in GOVS},
            })
            continue

        pie = entry.get("pie") or {}
        scale = entry.get("scale") or []
        max_p = parse_int(scale[-1] if scale else "")

        row = {
            "partner": label,
            "max_people": max_p,
            "error": "",
        }
        total_m3 = 0.0
        for g in GOVS:
            v = pie.get(g)
            if v:
                m3 = parse_value(v["value_raw"])
                pct = float(v["pct"].replace(",", "."))
                total_m3 += m3
            else:
                m3 = None
                pct = None
            row[f"m3_{g.lower().replace(' ', '_')}"] = m3
            row[f"pct_{g.lower().replace(' ', '_')}"] = pct
        row["total_m3"] = total_m3
        rows.append(row)

    # Compute ranks (only over rows without error)
    valid = [r for r in rows if r["error"] == ""]
    by_max = sorted(valid, key=lambda r: r["max_people"], reverse=True)
    rank_max = {r["partner"]: i for i, r in enumerate(by_max, 1)}
    by_m3 = sorted(valid, key=lambda r: r["total_m3"], reverse=True)
    rank_m3 = {r["partner"]: i for i, r in enumerate(by_m3, 1)}

    for r in rows:
        if r["error"]:
            r["rank_max_people"] = None
            r["rank_m3"] = None
            r["pct_cluster_max_people"] = None
            r["pct_cluster_m3"] = None
            continue
        r["rank_max_people"] = rank_max[r["partner"]]
        r["rank_m3"] = rank_m3[r["partner"]]
        r["pct_cluster_max_people"] = (
            r["max_people"] / cluster_max * 100 if cluster_max else None
        )
        r["pct_cluster_m3"] = (
            r["total_m3"] / cluster_m3_total * 100 if cluster_m3_total else None
        )

    # Sort output alphabetically by partner
    rows.sort(key=lambda r: r["partner"])

    # Write
    fieldnames = [
        "partner",
        "max_people",
        "total_m3",
        "m3_middle_area",
        "m3_khan_younis",
        "m3_gaza",
        "m3_north_gaza",
        "m3_rafah",
        "pct_middle_area",
        "pct_khan_younis",
        "pct_gaza",
        "pct_north_gaza",
        "pct_rafah",
        "pct_cluster_max_people",
        "pct_cluster_m3",
        "rank_max_people",
        "rank_m3",
        "error",
    ]

    def fmt(v):
        if v is None or v == "":
            return ""
        if isinstance(v, float):
            # Évite les valeurs longues type "21.71500000003"
            return f"{v:.4f}".rstrip("0").rstrip(".")
        return v

    with OUT_PATH.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: fmt(r.get(k)) for k in fieldnames})

    # Header row pour la baseline en haut, en commentaire métadonnée
    print(f"[saved] {OUT_PATH}")
    print(f"  Cluster baseline:  max_people={cluster_max:,d}   total_m3={cluster_m3_total:,.0f}")
    print(f"  Partner rows:      {len(rows)} (valid: {len(valid)})")


if __name__ == "__main__":
    main()
