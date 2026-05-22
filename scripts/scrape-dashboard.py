"""
Robust scraper: click partner, verify the data changed (else retry),
only record verified results.
"""
import csv
import json
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d"

OUT = Path("/tmp/pbi-data")
OUT.mkdir(exist_ok=True)
CSV_PATH = OUT / "partners.csv"
JSON_PATH = OUT / "partners_raw.json"

PARTNERS = [
    "AAH", "ACTED", "AFSC", "AH", "AIOCP", "ANERA", "BLDA", "CARE", "CCP-Japan", "CESVI",
    "CMWU", "CRS", "DCA/NCA", "DFD", "FAFD", "GDD", "GEM", "HA", "HF", "IDRF",
    "IHH", "IMC", "IRC", "IRW", "IWWAA", "MAAN", "MAP-UK", "MC", "MECA", "Mentor",
    "MSF-F", "MSF-OCB", "MSF-S", "NPA", "NRC", "OCK3", "Other", "Oxfam", "PAEEP", "PALSTD",
    "PARC", "PCRF", "PEF", "PFSA", "Project HOPE", "PSCF", "PUI", "PWJ", "QRCS", "RAHMA",
    "SCI", "SHAMS-OCD", "SI", "SIF", "SOS", "TDH", "UAWC", "UNDP", "UNICEF", "UNRWA",
    "WCK", "YDRO",
]

GAZA_GOVS = {"Khan Younis", "Gaza", "Middle Area", "North Gaza", "Rafah"}
PIE_RE = re.compile(
    r"(Khan Younis|North Gaza|Middle Area|Gaza|Rafah)\s+([\d.,…\s]+?(?:K|M)?)\s*\((\d+[.,]\d+)%\)"
)
SCALE_RE = re.compile(r"^[\d,]+$")

BASELINE_MAX_PEOPLE = "1,627,252"  # cluster baseline value


def extract_pie(page) -> dict:
    texts = page.evaluate("""() => {
        const out = [];
        document.querySelectorAll('text').forEach(t => {
            const txt = (t.textContent || '').trim();
            if (txt) out.push(txt);
        });
        return out;
    }""")
    pie = {}
    for t in texts:
        for m in PIE_RE.finditer(t):
            gov, val, pct = m.group(1), m.group(2).strip(), m.group(3)
            if gov in GAZA_GOVS:
                pie[gov] = {"value_raw": val, "pct": pct}
    return pie


def extract_people_scale(page) -> list:
    for f in page.frames:
        try:
            body = f.locator("body").inner_text(timeout=1000)
            if "CapPeopleReached" in body:
                lines = [l.strip() for l in body.split("\n") if SCALE_RE.match(l.strip())]
                return lines
        except Exception:
            pass
    return []


def is_baseline(pie: dict, scale: list) -> bool:
    """Return True if the data looks like the unfiltered cluster baseline."""
    if scale and scale[-1] == BASELINE_MAX_PEOPLE:
        return True
    # Baseline pie sums to ~97.2% with these specific values
    if pie.get("North Gaza", {}).get("pct") == "8,24" and pie.get("Middle Area", {}).get("pct") == "31,28":
        return True
    return False


def js_click(slicer_frame, partner_name) -> bool:
    """Use Playwright real click after JS scroll-into-view."""
    found = slicer_frame.evaluate("""(p) => {
        const els = Array.from(document.querySelectorAll('span, div, [role="option"], [role="listitem"]'));
        for (const el of els) {
            if ((el.textContent || '').trim() === p) {
                el.scrollIntoView({block: 'center', inline: 'center'});
                return true;
            }
        }
        return false;
    }""", partner_name)
    if not found:
        return False
    try:
        btn = slicer_frame.get_by_text(partner_name, exact=True).first
        btn.click(timeout=4000, force=True)
        return True
    except Exception:
        return False


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel="chrome")
    ctx = browser.new_context(viewport={"width": 1920, "height": 1400})
    page = ctx.new_page()
    print(f"[load]")
    page.goto(URL, wait_until="domcontentloaded", timeout=90000)
    print("[wait] 35s")
    page.wait_for_timeout(35000)

    baseline_pie = extract_pie(page)
    baseline_scale = extract_people_scale(page)
    print(f"[baseline] pie={baseline_pie}, max={baseline_scale[-1] if baseline_scale else '?'}")

    # Find slicer
    slicer_frame = None
    for f in page.frames:
        try:
            body = f.locator("body").inner_text(timeout=1000)
            if "HA" in body.split("\n") and "OCK3" in body.split("\n"):
                slicer_frame = f
                break
        except Exception:
            pass
    if not slicer_frame:
        print("ERROR: slicer not found")
        raise SystemExit(1)

    results = {"__baseline_cluster__": {"pie": baseline_pie, "scale": baseline_scale}}

    last_max = baseline_scale[-1] if baseline_scale else ""

    for idx, partner in enumerate(PARTNERS, 1):
        print(f"\n[{idx:02d}/{len(PARTNERS)}] {partner!r}", end=" ", flush=True)
        retries_left = 3
        success = False
        while retries_left > 0:
            if not js_click(slicer_frame, partner):
                print("NOT_IN_DOM", end=" ")
                break
            page.wait_for_timeout(3500)
            pie = extract_pie(page)
            scale = extract_people_scale(page)
            cur_max = scale[-1] if scale else ""
            # Test 1: max changed from previous read
            # Test 2: not equal to baseline
            if cur_max != last_max or not is_baseline(pie, scale):
                results[partner] = {"pie": pie, "scale": scale}
                total_pct = sum(float(v["pct"].replace(",", ".")) for v in pie.values()) if pie else 0
                print(f"OK pie={len(pie)} sum={total_pct:.1f}% max={cur_max}")
                last_max = cur_max
                success = True
                # Toggle off
                js_click(slicer_frame, partner)
                page.wait_for_timeout(1000)
                break
            else:
                retries_left -= 1
                print(f"[unchanged retry {3-retries_left}]", end=" ")
                # Try clicking the partner again
                page.wait_for_timeout(500)
        if not success:
            results[partner] = {"error": "data did not change", "pie": pie, "scale": scale}
            print("FAIL")

    JSON_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    with open(CSV_PATH, "w", newline="") as fcsv:
        w = csv.writer(fcsv)
        w.writerow(["partner", "governorate", "value_raw", "pct", "max_people_scale", "status"])
        for partner, data in results.items():
            if not isinstance(data, dict):
                continue
            scale = data.get("scale") or []
            max_p = scale[-1] if scale else ""
            pie = data.get("pie", {})
            status = "ok" if "error" not in data else data["error"]
            if not pie:
                w.writerow([partner, "(no data)", "", "", max_p, status])
            else:
                for gov, vals in pie.items():
                    w.writerow([partner, gov, vals["value_raw"], vals["pct"], max_p, status])

    print(f"\n[saved] {JSON_PATH} and {CSV_PATH}")
    browser.close()
