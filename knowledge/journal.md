# TRACE-Equity Arbeitsprotokoll

Lückenlose Dokumentation aller Entwicklungsschritte und methodischen Entscheidungen.

---

## Session: 2025-11-19 (Dienstag)

### **Ziel der Session**
1. Refactoring: Implementierung des Single Source of Truth Prinzips
2. Fix: Typo-Korrektur (Knowlege → Knowledge)
3. Fix: PythonAnywhere Deployment-Problem
4. Datenvalidierung: CSV-Analyse und Bereinigung
5. Wissenschaftliche Analyse: Quantitative und qualitative Auswertung

---

## 1. Single Source of Truth: Dynamisches Keyword-Loading

### Problem
- Keywords waren hardcoded in `app.py` (138 Keywords)
- Doppelung zwischen `Kodiermanual.md` und `app.py`
- Synchronisationsprobleme bei Keyword-Updates
- Fehleranfällig und schwer zu warten

### Lösung
**Implementierung eines dynamischen Parsers:**

```python
def parse_keywords_from_kodiermanual(filepath='Knowledge/Kodiermanual.md'):
    """
    Parst Keywords direkt aus dem Kodiermanual.md
    Single Source of Truth - keine Duplikation mehr!
    """
```

**Technische Details:**
- Verwendet `re.split()` zum Aufteilen nach Code-Sektionen
- Regex-Pattern: `r'##### Code [\d\.]+: '`
- Erkennt mehrfache Keyword-Sektionen (wichtig für Code 2.4)
- Entfernt Inline-Kommentare wie `(im Bildungskontext)`
- Validierung: Prüft auf 8 erwartete Codes

**Ergebnis:**
- ✅ 233 Keywords geladen (statt 138 hardcoded)
- ✅ Alle 8 Codes erfolgreich geparst
- ✅ Code 2.4: Beide Sektionen korrekt kombiniert (61 Keywords)

**Commit:** `c2e0d11` - "Implement Single Source of Truth: Dynamic keyword loading from Kodiermanual.md"

---

## 2. Typo-Korrektur: Knowlege → Knowledge

### Problem
- Ordnername `Knowlege/` enthielt Rechtschreibfehler
- Inkonsistent im gesamten Projekt

### Durchgeführte Änderungen
1. **Ordner umbenannt:** `mv Knowlege Knowledge`
2. **app.py aktualisiert:** Alle Pfadreferenzen korrigiert
3. **CLAUDE.md aktualisiert:** Dokumentation angepasst
4. **Git:** Korrekt als Rename erkannt

**Dateien betroffen:**
- `app.py`: Zeile 32 - `filepath = os.path.join(BASE_DIR, 'Knowledge', 'Kodiermanual.md')`
- `CLAUDE.md`: Alle Verweise auf den Ordner
- Alle Markdown-Dokumente im Ordner

**Commit:** Teil von `c2e0d11`

---

## 3. PythonAnywhere Deployment-Fix

### Problem
**502 Backend Error** auf PythonAnywhere nach Initial-Deployment

**Root Cause:**
- **Working Directory:** `/home/bsteiner/`
- **Source Code:** `/home/bsteiner/trace-equity/`
- Relative Pfade funktionierten nicht

### Lösung
**Absolute Pfad-Berechnung mit `BASE_DIR`:**

```python
# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_keywords_from_kodiermanual(filepath=None):
    if filepath is None:
        filepath = os.path.join(BASE_DIR, 'Knowledge', 'Kodiermanual.md')
```

**Vorher:**
- `filepath='Knowlege/Kodiermanual.md'` (relativ zum Working Directory)
- Suchte in: `/home/bsteiner/Knowlege/Kodiermanual.md` ❌

**Nachher:**
- `filepath=os.path.join(BASE_DIR, 'Knowledge', 'Kodiermanual.md')`
- Findet: `/home/bsteiner/trace-equity/Knowledge/Kodiermanual.md` ✅

**Ergebnis:**
- ✅ App läuft auf PythonAnywhere
- ✅ 233 Keywords korrekt geladen
- ✅ Funktioniert sowohl lokal als auch auf Server

**Commit:** Teil von `c2e0d11`

---

## 4. Fail-Fast Error Handling

### Problem
- Bei fehlendem Kodiermanual: App fiel zurück auf 2 Keywords
- Silent Failure → invalide Analyse-Ergebnisse
- Keine klare Fehlermeldung

### Lösung
**Explizite Fehlerbehandlung mit SystemExit:**

```python
except FileNotFoundError:
    print("="*80)
    print(f"CRITICAL ERROR: Kodiermanual.md not found")
    print(f"Looked for file at: {filepath}")
    print(f"App directory (BASE_DIR): {BASE_DIR}")
    # ... Hilfreiche Deployment-Anweisungen ...
    raise SystemExit("FATAL: Kodiermanual.md not found - cannot continue")
```

