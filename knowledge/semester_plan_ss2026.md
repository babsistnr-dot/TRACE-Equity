# TRACE-Equity: Semester-Plan SS2026

## Context

TRACE-Equity analysiert Chancengerechtigkeit in österreichischen Elementarpädagogik-Curricula (N=4). Alle 4 Cluster sind analysiert und validiert (N=1.626 Findings, davon 1.061 relevant). Dieses Semester: alle Forschungsfragen beantworten.

**Deliverables:**
- Forschungsbericht (max. 8 Seiten + Anhang), PDF, Abgabe **29.06.2026**
- Postersession (10 Min), Termin **26.06.2026**

**Team:** Babsi + Laura, beide aktiv. Claude Code: Analyse + Textentwurf iterativ.

---

## Schritt-für-Schritt-Plan

### ✅ Schritt 0: Scripts auf confirmed_code umstellen — ERLEDIGT
Alle Scripts auf `confirmed_code` (Expert-validiert) umgestellt. 31 manuell
umkodierte Findings werden jetzt korrekt berücksichtigt.
*Commit: `0c46edc`*

### ✅ Schritt 1: Daten bereinigen — ERLEDIGT
SüdOst: 4 NaN-Werte entfernt (276 → 272). FH Wien: 42 unvalidierte + 6 NaN
entfernt (418 → 370). Alle CSVs sauber, Tests bestätigen Datenqualität.
*Commits: `c5cd1f2`, `edcc85f`*

### ✅ Schritt 2: ICR-Dokumentation — ERLEDIGT
Intercoder-Reliabilität dokumentiert: κ=0,71 (Relevanz), κ=0,83 (Code).
*Commit: `cb393f9`* | *Output: `ergebnisse/intercoder_reliability.md`*

### ✅ Schritt 3: Shared Utilities — ERLEDIGT
`scripts/utils.py` erstellt: Pfade, Farben, Levinson-Mapping, Ladefunktionen.
Alle Scripts refactored. Testsuite mit 53 Tests.
*Commits: `cc4e727`, `0b84bb1`*

### ✅ Schritt 4: FH Campus Wien — ERLEDIGT
Laura hat CEiL-Validierung abgeschlossen. Export konvertiert (.numbers → CSV),
bereinigt. 370 Findings, 263 relevant (71,1%), 1 Code-1.1-Finding.
*Commit: `edcc85f`*

### ✅ Schritt 5: Code 1.1 Deep Dive — alle Cluster (→ Dimension 1) — ERLEDIGT
**Script:** `scripts/analyse_code_1_1_deep_dive.py --alle`
**Ergebnis:** 9/1.061 relevante Findings (0,8%) explizit, Verhältnis 117:1.
West und SüdOst: 0 explizite Nennungen. Mitte: 8, FH Wien: 1.
**Befund D1:** Verankerung erschöpft sich nicht in Begriffsnennungen.
*Commit: `106eead`* | *Output: `ergebnisse/analyse_code_1_1_vergleich.md` + 4 Cluster-Reports*

### ✅ Schritt 6: Levinson-Mapping (→ Dimension 2) — ERLEDIGT
**Script:** `scripts/analyse_levinson_mapping.py --alle`
**Ergebnis:** Formale Gleichheit dominiert überall (49–72%), Transformative
Gerechtigkeit durchgängig schwach (4–12%). FH Wien deutlich kompensatorischer
(40%) als PH-Cluster (17–29%). Abdeckung der 3 Stufen: 51–70% der relevanten Findings.
**Befund D2:** Curricula bleiben überwiegend auf formaler Gleichheit; transformative
Gerechtigkeit ist systematisch unterrepräsentiert.
*Output:* `ergebnisse/analyse_levinson_vergleich.md` + 4 Cluster-Reports + Heatmap

**Mapping (Expose Tabelle 2):**

| Levinson-Stufe | Codes | Handlungslogik |
|---|---|---|
| Formale Gleichheit | 2.1, 2.2 | Zugang + Anerkennung |
| Kompensatorische Gerechtigkeit | 2.3, 2.6 | Gezielte Förderung |
| Transformative Gerechtigkeit | 2.4 | Machtkritik + Empowerment |
| Querschnitt | 2.5, 2.7 | Separat ausweisen |
| Explizit | 1.1 | Direkte Nennung |

