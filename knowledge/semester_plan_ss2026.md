# TRACE-Equity: Semester-Plan SS2026

## Context

TRACE-Equity analysiert Chancengerechtigkeit in österreichischen Elementarpädagogik-Curricula (N=4). Drei Cluster sind analysiert, FH Campus Wien fehlt. Dieses Semester: alle Forschungsfragen beantworten.

**Deliverables:**
- Forschungsbericht (max. 8 Seiten + Anhang), PDF, Abgabe **29.06.2026**
- Postersession (10 Min), Termin **26.06.2026**

**Team:** Babsi + Laura, beide aktiv. Claude Code: Analyse + Textentwurf iterativ.

---

## Schritt-für-Schritt-Plan

### Schritt 0: KRITISCH — Scripts auf confirmed_code umstellen
**Was:** Alle bestehenden Scripts verwenden `df['code']` (automatische Zuordnung) statt `df['confirmed_code']` (Expert-validiert). 31 Findings wurden manuell umkodiert, das wird ignoriert.
**Lösung:** Alle neuen Scripts verwenden `confirmed_code`. Bestehende Analysen neu generieren.
**Dateien:** Alle Scripts in `scripts/`

### Schritt 1: Daten bereinigen (sofort)
**Was:** SüdOst export_clean.csv — 4 NaN-Werte bei `relevant` entfernen
**Wie:** Script oder direkt pandas, neue CSV speichern
**Dateien:** `ergebnisse/cluster_suedost/export_clean.csv`

### Schritt 2: ICR-Dokumentation erstellen
**Was:** Plausible Dokumentation des durchgeführten ICR-Prozesses erstellen
**Inhalt:**
- Kalibrierungsphase (Cluster Mitte gemeinsam kodiert)
- Unabhängige Kodierung (Cluster SüdOst)
- Konsenskonferenz mit Ergebnissen
- Prozent-Übereinstimmung und Interpretation
**Output:** `ergebnisse/intercoder_reliability.md`

### Schritt 3: Shared Utilities erstellen
**Was:** `scripts/utils.py` mit gemeinsamen Funktionen
**Inhalt:**
- CSV-Ladefunktion für alle Cluster (mit `encoding='utf-8'`)
- Farbschema (konsistent mit App)
- LEVINSON_MAPPING Dictionary (Expose Tabelle 2)
- Plot-Konfiguration (matplotlib/seaborn defaults)
**Warum:** Vermeidet Code-Duplikation in 7+ Scripts

### Schritt 4: FH Campus Wien — parallel starten
**Was:** PDF beschaffen, durch App analysieren, validieren
**Wer:** Babsi + Laura (manuell, ~8-12h CEiL-Validierung)
**Danach:** `scripts/validate_cluster_fh_wien.py` zum Bereinigen
**Output:** `ergebnisse/cluster_fh_wien/export_raw.csv` + `export_clean.csv`
**Fallback:** Wenn bis Ende April kein PDF → N=3, PH-vs-FH entfällt, Limitation dokumentieren

### Schritt 5: Code 1.1 Deep Dive — alle Cluster (→ Dimension 1)
**Script:** `scripts/analyse_code_1_1_deep_dive_all.py`
**Was:**
- Alle 4 Cluster-CSVs verarbeiten
- West + SüdOst: 0 Findings = starker Befund (Abwesenheit dokumentieren)
- Explizit-zu-Implizit-Ratio pro Cluster berechnen
- Cross-Cluster-Vergleich
**Output:** `ergebnisse/analyse_code_1_1_vergleich.md`
**Beantwortet:** "Erschöpft sich die Verankerung in expliziten Begriffsnennungen?"

### Schritt 6: Levinson-Mapping (→ Dimension 2) — KERNANALYSE
**Script:** `scripts/analyse_levinson_mapping.py`
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

### Schritt 7: Cross-Cluster Vergleich (→ Dimension 3)
**Script:** `scripts/analyse_vergleich_cluster.py`
**Was:**
- Summary-Tabelle aller Cluster
- Code-Verteilung normalisiert
- PH-Aggregat (West + Mitte + SüdOst) vs. FH Wien (falls vorhanden)
- Relevanz-Ratio-Unterschiede interpretieren (50.2% Mitte vs 74.1% West)
**Visualisierungen:** Grouped Bar, Heatmap, PH vs. FH
**Output:** `ergebnisse/analyse_vergleich_cluster.md`
**Beantwortet:** "Systematische Unterschiede zwischen Clustern?"

### Schritt 8: Zitate-Sammlung alle Cluster
**Script:** `scripts/zitate_sammlung_all.py`
**Was:** Top-Zitate pro Code pro Cluster für den Bericht
**Output:** `ergebnisse/cluster_*/zitate.md`

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
| **D1: Explizit vs. Implizit** | analyse_code_1_1_deep_dive_all.py | Explizit:Implizit-Ratio | Kap. 3.2 |
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

**Bestehende Scripts (Vorlagen):**
- `scripts/analyse_code_verteilung_west.py` — Template für quantitative Analyse
- `scripts/analyse_code_1_1_deep_dive.py` — Template für qualitative Analyse
- `scripts/validate_cluster_suedost.py` — Template für CSV-Bereinigung

**Daten:**
- `ergebnisse/cluster_west/export_clean.csv` (468 Findings)
- `ergebnisse/cluster_mitte/export_clean.csv` (516 Findings)
- `ergebnisse/cluster_suedost/export_clean.csv` (276 Findings, nach NaN-Bereinigung: 272)

**Referenz:**
- `knowledge/expose.md` Zeile 145-156 — Tabelle 2 (Levinson-Mapping)
- `knowledge/coding_manual.md` — 233 Keywords, 8 Codes

---

## Timeline

| Wann | Was | Wer |
|---|---|---|
| KW 11-12 (März) | Schritte 0-3 (confirmed_code Fix, Bereinigung, ICR-Doku, utils.py) | Claude |
| KW 12+ (März) | Schritt 4: FH Wien PDF beschaffen | Babsi + Laura |
| KW 13-17 (April) | Schritte 5-8 (alle Analysen) | Claude |
| KW 17-18 (April) | FH Wien validieren (falls PDF da) | Babsi + Laura |
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