**Vorher:**
- Silent Fallback auf 2 Keywords
- App startet, produziert aber falsche Ergebnisse

**Nachher:**
- App verweigert Start
- Klare Fehlermeldung mit Lösungsvorschlägen
- Deployment-Anleitung direkt im Fehler

**Commit:** Teil von `c2e0d11`

---

## 5. CSV-Datenvalidierung und Bereinigung

### 5.1 Initiale Validierung

**Datei:** `TRACE_Equity_Export_20251118_173805 (1).csv`

**Befunde:**
- 591 Total Findings
- 516 validierte Findings (87.3%)
- 75 nicht-validierte Findings (12.7%)

### 5.2 Duplikat-Analyse

**Hypothese:** Die 75 nicht-validierten Findings sind semantische Duplikate

**Methode:** Context-Overlap-Analyse
- Vergleich auf Seitenebene
- Wort-Überlappung berechnen
- Threshold: 70% Überlappung

**Python-Code:**
```python
overlap = len(not_val_words & val_words) / len(not_val_words)
if overlap > 0.7:
    semantic_duplicates += 1
```

**Ergebnis:**
- 71 von 75 (94.7%) sind semantische Duplikate
- Gleicher Textabschnitt, verschiedene Keywords
- 4 Findings keine klaren Duplikate

**Beispiel:**
```
Validiert: "geschlechterstereotype [...] Sprache [...]" (Keyword: "Geschlecht")
Nicht-validiert: "geschlechterstereotype [...] Sprache [...]" (Keyword: "Gender")
→ Gleicher Kontext, verschiedene Keywords → Duplikat
```

### 5.3 Bereinigung

**Durchgeführt:**
```python
cleaned_df = df[df['validated'] == True].copy()
cleaned_df.to_csv('TRACE_Equity_Export_20251118_173805_cleaned.csv')
```

**Ergebnis:**
- **Neue Datei:** `TRACE_Equity_Export_20251118_173805_cleaned.csv`
- **516 Findings** (100% validiert)
- **0 semantische Duplikate**
- **Bereit für wissenschaftliche Analyse**

**Dokumentiert in:** Dieses Protokoll

---

## 6. Wissenschaftliche Analyse

### 6.1 Analyse 1: Code-Verteilungs-Analyse (Quantitativ)

**Script:** `analyse_code_verteilung.py`

**Methodik:**
- Deskriptive Statistik
- Häufigkeitsanalysen
- Visualisierungen (matplotlib, seaborn)

**Outputs:**

#### A) Visualisierungen (4 PNGs, je 300 DPI)

1. **01_code_verteilung_alle.png**
   - Horizontales Balkendiagramm
   - Alle 516 Findings
   - Farbcodiert nach Code-Kategorien

2. **02_code_verteilung_relevant.png**
   - Nur relevante Findings (n=259)
   - Zeigt tatsächliche Verankerung

3. **03_relevanz_ratio.png**
   - Pie Chart: 259 relevant / 257 nicht-relevant
   - 50.2% Relevanz-Quote

4. **04_top_keywords.png**
   - Top 15 häufigste Keywords
   - "sozial" führt mit 53 Findings

#### B) Markdown-Report

**Datei:** `ergebnisse/analyse_1_code_verteilung.md`

**Inhalte:**
- Statistische Übersicht (Tabellen)
- Code-Verteilung absolut & relativ
- Top Keywords
- **Wissenschaftliche Interpretation:**
  - Schwerpunkte (Diversität dominiert mit 36.6%)
  - Lücken (Code 1.1 nur 1.6%)
  - Capability Approach Mapping
  - Methodenkritische Reflexion (50.2% Relevanz-Quote)

**Zentrale Befunde:**

| Code | Findings | Prozent | Interpretation |
|------|----------|---------|----------------|
| 2.1 Diversität | 189 | 36.6% | **Dominiert** - Fokus auf Diversitätsdiskurse |
| 2.7 Prof. Haltung | 122 | 23.6% | Stark - Reflexivität & Habitus |
| 2.6 Sprache | 90 | 17.4% | Moderat - Mehrsprachigkeit |
| 2.2 Inklusion | 82 | 15.9% | Moderat |
| 2.4 Benachteiligung | 37 | 7.2% | Schwach - Transformative Ansätze? |
| 2.5 Partnerschaft | 32 | 6.2% | Schwach |
| 2.3 Förderung | 31 | 6.0% | Schwach - Kompensation? |
| 1.1 Direkte Nennung | 8 | 1.6% | **Minimal** - Explizite Verankerung fehlt |

**Commit:** `eb77d99` - "Add scientific analysis scripts for TRACE-Equity data"

---

### 6.2 Analyse 2: Code 1.1 Deep Dive (Qualitativ)

**Script:** `analyse_code_1_1_deep_dive.py`

**Fokus:** Explizite Verankerung von Chancengleichheit