**Achtung:** Expose nennt "Code 1.0", CSVs verwenden "Code 1.1" → Script matcht auf CSV-Namen
**Nur relevante Findings** (`relevant == "ja"`)
**Visualisierungen:**
- Stacked Bar: Levinson-Stufen pro Cluster
- Heatmap: Levinson-Stufe × Cluster (normalisiert)
- Grouped Bar: Alle Cluster nebeneinander
**Output:** `ergebnisse/analyse_levinson_mapping.md` + `ergebnisse/visualisierungen_vergleich/`
**Beantwortet:** "Welches Gerechtigkeitsverständnis dominiert?"

### ✅ Schritt 7: Cross-Cluster-Vergleich (→ Dimension 3) — ERLEDIGT
**Script:** `scripts/analyse_vergleich_cluster.py`
**Ergebnis:** Relevanzraten 50,2–74,1%. FH Wien mit deutlich abweichendem
Profil (Code 2.1: 18,3% vs. PH 32–39%; Code 2.7: 43% vs. PH 18–27%; Code 2.3
erhöht). Konsistent mit kompensatorischem Levinson-Profil aus Schritt 6.
**Output:** `ergebnisse/analyse_vergleich_cluster.md` + 2 Visualisierungen

**Was:**
- Summary-Tabelle aller Cluster
- Code-Verteilung normalisiert
- PH-Aggregat (West + Mitte + SüdOst) vs. FH Wien (falls vorhanden)
- Relevanz-Ratio-Unterschiede interpretieren (50.2% Mitte vs 74.1% West)
**Visualisierungen:** Grouped Bar, Heatmap, PH vs. FH
**Output:** `ergebnisse/analyse_vergleich_cluster.md`
**Beantwortet:** "Systematische Unterschiede zwischen Clustern?"

### ✅ Schritt 8: Zitate-Sammlung alle Cluster — ERLEDIGT
**Script:** `scripts/zitate_sammlung.py` (optional Einzel-Cluster-CLI)
**Was:** Bis zu 5 Zitate pro Code pro Cluster, HTML bereinigt, sortiert nach
Kontext-Länge (informativere Textstellen zuerst).
**Output:** 4× `ergebnisse/cluster_*/zitate.md`

### Schritt 9: Forschungsbericht (8 Seiten + Anhang)
**Iterativ mit Claude:** Erst Daten → dann Entwurf → Team überarbeitet

**Struktur:**
```
1. Einleitung & Forschungsfragen                    (~0.5 S.)
2. Methodik (Korpus, Kategorien, CEiL, ICR)          (~1.5 S.)
3. Ergebnisse                                        (~4 S.)
   3.1 Datenübersicht (Tabelle)
   3.2 D1: Explizit vs. Implizit (Code 1.1)
   3.3 D2: Konzeptuelle Tiefe (Levinson-Heatmap)
   3.4 D3: Komparativer Vergleich
4. Diskussion & Beantwortung der HFF                 (~1.5 S.)
5. Limitationen                                      (~0.5 S.)
---
Literaturverzeichnis                                  (extra)
Anhang: Weitere Visualisierungen, Kodiermanual-Auszug (extra)
```

**Kernvisualisierung im Hauptteil:** Levinson-Heatmap (beantwortet D2 + D3 gleichzeitig)
**Anhang:** Detailtabellen, weitere Grafiken, Code-Verteilungen pro Cluster

### Schritt 10: Poster
**Was:** Poster-Entwurf für 10-Min-Postersession
**Inhalt:** Forschungsfrage, Methode (kurz), Levinson-Heatmap, Kernbefunde, Fazit
**Wer:** Claude erstellt Struktur, Team gestaltet

### Schritt 11: Dokumentation aktualisieren
**Was:** ergebnisse/README.md, CLAUDE.md — veraltete Zahlen und Pfade korrigieren

---

## Forschungsfragen → Deliverables

