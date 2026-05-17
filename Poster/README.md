# Poster — TRACE-Equity (A0, Postersession 26.06.2026)

Alles zum Poster an einem Ort. Einstieg je nach Rolle:

## Du willst das Poster nur ansehen / als Vorlage nutzen
- **`poster_render.pdf`** — so sieht das Poster aus (A0, vektoriell,
  scharf). Das ist die **Design-Vorlage** und das **primäre
  Druck-Artefakt** für die Druckerei.
- `Poster_TRACE-Equity.pptx` — dasselbe als 1 A0-Folie (Poster als
  Bild, **nicht** text-editierbar).

## Du willst Texte herauskopieren (Laura)
- **`poster_texte.md`** — nur die fertigen Poster-Texte, blockweise
  zum Direkt-Kopieren. Wortlaut + Zahlen gegen die Kurzversion des
  Berichts geprüft — beim Umgestalten **nicht verändern**.

## Du willst das Poster weiter gestalten
- `poster.html` — editierbare HTML/CSS-Quelle (in jedem Editor /
  Browser / Designtool nutzbar; **kein Claude Design nötig**).
- `levinson_heatmap.png` — die Heatmap (600 dpi), von `poster.html`
  referenziert. Unverändert einbetten.
- `poster_konzept.md` — Layout-Raster, evidenzbasierte Designregeln
  (Schriftgrößen @ A0, 3-Farben-Regel, Farbsehschwäche-Check),
  bewusste Auslassungen.

## Hintergrund / Reproduktion
- `poster_prompt_claudeai.md` — das Briefing, mit dem das Poster in
  Claude Design entstand (Doku/Reproduktion).
- `Poster Trace Equity.html` + `Poster Trace Equity_files/` —
  roher Claude-Design-Export (`_bootstrap.html` ist Input der
  Pipeline; Vendor-Dateien via `.gitignore` ausgeschlossen).

## Neu erzeugen (nach Änderung an poster.html oder neuem Export)
```
python scripts/extract_poster_html.py   # nur bei neuem Claude-Design-Export
python scripts/render_poster.py          # → poster_render.pdf + .png + .pptx
```
(aus dem Projekt-Root ausführen)

## Noch offen vor finalem Druck
- Echtes Uni-Graz-Logo statt Platzhalter (oben rechts).
- QR-Code-Ziel festlegen + generieren.
- Graustufen-/Farbsehschwäche-Druckcheck der Heatmap.