**Methodik:**
- Reflexive Thematische Analyse (RTA)
- Semantische Differenzierung
- Kontextkategorisierung
- Capability Approach Mapping

**Outputs:**

#### A) Qualitativer Report

**Datei:** `ergebnisse/analyse_2_code_1_1_deep_dive.md`

**Befunde:**

**Keyword-Verteilung (8 relevante Findings):**
- Bildungsgerechtigkeit: 5x (Seiten 10, 16, 49, 50, 53)
- Chancengleichheit: 1x (Seite 10)
- Teilhabegerechtigkeit: 1x (Seite 10)
- Chancengerechtigkeit: 1x (Seite 68)

**Semantische Differenzierung:**

| Begriff | Konzeptuelle Rahmung | Theoretischer Bezug |
|---------|---------------------|---------------------|
| Chancengleichheit | Formale Gleichheit | Liberal-egalitär |
| Chancengerechtigkeit | Substanzielle Gerechtigkeit | Capability Approach (Sen) |
| Equity | Fairness durch Berücksichtigung | Educational Equity |
| Bildungsgerechtigkeit | Gerechtigkeit im Bildungskontext | Kritische Bildungstheorie |

**Verwendungskontexte:**
- Normativ (Leitprinzip): 4 Findings
- Beschreibend (Modulinhalte): 1 Finding
- Kompetenzbezogen: 1 Finding
- Organisatorisch: 2 Findings

**Zentrale Interpretation:**

**Implizit-zu-Explizit-Ratio: 31.4:1**
- Von 259 relevanten Findings: nur 8 explizit
- Chancengleichheit wird primär **implizit** behandelt (Codes 2.1-2.7)
- Explizite Benennung als Leitprinzip: **selten**

**Kritische Frage:**
> Reicht implizite Verankerung für professionelle Habitusbildung?

#### B) Zitate-Sammlung

**Datei:** `ergebnisse/analyse_2_zitate.md`

**Struktur:**
- Nach Keywords gruppiert
- Mit Seitenzahlen
- Verwendungskontext kategorisiert
- Bereit für Paper-Zitate

**Nutzung:**
- Direkte Belege für curriculare Verankerung
- Vergleich mit anderen Hochschulen
- Präsentationen

**Commit:** `eb77d99` - "Add scientific analysis scripts for TRACE-Equity data"

---

## 7. Methodenkritische Reflexion

### 7.1 Relevanz-Quote: 50.2%

**Befund:**
- Von 516 Findings: 259 relevant, 257 nicht-relevant
- Precision: 50.2%

**Interpretation:**
- ✅ **Methodisch wertvoll** für CEiL-Prinzip (Critical Expert in the Loop)
- ✅ Zeigt Notwendigkeit menschlicher Validierung
- ✅ Transparenz durch dokumentierte False Positives

**Mögliche Erklärungen für False Positives:**
1. **Kontextabhängigkeit:** Keyword erscheint, aber Bedeutung passt nicht
   - Beispiel: "sozial" in "sozial-emotionale Entwicklung"
2. **Semantische Überlappung:** Mehrere Keywords im gleichen Textabschnitt
3. **Zu breite Keywords:** "sozial", "Haltung" sind weit gefasst

### 7.2 Code-Konsistenz: 97.7%

**Befund:**
- Von 516 validierten Findings: 504 Code bestätigt, 12 geändert
- Code-Change-Rate: 2.3%

**Interpretation:**
- ✅ **Sehr hohe Zuverlässigkeit** der automatischen Keyword-Zuordnung
- ✅ Nur 12 manuelle Korrekturen nötig
- ✅ Validiert die Qualität des Kodiermanuals

### 7.3 Single Source of Truth: Erfolgreich

**Vorher:**
- 138 Keywords hardcoded
- Duplikation, Synchronisationsprobleme
- Fehleranfällig

**Nachher:**
- 233 Keywords dynamisch geladen
- Keine Duplikation
- Ein Update in Kodiermanual.md → automatisch übernommen

**Vorteil für Forschung:**
- Methodentransparenz: Alle Keywords dokumentiert
- Reproduzierbarkeit: Kodiermanual = Code
- Iterative Verfeinerung möglich

---

## 8. Technische Details

### Dependencies
```txt
Flask==2.3.0
PyPDF2==3.0.1
pandas==2.0.3
openpyxl==3.1.2
matplotlib==3.10.7
seaborn==0.13.2
```

### Python-Version
- Lokal: 3.14
- PythonAnywhere: 3.10

### Dateisystem-Struktur

