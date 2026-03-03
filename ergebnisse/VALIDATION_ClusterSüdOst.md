# Validation Report: Cluster SüdOst

**Curriculum:** Cluster Süd Ost - Burgenland, Kärnten, Steiermark.pdf
**Validationsdatum:** 19.11.2025
**Original CSV:** TRACE_Equity_Export_ClusterSüdOst.csv
**Bereinigte CSV:** TRACE_Equity_Export_ClusterSüdOst_cleaned.csv

---

## 1. Validierungsstatus

| Status | Anzahl | Prozent |
|--------|--------|---------|
| **Total Findings** | 319 | 100% |
| Validiert | 276 | 86.5% |
| Nicht validiert | 43 | 13.5% |

### Interpretation

✅ **86.5% validiert** - Validierungsprozess ist weit fortgeschritten

⚠️ **43 nicht-validierte Findings** - Wahrscheinlich semantische Duplikate:
- 23/43 (53.5%) haben gleiche Seite + gleiches Keyword wie validierte Findings
- Typisches Muster: Mehrere Keywords im gleichen Textabschnitt gefunden
- Empfehlung: Nicht-validierte Findings entfernen (bereits geschehen in `_cleaned.csv`)

---

## 2. Relevanz-Analyse (nur validierte Findings, n=276)

| Relevanz | Anzahl | Prozent |
|----------|--------|---------|
| **Relevant (ja)** | 192 | 69.6% |
| **Nicht relevant (nein)** | 80 | 29.0% |
| Fehlende Werte | 4 | 1.4% |

### Interpretation

**69.6% Relevanz-Ratio** - Deutlich höher als bei Cluster Mitte (50.2%)

**Mögliche Erklärungen:**
1. **Unterschiedliche Curricula-Struktur**: Cluster SüdOst könnte Chancengleichheits-Thematik expliziter verankern
2. **Lerneffekt bei Validierung**: Besseres Verständnis der Relevanzkriterien im zweiten Durchgang
3. **Kürzeres Curriculum**: Weniger Findings insgesamt → präzisere Keyword-Treffer

**Methodenkritische Frage:**
- Sind die Curricula tatsächlich so unterschiedlich?
- Oder hat sich die Validierungspraxis zwischen beiden Sessions verändert?

---

## 3. Code-Verteilung (alle Findings, n=319)

| Code | Anzahl | Prozent |
|------|--------|---------|
| Code 2.1: Diversität & Heterogenität | 130 | 40.8% |
| Code 2.7: Professionelle Haltung & Ethik | 69 | 21.6% |
| Code 2.3: Individuelle Förderung & Differenzierung | 27 | 8.5% |
| Code 2.5: Bildungspartnerschaft & Sozialraumorientierung | 26 | 8.2% |
| Code 2.2: Inklusion & Partizipation | 24 | 7.5% |
| Code 2.4: Abbau von Benachteiligung & Diskriminierung | 22 | 6.9% |
| Code 2.6: Sprachliche Bildung & Mehrsprachigkeit | 21 | 6.6% |
| **Code 1.1: Direkte Nennung** | **0** | **0%** |

### Auffälligkeiten

❌ **Code 1.1 fehlt komplett** - Keine explizite Nennung von Chancengleichheit gefunden
- Cluster Mitte hatte 8 Findings (1.6%)
- Bedeutet: Cluster SüdOst verankert Chancengleichheit **ausschließlich implizit**

✅ **Code 2.1 dominiert** - Diversität & Heterogenität mit 40.8%
- Cluster Mitte: 36.6% → ähnliches Muster

✅ **Code 2.7 stark vertreten** - Professionelle Haltung & Ethik mit 21.6%
- Cluster Mitte: 18.4% → vergleichbar

---

## 4. Code-Verteilung (nur relevante Findings, n=192)

