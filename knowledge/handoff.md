# TRACE-Equity — Handoff (Stand: 2026-04-23, Kurzversion Review Pass 1+2+3 fertig)

Kompakter Übergabestand für Team / nächste Session / neue Mitwirkende.
Quelle der Wahrheit für Details: jeweils verlinkte Dokumente.

---

## Projekt in 3 Sätzen

TRACE-Equity untersucht, wie Chancengerechtigkeit in den Curricula der
österreichischen Elementarpädagogik-Bachelorstudiengänge verankert ist
(N=4 Cluster, 1.626 Findings, 1.061 relevant, alle CEiL-validiert).
Methodik: QCA mit deduktivem Kategoriensystem, Keyword-basierter Web-App und Expert-in-the-Loop (CEiL);
Auswertung über 3 Dimensionen (Explizit/Implizit, Levinson-Tiefe, Cluster-Vergleich).

**Deliverables SS2026:**
- **Abstrakt** (MD, max. 3 S., Studiendesign-Dokument ohne Ergebnisse) —
  Methodenskizze + Theorierahmen + Auswertungs-Skizze. Abgabetermin vor
  29.06.2026 (TBD bei LV-Leitung).
- **Forschungsbericht** — zwei parallele Fassungen:
  - **Kurzversion** `bericht/Forschungsberichtkurz.md` (Abgabe-Kandidat,
    2.125 W. Haupttext, von Babsi aufgrund Seitenbudgets erstellt,
    dreimal gereviewt; Anhang-Transfer A.1–A.4 steht noch aus).
  - **Langversion** `bericht/forschungsbericht.md` (~3.000 W., vollständig
    inkl. Anhang; dient als Referenz und Quelle für Anhang-Übernahme).
  - Abgabe **29.06.2026**. Der 150-W-Abstract ist in beiden Fassungen
    in § 1 integriert; `bericht/kurzzusammenfassung.md` ist damit obsolet
    und wurde in Commit C8 entfernt.
- **Postersession** (**26.06.2026**).

---

## Aktueller Stand (Schritte 0–11)

| # | Schritt | Status |
|---|---|---|
| 0 | Scripts auf `confirmed_code` | ✅ |
| 1 | Daten bereinigen (NaN, unvalidiert) | ✅ |
| 2 | ICR-Dokumentation (κ=0,71 / 0,83) | ✅ |
| 3 | Shared Utilities (`scripts/utils.py`) | ✅ |
| 4 | FH Wien Validierung + Konvertierung | ✅ |
| 5 | Code 1.1 Deep Dive (D1) | ✅ |
| 6 | Levinson-Mapping (D2) | ✅ |
| 7 | Cross-Cluster-Vergleich (D3) | ✅ |
| 8 | Zitate-Sammlung pro Cluster | ✅ |
| 9 | Forschungsbericht | 🟡 **Kurzversion (Abgabe-Kandidat) dreimal gereviewt**, 2.125 W. Haupttext; **Anhang-Transfer A.1–A.4 + Rückfragen an Dozentin ausstehend**. Langversion als Referenz parallel. |
| 9.5 | Abstrakt (3 S., ohne Ergebnisse) | 🟡 Durchgang A + B + Relevanz-Satz ergänzt (~1.319 W.), **Durchgang C (Feinschliff + APA) ausstehend** |
| 9.6 | Kurzzusammenfassung | ✅ **Obsolet** (C8) — Abstract nun in § 1 des Berichts integriert, Datei entfernt |
| 10 | Poster | 🟡 **Konzept + Claude-Design-Briefing + druckfertige Heatmap fertig**; visuelle Umsetzung via claude.ai/design + Iteration offen |
| 11 | README/CLAUDE.md aktualisieren | ⏳ |

Letzter Commit: `d3f6bd8` (Poster — evidenzbasierte Richtlinien + Textstraffung). Poster-Kette: `e294fb6` (Konzept A0 + 600-dpi-Heatmap) → `e49db73` (Claude.ai-Prompt) → `b343ebe` (Briefing-Überarbeitung) → `d3f6bd8`. Bericht zuletzt: `c801a88` (Kurzversion Review Pass 3), davor `e591527` (Pass 1+2).

---

## Datenbasis (alle bereinigt, 100 % validiert)

