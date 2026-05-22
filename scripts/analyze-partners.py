"""
Analyse with shift correction.
The scraper's data labeled 'X' is actually for the partner BEFORE X
when click N was processed but read happened before update.
Strategy:
  - Read raw JSON
  - Compute total m3 per slot
  - Detect baseline slots (click failed)
  - Shift labels backward by 1 to align reading to actual selected partner
"""
import json
import re
from pathlib import Path

raw = json.loads(Path("/tmp/pbi-data/partners_raw.json").read_text())

PARTNERS_ORDER = [
    "AAH", "ACTED", "AFSC", "AH", "AIOCP", "ANERA", "BLDA", "CARE", "CCP-Japan", "CESVI",
    "CMWU", "CRS", "DCA/NCA", "DFD", "FAFD", "GDD", "GEM", "HA", "HF", "IDRF",
    "IHH", "IMC", "IRC", "IRW", "IWWAA", "MAAN", "MAP-UK", "MC", "MECA", "Mentor",
    "MSF-F", "MSF-OCB", "MSF-S", "NPA", "NRC", "OCK3", "Other", "Oxfam", "PAEEP", "PALSTD",
    "PARC", "PCRF", "PEF", "PFSA", "Project HOPE", "PSCF", "PUI", "PWJ", "QRCS", "RAHMA",
    "SCI", "SHAMS-OCD", "SI", "SIF", "SOS", "TDH", "UAWC", "UNDP", "UNICEF", "UNRWA",
    "WCK", "YDRO",
]

BASELINE_MAX = "1,627,252"

# Known truth values (from user tooltips)
KNOWN = {
    "HA": {"max_people": "15,138",
           "expected_pie": {"Khan Younis": 21.72, "Gaza": 90.87, "Middle Area": 48.17}},
    "UNICEF": {"max_people": "940,560",
               "expected_pie": {"Khan Younis": 4620, "Gaza": 10370, "Middle Area": 20470}},
}


def parse_value(s: str) -> float:
    if not s:
        return 0.0
    s = s.strip().replace("…", "").replace("...", "")
    mult = 1.0
    if s.endswith("K"):
        s = s[:-1].strip()
        mult = 1000.0
    elif s.endswith("M"):
        s = s[:-1].strip()
        mult = 1_000_000.0
    s = s.replace(",", ".").replace(" ", "")
    try:
        return float(s) * mult
    except ValueError:
        return 0.0


def slot_summary(slot):
    pie = slot.get("pie") or {}
    scale = slot.get("scale") or []
    max_p = scale[-1] if scale else ""
    is_baseline = max_p == BASELINE_MAX
    total = sum(parse_value(v["value_raw"]) for v in pie.values())
    return {
        "pie": pie,
        "max_people_str": max_p,
        "max_people": int(max_p.replace(",", "")) if max_p else 0,
        "is_baseline": is_baseline,
        "total_m3": total,
        "n_govs": len(pie),
    }


# Build slot data
slots = []
for p in PARTNERS_ORDER:
    if p in raw and isinstance(raw[p], dict):
        slots.append({"label": p, **slot_summary(raw[p])})
    else:
        slots.append({"label": p, "pie": {}, "max_people": 0, "is_baseline": True, "total_m3": 0, "n_govs": 0})

# Detect the shift pattern by looking at first baseline slot
# Slots 1-3 (AAH, ACTED, AFSC) are usually correct
# Then shift starts when first baseline appears
# Shift means: data labeled idx X is actually partner at idx X-1

# Match known values to find correct positions
print("=== Looking for HA's known max_people (15,138) ===")
for i, s in enumerate(slots):
    if s["max_people_str"] == "15,138":
        actual_partner = PARTNERS_ORDER[i - 1] if i > 0 else "?"
        print(f"  Found at slot {i} (label='{s['label']}') → actually partner at idx {i-1} = '{actual_partner}'")