| Code | Anzahl | Prozent |
|------|--------|---------|
| Code 2.1: Diversität & Heterogenität | 84 | 43.8% |
| Code 2.7: Professionelle Haltung & Ethik | 33 | 17.2% |
| Code 2.3: Individuelle Förderung & Differenzierung | 19 | 9.9% |
| Code 2.5: Bildungspartnerschaft & Sozialraumorientierung | 18 | 9.4% |
| Code 2.2: Inklusion & Partizipation | 17 | 8.9% |
| Code 2.6: Sprachliche Bildung & Mehrsprachigkeit | 12 | 6.2% |
| Code 2.4: Abbau von Benachteiligung & Diskriminierung | 9 | 4.7% |

### Interpretation

**Schwerpunkte:**
1. **Diversität** (43.8%) - Anerkennung und Wertschätzung von Vielfalt
2. **Professionelle Haltung** (17.2%) - Reflexivität und Ethik
3. **Individuelle Förderung** (9.9%) - Stärkenorientierung

**Lücken:**
- **Code 2.4** (Abbau von Benachteiligung) nur 4.7% - Schwache Verankerung transformativer Ansätze
- **Code 1.1** (Direkte Nennung) 0% - Keine explizite Benennung als Leitprinzip

---

## 5. Vergleich: Cluster Mitte vs. Cluster SüdOst

| Metrik | Cluster Mitte | Cluster SüdOst |
|--------|---------------|----------------|
| **Total Findings (validiert)** | 516 | 276 |
| **Relevant** | 259 (50.2%) | 192 (69.6%) |
| **Nicht relevant** | 257 (49.8%) | 80 (29.0%) |
| **Code 1.1 (Direkte Nennung)** | 8 (1.6%) | 0 (0%) |
| **Code 2.1 (Diversität)** | 189 (36.6%) | 84 (43.8%) |
| **Code 2.7 (Haltung)** | 95 (18.4%) | 33 (17.2%) |

### Zentrale Befunde

**Gemeinsamkeiten:**
- Beide Curricula: Dominanz von Code 2.1 (Diversität)
- Beide: Starke Verankerung professioneller Haltung (Code 2.7)
- Beide: Schwache Verankerung transformativer Ansätze (Code 2.4)

**Unterschiede:**
- **Relevanz-Ratio**: SüdOst 69.6% vs. Mitte 50.2% → 19.4 Prozentpunkte Differenz
- **Direkte Nennung**: SüdOst 0% vs. Mitte 1.6% → SüdOst noch impliziter
- **Findings gesamt**: Mitte 516 vs. SüdOst 276 → SüdOst 53.5% weniger Findings

**Mögliche Erklärungen:**
1. **Curriculum-Umfang**: Cluster Mitte umfasst mehr Hochschulen (OÖ Linz, Salzburg) → längeres Dokument
2. **Curricula-Struktur**: Unterschiedliche didaktische Konzepte
3. **Validierungs-Lerneffekt**: Präzisere Relevanzbeurteilung bei zweitem Curriculum

---

## 6. Nicht-validierte Findings (n=43)

### Code-Verteilung (nicht-validiert)

| Code | Anzahl |
|------|--------|
| Code 2.1: Diversität & Heterogenität | 18 |
| Code 2.7: Professionelle Haltung & Ethik | 12 |
| Code 2.5: Bildungspartnerschaft & Sozialraumorientierung | 6 |
| Code 2.6: Sprachliche Bildung & Mehrsprachigkeit | 4 |
| Code 2.4: Abbau von Benachteiligung & Diskriminierung | 3 |

### Semantische Duplikat-Analyse

**Methode:** Gleiche Seite + gleiches Keyword = wahrscheinlich semantisches Duplikat

**Ergebnis:**
- 23/43 (53.5%) haben gleiche Seite & Keyword wie validierte Findings
- Wahrscheinlich: Mehrere Keywords im gleichen Textabschnitt gefunden
- Vergleich Cluster Mitte: 71/75 (94.7%) waren Duplikate

**Interpretation:**
- Bei Cluster SüdOst wurden **mehr Findings aktiv nicht validiert** (nicht nur automatische Duplikate)
- Könnte bedeuten: Strengere Relevanzkriterien angewandt

---

## 7. Datenqualität

### Fehlende Werte