```
TRACE-Equity/
├── app.py                              # Flask backend (Single Source of Truth parser)
├── analyse_code_verteilung.py          # Quantitative Analyse
├── analyse_code_1_1_deep_dive.py       # Qualitative Analyse
├── templates/
│   └── index.html                      # Frontend
├── Knowledge/                          # Korrigierte Schreibweise
│   ├── Kodiermanual.md                 # SINGLE SOURCE OF TRUTH (233 keywords)
│   ├── abstract.md
│   ├── forschungsmethode.md
│   ├── DEPLOYMENT_ERFOLG.md
│   └── WIE_STARTE_ICH_DIE_APP.md
├── uploads/                            # PDF uploads (gitignored)
├── ergebnisse/                         # Analyse results (gitignored)
│   ├── TRACE_Equity_Export_*_cleaned.csv
│   ├── analyse_1_code_verteilung.md
│   ├── analyse_1_visualisierungen/
│   │   ├── 01_code_verteilung_alle.png
│   │   ├── 02_code_verteilung_relevant.png
│   │   ├── 03_relevanz_ratio.png
│   │   └── 04_top_keywords.png
│   ├── analyse_2_code_1_1_deep_dive.md
│   └── analyse_2_zitate.md
├── CLAUDE.md                           # Projekt-Dokumentation
├── ARBEITSPROTOKOLL.md                 # Dieses Dokument
├── README.md
└── requirements.txt
```

---

## 9. Git Commits (Session)

### Commit 1: `c2e0d11`
**Message:** "Implement Single Source of Truth: Dynamic keyword loading from Kodiermanual.md"

**Änderungen:**
- app.py: Keyword-Parser implementiert
- CLAUDE.md: Dokumentation aktualisiert (233 keywords)
- Knowlege/ → Knowledge/ (Rename)
- Alle Referenzen korrigiert

**Stats:**
- 8 files changed
- 770 insertions(+)
- 304 deletions(-)

### Commit 2: `eb77d99`
**Message:** "Add scientific analysis scripts for TRACE-Equity data"

**Änderungen:**
- analyse_code_verteilung.py: Neu
- analyse_code_1_1_deep_dive.py: Neu
- 15 alte Test-Dateien gelöscht

**Stats:**
- 17 files changed
- 710 insertions(+)
- 39,427 deletions(-)

---

## 10. Nächste Schritte (Optional)

### Mögliche weitere Analysen

1. **False-Positive-Analyse**
   - Welche Keywords produzieren am meisten Rauschen?
   - Systematische Muster identifizieren
   - Keyword-Liste verfeinern

2. **Code 2.4 Deep Dive**
   - Transformative vs. kompensatorische Ansätze
   - Empowerment-Analyse
   - Strukturelle Veränderung im Curriculum?

3. **Komparative Analyse**
   - Weitere Hochschulen analysieren
   - Cluster-Vergleiche
   - Typologie curricularer Ansätze

4. **Visualisierung: Heatmap**
   - Seitenbasierte Code-Verteilung
   - Wo im Curriculum konzentrieren sich welche Themen?

---

## 11. Qualitätssicherung

### Validierung der Ergebnisse

✅ **Code-Loading:** 233 Keywords erfolgreich geparst
✅ **Deployment:** PythonAnywhere funktioniert
✅ **Datenbereinigung:** 516 validierte Findings, keine Duplikate
✅ **Visualisierungen:** 4 PNG-Dateien generiert (300 DPI)
✅ **Reports:** 2 Markdown-Dokumente erstellt
✅ **Reproduzierbarkeit:** Python-Scripts wiederverwendbar

### Intersubjektivität

- Code-Konsistenz: 97.7% (Expert-Validierung bestätigt Keywords)
- Transparenz: Alle Findings dokumentiert
- Nachvollziehbarkeit: Dieses Protokoll + CLAUDE.md

---

## 12. Wissenschaftlicher Ertrag

### Quantitativ
- 516 validierte Findings
- 8 Code-Kategorien
- 86 eindeutige Keywords gefunden
- 259 relevante Findings für Interpretation

### Qualitativ
- Explizite vs. implizite Verankerung identifiziert (1:31.4 Ratio)
- Schwerpunkte: Diversität > Professionelle Haltung > Sprache
- Lücken: Direkte Nennung, transformative Ansätze
- Capability Approach Mapping durchgeführt

### Methodisch
- Single Source of Truth erfolgreich implementiert
- CEiL-Prinzip validiert (50.2% Relevanz = menschliche Validierung notwendig)
- Promptotyping-Workflow dokumentiert
- Reproduzierbare Scripts erstellt

---

## 13. Zeitaufwand

| Tätigkeit | Dauer (ca.) |
|-----------|-------------|
| Single Source of Truth Refactoring | 2h |
| PythonAnywhere Debugging | 1h |
| CSV-Validierung & Bereinigung | 1h |
| Analyse 1: Code-Verteilung | 1.5h |
| Analyse 2: Code 1.1 Deep Dive | 1h |
| Dokumentation & Commits | 1h |
| **Gesamt** | **~7.5h** |

---

## Metadaten

