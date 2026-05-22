"""
Scraper strict du dashboard WASH Cluster (Power BI).

Différence vs version précédente : on ne se contente plus de « la valeur a
changé ». Pour CHAQUE partenaire on exige :

  1. État de départ = baseline cluster (réinitialisation explicite si besoin).
  2. Click sur le partenaire.
  3. Attente active jusqu'à ce que la lecture diffère de la baseline ET reste
     stable sur 2 lectures consécutives (= le filtre PowerBI est appliqué).
  4. Toggle off du partenaire.
  5. Confirmation du retour à la baseline (sinon on tente un reset plus
     agressif via la slicer).

Si l'une de ces étapes échoue → on enregistre `{"error": "verification_failed"}`
SANS jamais écrire de valeurs douteuses sous l'étiquette du partenaire.

Sortie : dashboard-scrape/partners.csv + partners_raw.json
"""
import csv
import json
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d"

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "dashboard-scrape"
OUT_DIR.mkdir(exist_ok=True)
CSV_PATH = OUT_DIR / "partners.csv"
JSON_PATH = OUT_DIR / "partners_raw.json"

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

BASELINE_MAX_PEOPLE = "1,627,252"

# Ancres connues (lues directement par tooltip dans le dashboard)
# Sert à vérifier la fiabilité du scrape à la fin
EXPECTED_ANCHORS = {
    "HA": {"max_people": "15,138"},
    "UNICEF": {"max_people": "940,560"},
}

# Timing
SETTLE_MS = 1500           # entre deux lectures de stabilité
POLL_INTERVAL_MS = 800     # entre deux polls
MAX_WAIT_FILTER_MS = 20000 # temps max pour qu'un click prenne effet
MAX_WAIT_RESET_MS = 15000  # temps max pour revenir baseline
RESET_ATTEMPTS = 3


# ---------- Extraction ----------

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


def extract_scale(page) -> list:
    for f in page.frames:
        try:
            body = f.locator("body").inner_text(timeout=1000)
            if "CapPeopleReached" in body:
                lines = [l.strip() for l in body.split("\n") if SCALE_RE.match(l.strip())]
                return lines
        except Exception:
            pass
    return []


def read_state(page) -> dict:
    """Lecture complète de l'état du dashboard. Retourne dict avec pie/scale/max/sig."""
    pie = extract_pie(page)
    scale = extract_scale(page)
    max_p = scale[-1] if scale else ""
    # Signature : permet de comparer deux états entre eux (stabilité, égalité, ...)
    sig = (
        max_p,
        tuple(sorted((g, v["value_raw"], v["pct"]) for g, v in pie.items())),
    )
    return {"pie": pie, "scale": scale, "max": max_p, "sig": sig}


def is_baseline(state: dict) -> bool:
    return state["max"] == BASELINE_MAX_PEOPLE


def is_empty(state: dict) -> bool:
    return not state["max"]


# ---------- Slicer interaction ----------

def click_partner(slicer_frame, partner: str) -> bool:
    """Click direct via JS sur le .slicerItemContainer dont le textContent matche.

    Diagnostiqué : les click Playwright (.get_by_text().click(), .locator().nth().click(),
    page.mouse.click(x,y)) ratent d'une ligne et sélectionnent l'item juste au-dessus
    (probablement à cause d'un transform interne du slicer Power BI virtualisé). Seul
    le `element.click()` direct via JS sur le bon container fonctionne de manière fiable.
    """
    return slicer_frame.evaluate("""(p) => {
        const items = document.querySelectorAll('.slicerItemContainer');
        for (const el of items) {
            if ((el.textContent || '').trim() === p) {
                el.scrollIntoView({block: 'center', inline: 'center'});
                el.click();
                return true;
            }
        }
        return false;
    }""", partner)


# ---------- Waits ----------

def wait_for(page, predicate, timeout_ms: int, label: str = "") -> dict | None:
    """Poll read_state until predicate(state) is True. Returns final state, or None on timeout."""
    elapsed = 0
    state = None
    while elapsed < timeout_ms:
        page.wait_for_timeout(POLL_INTERVAL_MS)
        elapsed += POLL_INTERVAL_MS
        state = read_state(page)
        if predicate(state):
            return state
    return None


def wait_for_filtered(page, baseline_sig) -> dict | None:
    """Attend que le dashboard sorte de la baseline ET se stabilise sur 2 lectures."""
    # Étape 1 : attendre divergence de la baseline
    diverged = wait_for(
        page,
        lambda s: not is_baseline(s) and not is_empty(s) and s["sig"] != baseline_sig,
        MAX_WAIT_FILTER_MS,
    )
    if not diverged:
        return None
    # Étape 2 : stabilité — la prochaine lecture doit être identique
    page.wait_for_timeout(SETTLE_MS)
    second = read_state(page)
    if second["sig"] != diverged["sig"]:
        # Pas encore stable, on attend un peu plus
        third = wait_for(
            page,
            lambda s: s["sig"] == second["sig"] and not is_baseline(s),
            6000,
        )
        return third if third else None
    return second


def wait_for_baseline(page) -> dict | None:
    return wait_for(page, is_baseline, MAX_WAIT_RESET_MS)


