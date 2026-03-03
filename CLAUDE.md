# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**TRACE-Equity** (Tracking Representations of Access, Chances and Equity) is a qualitative research project analyzing how equity and equal opportunity are embedded in Austrian elementary pedagogy bachelor degree curricula.

### Research Methodology

The project combines:
- **Qualitative Content Analysis (QCA)** with **Reflexive Thematic Analysis (RTA)**
- **Keyword-based text analysis** with manual validation (Version A - implemented)
- **Critical Expert in the Loop (CEiL)**: Mandatory human validation of all findings
- **Promptotyping**: Structured prompt engineering methodology combining Requirements Engineering, User-Centred Design, and Scholar-Centred Design principles

---

## Current Implementation Status

### ✅ **Fully Implemented: Version A - Keyword-Based Analysis**

The project has been fully implemented as a **Flask Web Application** with the following features:

#### **Core Features**

**1. PDF Analysis (F1)**
- Automatic text extraction from curriculum PDFs using PyPDF2
- Page-by-page processing
- **233 keywords across 8 code categories** dynamically loaded from [coding_manual.md](knowledge/coding_manual.md)
- **Single Source of Truth**: Keywords are parsed directly from the Kodiermanual at runtime (no hardcoding)

**2. Keyword Search with Visual Highlighting**
- Case-insensitive keyword search
- **Color-coded keyword highlighting** - each code category has its own color:
  - Code 1.1 (Direkte Nennung): Red (#e74c3c)
  - Code 2.1 (Diversität): Blue (#3498db)
  - Code 2.2 (Inklusion): Green (#2ecc71)
  - Code 2.3 (Individuelle Förderung): Orange (#f39c12)
  - Code 2.4 (Abbau Benachteiligung): Purple (#9b59b6)
  - Code 2.5 (Bildungspartnerschaft): Turquoise (#1abc9c)
  - Code 2.6 (Sprachliche Bildung): Dark Orange (#e67e22)
  - Code 2.7 (Professionelle Haltung): Dark Gray (#34495e)
- Context extraction (±200 characters around keyword)
- Keywords displayed **bold and colored** in context

**3. Expert Validation Interface (F3 - CEiL)**
- Manual validation for each finding:
  - "Relevant?" dropdown (Ja/Nein)
  - Code confirmation/modification dropdown
  - Notes field for qualitative remarks
- **Automatic saving** - all validations saved immediately to JSON
- **Visual feedback** - "✓ Gespeichert" indicator on successful save
- **Progress tracking** - visual progress bar showing "X / Y validiert"

**4. Multi-Session Management**
- **Multiple PDF sessions** - work on unlimited curricula simultaneously
- **Session persistence** - uses browser localStorage
- **Session list** displaying:
  - PDF name
  - Number of findings
  - Date/time of analysis
- **Resume functionality** - continue work on any saved session
- **Delete sessions** - clean up completed analyses

**5. Data Export (F5)**
- **CSV export with all validations** - fully functional on both local and PythonAnywhere
- **BytesIO implementation** - memory-based export (no temporary files on server)
- **uWSGI-compatible** - works with PythonAnywhere's production server
- Columns: pdf_name, page, keyword, context, validated, relevant, confirmed_code, notes
- **HTML tag removal** - clean CSV output (strips highlighting tags)
- UTF-8 encoding with BOM for Excel compatibility
- Direct download to browser's download folder

**6. User Interface Improvements**
- **Progress tracking** - visual progress bar with readable dark text
  - Shows "X / Y validiert" centered over progress bar
  - Always visible regardless of progress percentage
- **Enhanced Code Dropdown** - full code descriptions in validation interface
  - "Code 2.1: Diversität & Heterogenität" instead of just "Code 2.1"
  - Easier to confirm or change code assignments during validation

#### **Technical Stack**

**Backend:**
- Python 3.10+ (3.14 locally, 3.10 on PythonAnywhere)
- Flask 2.3.0 (web framework)
- PyPDF2 3.0.1 (PDF text extraction)
- Pandas 2.0.3 (data manipulation)
- openpyxl 3.1.2 (Excel support)

**Frontend:**
- HTML5/CSS3/JavaScript (ES6+)
- No external dependencies (all inline)
- Purple gradient design (#667eea → #764ba2)
- Responsive layout

**Hosting:**
- Production: PythonAnywhere (http://bsteiner.pythonanywhere.com)
- Local development: http://localhost:5000

#### **Architecture: Single Source of Truth**

The application follows a **Single Source of Truth** principle:

- **[knowledge/coding_manual.md](knowledge/coding_manual.md)** - The authoritative source for all keywords
- **app.py** - Dynamically parses keywords from coding_manual.md at startup
- **No keyword duplication** - All keyword updates happen in the Kodiermanual only

This ensures:
- ✅ Easy maintenance (update keywords in one place)
- ✅ No synchronization issues between files
- ✅ Automatic updates (restart app after Kodiermanual changes)
- ✅ Clear separation: methodology (MD) vs. implementation (Python)

#### **File Structure**

```
TRACE-Equity/
├── app.py                                    # Flask backend - parses coding_manual.md dynamically
├── templates/
│   └── index.html                            # Frontend UI
├── knowledge/                                # Promptotyping Documents
│   ├── coding_manual.md                      # REFERENCE — SINGLE SOURCE OF TRUTH, 233 keywords
│   ├── requirements.md                       # REQUIREMENTS — Funktionale Anforderungen
│   ├── abstract.md                           # KNOWLEDGE — Forschungskontext
│   ├── methodology.md                        # KNOWLEDGE — QCA + RTA Methodik
│   └── journal.md                            # JOURNAL — Entwicklungsprotokoll
├── docs/                                     # Forschungs-Artefakte (Outputs)
│   ├── expose.md                             # Akademisches Exposé
│   └── expose_narrative.md                   # Narratives Exposé
├── scripts/                                  # Analyse-Skripte (post-export)
│   ├── analyse_code_verteilung.py            # Cluster Mitte: Quantitative Analyse
│   ├── analyse_code_1_1_deep_dive.py         # Cluster Mitte: Code 1.1 Tiefenanalyse
│   ├── analyse_code_verteilung_suedost.py    # Cluster SüdOst: Quantitative Analyse
│   └── validate_cluster_suedost.py           # Cluster SüdOst: CSV-Validierung
├── uploads/                                  # PDFs der analysierten Curricula
│   ├── Cluster Mitte_OÖ_Linz, Salzburg.pdf
│   ├── Cluster Süd Ost_Burgenland, Kärnten, Steiermark.pdf
│   ├── PH Burgenland, Kärnten, Steiermark.pdf
│   ├── PH Oberösterreich.pdf
│   └── PH Tirol.pdf
├── ergebnisse/                               # Analyseergebnisse nach Cluster getrennt
│   ├── README.md
│   ├── cluster_west/
│   │   └── export.csv                        # 534 Findings, 476 validiert (89%)
│   ├── cluster_mitte/
│   │   ├── export_raw.csv                    # 591 Findings (roh)
│   │   ├── export_clean.csv                  # 516 Findings (bereinigt, vollständig validiert)
│   │   ├── analyse_code_verteilung.md        # Quantitativer Report
│   │   ├── analyse_code_1_1_deep_dive.md     # Qualitativer Report Code 1.1
│   │   ├── zitate.md                         # Zitate-Sammlung
│   │   └── visualisierungen/                 # 4 PNG-Grafiken
│   └── cluster_suedost/
│       ├── export_raw.csv                    # 319 Findings (roh)
│       ├── export_clean.csv                  # 276 Findings (bereinigt, vollständig validiert)
│       ├── validation_report.md              # Validierungsbericht
│       ├── analyse_code_verteilung.md        # Quantitativer Report
│       └── visualisierungen/                 # 4 PNG-Grafiken
├── _archive/                                 # Archivierte Docs (veraltet, aber aufbewahrt)
│   ├── deployment.md                         # PythonAnywhere deployment (Okt 2025)
│   └── quickstart.md                         # Lokale Entwicklung (Okt 2025)
├── requirements.txt                          # Python dependencies
└── README.md                                 # Project overview
```

#### **Key Routes**

- `GET /` - Main page with upload and session list
- `POST /upload` - Upload and analyze PDF (with error handling and debug logging)
- `GET /load_session/<session_id>` - Load existing session
- `POST /save_validation` - Save validation (auto-triggered)
- `GET /export/<session_id>` - Export results as CSV (BytesIO implementation for PythonAnywhere compatibility)

---

## Data Structure

### Kodiermanual (Coding Manual)

**Total: 233 keywords across 8 code categories** (parsed dynamically from [knowledge/coding_manual.md](knowledge/coding_manual.md))

**Code 1.1: Direkte Nennung** (7 keywords)
- Explicit mentions: "Chancengleichheit", "Chancengerechtigkeit", "Equality", "Equity", "Educational Equity", "Bildungsgerechtigkeit", "Teilhabegerechtigkeit"

**Code 2.1: Diversität & Heterogenität** (28 keywords)
- Diversity, multiculturality, gender sensitivity, cultural/ethnic/religious diversity, family forms

**Code 2.2: Inklusion & Partizipation** (20 keywords)
- Inclusion, integration, participation, belonging, barrier-free environments, equal participation

**Code 2.3: Individuelle Förderung & Differenzierung** (33 keywords)
- Individual support, differentiation, strengths-based approaches, talent development, adaptive support

**Code 2.4: Abbau von Benachteiligung & Diskriminierung** (61 keywords)
- Problem recognition: disadvantage, discrimination, inequality, stereotypes, marginalization
- Transformative action: empowerment, structural change, anti-bias, critical reflection of power structures

**Code 2.5: Bildungspartnerschaft & Sozialraumorientierung** (22 keywords)
- Educational partnerships, networking, community orientation, multiprofessional teams, social space orientation

**Code 2.6: Sprachliche Bildung & Mehrsprachigkeit** (30 keywords)
- Language education, multilingualism, literacy, German as second language (DaZ), emergent literacy, translanguaging

**Code 2.7: Professionelle Haltung & Ethik** (32 keywords)
- Professional attitude, ethics, self-reflection, values, pedagogical habitus, critical self-reflection, appreciation, respect

### Analysis Results JSON Structure

```json
{
  "pdf_name": "PH Burgenland.pdf",
  "timestamp": "20241021_140530",
  "total_results": 120,
  "results": [
    {
      "pdf_name": "PH Burgenland.pdf",
      "page": 12,
      "code": "Code 2.4: Abbau von Benachteiligung & Diskriminierung",
      "keyword": "Empowerment",
      "context": "...strukturelle Veränderung durch <strong style='...'>Empowerment</strong>...",
      "position": 1245,
      "validated": true,
      "relevant": "ja",
      "confirmed_code": "Code 2.4",
      "notes": "Transformatives Konzept klar erkennbar"
    }
  ]
}
```

---

## Development Workflow

### Local Development

1. **Start the app:**
   ```bash
   # chstn's machine:
   cd "C:\Users\chstn\Documents\Master Elementarpädagogik\TRACE-Equity"
   # Babsi's machine:
   cd "C:\Users\Babsi\Documents\Master Elementarpädagogik\3. Semester\SE Forschungsmethoden\TRACE-Equity"
   python app.py
   ```

2. **Access:** http://localhost:5000

3. **Test workflow:**
   - Upload PDF
   - Verify keyword highlighting
   - Make validations
   - Check auto-save ("✓ Gespeichert")
   - Close browser
   - Reopen → Resume session

### Deployment to PythonAnywhere

See [deployment.md](knowledge/deployment.md) for complete step-by-step instructions.

**Quick summary:**
1. Upload files via "Files" tab
2. Ensure virtual environment: `/home/bsteiner/trace-equity/venv`
3. Install dependencies: `pip install Flask PyPDF2 pandas openpyxl`
4. Configure WSGI file
5. Link virtualenv path in Web tab
6. Reload app

**Production URL:** http://bsteiner.pythonanywhere.com

### Scientific Analysis Scripts

Four Python scripts for post-export analysis (run after CSV export from app):

```bash
# Skripte aus dem Projekt-Root ausführen:
python scripts/analyse_code_verteilung.py
python scripts/analyse_code_1_1_deep_dive.py
python scripts/analyse_code_verteilung_suedost.py
python scripts/validate_cluster_suedost.py
```

Alle Skripte verwenden relative Pfade (`../ergebnisse/cluster_*/`) und müssen aus dem **Projekt-Root** ausgeführt werden.

---

## Current Analysis Status (Stand: März 2026)

Drei Cluster wurden analysiert und vollständig (oder teilweise) validiert:

### Cluster West (Tirol, Vorarlberg, Edith Stein)
- **Datei:** `ergebnisse/Cluster West_TRACE_Equity_Export_.csv`
- **Findings gesamt:** 534 | **Validiert:** 476 (89%) — **58 noch offen**
- **Relevant "ja":** 347 | **Relevant "nein":** 121
- **Code 1.1 Treffer:** 0 (kein direktes Chancengleichheit/Equity im Curriculum)

### Cluster Mitte (OÖ, Linz, Salzburg)
- **Datei:** `ergebnisse/TRACE_Equity_Export_ClusterMitte.csv` (Roh)
- **Cleaned:** `ergebnisse/TRACE_Equity_Export_20251118_173805_cleaned.csv` (die Datei, auf die Analyse-Skripte zeigen)
- **Findings gesamt:** 591 | **Validiert:** 516 (87%) — **75 noch offen**
- **Relevant "ja":** 259 | **Relevant "nein":** 257
- **Analyse:** `ergebnisse/analyse_1_code_verteilung.md`, `analyse_2_code_1_1_deep_dive.md`, `analyse_2_zitate.md`
- **Visualisierungen:** `ergebnisse/analyse_1_visualisierungen/` (4 PNGs)

### Cluster SüdOst (Burgenland, Kärnten, Steiermark)
- **Datei:** `ergebnisse/TRACE_Equity_Export_ClusterSüdOst.csv` (Roh)
- **Cleaned:** `ergebnisse/TRACE_Equity_Export_ClusterSüdOst_cleaned.csv`
- **Findings gesamt:** 319 | **Validiert:** 276 (vollständig bereinigt)
- **Relevant "ja":** 192 | **Relevant "nein":** 80
- **Validierungsbericht:** `ergebnisse/VALIDATION_ClusterSüdOst.md`
- **Analyse:** `ergebnisse/analyse_1_code_verteilung_suedost.md`
- **Visualisierungen:** `ergebnisse/analyse_1_visualisierungen_suedost/` (4 PNGs)

---

### Known Issues & Solutions

**Issue 1: CSV Export on PythonAnywhere (RESOLVED - 2025-10-22)**
- **Problem**: `send_file()` with file-based CSV failed on uWSGI with "FileNotFoundError"
- **Root Cause**: PythonAnywhere uses uWSGI which has issues with temporary file handling
- **Solution**: Implemented BytesIO (memory-based) export instead of file-based export
- **Implementation**:
  - CSV is created in memory using `BytesIO()`
  - Returned as `Response()` with proper headers
  - No temporary files created on server
  - Works on both local development and PythonAnywhere production

**Issue 2: Progress Bar Text Visibility (RESOLVED - 2025-10-22)**
- **Problem**: White text on gray background was unreadable
- **Solution**:
  - Changed text color to dark gray (`#333`)
  - Positioned text outside of progress fill bar
  - Centered text absolutely over entire progress bar
  - Reduced font size to 14px

**Issue 3: Code Dropdown Usability (RESOLVED - 2025-10-22)**
- **Problem**: Dropdown only showed code numbers (e.g., "Code 2.1")
- **Solution**: Added full descriptions (e.g., "Code 2.1: Diversität & Heterogenität")
- **Benefit**: Easier to confirm or change code assignments during validation

---

## Methodological Principles

### Quality Standards

**Document Quality Assessment:**
1. **Authenticity**: Verify genuine authorship and original source
2. **Credibility**: Assess reliability and potential bias
3. **Representativeness**: Evaluate typicality vs. idiosyncratic content
4. **Meaning**: Ensure clarity and contextualization

**Analysis Quality:**
- **Transparency**: All steps traceable (JSON storage, validation logging)
- **Clear categories**: 8-code structure from Kodiermanual
- **Consistent coding**: Same keyword list applied across all curricula
- **Expert validation**: Manual review of all findings (CEiL principle)

### Reflexive Thematic Analysis (RTA)

The implementation allows for RTA principles:
1. **Multiple coding**: Single passage can be relevant for multiple codes
2. **Evolving interpretation**: Notes field captures qualitative insights
3. **Flexibility**: Code can be changed during validation
4. **Researcher reflexivity**: Manual validation ensures expert judgment

### Critical Considerations

- **No automatic interpretation**: All findings require human validation
- **Hermeneutic circle**: Iterative review possible through session management
- **Group authorship**: Curricula are institutional documents (acknowledged in analysis)
- **No causal claims**: Descriptive analysis only

---

## Future Development Options

### Version B: LLM-Based Analysis (Not Implemented)

Future enhancement could include:
- Gemini 2.5 Pro integration for semantic analysis
- Automatic thematic clustering
- Latent meaning detection
- Comparative institutional analysis
- Visualization (heatmaps, charts)

**Decision:** Version A (keyword-based) was chosen for:
- Simplicity (no API keys needed)
- Local privacy (no data sent to external services)
- Transparency (clear keyword matching logic)
- Sufficient for research question

---

## Promptotyping Method - Guide

### Kernprinzip: Context Compression
- **Nicht** mehr Informationen → **bessere** Informationen
- Komplexe Anforderungen auf relevante Essenz reduzieren
- Fokussierte Token = bessere LLM-Performance

### Phase 1: Dokument-Setup

**Die 3 Kernfragen beantworten:**

**WHAT? (Pflicht)**
```
README.md → WARUM? Kontext, Motivation, Domäne
requirements.md → WAS? Funktionale + nicht-funktionale Anforderungen
```

**USING WHAT? (Optional)**
```
DATA.md → WOMIT? Datenstrukturen, APIs, Beispiele
coding_manual.md → Keywords und Code-Definitionen
```

**HOW? (Je nach Bedarf)**
```
deployment.md → Deployment-Anleitung
quickstart.md → Lokale Entwicklung
```

### Phase 2: Iterative Entwicklung

**4-Phasen-Zyklus:**

1. **Prompt Engineering**: Klare Anforderung formulieren
2. **Prototyping**: Schrittweise implementieren und testen
3. **Critical Expert Review**: User testet, gibt Feedback
4. **Evaluation & Dokumentation**: Learnings dokumentieren

### Phase 3: Expert-in-the-Loop Integration

- Kontinuierliche User-Tests während Entwicklung
- Iterative Verbesserung basierend auf Feedback
- Alle Änderungen dokumentiert in CLAUDE.md

---

## Communication Guidelines

This is an academic research project in German-speaking Austria:
- **Primary language**: German (for documentation and user interface)
- **Academic terminology**: Aligns with German educational research conventions
- **Context**: Austrian Pädagogische Hochschulen, Bachelor Elementarpädagogik

---

## Key Theoretical Frameworks

The analysis is grounded in:
- Critical educational sociology (Bourdieu, reproduction theory)
- Capability Approach (Sen, Nussbaum)
- Intersectionality theory (Crenshaw, Winker & Degele)
- Curriculum theory (Klafki, documentary method per Bohnsack)
- Professionalization theory (Fröhlich-Gildhoff)
- Inclusive pedagogy (Prengel)

---

## Key Files Reference

**Promptotyping Documents (knowledge/):**
- **[knowledge/coding_manual.md](knowledge/coding_manual.md)** — REFERENCE: 233 keywords (Single Source of Truth)
- **[knowledge/requirements.md](knowledge/requirements.md)** — REQUIREMENTS: Funktionale Anforderungen
- **[knowledge/abstract.md](knowledge/abstract.md)** — KNOWLEDGE: Forschungskontext
- **[knowledge/methodology.md](knowledge/methodology.md)** — KNOWLEDGE: QCA + RTA Methodik
- **[knowledge/journal.md](knowledge/journal.md)** — JOURNAL: Entwicklungsprotokoll
- **[_archive/deployment.md](_archive/deployment.md)** — TECHNICAL: PythonAnywhere deployment (archiviert)
- **[_archive/quickstart.md](_archive/quickstart.md)** — TECHNICAL: Lokale Entwicklung (archiviert)

**Forschungs-Artefakte (docs/):**
- **[docs/expose.md](docs/expose.md)** — Akademisches Exposé
- **[docs/expose_narrative.md](docs/expose_narrative.md)** — Narratives Exposé

**Sonstiges:**
- **[README.md](README.md)** — Project overview
- **[ergebnisse/README.md](ergebnisse/README.md)** — Results folder documentation

---

## Contact & Collaboration

**Project Lead:** Babsi
**Institution:** Master Elementarpädagogik, 3. Semester
**Research Team:** Working group analyzing multiple PH curricula
**Production URL:** http://bsteiner.pythonanywhere.com