**Session-Datum:** 2025-11-19 (Dienstag)
**Bearbeiter:** Babsi + Claude Code
**Python-Version:** 3.14 (lokal) / 3.10 (PythonAnywhere)
**Curriculum analysiert:** Cluster Mitte_OÖ_Linz, Salzburg.pdf
**Findings validiert:** 516
**Commits:** 2 (c2e0d11, eb77d99)

---

---

## Session: 2026-01 bis 2026-02 (Jänner–Februar)

### Repo-Reorganisation und Cluster West

#### Repo-Struktur bereinigt
Das Repository wurde grundlegend reorganisiert. Die bisherige flache
Struktur (alle Dateien im Root, Ergebnisse in `.gitignore`) wurde durch
eine cluster-basierte Ordnerstruktur ersetzt:
- `ergebnisse/cluster_west/`, `cluster_mitte/`, `cluster_suedost/` — je
  mit `export_raw.csv`, `export_clean.csv` und Analyse-Outputs
- `knowledge/` — alle Promptotyping-Dokumente (vorher teils in `docs/`,
  teils im Root)
- `uploads/` — Curriculum-PDFs (aus `.gitignore` entfernt)

#### Cluster West bereinigt und analysiert
- `export_raw.csv` bereinigt: 66 unvalidierte/unvollständige Findings
  entfernt → 468 Findings in `export_clean.csv` (100% validiert)
- Erste quantitative Analyse erstellt (Code-Verteilung, Keywords,
  Relevanz-Ratio)
- Befund: **0 Code-1.1-Findings** — keine explizite Nennung von
  Chancengleichheit im Cluster West

#### Exposé konsolidiert
Drei Versionen des Exposés (Root, `docs/expose.md`, `docs/expose_narrative.md`)
auf eine finale Version reduziert und nach `knowledge/expose.md` verschoben.
Die übrigen Dateien in `docs/` wurden gelöscht, der Ordner entfernt.

---

## Session: 2026-03 (März)

### Semesterplanung und Infrastruktur (Schritte 0–4)

#### Semesterplan erstellt
Plan für SS2026 mit 12 Schritten (0–11), Timeline und Deliverables
dokumentiert in `knowledge/semester_plan_ss2026.md`. Zwei Deliverables:
- Forschungsbericht (8 Seiten + Anhang), Abgabe 29.06.2026
- Postersession (10 Min), Termin 26.06.2026

#### Schritt 0: confirmed_code-Bug behoben
Alle Analyse-Scripts verwendeten `df['code']` (automatische Zuordnung)
statt `df['confirmed_code']` (Expert-validiert). Das bedeutete: 31 Findings,
die im CEiL-Verfahren manuell umkodiert wurden, flossen mit dem falschen
Code in die Analyse ein. Alle Scripts wurden auf `confirmed_code` umgestellt.

#### Schritt 1: SüdOst NaN-Werte bereinigt
4 Findings in `cluster_suedost/export_clean.csv` hatten `validated=True`
aber `relevant=NaN` — die Relevanz-Bewertung war in der App nicht ausgefüllt
worden. Diese 4 Findings wurden entfernt (276 → 272).

#### Schritt 2: ICR-Dokumentation erstellt
Intercoder-Reliabilität dokumentiert in `ergebnisse/intercoder_reliability.md`:
- Kalibrierungsphase: Cluster Mitte gemeinsam kodiert
- Unabhängige Kodierung: Cluster SüdOst doppelt kodiert
- Ergebnis: κ = 0,71 (Relevanz), κ = 0,83 (Codezuordnung)
- Interpretation nach Landis & Koch (1977): substanziell bis fast perfekt

#### Schritt 3: Shared Utilities erstellt
`scripts/utils.py` als zentrale Konfiguration: Pfade, Farben, Ladefunktionen,
Levinson-Mapping. Alle Scripts refactored, drei cluster-spezifische Scripts
zu einem vereinheitlicht (`analyse_code_verteilung.py` mit CLI-Parametern).

#### Schritt 4: FH Campus Wien integriert
Laura lieferte den validierten Export als Apple Numbers Datei. Konvertiert
zu CSV, bereinigt (42 unvalidierte + 6 NaN-relevant entfernt): 418 → 370
Findings, davon 263 relevant (71,1%). 1 Code-1.1-Finding identifiziert.

#### Test Suite erstellt
49 Tests in `tests/test_scripts.py`: Konfiguration, Ladefunktionen,
Datenqualität über alle 4 Cluster, Filterfunktionen, Levinson-Mapping,
Regressionstests gegen bekannte Zahlen.

---

## Session: 2026-04-08 (Dienstag)

### **Ziel der Session**
Analyse-Infrastruktur bereinigen und mit der systematischen Beantwortung der
Forschungsfragen beginnen (Schritt 5 des Semesterplans).

---

### 1. Bereinigung der Analyse-Infrastruktur

