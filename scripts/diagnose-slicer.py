"""
Diagnostic v2 : on enumère tous les .slicerItemContainer, on identifie celui
dont textContent === 'HA', puis on tente plusieurs stratégies de click et on
observe quel item se retrouve en état sélectionné après chaque tentative.

But : trouver une stratégie de click qui sélectionne RÉELLEMENT le partenaire
visé.
"""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://app.powerbi.com/view?r=eyJrIjoiNDBjNmQwOTktNzFmOS00YWFkLThlYTItN2ExNWZmNzJhNTUyIiwidCI6Ijc3NDEwMTk1LTE0ZTEtNGZiOC05MDRiLWFiMTg5MjAyMzY2NyIsImMiOjh9&pageName=109fa3d4608ac422357d"

OUT = Path("/tmp/diag")
OUT.mkdir(exist_ok=True)


def list_slicer_items(slicer_frame):
    return slicer_frame.evaluate("""() => {
        const items = Array.from(document.querySelectorAll('.slicerItemContainer'));
        return items.map((el, i) => ({
            index: i,
            text: (el.textContent || '').trim(),
            bg: getComputedStyle(el).backgroundColor,
            rect: el.getBoundingClientRect().toJSON(),
        }));
    }""")


def find_selected(items):
    return [it for it in items if it["bg"] != "rgb(255, 255, 255)" and it["bg"] != "rgba(0, 0, 0, 0)"]


def reset_all_selections(slicer_frame, page):
    """Désélectionne tout en cliquant deux fois sur AAH puis lit l'état."""
    # Stratégie simple : clic sur le premier item sélectionné, jusqu'à 0 sélection
    for _ in range(5):
        items = list_slicer_items(slicer_frame)
        selected = find_selected(items)
        if not selected:
            return True
        target = selected[0]
        slicer_frame.evaluate("""(idx) => {
            const items = document.querySelectorAll('.slicerItemContainer');
            items[idx].click();
        }""", target["index"])
        page.wait_for_timeout(1500)
    return False


def try_click_strategy(slicer_frame, page, partner, strategy):
    """Tente une stratégie de click. Retourne (items_selected_after, label_we_wanted_was_selected)."""
    # Trouver l'index du partenaire
    items = list_slicer_items(slicer_frame)
    target_idx = next((it["index"] for it in items if it["text"] == partner), None)
    if target_idx is None:
        return None, False

    if strategy == "js_click_by_index":
        slicer_frame.evaluate("""(idx) => {
            const items = document.querySelectorAll('.slicerItemContainer');
            items[idx].scrollIntoView({block: 'center'});
            items[idx].click();
        }""", target_idx)
    elif strategy == "playwright_get_by_text":
        btn = slicer_frame.get_by_text(partner, exact=True).first
        btn.click(timeout=4000, force=True)
    elif strategy == "playwright_coordinate":
        # Récupérer le rect après scroll et cliquer aux coordonnées exactes
        rect = slicer_frame.evaluate("""(idx) => {
            const items = document.querySelectorAll('.slicerItemContainer');
            items[idx].scrollIntoView({block: 'center'});
            return items[idx].getBoundingClientRect().toJSON();
        }""", target_idx)
        # Le frame est dans la page principale → calculer coords absolues
        cx = rect["x"] + rect["width"] / 2
        cy = rect["y"] + rect["height"] / 2
        page.mouse.click(cx, cy)
    elif strategy == "playwright_locator_by_index":
        loc = slicer_frame.locator(".slicerItemContainer").nth(target_idx)
        loc.scroll_into_view_if_needed()
        loc.click(force=True)

    page.wait_for_timeout(3000)
    items_after = list_slicer_items(slicer_frame)
    selected = find_selected(items_after)
    matched = any(s["text"] == partner for s in selected)
    return selected, matched


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_context(viewport={"width": 1920, "height": 1400}).new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=90000)
        page.wait_for_timeout(35000)

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
            return

        # Liste initiale
        items = list_slicer_items(slicer_frame)
        print(f"Total slicerItemContainer items: {len(items)}")
        print("First 5:", [it["text"] for it in items[:5]])
        ha_idx = next((it["index"] for it in items if it["text"] == "HA"), None)
        print(f"HA index in slicerItemContainer list: {ha_idx}")
        print()

        # Test chaque stratégie
        for strat in ["js_click_by_index", "playwright_get_by_text", "playwright_coordinate", "playwright_locator_by_index"]:
            print(f"=== Strategy: {strat} ===")
            # Reset
            reset_all_selections(slicer_frame, page)
            page.wait_for_timeout(2000)
            selected_before = find_selected(list_slicer_items(slicer_frame))
            print(f"  Before click: {len(selected_before)} selected ({[s['text'] for s in selected_before]})")
            selected_after, matched = try_click_strategy(slicer_frame, page, "HA", strat)
            if selected_after is None:
                print("  -> Target not found")
                continue
            labels = [s["text"] for s in selected_after]
            mark = "✓" if matched else "✗"
            print(f"  {mark} After click 'HA': selected = {labels}")
            print()

        browser.close()


if __name__ == "__main__":
    main()
