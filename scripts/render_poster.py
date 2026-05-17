"""Rendert bericht/poster.html via Headless-Chrome in eine
hochauflösende A0-PNG (Druckqualität) und baut daraus ein
einseitiges A0-PPTX (Poster als vollflächiges Bild).

Hintergrund: HTML→editierbares PPTX ist nicht verlustfrei möglich.
Für eine Postersession ist das Poster eine fixe Leinwand — daher
PNG in Druckauflösung auf genau einer A0-Folie.

    python scripts/render_poster.py            # PNG + PPTX
    python scripts/render_poster.py --png-only # nur PNG

Voraussetzungen: Google Chrome installiert; python-pptx (wird bei
Bedarf gemeldet).
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTER_HTML = ROOT / "bericht" / "poster.html"
PNG_OUT = ROOT / "bericht" / "poster_render.png"
PPTX_OUT = ROOT / "bericht" / "Poster_TRACE-Equity.pptx"

# A0 Hochformat
A0_W_PX, A0_H_PX = 3179, 4494          # CSS-Pixel @ 96 dpi
A0_W_MM, A0_H_MM = 841, 1189
SCALE = 3                               # 3 → ~288 dpi @ A0 (druckfähig)

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_chrome():
    for c in CHROME_CANDIDATES:
        if Path(c).is_file():
            return c
    raise SystemExit("Chrome/Edge nicht gefunden.")


def render_png():
    if not POSTER_HTML.is_file():
        raise SystemExit(f"Fehlt: {POSTER_HTML} — erst extract_poster_html.py.")
    chrome = find_chrome()
    uri = POSTER_HTML.resolve().as_uri()
    args = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--no-sandbox",
        f"--force-device-scale-factor={SCALE}",
        f"--window-size={A0_W_PX},{A0_H_PX}",
        "--virtual-time-budget=15000",
        "--default-background-color=ECEAF3",
        f"--screenshot={PNG_OUT}",
        uri,
    ]
    subprocess.run(args, check=False, capture_output=True)
    if not PNG_OUT.is_file():
        raise SystemExit("Render fehlgeschlagen (keine PNG erzeugt).")
    try:
        from PIL import Image
        w, h = Image.open(PNG_OUT).size
        dpi = round(w / (A0_W_MM / 25.4))
        print(f"[OK] {PNG_OUT.relative_to(ROOT)}  {w}×{h}px  (~{dpi} dpi @ A0)")
        if dpi < 150:
            print("  [WARN] < 150 dpi — für Druck ggf. SCALE erhöhen.")
    except ModuleNotFoundError:
        print(f"[OK] {PNG_OUT.relative_to(ROOT)} erzeugt (PIL fehlt → keine Maßprüfung).")


def build_pptx():
    try:
        from pptx import Presentation
        from pptx.util import Mm
    except ModuleNotFoundError:
        raise SystemExit("python-pptx fehlt → 'pip install python-pptx', "
                          "dann erneut (oder --png-only).")
    prs = Presentation()
    prs.slide_width = Mm(A0_W_MM)
    prs.slide_height = Mm(A0_H_MM)
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # leeres Layout
    slide.shapes.add_picture(str(PNG_OUT), 0, 0,
                             width=Mm(A0_W_MM), height=Mm(A0_H_MM))
    prs.save(PPTX_OUT)
    print(f"[OK] {PPTX_OUT.relative_to(ROOT)}  (1 Folie, A0, Bild vollflächig)")


if __name__ == "__main__":
    render_png()
    if "--png-only" not in sys.argv:
        build_pptx()
