# Ergebnisse / Results

Dieser Ordner enthält die Analyse-Ergebnisse des TRACE-Equity Projekts.

## Inhalt

Die Dateien in diesem Ordner werden **nicht in Git versioniert** (siehe `.gitignore`), da sie große Datenmengen und persönliche Analyseergebnisse enthalten.

### Typische Dateien:

#### 1. PDF-Analyse-Ergebnisse
- `analyse_YYYYMMDD_HHMMSS.json` - Rohdaten der PDF-Keyword-Analyse
- Session-spezifische JSON-Dateien mit allen Findings

#### 2. Export-Dateien
- `TRACE_Equity_Export_YYYYMMDD_HHMMSS.csv` - Exportierte validierte Findings
- `TRACE_Equity_Export_*_cleaned.csv` - Bereinigte Versionen (Duplikate entfernt)

#### 3. Wissenschaftliche Analysen

**Quantitative Analyse:**
- `analyse_1_code_verteilung.md` - Statistischer Report zur Code-Verteilung
- `analyse_1_visualisierungen/` - Ordner mit PNG-Grafiken (4 Visualisierungen)
  - `01_code_verteilung_alle.png` - Alle Findings
  - `02_code_verteilung_relevant.png` - Nur relevante Findings
  - `03_relevanz_ratio.png` - Relevanz-Verteilung (Pie Chart)
  - `04_top_keywords.png` - Top 15 Keywords

**Qualitative Analyse:**
- `analyse_2_code_1_1_deep_dive.md` - Deep Dive: Direkte Nennung von Chancengleichheit
- `analyse_2_zitate.md` - Strukturierte Zitate-Sammlung für wissenschaftliche Arbeiten

---

## Neue Analyse erstellen

### 1. PDF hochladen und analysieren
```bash
# Lokal
python app.py
# → http://localhost:5000

# Oder PythonAnywhere
# → http://bsteiner.pythonanywhere.com
```

### 2. Validierung durchführen
- Manual review aller Findings
- Relevanz-Bewertung (ja/nein)
- Code-Bestätigung oder -Änderung
- Optionale Notizen

### 3. Export als CSV
- Button "Exportieren" klicken
- CSV wird in diesem Ordner gespeichert

### 4. Wissenschaftliche Analysen ausführen

**Quantitative Analyse:**
```bash
python analyse_code_verteilung.py
```

**Qualitative Analyse (Code 1.1):**
```bash
python analyse_code_1_1_deep_dive.py
```

---

## Ordnerstruktur (Beispiel)

```
ergebnisse/
├── README.md                                          # Diese Datei
├── .gitkeep                                           # Git-Tracking
│
├── analyse_20251118_173805.json                       # Session-Daten
├── TRACE_Equity_Export_20251118_173805.csv            # Original-Export
├── TRACE_Equity_Export_20251118_173805_cleaned.csv    # Bereinigt
│
├── analyse_1_code_verteilung.md                       # Quantitativer Report
├── analyse_1_visualisierungen/
│   ├── 01_code_verteilung_alle.png
│   ├── 02_code_verteilung_relevant.png
│   ├── 03_relevanz_ratio.png
│   └── 04_top_keywords.png
│
├── analyse_2_code_1_1_deep_dive.md                    # Qualitativer Report
└── analyse_2_zitate.md                                # Zitate-Sammlung
```

---

## Wichtig

⚠️ **Nicht committen:** Diese Dateien sollten NICHT in Git committed werden
- Enthalten Rohdaten und persönliche Analyseergebnisse
- Große Dateigröße (CSV/JSON)
- Sessions sind lokal/serverseitig gespeichert

✅ **Backup:** Sichere wichtige Ergebnisse separat
- CSV-Exports extern sichern
- Visualisierungen für Paper kopieren
- Reports für wissenschaftliche Arbeit archivieren

---

**Erstellt:** 2025-11-19
**Projekt:** TRACE-Equity (Tracking Representations of Access, Chances and Equity)