#### Was wir gemacht haben
Alle Analyse-Artefakte aus dem Wintersemester wurden entfernt, weil sie auf
einem methodischen Fehler basierten: Die Scripts verwendeten das Feld `code`
(automatische Keyword-Zuordnung) statt `confirmed_code` (Expert-validierte
Zuordnung). Der Unterschied betrifft 31 Findings, die im CEiL-Verfahren
manuell umkodiert wurden — diese Korrekturen wurden von den alten Scripts
ignoriert.

#### Konkret entfernt
- 12 Visualisierungen (PNG-Dateien) aus Cluster West, Mitte und SüdOst
- 3 veraltete Markdown-Reports (`analyse_code_verteilung.md`)
- 1 veraltete Zitate-Sammlung (`zitate.md`, Cluster Mitte)
- 1 veralteter Validierungsbericht (`validation_report.md`, Cluster SüdOst)
- 1 Apple-Numbers-Datei (FH Wien Original, bereits in CSV konvertiert)
- 1 veraltetes Analyse-Script (`analyse_code_verteilung.py`)

#### Warum das alte Analyse-Script entfällt
Das Script `analyse_code_verteilung.py` erstellte deskriptive
Häufigkeitsstatistiken und Balkendiagramme pro Cluster. Diese Outputs werden
durch die neuen, forschungsfragengeleiteten Scripts vollständig ersetzt:
- Die **Levinson-Analyse** (Schritt 6) liefert die inhaltlich relevante
  Code-Aufschlüsselung nach Gerechtigkeitsstufen
- Der **Cross-Cluster-Vergleich** (Schritt 7) liefert die deskriptive
  Übersichtstabelle, die im Ergebnisteil des Berichts benötigt wird

Rein deskriptive Häufigkeitsauszählungen ohne theoretischen Bezug beantworten
keine Forschungsfrage und wurden daher nicht weiter mitgeführt.

---

### 2. Schritt 5: Code 1.1 Deep Dive — Dimension 1

#### Forschungsfrage
> *"Erschöpft sich die curriculare Verankerung in expliziten Begriffsnennungen
> oder wird Chancengerechtigkeit über konkrete pädagogische
> Handlungskompetenzen operationalisiert?"*

#### Methode
Code 1.1 ("Direkte Nennung") erfasst Textstellen, in denen Begriffe wie
"Chancengleichheit", "Chancengerechtigkeit", "Bildungsgerechtigkeit" oder
"Equity" explizit verwendet werden. Alle übrigen Codes (2.1–2.7) erfassen
implizite Bezüge über pädagogische Handlungsfelder wie Diversität, Inklusion
oder Sprachbildung. Durch den Vergleich von expliziten und impliziten
Findings lässt sich bestimmen, auf welche Weise Chancengerechtigkeit im
Curriculum verankert ist.

#### Ergebnisse

| Cluster | Relevante Findings | Code 1.1 (explizit) | Code 2.x (implizit) | Verhältnis |
|---|---|---|---|---|
| West | 347 | 0 | 347 | nur implizit |
| Mitte | 259 | 8 | 251 | 31:1 |
| SüdOst | 192 | 0 | 192 | nur implizit |
| FH Wien | 263 | 1 | 262 | 262:1 |
| **Gesamt** | **1.061** | **9** | **1.052** | **117:1** |

#### Interpretation
Von 1.061 relevanten Findings über alle 4 Cluster hinweg enthalten nur
9 (0,8%) eine explizite Nennung von Chancengerechtigkeit. Die restlichen
99,2% verankern das Thema implizit über pädagogische Handlungsfelder.

Zwei Cluster (West, SüdOst) enthalten **keine einzige** explizite
Begriffnennung — trotz substanzieller impliziter Verankerung (347 bzw.
192 relevante Findings). Cluster Mitte zeigt mit 8 expliziten Nennungen
die stärkste explizite Verankerung, wobei "Bildungsgerechtigkeit" der am
häufigsten verwendete Begriff ist (5 von 8 Nennungen). FH Wien hat genau
1 explizite Nennung ("Chancengerechtigkeit", Seite 65).

**Befund D1:** Die curriculare Verankerung erschöpft sich eindeutig nicht
in expliziten Begriffsnennungen. Chancengerechtigkeit wird als
Querschnittsthema behandelt, das sich in konkreten pädagogischen
Handlungsfeldern manifestiert, ohne als eigenständiges Leitkonzept benannt
zu werden.

---

### 3. Methodik-Dokumentation

Für das Forschungsteam wurde eine zentrale Methodik-Dokumentation erstellt
(`ergebnisse/analyse_methodik.md`), die alle drei Analyse-Dimensionen
erklärt:
- D1: Explizit vs. Implizit (abgeschlossen)
- D2: Konzeptuelle Tiefe nach Levinson (nächster Schritt)
- D3: Cross-Cluster-Vergleich (danach)

Das Dokument beschreibt für jede Dimension: Was wird untersucht, warum ist
es wichtig, wie sind die Ergebnisse zu lesen, und welches Script erzeugt
die Outputs.

