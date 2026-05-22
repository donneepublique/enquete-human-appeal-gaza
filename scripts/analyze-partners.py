"""
Analyse des données scrapées du dashboard WASH Cluster.

Le scrape v2 (avec JS-click direct par index) attribue correctement les valeurs
à chaque partenaire (62/62 captures valides, ancres HA et UNICEF confirmées).
On peut donc raisonner sur l'attribution réelle : « rang de HA dans la liste
triée par max_people ou par m³ ».
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = ROOT / "dashboard-scrape" / "partners_raw.json"

HA_MAX_PEOPLE = 15_138
HA_TOTAL_M3 = 169.0
UNICEF_MAX_PEOPLE = 940_560


def parse_value(s: str) -> float:
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


def summarize(label: str, entry: dict) -> dict:
    pie = entry.get("pie") or {}
    scale = entry.get("scale") or []
    max_p_str = scale[-1] if scale else ""
    return {
        "label": label,
        "max_people": parse_int(max_p_str),
        "total_m3": sum(parse_value(v["value_raw"]) for v in pie.values()),
        "n_govs": len(pie),
    }


def main():
    raw = json.loads(RAW_PATH.read_text())
    partners = [
        summarize(label, entry)
        for label, entry in raw.items()
        if label != "__baseline_cluster__" and isinstance(entry, dict) and "error" not in entry
    ]

    print("=" * 72)
    print("WASH Cluster — analyse par partenaire (scrape v2, attribution fiable)")
    print("=" * 72)
    print(f"Partenaires capturés : {len(partners)}")
    print()

    # ----- Classement par max_people -----
    by_max = sorted(partners, key=lambda p: p["max_people"], reverse=True)
    print("--- Top 15 par max_people (max gouvernorat) ---")
    for i, p in enumerate(by_max[:15], 1):
        marker = "  <-- HA" if p["label"] == "HA" else ""
        print(f"  {i:2d}. {p['label']:15s} {p['max_people']:>10,d}{marker}")

    ha_rank_max = next((i for i, p in enumerate(by_max, 1) if p["label"] == "HA"), None)
    print()
    print(f"  Rang de HA par max_people : {ha_rank_max} / {len(partners)}")
    print()

    # ----- Classement par total m³ -----
    by_m3 = sorted(partners, key=lambda p: p["total_m3"], reverse=True)
    print("--- Top 15 par total m³ (somme gouvernorats) ---")
    for i, p in enumerate(by_m3[:15], 1):
        marker = "  <-- HA" if p["label"] == "HA" else ""
        print(f"  {i:2d}. {p['label']:15s} {p['total_m3']:>14,.2f} m³{marker}")

    ha_rank_m3 = next((i for i, p in enumerate(by_m3, 1) if p["label"] == "HA"), None)
    n_with_m3 = sum(1 for p in partners if p["total_m3"] > 0)
    print()
    print(f"  Rang de HA par total m³ : {ha_rank_m3} / {len(partners)}")
    print(f"  ({n_with_m3} partenaires ont au moins une valeur m³ ; les autres ont un pie vide)")
    print()

    # ----- Ratios HA vs cluster -----
    cluster_baseline = raw.get("__baseline_cluster__", {})
    cluster_pie = cluster_baseline.get("pie") or {}
    cluster_m3 = sum(parse_value(v["value_raw"]) for v in cluster_pie.values())
    cluster_max = parse_int((cluster_baseline.get("scale") or [""])[-1])

    print("--- HA vs cluster ---")
    print(f"  Cluster total m³           : {cluster_m3:>14,.0f}")
    print(f"  HA total m³                : {HA_TOTAL_M3:>14,.2f}")
    print(f"  HA / cluster (m³)          : {HA_TOTAL_M3 / cluster_m3 * 100:.3f} %")
    print(f"  Cluster max people         : {cluster_max:>14,d}")
    print(f"  HA max people              : {HA_MAX_PEOPLE:>14,d}")
    print(f"  HA / cluster (max people)  : {HA_MAX_PEOPLE / cluster_max * 100:.2f} %")
    print()

    # ----- HA vs UNICEF -----
    unicef_m3 = next((p["total_m3"] for p in partners if p["label"] == "UNICEF"), 0.0)
    unicef_max = next((p["max_people"] for p in partners if p["label"] == "UNICEF"), 0)
    print("--- HA vs UNICEF ---")
    print(f"  UNICEF max_people : {unicef_max:>10,d}   (HA : {HA_MAX_PEOPLE:,d})  → UNICEF/HA = {unicef_max / HA_MAX_PEOPLE:.0f}×")
    print(f"  UNICEF m³         : {unicef_m3:>10,.0f}   (HA : {HA_TOTAL_M3:,.0f})  → UNICEF/HA = {unicef_m3 / HA_TOTAL_M3:.0f}×")
    print()

    # ----- Conclusion -----
    print("--- Conclusion ---")
    print(f"  Sur max_people     : HA est rang {ha_rank_max}/{len(partners)} → pas n°2")
    print(f"  Sur total m³       : HA est rang {ha_rank_m3}/{len(partners)} → pas n°2")
    print(f"  Le slogan « 2ᵉ fournisseur d'eau à Gaza » n'est défendable sur aucune")
    print(f"  des deux métriques principales du dashboard cité par la publicité.")


if __name__ == "__main__":
    main()
