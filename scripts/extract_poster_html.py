"""Extrahiert eine saubere, standalone poster.html aus dem von Claude
Design gespeicherten _bootstrap.html.

Claude Design speichert das Poster eingebettet in eine App-/Preview-
Hülle (omelette-/Babel-Injektion, designer-overlay, Auto-Scale-Skript).
Dieses Skript zieht nur das echte Poster heraus:

  - die echte Poster-CSS (erstes attributloses <style>)
  - das <article class="poster"> … </article>

und baut daraus ein minimales, druckfähiges HTML in Originalgröße
(A0 @ 96 dpi = 3179 × 4494 px), ohne Preview-Skalierung.

Die Heatmap wird auf die projektinterne 600-dpi-PNG umgebogen
(neben poster.html als levinson_heatmap.png kopiert).

Re-run, wenn Claude Design eine neue Version exportiert.

    python scripts/extract_poster_html.py
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BERICHT = ROOT / "bericht"
SRC = BERICHT / "Poster Trace Equity_files" / "_bootstrap.html"
OUT_HTML = BERICHT / "poster.html"
HEATMAP_SRC = ROOT / "ergebnisse" / "visualisierungen_vergleich" / "levinson_heatmap_poster.png"
HEATMAP_DST = BERICHT / "levinson_heatmap.png"
FONTS_CSS_REL = "./Poster Trace Equity_files/css2"

# A0 Hochformat in CSS-Pixeln @ 96 dpi
A0_W, A0_H = 3179, 4494


def main():
    html = SRC.read_text(encoding="utf-8")

    # Echte Poster-CSS: erstes attributloses <style> … </style>.
    # (Die Injektions-Styles haben Attribute: data-omelette-injected /
    #  data-designer-overlay — matchen das blanke <style> nicht.)
    css_m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not css_m:
        raise SystemExit("Poster-CSS (<style>) nicht gefunden.")
    css = css_m.group(1).strip()

    # Poster-Markup: <article class="poster"> … </article>
    art_m = re.search(r'<article class="poster".*?</article>', html, re.S)
    if not art_m:
        raise SystemExit('<article class="poster"> nicht gefunden.')
    article = art_m.group(0)

    out = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>TRACE-Equity – A0 Poster</title>
<link rel="preconnect" href="https://fonts.googleapis.com/">
<link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin>
<link href="{FONTS_CSS_REL}" rel="stylesheet">
<style>
{css}
</style>
</head>
<body style="margin:0;background:#ECEAF3;">
<div class="poster-shell" id="shell" style="width:{A0_W}px;height:{A0_H}px;position:relative;">
{article}
</div>
</body>
</html>
"""
    OUT_HTML.write_text(out, encoding="utf-8")

    if not HEATMAP_SRC.exists():
        raise SystemExit(f"Heatmap fehlt: {HEATMAP_SRC}")
    shutil.copyfile(HEATMAP_SRC, HEATMAP_DST)

    print(f"[OK] {OUT_HTML.relative_to(ROOT)}  ({len(out):,} Zeichen)")
    print(f"[OK] {HEATMAP_DST.relative_to(ROOT)}  "
          f"({HEATMAP_DST.stat().st_size:,} Bytes, 600 dpi)")
    print(f"     CSS {len(css):,} Z. · Article {len(article):,} Z.")


if __name__ == "__main__":
    main()