def reset_to_baseline(page, slicer_frame, currently_selected: str | None) -> bool:
    """Force le retour à la baseline. Toggle off le partenaire courant, puis vérifie."""
    for attempt in range(RESET_ATTEMPTS):
        state = read_state(page)
        if is_baseline(state):
            return True
        if currently_selected and attempt == 0:
            click_partner(slicer_frame, currently_selected)
            page.wait_for_timeout(1500)
        else:
            # Ré-click sur le partenaire pour toggle off
            if currently_selected:
                click_partner(slicer_frame, currently_selected)
                page.wait_for_timeout(1500)
        final = wait_for_baseline(page)
        if final:
            return True
    return False


# ---------- Main loop ----------

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        ctx = browser.new_context(viewport={"width": 1920, "height": 1400})
        page = ctx.new_page()
        print("[load]")
        page.goto(URL, wait_until="domcontentloaded", timeout=90000)
        print("[wait] 35s")
        page.wait_for_timeout(35000)

        baseline_state = read_state(page)
        if not is_baseline(baseline_state):
            print(f"WARN: initial state is not baseline (max={baseline_state['max']!r})")
        print(f"[baseline] max={baseline_state['max']} pie={len(baseline_state['pie'])}")

        # Localiser la slicer
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

        results = {
            "__baseline_cluster__": {
                "pie": baseline_state["pie"],
                "scale": baseline_state["scale"],
            }
        }

        for idx, partner in enumerate(PARTNERS, 1):
            print(f"\n[{idx:02d}/{len(PARTNERS)}] {partner!r}", end=" ", flush=True)

            # 1. Garantir le départ à la baseline
            cur = read_state(page)
            if not is_baseline(cur):
                print("[reset]", end=" ", flush=True)
                if not reset_to_baseline(page, slicer_frame, None):
                    results[partner] = {"error": "could_not_reset_before_click"}
                    print("RESET_FAIL")
                    continue

            # 2. Click partenaire
            if not click_partner(slicer_frame, partner):
                results[partner] = {"error": "not_in_slicer_dom"}
                print("NOT_IN_DOM")
                continue

            # 3. Attendre filtre appliqué + stable
            filtered = wait_for_filtered(page, baseline_state["sig"])
            if not filtered:
                results[partner] = {"error": "filter_did_not_apply"}
                print("NO_FILTER")
                # Tenter un reset pour le suivant
                reset_to_baseline(page, slicer_frame, partner)
                continue

            # 4. Sauvegarde
            total_pct = sum(float(v["pct"].replace(",", ".")) for v in filtered["pie"].values()) if filtered["pie"] else 0
            results[partner] = {
                "pie": filtered["pie"],
                "scale": filtered["scale"],
            }
            print(f"OK max={filtered['max']} pie={len(filtered['pie'])} sum={total_pct:.1f}%")

            # 5. Toggle off + confirmer baseline
            click_partner(slicer_frame, partner)
            back = wait_for_baseline(page)
            if not back:
                # Reset agressif
                if not reset_to_baseline(page, slicer_frame, partner):
                    print("  [WARN] could not return to baseline cleanly")

        # ----- Sauvegarde -----
        JSON_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False))

        with open(CSV_PATH, "w", newline="") as fcsv:
            w = csv.writer(fcsv)
            w.writerow(["partner", "governorate", "value_raw", "pct", "max_people_scale", "status"])
            for partner, data in results.items():
                if not isinstance(data, dict):
                    continue
                if "error" in data:
                    w.writerow([partner, "(error)", "", "", "", data["error"]])
                    continue
                scale = data.get("scale") or []
                max_p = scale[-1] if scale else ""
                pie = data.get("pie", {})
                if not pie:
                    w.writerow([partner, "(no data)", "", "", max_p, "ok"])
                else:
                    for gov, vals in pie.items():
                        w.writerow([partner, gov, vals["value_raw"], vals["pct"], max_p, "ok"])

        # ----- Vérification des ancres -----
        print("\n" + "=" * 70)
        print("ANCRES DE VÉRIFICATION")
        print("=" * 70)
        for anchor, expected in EXPECTED_ANCHORS.items():
            entry = results.get(anchor, {})
            scale = entry.get("scale") or []
            got_max = scale[-1] if scale else "(absent)"
            want_max = expected["max_people"]
            status = "✓" if got_max == want_max else "✗"
            print(f"  {status} {anchor}: expected max={want_max}, got max={got_max}")

        # ----- Statistiques globales -----
        n_ok = sum(1 for k, v in results.items() if k != "__baseline_cluster__" and isinstance(v, dict) and "error" not in v)
        n_err = sum(1 for k, v in results.items() if k != "__baseline_cluster__" and isinstance(v, dict) and "error" in v)
        print()
        print(f"Captures valides : {n_ok} / {len(PARTNERS)}")
        print(f"Échecs           : {n_err} / {len(PARTNERS)}")
        print(f"\n[saved] {JSON_PATH}")
        print(f"[saved] {CSV_PATH}")
        browser.close()


if __name__ == "__main__":
    main()