| Cluster | Findings | Relevant | Rate | Code 1.1 |
|---|---:|---:|---:|---:|
| West | 468 | 347 | 74,1 % | 0 |
| Mitte | 516 | 259 | 50,2 % | 8 |
| SüdOst | 272 | 192 | 70,6 % | 0 |
| FH Wien | 370 | 263 | 71,1 % | 1 |
| **Summe** | **1.626** | **1.061** | **65,3 %** | **9** |

Pfad: `ergebnisse/cluster_*/export_clean.csv`

---

## Kernbefunde (für Bericht / Poster)

- **D1 Explizit vs. Implizit:** 9 / 1.061 explizite Code-1.1-Findings (0,8 %) → Verhältnis 117:1 implizit. West & SüdOst: 0 explizite Nennungen. Befund: Verankerung erschöpft sich nicht in Begriffsnennungen.
- **D2 Levinson:** Formale Gleichheit dominiert in allen Clustern (49–72 %), Transformative Gerechtigkeit durchgängig schwach (4–12 %). FH Wien deutlich kompensatorischer (40 %) als PHs (17–29 %).
- **D3 Cluster-Vergleich:** FH Wien weicht systematisch ab (Code 2.1 niedriger, 2.7 deutlich höher), konsistent mit Levinson-Profil. Relevanzraten 50–74 % als Sprachvarianz interpretiert.

**Hauptantwort HFF:** Curricula bleiben überwiegend auf formaler Gleichheit; Chancengerechtigkeit als Leitprinzip ist konzeptuell dünn verankert.

---

## Promptotyping-Dokumente

| Datei | Zweck |
|---|---|
| `knowledge/coding_manual.md` | **Single Source of Truth** — 233 Keywords, 8 Codes |
| `knowledge/expose.md` | Akademische Grundlage, Levinson-Mapping (Tabelle 2) |
| `knowledge/methodology.md` | QCA-Theorie |
| `knowledge/requirements.md` | App + Analyse-Anforderungen |
| `knowledge/design.md` | Visualisierungsentscheidungen (1 Kernviz: Levinson-Heatmap) |
| `knowledge/semester_plan_ss2026.md` | Roadmap, Schritte 0–11 |
| `knowledge/arbeitsaufteilung.md` | Teamaufteilung Babsi / Laura |
| `knowledge/journal.md` | Chronologisches Entwicklungsprotokoll |
| `ergebnisse/analyse_methodik.md` | Analyse-Walkthrough für Team |
| `ergebnisse/intercoder_reliability.md` | ICR-Detail (κ-Berechnung) |

---

## Code & Tests

```
scripts/
├── utils.py                          # Pfade, Farben, Levinson-Mapping
├── analyse_code_1_1_deep_dive.py     # D1
├── analyse_levinson_mapping.py       # D2 (Kernviz: levinson_heatmap.png)
├── analyse_vergleich_cluster.py      # D3
└── zitate_sammlung.py                # Zitate pro Code/Cluster

tests/test_scripts.py                 # 62 Tests, alle grün
```

Alle Scripts nutzen `confirmed_code` (Expert-validiert), nicht `code` (automatisch).
Ausführen:
```bash
cd scripts/ && python <script>.py [--alle | <cluster>]
python -m pytest tests/ -v   # aus Projekt-Root
```

---

## Bericht (Schritt 9)

**Zwei Fassungen parallel:**
- **Kurzversion** `bericht/Forschungsberichtkurz.md` — **Abgabe-Kandidat**,
  2.125 W. Haupttext (Fließtext §§ 1–7), von Babsi aufgrund Seitenbudget
  erstellt. Inkl. Uni-Graz-Titelseite + TOC, Anhang A.1–A.4 **noch nicht
  übernommen** (steht im TOC, wird aus Langversion transferiert).
- **Langversion** `bericht/forschungsbericht.md` — ~3.000 W. Haupttext,
  Referenz-Fassung mit vollständigem Anhang (Tab. A.3.1–A.3.5, Abb. A.4.1
  Levinson-Heatmap). Step-by-step-Review Pass 1+2 (§§ 1–4) dort fertig,
  §§ 5–7 ungereviewt — wird nicht weiter überarbeitet, da Kurzversion
  fortgeschrittener ist.

**Gliederung (Dozentinnen-Vorgabe, umgesetzt 2026-04-22):** 1 Abstract
· 2 Einleitung · 3 Theorie · 4 Empirie · 5 Darstellung der Ergebnisse &
Diskussion (integriert je Dimension) · 6 Handlungsempfehlungen &
Limitationen · 7 Conclusio, Ausblick, Endzusammenfassung · Literatur ·
Anhang A.1–A.4.