---

### 4. CLAUDE.md aktualisiert

Die Projektdokumentation wurde auf den aktuellen Stand gebracht:
- FH Campus Wien als 4. Cluster mit Zahlen ergänzt
- Veraltete Dateireferenzen entfernt
- Testsuite dokumentiert (53 Tests)
- Behobene Issues dokumentiert (confirmed_code-Bug, NaN-Bereinigung)

---

### Outputs dieser Session

| Output | Pfad |
|---|---|
| Code-1.1-Report Cluster West | `ergebnisse/cluster_west/analyse_code_1_1_deep_dive.md` |
| Code-1.1-Report Cluster Mitte | `ergebnisse/cluster_mitte/analyse_code_1_1_deep_dive.md` |
| Code-1.1-Report Cluster SüdOst | `ergebnisse/cluster_suedost/analyse_code_1_1_deep_dive.md` |
| Code-1.1-Report FH Wien | `ergebnisse/cluster_fh_wien/analyse_code_1_1_deep_dive.md` |
| Cross-Cluster-Vergleich D1 | `ergebnisse/analyse_code_1_1_vergleich.md` |
| Methodik-Dokumentation | `ergebnisse/analyse_methodik.md` |

### Nächste Schritte

- **Schritt 6:** Levinson-Mapping (Dimension 2) — Welches Gerechtigkeitsverständnis dominiert?
- **Schritt 7:** Cross-Cluster-Vergleich (Dimension 3) — Systematische Unterschiede?
- **Schritt 8:** Zitate-Sammlung für den Forschungsbericht

---

**Dokumentiert durch:** Babsi + Claude Code
**Letzte Aktualisierung:** 2026-04-08

---

## Session: 2026-04-14 (Dienstag)

### **Ziel der Session**
Schritt 6 des Semesterplans umsetzen: das Levinson-Mapping als Kernanalyse
für Dimension 2 (Konzeptuelle Tiefe). Zentrale Forschungsfrage: Welches
Gerechtigkeitsverständnis — formale Gleichheit, kompensatorische oder
transformative Gerechtigkeit — dominiert in den untersuchten Curricula?

---

### 1. Konzeptuelle Entscheidung vor der Implementierung

Das Kodiermanual umfasst acht Codes; das Levinson-Mapping laut Exposé
(Tabelle 2) verteilt diese auf drei Gerechtigkeitsstufen plus zwei
Querschnittskategorien und die explizite Nennung (Code 1.1). Für die
Hauptauswertung der Dimension 2 haben wir uns entschieden, ausschließlich
die drei Levinson-Stufen auszuwerten:

- **Formale Gleichheit** (Codes 2.1 Diversität, 2.2 Inklusion)
- **Kompensatorische Gerechtigkeit** (Codes 2.3 Individuelle Förderung, 2.6 Sprachliche Bildung)
- **Transformative Gerechtigkeit** (Code 2.4 Abbau von Benachteiligung)

Begründung: Die Querschnittskategorien (2.5 Bildungspartnerschaft, 2.7
Professionelle Haltung) lassen sich nicht sinnvoll einer der drei Stufen
zuordnen, und Code 1.1 wurde bereits in Schritt 5 separat behandelt. Um
Transparenz zu wahren, werden die ausgeschlossenen Findings separat
ausgewiesen (absolut und als "Abdeckungsrate der drei Stufen").

### 2. Implementierung

Neues Script `scripts/analyse_levinson_mapping.py` mit CLI analog zu
Schritt 5 (`--alle`, einzelne Cluster). Pro Cluster entsteht ein
Markdown-Report mit drei Tabellen (prozentuale Verteilung über die drei
Stufen, absolute Zahlen, orthogonale Kategorien) und ein horizontales
Stacked-Bar-Diagramm. Der Cross-Cluster-Report enthält die
**Levinson-Heatmap als Kernvisualisierung** des Forschungsberichts
(3 Stufen × 4 Cluster, prozentual normalisiert, mit Abdeckungsraten im
Untertitel) sowie ein ergänzendes Grouped-Bar-Diagramm.

### 3. Ergebnisse (nur relevante Findings, prozentual über die drei Stufen)

| Cluster | Formale Gleichheit | Kompensatorisch | Transformativ | Abdeckung |
|---|---:|---:|---:|---:|
| West | 67,1% | 28,9% | 4,0% | 64,8% |
| Mitte | 71,8% | 16,6% | 11,6% | 69,9% |
| SüdOst | 69,7% | 23,5% | 6,8% | 68,8% |
| FH Wien | 48,9% | 39,8% | 11,3% | 50,6% |

**Befund D2:** Formale Gleichheit dominiert in allen vier Clustern;
transformative Gerechtigkeit bleibt durchgängig unterrepräsentiert
(4–12%). Die FH Campus Wien fällt durch einen deutlich höheren Anteil
kompensatorischer Gerechtigkeit auf als die drei PH-Cluster.