| Spalte | Fehlende Werte |
|--------|----------------|
| pdf_name | 0 |
| page | 0 |
| code | 0 |
| keyword | 0 |
| context | 0 |
| validated | 0 |
| **relevant** | **47** |
| **confirmed_code** | **43** |
| notes | 319 (erwartet) |

### Interpretation

✅ **Kerndaten vollständig** - Alle PDF-Namen, Seiten, Codes, Keywords, Contexte vorhanden

⚠️ **47 Findings ohne Relevanz-Angabe** - Davon:
- 43 nicht validiert (erklärbar: keine Validierung = kein relevant-Wert)
- 4 validiert ABER ohne Relevanz-Angabe → **Inkonsistenz!**

⚠️ **43 Findings ohne confirmed_code** - Entspricht exakt den nicht-validierten Findings → konsistent

✅ **Notes-Spalte leer** - Erwartbar (optionales Feld)

---

## 8. Empfehlung & Nächste Schritte

### Bereinigung

✅ **Bereinigte CSV erstellt:** `TRACE_Equity_Export_ClusterSüdOst_cleaned.csv`
- Nur validierte Findings (n=276)
- Keine Duplikate
- Bereit für wissenschaftliche Analyse

### Nächste Schritte

**1. Wissenschaftliche Analysen durchführen**

Quantitative Analyse:
```bash
python analyse_code_verteilung.py
```
- CSV_FILE anpassen auf: `TRACE_Equity_Export_ClusterSüdOst_cleaned.csv`
- Erstellt 4 Visualisierungen + Markdown-Report

**2. Qualitative Analyse (Optional)**

Code 1.1 Deep Dive: **NICHT möglich** - Keine Findings in Code 1.1 vorhanden

Alternative: **Code 2.1 Deep Dive** (Diversität & Heterogenität)
- 84 relevante Findings
- Analyse der Diversitäts-Konzepte im Curriculum

**3. Komparative Analyse**

Vergleich Cluster Mitte vs. Cluster SüdOst:
- Unterschiede in Code-Verteilung
- Implizite vs. explizite Verankerung
- Theoretische Rahmungen (Diversity vs. Equity)

---

## 9. Methodenkritische Reflexion

### Relevanz-Ratio: 69.6% (SüdOst) vs. 50.2% (Mitte)

**Interpretation 1: Curricula sind tatsächlich unterschiedlich**
- SüdOst hat präzisere Keyword-Treffer
- Chancengleichheit thematisch fokussierter

**Interpretation 2: Validierungs-Lerneffekt**
- Besseres Verständnis der Relevanzkriterien im zweiten Durchgang
- Präzisere Beurteilung bei SüdOst

**Interpretation 3: Methodisches Artefakt**
- Unterschiedliche Tagesform bei Validierung
- Keine Intercoder-Reliabilität (nur eine Person validiert)

**Empfehlung:**
- Relevanz-Kriterien explizit dokumentieren
- Stichprobenartige Re-Validierung von Cluster Mitte
- Bei weiteren Curricula: Relevanz-Ratio beobachten

### Code 1.1 fehlt komplett

**Kritische Frage:**
- Ist das ein tatsächlicher Befund (SüdOst benennt Chancengleichheit nie explizit)?
- Oder ein methodisches Problem (Keywords zu eng gefasst)?

**Prüfung:**
- Manuelle Suche nach "Gerechtigkeit", "Fairness", "gleiche Chancen"
- Falls gefunden: Keywords erweitern

---

## Siehe auch

- **Quantitative Analyse (Cluster Mitte):** `analyse_1_code_verteilung.md`
- **Qualitative Analyse (Cluster Mitte):** `analyse_2_code_1_1_deep_dive.md`
- **Zitate-Sammlung (Cluster Mitte):** `analyse_2_zitate.md`

---

**Erstellt:** 19.11.2025
**Methodik:** Reflexive Thematic Analysis (RTA) + Critical Expert in the Loop (CEiL)
**Qualitätssicherung:** Semantische Duplikat-Analyse, Validierungsstatus-Prüfung
