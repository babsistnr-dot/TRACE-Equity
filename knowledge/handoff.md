# TRACE-Equity — Handoff (Stand: 2026-04-22, nach Review Pass 1+2 §§ 1–4)

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
- **Forschungsbericht** (MD, ~6,5 S. Haupttext + Anhang, Dozentinnen-
  Gliederung 1–7), Abgabe **29.06.2026**. Der 150-W-Abstract ist
  integriert in § 1; `bericht/kurzzusammenfassung.md` ist damit obsolet
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
| 9 | Forschungsbericht | 🟡 **Remap C1–C8 + Review Pass 1+2 (§§ 1–4) fertig** (~3.000 W. Haupttext, ~6 S.), **Review §§ 5–7 + Rückfragen an Dozentin ausstehend** |
| 9.5 | Abstrakt (3 S., ohne Ergebnisse) | 🟡 Durchgang A + B + Relevanz-Satz ergänzt (~1.319 W.), **Durchgang C (Feinschliff + APA) ausstehend** |
| 9.6 | Kurzzusammenfassung | ✅ **Obsolet** (C8) — Abstract nun in § 1 des Berichts integriert, Datei entfernt |
| 10 | Poster | ⏳ |
| 11 | README/CLAUDE.md aktualisieren | ⏳ |

Letzter Commit: `09c90b0` (Review Pass 2 — § 4 Empirie: „elf"→„neun" Hochschulen, 3× satztrennender Doppelpunkt entfernt). Davor `445c510` (Review Pass 1 — §§ 1–3: Passiv-/Nominalstil, Doppelpunkte, Theorie-Gap-Fixes).

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

- Pfad: `bericht/forschungsbericht.md` (Markdown, kein PDF-Export gewünscht)
- **Neue Gliederung (Dozentinnen-Vorgabe, umgesetzt 2026-04-22):** 1 Abstract
  · 2 Einleitung · 3 Theorie · 4 Empirie · 5 Darstellung der Ergebnisse &
  Diskussion (integriert je Dimension) · 6 Handlungsempfehlungen &
  Limitationen · 7 Conclusio, Ausblick, Endzusammenfassung · Literatur ·
  Anhang A.1–A.4.
- Umfang pro Kapitel: Abstract 140 W · Einleitung 248 W · Theorie 454 W
  · Empirie 440 W · Erg.+Disk. 926 W · Handl.+Lim. 410 W · Conclusio 399 W
  · **Gesamt Haupttext: ~3.000 W (~6 S.)**.
- Kernvisualisierung: `bericht/abbildungen/levinson_heatmap.png`
  (Anhang A.4.1).
- **Stand:** Remap C1–C8 (Struktur + Obsoletierung Kurzzsfg.) fertig;
  Step-by-step-Review mit Babsi läuft (Pass 1: §§ 1–3, Pass 2: § 4).
  §§ 5–7 noch ungereviewt. Review-Kriterien: satztrennende Doppelpunkte
  (KI-Stil) entfernen, reifizierende Agens-Formulierungen („die Studie
  fragt…") in Passiv/Nominalstil umformulieren, Content-Gaps markieren.
- **Mapping alter → neuer Bericht:**
  - C1 Skelett mit Parking alter Inhalte (`85568bf`)
  - C2 § 5 Ergebnisse & Diskussion integriert je Dimension (`5a1c718`)
  - C3 § 4 Empirie auf 440 W gekürzt, ICR-Details in Anhang A.2 (`1d76ba2`)
  - C4 § 3 Theorie neu, 449 W (OECD, Stojanov, Gomolla, Levinson) (`5fc9070`)
  - C5 § 6.1 Handlungsempfehlungen E1/E2/E3 formuliert (`66ec336`)
  - C6 § 7 Conclusio, Ausblick, Endzsfg. neu (`9388202`)
  - C7 Abstract + Einleitung final, Kuckartz im Lit.verz., Redundanz-Pass
    (`c11b034`)
  - C8 Kurzzsfg. obsolet (`f3f09ba`)
- **Review-Passes (step-by-step mit Babsi):**
  - Pass 1 — §§ 1–3 (`445c510`): Abstract in Passiv-/Nominalstil
    umgeschrieben (kein „Wir"/„die Studie" als Agens); Einleitung + Theorie
    satztrennende Doppelpunkte entfernt; Theorie-Gaps (Stränge benannt,
    Frühpädagogik-Beleg, Schlusssatz) behoben; § 5.4 „interpretieren wir"
    passiviert (Stilkonsistenz).
  - Pass 2 — § 4 (`09c90b0`): Zahlen-Inkonsistenz „elf" → „neun" PHs
    (konsistent zu Tab. A.3.1) in § 4.1 + § 5.1; drei satztrennende
    Doppelpunkte entfernt (§ 4.2 *Single Source of Truth*, § 4.4 ICR-Satz,
    § 4.4 Schlussfragment umformuliert).
- **Offene Rückfragen an Dozentin (vor Abgabe):**
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

## Nächste Schritte (Reihenfolge)

1. **Dozentin-Rückfragen klären** (vor Team-Review, blockierend für
   Punkte 2–4): 150 Zeichen vs. Wörter · Seiten-Zählweise · integrierte
   vs. 5.1/5.2-Struktur · Adressatenkreis der Empfehlungen.
2. **Schritt 9 — Step-by-step-Review §§ 5–7** (mit Babsi fortsetzen):
   § 5 Darstellung der Ergebnisse & Diskussion (926 W., 4 Teilabschnitte),
   § 6 Handlungsempfehlungen + Limitationen (410 W.), § 7 Conclusio +
   Ausblick + Endzsfg. (399 W.). Kriterien identisch zu Pass 1+2.
   Danach Team-Schlussprüfung (Laura): autarke Lesbarkeit, Kreuzverweise
   (Tab./Abb./§-Nummern), Anhang-Vollständigkeit, Zitate-Balance
   (aktuell nur Cluster Mitte im Hauptteil).
3. **Schritt 9.5C Abstrakt — Feinschliff** — Wortzahl-Check (≤ 1.500 W.,
   aktuell 1.319 W.), APA-Konformität der 9 Einträge, Kreuzabgleich
   mit Bericht (κ-Werte, N, „in Anlehnung an"-Formulierung).
4. **Schritt 10 Poster** — Inhalt: HFF, Methode kompakt, Levinson-
   Heatmap, Kernbefunde, Fazit. Format mit Team klären.
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
- **Poster-Format ungeklärt**: vor Schritt 10 mit LV-Leitung klären.
- **Abstrakt vs. Kurzzusammenfassung konsistent halten**: Korpus-Zahlen,
  Methoden-Bezeichner und Literaturangaben müssen in beiden Dokumenten
  sowie im Bericht identisch sein (manueller Abgleich beim Feinschliff).

---

## Team & Rollen

- **Babsi** (Lead): finale inhaltliche Entscheidungen, Bericht-Review, Postersession
- **Laura**: CEiL-Validierung (FH Wien abgeschlossen), Bericht-Review, Postersession
- **Claude Code**: Analyse-Scripts, Textentwürfe, Doku-Pflege — Co-Researcher, nicht Autor

---

**Erstellt:** 2026-04-15 | **Aktualisiert:** 2026-04-22 | **Stand:** nach Review Pass 1+2 (§§ 1–4)