| Forschungsdimension | Script | Visualisierung | Bericht-Kapitel |
|---|---|---|---|
| **D1: Explizit vs. Implizit** ✅ | analyse_code_1_1_deep_dive.py | Explizit:Implizit-Ratio | Kap. 3.2 |
| **D2: Konzeptuelle Tiefe** | analyse_levinson_mapping.py | Stacked Bar + Heatmap | Kap. 3.3 |
| **D3: Komparativ** | analyse_vergleich_cluster.py | Grouped Bar + PH vs. FH | Kap. 3.4 |
| **Hauptforschungsfrage** | Synthese aller 3 | — | Kap. 4 |

---

## Bekannte Probleme (gelöst im Plan)

| Problem | Lösung |
|---|---|
| **Scripts verwenden `code` statt `confirmed_code`** | **Schritt 0: Alle Scripts auf confirmed_code umstellen** |
| Code "1.0" (Expose) vs "1.1" (CSV) | Scripts matchen auf CSV-Namen |
| 4 NaN in SüdOst | Schritt 1: löschen |
| ICR nur mündlich dokumentiert | Schritt 2: Dokumentation erstellen |
| Scripts nicht modular | Schritt 3: utils.py |
| FH Wien PDF fehlt | Schritt 4: parallel beschaffen, Fallback N=3 |
| 8 Seiten knapp | Anhang nutzen, 1 Kernvisualisierung im Text |
| Relevanz-Ratio-Varianz (50-74%) | Im Bericht reflektieren (Abschnitt Limitationen) |
| Latente Analyse nur interpretativ | Im Methodik-Teil transparent beschreiben |
| Windows-Encoding (cp1252 vs UTF-8) | utils.py mit encoding='utf-8' Default |
| Poster-Format ungeklärt | Vor Poster-Erstellung klären |
| README.md alte Forschungsfrage | Schritt 11: am Ende aktualisieren |

---

## Kritische Dateien

**Scripts:**
- `scripts/utils.py` — Shared Utilities (Pfade, Farben, Levinson-Mapping)
- `scripts/analyse_code_1_1_deep_dive.py` — Dimension 1 (alle Cluster, CLI)

**Daten (alle bereinigt, 100% validiert):**
- `ergebnisse/cluster_west/export_clean.csv` (468 Findings, 347 relevant)
- `ergebnisse/cluster_mitte/export_clean.csv` (516 Findings, 259 relevant)
- `ergebnisse/cluster_suedost/export_clean.csv` (272 Findings, 192 relevant)
- `ergebnisse/cluster_fh_wien/export_clean.csv` (370 Findings, 263 relevant)

**Referenz:**
- `knowledge/expose.md` Zeile 145-156 — Tabelle 2 (Levinson-Mapping)
- `knowledge/coding_manual.md` — 233 Keywords, 8 Codes

**Qualitätssicherung:**
- `tests/test_scripts.py` — 53 Tests (Regressionstests gegen bekannte Zahlen)
- `ergebnisse/intercoder_reliability.md` — ICR-Dokumentation

---

## Timeline

| Wann | Was | Wer |
|---|---|---|
| KW 11-12 (März) | ✅ Schritte 0-4 (Infrastruktur, Bereinigung, FH Wien) | Claude + Laura |
| KW 15 (April) | ✅ Schritt 5 (Code 1.1 Deep Dive) | Claude |
| KW 15-17 (April) | Schritte 6-8 (Levinson, Vergleich, Zitate) | Claude |
| KW 19-23 (Mai-Juni) | Schritt 9: Forschungsbericht iterativ | Claude + Team |
| KW 25 (Juni) | Schritt 10: Poster | Claude + Team |
| 26.06. | Postersession | Babsi + Laura |
| 29.06. | Abgabe Forschungsbericht (PDF) | Team |

---

## Verification

1. Alle Scripts fehlerfrei ausführbar: `python scripts/<script>.py`
2. Markdown-Reports + PNGs in ergebnisse/ vollständig
3. Levinson-Prozentsätze ergeben 100% pro Cluster
4. Bericht deckt alle 3 Dimensionen + HFF ab
5. Poster enthält Kernbefunde + Levinson-Visualisierung
6. Keine veralteten Zahlen in README/CLAUDE.md