print("\n=== Looking for UNICEF's known max_people (940,560) ===")
for i, s in enumerate(slots):
    if s["max_people_str"] == "940,560":
        actual_partner = PARTNERS_ORDER[i - 1] if i > 0 else "?"
        print(f"  Found at slot {i} (label='{s['label']}') → actually partner at idx {i-1} = '{actual_partner}'")

# Apply shift: slot[i] data → partner[i-1], except first 3 are correct
# Verify by HA: slot 19 (HF/labeled) has baseline; slot 20 (IDRF labeled) has 15,138 → HA's data is at slot 20
# So partner HA (index 17) ↔ slot 20 = shift of +3? Or shift of 2 (i-1 = 19, but label HA is at i=17)

# Looking at this: shift is irregular. Let me just identify all known matches:
# - HA expected max=15,138 found at slot 20 (label IDRF) → HA's data is at slot 20, BUT HA's label position is 17
# - The offset for HA = slot 20 - HA index 17 = +3
# - That's weird

# Let me look more carefully: maybe shift = +2 from the first baseline onwards
# Slot 4 = AH (baseline = click failed)
# Slot 5 = AIOCP, real data, but for whom?
# Looking at the sequence:
#   AAH(0)→OK_AAH, ACTED(1)→OK_ACTED, AFSC(2)→OK_AFSC
#   AH(3) clicked but read showed baseline (click failed or update delayed)
#   AIOCP(4) clicked, read showed... real data, but is it for AH or AIOCP?
#   ...

# Practical: I can't reliably attribute slots to partners. So instead, let me:
# - For each known partner (HA, UNICEF), find their data
# - For ALL partners, rank by total m3 and max_people of the data CAPTURED in their slot (acknowledging label uncertainty)

print("\n\n=== ALL SLOTS DATA (raw, label uncertain after first failed click) ===")
print(f"{'idx':>3} {'label':<15} {'baseline?':>10} {'#govs':>5} {'total_m3':>14} {'max_people':>12}")
print("-" * 70)
for i, s in enumerate(slots):
    bsmark = "BASE" if s["is_baseline"] else ""
    total_str = f"{s['total_m3']:,.1f}" if s["total_m3"] < 10000 else f"{s['total_m3']:,.0f}"
    print(f"{i:>3} {s['label']:<15} {bsmark:>10} {s['n_govs']:>5} {total_str:>14} {s['max_people']:>12,}")

# Rank non-baseline slots by total_m3
print("\n\n=== RANKING BY TOTAL m3 (non-baseline slots only) ===")
ranked = [s for s in slots if not s["is_baseline"] and s["total_m3"] > 0]
ranked.sort(key=lambda x: -x["total_m3"])
print(f"{'#':>4} {'slot_label':<15} {'total_m3':>14} {'max_people':>12}")
print("-" * 60)
for rk, s in enumerate(ranked, 1):
    total_str = f"{s['total_m3']:,.1f}" if s["total_m3"] < 10000 else f"{s['total_m3']:,.0f}"
    print(f"{rk:>4} {s['label']:<15} {total_str:>14} {s['max_people']:>12,}")

# Rank by max_people
print("\n\n=== RANKING BY MAX_PEOPLE (non-baseline slots only) ===")
ranked2 = [s for s in slots if not s["is_baseline"] and s["max_people"] > 0]
ranked2.sort(key=lambda x: -x["max_people"])
print(f"{'#':>4} {'slot_label':<15} {'max_people':>12} {'total_m3':>14}")
print("-" * 60)
for rk, s in enumerate(ranked2[:20], 1):
    total_str = f"{s['total_m3']:,.1f}" if s["total_m3"] < 10000 else f"{s['total_m3']:,.0f}"
    print(f"{rk:>4} {s['label']:<15} {s['max_people']:>12,} {total_str:>14}")

print("\nNB: 'slot_label' is just where the data was scraped — the real partner may be 1+ positions earlier in the partner list. Real rank by VALUE remains correct.")