### 4. Qualitätssicherung

Vier neue Regressionstests für die Levinson-Verteilung ergänzt;
Testsuite umfasst nun 57 Tests, alle grün.

### Outputs dieser Session

| Output | Pfad |
|---|---|
| Levinson-Analyse pro Cluster (4×) | `ergebnisse/cluster_*/analyse_levinson.md` |
| Stacked Bar pro Cluster (4×) | `ergebnisse/cluster_*/visualisierungen/levinson_verteilung.png` |
| Cross-Cluster-Vergleich D2 | `ergebnisse/analyse_levinson_vergleich.md` |
| **Kernvisualisierung Heatmap** | `ergebnisse/visualisierungen_vergleich/levinson_heatmap.png` |
| Grouped Bar (Anhang) | `ergebnisse/visualisierungen_vergleich/levinson_grouped_bar.png` |

### Nächste Schritte

- **Schritt 7:** Cross-Cluster-Vergleich (Dimension 3) — systematische Unterschiede
- **Schritt 8:** Zitate-Sammlung für den Forschungsbericht

---

**Dokumentiert durch:** Babsi + Claude Code
**Letzte Aktualisierung:** 2026-04-14

---

## Session: 2026-04-15 (Mittwoch)

### **Ziel der Session**
Schritt 7 des Semesterplans umsetzen: den Cross-Cluster-Vergleich auf
Code-Ebene als Beantwortung der Dimension 3 der Forschungsfrage
("Gibt es systematische Unterschiede zwischen den vier Clustern?").

---

### 1. Konzeptuelle Entscheidung

Ein PH-Sammelwert (West + Mitte + SüdOst aggregiert) wurde bewusst nicht
gebildet. Alle vier Cluster bleiben als eigenständige Einheiten im
Vergleich, die institutionelle Einordnung (Pädagogische Hochschulen vs.
Fachhochschule) wird ausschließlich im Interpretationstext vorgenommen.
Grund: Ein Aggregat würde vortäuschen, dass die drei PH-Standorte
intern homogen sind — tatsächlich variieren sie deutlich (etwa bei
Relevanzrate und Code 2.3).

### 2. Implementierung

Neues Script `scripts/analyse_vergleich_cluster.py` (ohne
Einzel-Cluster-CLI, da per Definition cross-cluster). Das Script
erzeugt eine Summary-Tabelle, drei Detailtabellen (prozentual,
absolut, Spannweite je Code) sowie zwei Visualisierungen (Grouped Bar
und Heatmap 8 Codes × 4 Cluster). Die Kernvisualisierung des
Forschungsberichts bleibt die Levinson-Heatmap aus Schritt 6; die hier
erzeugten Grafiken sind für Anhang und Postersession gedacht.

### 3. Ergebnisse

**Relevanzraten:** 50,2% (Mitte) bis 74,1% (West). Diese Varianz
interpretieren wir als methodischen Hinweis auf Unterschiede in der
curricularen Sprache (generische vs. fachspezifische Begriffsdichte),
nicht als inhaltlichen Befund zu Chancengerechtigkeit.

**Systematische Abweichung FH Wien ↔ PH-Cluster:**

| Code | West | Mitte | SüdOst | FH Wien |
|---|---:|---:|---:|---:|
| 2.1 Diversität | 32,3% | 35,1% | 39,1% | 18,3% |
| 2.3 Individuelle Förderung | 8,9% | 3,9% | 8,9% | 12,9% |
| 2.7 Professionelle Haltung | 26,5% | 21,6% | 18,2% | 43,0% |

Die FH Wien zeigt einen deutlich geringeren Anteil bei Diversitäts-
Begriffen und einen auffällig hohen Anteil bei Professioneller Haltung
und Ethik. Das fügt sich konsistent in den Levinson-Befund aus Schritt 6,
wo die FH Wien das kompensatorischste Profil aufwies.

### 4. Qualitätssicherung

Fünf neue Regressionstests für Summe aller relevanten Findings sowie
Code-Verteilungen pro Cluster. Testsuite umfasst nun 62 Tests, alle grün.

### Outputs dieser Session

| Output | Pfad |
|---|---|
| Cross-Cluster-Report D3 | `ergebnisse/analyse_vergleich_cluster.md` |
| Grouped Bar | `ergebnisse/visualisierungen_vergleich/code_verteilung_grouped_bar.png` |
| Heatmap Codes × Cluster | `ergebnisse/visualisierungen_vergleich/code_verteilung_heatmap.png` |

### Nächste Schritte

- **Schritt 8:** Zitate-Sammlung pro Code pro Cluster für den Bericht
- **Schritt 9:** Forschungsbericht (8 Seiten + Anhang) iterativ

---

**Dokumentiert durch:** Babsi + Claude Code
**Letzte Aktualisierung:** 2026-04-15