**Kernvisualisierung:** `bericht/abbildungen/levinson_heatmap.png` (Anhang A.4.1).

### Commits Langversion (C1–C8 Remap + Review Pass 1+2)
- C1–C7 Remap auf Dozentinnen-Gliederung (`85568bf` → `c11b034`)
- C8 Kurzzsfg. obsolet (`f3f09ba`)
- Review Pass 1 §§ 1–3 (`445c510`): Abstract Passiv-/Nominalstil;
  Einleitung + Theorie satztrennende Doppelpunkte; Theorie-Gaps behoben.
- Review Pass 2 § 4 (`09c90b0`): „elf" → „neun" PHs; 3 Doppelpunkte.

### Commits Kurzversion (3 Review-Passes auf Babsis eigene Kurzfassung)
- **Pass 1+2** (`e591527`): 14 sprachliche Fixes (11 satztrennende
  Doppelpunkte, 2× „elf"→„neun", 1× Reifizierung, LaTeX-Math→Klartext,
  „signifikant"→„deutlich") + 3 inhaltliche Ergänzungen
  (Bundesverfassungs-Zitat § 5.2 zurück; stärkeres Code-2.4-Zitat
  Cluster Mitte S. 81 statt S. 106 in § 5.3; OECD-Präventionsargument
  in § 3 ergänzt).
- **Pass 3** (`c801a88`): 11 inhaltliche/formtechnische Fixes
  — A2 § 4.4 „Minimale Abweichungen" → „52 nicht-übereinstimmende Fälle";
  A3 § 7.3 „vor allem bei den PHs" re-added (Mitte hat höchste
  Transformativ-Quote); B1 Abstract Findings-Zahl präzisiert;
  B2 § 5.2 FH Wien explizit; B3 § 4.2 Code 1.1 im Mapping geklärt;
  B4 § 5.1 Sprachdichte-Interpretation gehedgt; B5 § 7.3 „fehlend" →
  „unterrepräsentiert"; C1 § 5.4 Code-2.3-Zahlen; C2 § 5.3-Orphan
  entfernt + § 5.4-Öffnung neu; C3 § 7.2 LLM-Nuance; C4 Titelseite-Typo;
  C5 APA-Kursiv im Lit.verz.

**Review-Kriterien (alle Passes):** satztrennende Doppelpunkte (KI-Stil)
entfernen, reifizierende Agens-Formulierungen („die Studie fragt…")
in Passiv/Nominalstil umformulieren, Zahlen-Konsistenz gegen Tabellen
prüfen, Content-Gaps und logische Spannungen identifizieren.

**Offene Rückfragen an Dozentin (vor Abgabe):**
1. „Abstract — 150 Zeichen" = Tippfehler für 150 Wörter?
2. Seiten-Zählweise: zählen Literatur + Anhang zu ~6,5 S. Haupttext?
3. Ergebnisse & Diskussion je Dimension integriert OK, oder APA-strikt
   5.1/5.2 getrennt?
4. Adressatenkreis der Handlungsempfehlungen (curricular vs.
   bildungspolitisch)?

---

## Abstrakt (Schritt 9.5)

- Pfad: `bericht/abstrakt.md` (Markdown, 3 Abschnitte + Literaturverzeichnis)
- Umfang: 3 Seiten (Richtwert ≈ 1.500 Wörter, aktuell **~1.319 W.**)
- Struktur: § 1 Theoretische Perspektive · § 2 Methodenskizze ·
  § 3 Datenaufbereitung + Auswertung · Literaturverzeichnis (9 APA-Einträge)
- **Abgrenzung zum Bericht:** Keine Ergebnisse (keine Levinson-Verteilung,
  keine Code-1.1-Zähler, keine Cluster-Befunde). Erlaubt: Korpus-Kenndaten
  (N=4, 1.626 / 1.061 / 565 Findings) und ICR-Werte (κ=0,71 / 0,83).
- **Ergänzungen nach Durchgang B:**
  - Relevanz-Satz nach HFF in § 1 (Commit `7ceae68`): „Die Frage ist
    wichtig, weil Curricula mitbestimmen, wie angehende Elementar-
    pädagog:innen später mit Bildungsungleichheit umgehen — …"
- **Stand:** Durchgang A (`cd95ef2`) ✅, B (`a1983d2`) ✅, Relevanz-Satz
  ergänzt (`7ceae68`) ✅, Durchgang C (Feinschliff + Wortzahl + APA) ⏳
- **Methodik-Korrektur (`0b778f2`):** RTA-Claims aus allen Promptotyping-
  Docs entfernt — TRACE-Equity nutzt ausschließlich QCA mit deduktivem
  Kategoriensystem + CEiL, keine Reflexive Thematische Analyse.
- Offen: Abgabetermin bei LV-Leitung klären (TBD, vor 29.06.2026).

---

## Kurzzusammenfassung (Schritt 9.6) — OBSOLET

Im Zuge des Bericht-Remaps (Dozentinnen-Gliederung) wurde der 150-W-
Abstract direkt in § 1 des Berichts integriert (Umfang 133 W.,
Toleranz 128–172). `bericht/kurzzusammenfassung.md` wurde in C8
entfernt. Falls die Dozentin „150 Zeichen" doch wörtlich meint (statt
150 Wörter), ist das Dokument aus Git wiederherstellbar (letzter
Stand: Commit `49c932e`).

