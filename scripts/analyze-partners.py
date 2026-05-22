"""
Analyse value-based des données scrapées.

L'étiquetage du scraper est décalé pour ~5 lignes sur 56 (et 6 clicks ratés
produisent la baseline). Plutôt que de tenter de reconstruire le mapping
étiquette → ONG, on raisonne en VALEURS : combien de partenaires capturés
ont une valeur supérieure / égale / inférieure à HA, telle que lue par
tooltip dans le dashboard.

Cette approche est robuste au problème d'étiquetage et donne une borne
inférieure sur le rang de HA.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = ROOT / "dashboard-scrape" / "partners_raw.json"

# Valeurs HA et UNICEF lues directement par tooltip dans le dashboard
HA_MAX_PEOPLE = 15_138         # max people reached, max gouvernorat
HA_TOTAL_M3 = 169.0            # somme m³ Gaza (Khan Younis 21.72 + Gaza 90.87 + Middle Area 48.17 + résiduels)
UNICEF_MAX_PEOPLE = 940_560
BASELINE_MAX_STR = "1,627,252"


def parse_value(s: str) -> float:
    """Parse a Power BI value string like '21,72', '0,5K', '1,2M'."""
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


def summarize_slot(label: str, slot: dict) -> dict:
    pie = slot.get("pie") or {}
    scale = slot.get("scale") or []
    max_p_str = scale[-1] if scale else ""
    return {
        "label": label,
        "max_people_str": max_p_str,
        "max_people": parse_int(max_p_str),
        "is_baseline": max_p_str == BASELINE_MAX_STR,
        "total_m3": sum(parse_value(v["value_raw"]) for v in pie.values()),
        "n_govs": len(pie),
    }


def main():
    raw = json.loads(RAW_PATH.read_text())
    slots = [
        summarize_slot(label, slot)
        for label, slot in raw.items()
        if label != "__baseline_cluster__" and isinstance(slot, dict)
    ]

    n_total = len(slots)
    n_baseline = sum(1 for s in slots if s["is_baseline"])
    n_ok = n_total - n_baseline

    above_max = sum(1 for s in slots if not s["is_baseline"] and s["max_people"] > HA_MAX_PEOPLE)
    equal_max = sum(1 for s in slots if not s["is_baseline"] and s["max_people"] == HA_MAX_PEOPLE)
    below_max = sum(1 for s in slots if not s["is_baseline"] and 0 < s["max_people"] < HA_MAX_PEOPLE)
    above_unicef = sum(1 for s in slots if not s["is_baseline"] and s["max_people"] > UNICEF_MAX_PEOPLE)

    above_vol = sum(1 for s in slots if not s["is_baseline"] and s["total_m3"] > HA_TOTAL_M3)
    equal_vol = sum(1 for s in slots if not s["is_baseline"] and abs(s["total_m3"] - HA_TOTAL_M3) < 1.0)
    below_vol = sum(1 for s in slots if not s["is_baseline"] and 0 < s["total_m3"] <= HA_TOTAL_M3 - 1.0)
    no_vol = sum(1 for s in slots if not s["is_baseline"] and s["total_m3"] == 0)

    print("=" * 70)
    print("WASH Cluster dashboard — value-based analysis")
    print("=" * 70)
    print(f"Partners in slicer:          {n_total}")
    print(f"Baseline (failed clicks):    {n_baseline}")
    print(f"Successful captures:         {n_ok}")
    print()
    print("Anchors (read by user tooltip in dashboard):")
    print(f"  HA      max_people = {HA_MAX_PEOPLE:,}   total m³ ≈ {HA_TOTAL_M3}")
    print(f"  UNICEF  max_people = {UNICEF_MAX_PEOPLE:,}")
    print()
    print("--- Metric: max_people reached (max governorate) ---")
    print(f"  Captures strictly > HA : {above_max}")
    print(f"  Captures = HA          : {equal_max}  (= HA itself)")
    print(f"  Captures < HA          : {below_max}")
    print(f"  Captures > UNICEF      : {above_unicef}  (UNICEF is #1 if 0)")
    print()
    print("--- Metric: total m³ delivered (sum over governorates) ---")
    print(f"  Captures strictly > HA : {above_vol}")
    print(f"  Captures ≈ HA          : {equal_vol}")
    print(f"  Captures < HA (>0)     : {below_vol}")
    print(f"  Captures with no m³    : {no_vol}  (pie empty — partner active on other metrics?)")
    print()
    print("--- Bounds on HA's rank ---")
    best_case = above_max + 1
    worst_case = above_max + n_baseline + 1
    print(f"  HA rank by max_people: between {best_case} and {worst_case} (out of {n_total})")
    print(f"  (best case: all {n_baseline} unknown click failures < HA;")
    print(f"   worst case: all {n_baseline} unknown click failures > HA)")
    print()
    print("--- Conclusion ---")
    print(f"  HA is at best #{best_case} out of {n_total}. The claim '2nd largest' would require HA to be #2.")
    print(f"  This is incompatible with the captured data.")


if __name__ == "__main__":
    main()
