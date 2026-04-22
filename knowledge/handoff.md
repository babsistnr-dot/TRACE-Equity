# TRACE-Equity — Handoff (Stand: 2026-04-22)

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
- **Kurzzusammenfassung** (MD, max. 150 W., *mit* Ergebnissen) — als LV-
  Zusatzanforderung zum Abstrakt; „ganz am Schluss" zu verfassen.
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
| 9 | Forschungsbericht | 🟡 Durchgänge A+B+C fertig, Kapitel 3 auf ≤2 S. verdichtet (Tabellen/Heatmap in Anhang), **Schlussprüfung ausstehend** |
| 9.5 | Abstrakt (3 S., ohne Ergebnisse) | 🟡 Durchgang A + B + Relevanz-Satz ergänzt (~1.319 W.), **Durchgang C (Feinschliff + APA) ausstehend** |
| 9.6 | Kurzzusammenfassung (150 W., mit Ergebnissen) | 🟡 Rohtext fertig (146 W.), Feinschliff mit Bericht-Abgabe gemeinsam |
| 10 | Poster | ⏳ |
| 11 | README/CLAUDE.md aktualisieren | ⏳ |

Letzter Commit: `b0441e4` (Bericht Kap. 3 — Tabellen + Heatmap in Anhang verschoben), gepusht zu `origin/master`.

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
- Aktueller Umfang: 3.049 W. (Hauptteil ~6 S. + Anhang)
- Kernvisualisierung: `bericht/abbildungen/levinson_heatmap.png`
  (jetzt in Anhang A.4.1, nicht mehr im Hauptteil)
- **Stand:** Durchgänge A (Skelett) ✅, B (Rohtext) ✅, C (Feinschliff) ✅;
  Kapitel 3 auf ≤ 2 S. verdichtet (Commit `b0441e4`) — inhaltliche
  Schlussprüfung durch Team ausstehend
- Struktur: Einleitung (0,5) – Methodik (1,5) – Ergebnisse (2, reine
  Prosa, alle Tabellen/Heatmap im Anhang) – Diskussion (1,5) – Limitationen
  (0,5) + Literatur + Anhang A.1–A.4
- **9C-Arbeiten (Commits `d77e73a` → `c344eb8`):**
  - Zitat-Accuracy geprüft + korrigiert: Tai et al. (2024), OECD (2018),
    Gomolla & Radtke, Stojanov, Morgan (2022), Levinson et al. (2022)
  - Levinson-Dreistufen-Typologie als Adaption ausgewiesen
    (Methodik 2.2: „in Anlehnung an Levinson et al. (2022)")
  - Enumerations-Stil (Erstens/Zweitens) in 3.3, 4.1, 4.2, 5 in Fließprosa
- **Kapitel-3-Restructure (`b0441e4`):**
  - 4 Inline-Tabellen (§ 3.1–3.4) in Anhang A.3 verschoben (A.3.1–A.3.5)
  - Levinson-Heatmap aus § 3.3 in Anhang A.4.1 verschoben
  - Kreuzverweise „(Tab. A.3.x)" / „(Abb. A.4.1)" in den Fließtext
  - Prosa behält präzise Prozentwerte inline → lesbar ohne Tabellen-Lookup
  - Originalzitate Cluster Mitte (S. 10 + S. 106) bleiben als analytische
    Evidenz im Hauptteil
  - Kapitel-3-Umfang: 1.057 W → 721 W

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

## Kurzzusammenfassung (Schritt 9.6)

- Pfad: `bericht/kurzzusammenfassung.md` (eigenes Dokument, separat vom
  Abstrakt)
- Umfang: max. 150 W. (aktuell **146 W.**, 4 W. Buffer)
- LV-Anforderung (Zusatz zum Abstrakt): „Eine maximal 150 Worte
  umfassende Kurzzusammenfassung, die Sie ganz am Schluss verfassen. Sie
  fasst Thema, Frage, Methode und Ergebnisse prägnant zusammen."
- **Abgrenzung zum Abstrakt:** *enthält* Ergebnisse (Levinson-Verteilung
  49–72 % / 4–12 %, 0,8 % explizite Nennungen) und Levinson-Stufen-
  Definition; keine κ-Werte (zu detailliert für 150 W.).
- **Entstehung:** erst als Absatz im Abstrakt angelegt (`719af82`), dann
  in eigenes Dokument ausgelagert (`4a755fa`), Levinson-Stufen ergänzt +
  κ-Werte entfernt (`4bec68b`), Relevanz-Satz integriert + auf 146 W.
  gekürzt (`49c932e`).
- **Stand:** Rohtext finalisiert; Feinschliff gemeinsam mit Bericht-
  Schlussprüfung vor Abgabe.

---

## Nächste Schritte (Reihenfolge)

1. **Schritt 9 Schlussprüfung** — Team-Review des finalisierten Berichts
   inkl. Kapitel-3-Restructure (Prüfung: Prosa autark lesbar? Kreuz-
   verweise eindeutig? Anhang-Tabellen vollständig?). Wortzahl-Check,
   ggf. letzte Kürzungen. Restliche Zitate (Mayring, Hsieh & Shannon,
   Landis & Koch) bei Bedarf gegenprüfen. Bekannte Lücken: asymmetrische
   Zitate (nur Cluster Mitte im Hauptteil), Reflexivitäts-Abschnitt,
   Querschnittscodes 2.5 + 2.7 in Diskussion.
2. **Schritt 9.5C Abstrakt — Feinschliff** — Wortzahl-Check (≤ 1.500 W.,
   aktuell 1.319 W. → Puffer 181 W.), APA-Konformität der 9 Einträge
   (Spot-Check Bandzahlen / Verlage / Auflagen), Begriffsdichte in § 2
   prüfen, Kreuzabgleich mit Bericht (κ-Werte, N, „in Anlehnung an"-
   Formulierung).
3. **Schritt 9.6 Kurzzusammenfassung — Feinschliff** — Finale Abstimmung
   mit Bericht-Prozentwerten; sicherstellen, dass Zahlen exakt den
   finalen Tabellen im Anhang A.3 entsprechen.
4. **Schritt 10 Poster** — Inhalt: HFF, Methode kompakt, Levinson-Heatmap,
   Kernbefunde, Fazit. Format mit Team klären.
5. **Schritt 11 Doku** — `ergebnisse/README.md` und `CLAUDE.md` aktualisieren (alte Zahlen / Pfade).
6. **Abgabe 29.06.2026** — finale Konvertierung MD → Abgabeformat durch Team.

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

**Erstellt:** 2026-04-15 | **Aktualisiert:** 2026-04-22 | **Stand:** nach Commit `b0441e4`
