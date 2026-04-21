# TRACE-Equity — Handoff (Stand: 2026-04-21)

Kompakter Übergabestand für Team / nächste Session / neue Mitwirkende.
Quelle der Wahrheit für Details: jeweils verlinkte Dokumente.

---

## Projekt in 3 Sätzen

TRACE-Equity untersucht, wie Chancengerechtigkeit in den Curricula der
österreichischen Elementarpädagogik-Bachelorstudiengänge verankert ist
(N=4 Cluster, 1.626 Findings, 1.061 relevant, alle CEiL-validiert).
Methodik: QCA + RTA mit Keyword-basierter Web-App und Expert-in-the-Loop;
Auswertung über 3 Dimensionen (Explizit/Implizit, Levinson-Tiefe, Cluster-Vergleich).

**Deliverables SS2026:**
- **Abstrakt** (MD, max. 3 S.) — Methodenskizze + Theorierahmen + Auswertungs-Skizze. Abgabetermin vor 29.06.2026 (TBD bei LV-Leitung).
- **Forschungsbericht** (PDF/MD, max. 8 S. + Anhang), Abgabe **29.06.2026**.
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
| 9 | Forschungsbericht | 🟡 Durchgang A + B + C-Feinschliff fertig, **Schlussprüfung ausstehend** |
| 9.5 | Abstrakt (3 S., separate LV-Abgabe) | ⏳ |
| 10 | Poster | ⏳ |
| 11 | README/CLAUDE.md aktualisieren | ⏳ |

Letzter Commit: `c344eb8` (Step 9C Levinson-Mapping als Adaption), gepusht zu `origin/master`.

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
| `knowledge/methodology.md` | QCA + RTA Theorie |
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
- Kernvisualisierung: `bericht/abbildungen/levinson_heatmap.png`
- **Stand:** Durchgang A (Skelett) ✅, Durchgang B (Rohtext) ✅,
  Durchgang C (Feinschliff) ✅ — inhaltliche Schlussprüfung durch Team ausstehend
- Struktur: Einleitung (0,5) – Methodik (1,5) – Ergebnisse 4× (4) – Diskussion (1,5) – Limitationen (0,5) + Literatur + Anhang A.1–A.4
- **9C-Arbeiten (Commits `d77e73a` → `c344eb8`):**
  - Zitat-Accuracy geprüft + korrigiert: Tai et al. (2024), OECD (2018),
    Gomolla & Radtke, Stojanov, Morgan (2022), Levinson et al. (2022)
  - Levinson-Dreistufen-Typologie als Adaption ausgewiesen
    (Methodik 2.2: „in Anlehnung an Levinson et al. (2022)")
  - Enumerations-Stil (Erstens/Zweitens) in 3.3, 4.1, 4.2, 5 in Fließprosa

---

## Nächste Schritte (Reihenfolge)

1. **Schritt 9 Schlussprüfung** — Team-Review des finalisierten Berichts,
   Wortzahl-Check, ggf. letzte Kürzungen. Restliche Zitate (Mayring,
   Hsieh & Shannon, Landis & Koch) bei Bedarf gegenprüfen.
2. **Schritt 10 Poster** — Inhalt: HFF, Methode kompakt, Levinson-Heatmap, Kernbefunde, Fazit. Format mit Team klären.
3. **Schritt 11 Doku** — `ergebnisse/README.md` und `CLAUDE.md` aktualisieren (alte Zahlen / Pfade).
4. **Abgabe 29.06.2026** — finale Konvertierung MD → Abgabeformat durch Team.

---

## Bekannte Risiken

- **Seitenbudget knapp** (8 S.): Anhang aktiv nutzen, nur Levinson-Heatmap im Hauptteil.
- **Relevanz-Ratio-Varianz** (50–74 %): in Limitationen reflektieren.
- **Latente Analyse interpretativ**: Methodik-Teil transparent halten.
- **Poster-Format ungeklärt**: vor Schritt 10 mit LV-Leitung klären.

---

## Team & Rollen

- **Babsi** (Lead): finale inhaltliche Entscheidungen, Bericht-Review, Postersession
- **Laura**: CEiL-Validierung (FH Wien abgeschlossen), Bericht-Review, Postersession
- **Claude Code**: Analyse-Scripts, Textentwürfe, Doku-Pflege — Co-Researcher, nicht Autor

---

**Erstellt:** 2026-04-15 | **Aktualisiert:** 2026-04-21 | **Stand:** nach Commit `c344eb8`