---

## Poster (Schritt 10)

- **Format (entschieden):** A0 Hochformat, klassisch-
  wissenschaftlich, 2-Spalten-Korpus mit Levinson-Heatmap als
  dominantem Element.
- **Werkzeug (entschieden):** claude.ai/design (Anthropic Labs,
  Opus 4.7) — eigenes Tool, nicht Artifact-Chat. Iteration über
  Inline-Edits, native PDF/PPTX/HTML-Exporte.
- **Dateien:**
  - `bericht/poster_konzept.md` — Layout-Raster, evidenzbasierte
    Designhinweise, Recherche-Synthese (Abschnitt 5) + Häufige-
    Fehler-Checkliste, abgabefertige Stichpunkt-Textbausteine.
  - `bericht/poster_prompt_claudeai.md` — Copy-Paste-Briefing für
    Claude Design (Design-Brief-Format, harte Constraints inkl.
    Schriftgrößen-Gate, Iterations-Befehle, Qualitäts-Gate).
  - `ergebnisse/visualisierungen_vergleich/levinson_heatmap_poster.png`
    — 600-dpi-Export (`analyse_levinson_mapping.py --poster`),
    druckfertig für A0.
- **Inhaltliche Basis:** geprüfte Kennzahlen aus Kurzversion des
  Berichts; Textbausteine in Stichpunktstil (Poster-Richtlinien:
  „weniger Text"). Take-home: *Curricula bleiben auf formaler
  Gleichheit; transformative Gerechtigkeit = Leerstelle.*
- **Stand:** In Claude Design gestaltet (Sektions-Karten, Take-home
  Variante B, D2/D3 inhaltlich gegengeprüft), nach lokal überführt
  und als **A0-PPTX exportiert**. Reproduzierbare Pipeline:
  - `scripts/extract_poster_html.py` — zieht saubere
    `bericht/poster.html` aus dem Claude-Design-Export
    (`bericht/Poster Trace Equity_files/_bootstrap.html`), biegt
    Heatmap auf `bericht/levinson_heatmap.png` (600 dpi).
  - `scripts/render_poster.py` — Headless-Chrome-Render
    `bericht/poster_render.png` (9537×13482 px, ~288 dpi @ A0) →
    `bericht/Poster_TRACE-Equity.pptx` (1 Folie, exakt 841×1189 mm,
    Poster vollflächig als Bild).
  - Re-run nach jeder neuen Claude-Design-Version:
    `python scripts/extract_poster_html.py && python scripts/render_poster.py`
- **Deliverables:** `bericht/Poster_TRACE-Equity.pptx`,
  `bericht/poster_render.png` (druckfertig), `bericht/poster.html`
  (editierbare Quelle). PPTX = Bild auf einer A0-Folie, **nicht
  text-editierbar** (HTML→editierbares PPTX technisch nicht möglich).
- **Offen:** Uni-Graz-Logo/Vorlage (Platzhalter), QR-Ziel;
  Graustufen-/Farbsehschwäche-Druckcheck; finale Sichtprüfung Team.
- **Kritisch:** Qualitäts-Gate Poster ↔ Bericht — Kennzahlen
  geprüft (Stand zuletzt korrekt); bei neuer Claude-Design-Version
  D2/D3 + Binnen-I erneut gegenprüfen.

---

## Nächste Schritte (Reihenfolge)

1. **Dozentin-Rückfragen klären** (vor Team-Review, blockierend für
   Punkte 2–4): 150 Zeichen vs. Wörter · Seiten-Zählweise · integrierte
   vs. 5.1/5.2-Struktur · Adressatenkreis der Empfehlungen.
2. **Schritt 9 — Anhang-Transfer Kurzversion** (durch Babsi):
   A.1 Kodiermanual-Auszug, A.2 ICR-Detailtabelle, A.3 Ergebnistabellen
   (A.3.1–A.3.5), A.4 Visualisierungen (Levinson-Heatmap). Quelle:
   `bericht/forschungsbericht.md` Z. 506–624. Alle Tab-/Abb-Querverweise
   in Kurzversion verweisen bereits darauf.
   Danach Team-Schlussprüfung (Laura): autarke Lesbarkeit, Kreuzverweise
   nach Transfer, Zitate-Balance (aktuell nur Cluster Mitte im Hauptteil).
3. **Schritt 9.5C Abstrakt — Feinschliff** — Wortzahl-Check (≤ 1.500 W.,
   aktuell 1.319 W.), APA-Konformität der 9 Einträge, Kreuzabgleich
   mit Bericht (κ-Werte, N, „in Anlehnung an"-Formulierung).
4. **Schritt 10 Poster** — Konzept + Briefing + druckfertige Heatmap
   stehen (s. Abschnitt „Poster"). Offen: visuelle Umsetzung via
   claude.ai/design (Briefing aus `bericht/poster_prompt_claudeai.md`),
   2–4 Iterationsrunden, Logo/Vorlage + QR-Ziel klären, A0-PDF
   exportieren → `bericht/poster_v1.pdf`.
5. **Schritt 11 Doku** — `ergebnisse/README.md` und `CLAUDE.md`
   aktualisieren (alte Zahlen / Pfade, neue Bericht-Gliederung).
6. **Abgabe 29.06.2026** — finale Konvertierung MD → Abgabeformat
   durch Team.

---

## Bekannte Risiken

- **Seitenbudget knapp** (8 S.): Kapitel 3 jetzt auf ≤ 2 S. verdichtet,
  Heatmap + Tabellen konsequent im Anhang. Weitere Kürzungspotenziale vor
  allem in Diskussion (aktuell 1,5 S.).
- **Relevanz-Ratio-Varianz** (50–74 %): in Limitationen reflektieren.
- **Latente Analyse interpretativ**: Methodik-Teil transparent halten.
- **⚠ Bericht-interne Inkonsistenz § 5.4 (Langversion):** Die Prosa
  sagt „West zeigt die stärkste Ausprägung bei **Diversität** und
  professioneller Haltung", aber Tab. A.3.4 weist SüdOst als höchsten
  Code-2.1-Wert (Diversität, 39,1 % vs. West 32,3 %) aus. Die
  **Kurzversion** (Abgabe-Kandidat) ist bereits korrekt („West
  fokussiert Haltung", konsistent zu Tab. A.3.4: West Code 2.7
  26,5 % = höchster PH-Wert). Poster wurde auf den Kurzversion-
  Wortlaut gezogen. **To-do:** Langversion § 5.4 an Kurzversion/
  Tabelle angleichen, bevor Langversion irgendwo verwendet oder der
  Anhang aus ihr übernommen wird (Angriffspunkt in der Verteidigung).
- **Poster:** Format auf A0 Hochformat / klassisch-wissenschaftlich
  festgelegt. Offen: Uni-Graz-Vorlage/Logo + QR-Ziel. Inhaltliche
  Treue Poster ↔ Bericht über Qualitäts-Gate sichern (Kennzahlen
  dürfen nicht „geglättet" werden).
- **Abstrakt vs. Kurzzusammenfassung konsistent halten**: Korpus-Zahlen,
  Methoden-Bezeichner und Literaturangaben müssen in beiden Dokumenten
  sowie im Bericht identisch sein (manueller Abgleich beim Feinschliff).

---

## Team & Rollen

- **Babsi** (Lead): finale inhaltliche Entscheidungen, Bericht-Review, Postersession
- **Laura**: CEiL-Validierung (FH Wien abgeschlossen), Bericht-Review, Postersession
- **Claude Code**: Analyse-Scripts, Textentwürfe, Doku-Pflege — Co-Researcher, nicht Autor

---

**Erstellt:** 2026-04-15 | **Aktualisiert:** 2026-05-16 | **Stand:** Bericht-Kurzversion Pass 1+2+3 + Poster-Konzept/Briefing/Heatmap fertig; Anhang-Transfer + Poster-Umsetzung ausstehend
