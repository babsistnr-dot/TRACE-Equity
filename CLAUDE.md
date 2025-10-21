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
- 138 keywords across 8 code categories (from Kodiermanual.md)

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
- CSV export with all validations
- Columns: pdf_name, page, code, keyword, context, validated, relevant, confirmed_code, notes
- UTF-8 encoding with BOM for Excel compatibility

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

#### **File Structure**

```
TRACE-Equity/
├── app.py                          # Flask backend (9KB)
├── templates/
│   └── index.html                  # Frontend UI (20KB)
├── uploads/                        # Uploaded PDFs (gitignored)
├── ergebnisse/                     # Analysis results JSON (gitignored)
├── requirements.txt                # Python dependencies
├── Kodiermanual.md                 # Coding manual (8 codes, 138 keywords)
├── DEPLOYMENT_ERFOLG.md            # PythonAnywhere deployment guide
├── WIE_STARTE_ICH_DIE_APP.md      # Local development guide
└── [documentation files]
```

#### **Key Routes**

- `GET /` - Main page with upload and session list
- `POST /upload` - Upload and analyze PDF
- `GET /load_session/<session_id>` - Load existing session
- `POST /save_validation` - Save validation (auto-triggered)
- `GET /export/<session_id>` - Export results as CSV

---

## Data Structure

### Kodiermanual (Coding Manual)

**Code 1.1: Direkte Nennung** (2 keywords)
- Explicit mentions of "Chancengleichheit", "Chancengerechtigkeit"

**Code 2.1: Diversität & Heterogenität** (16 keywords)
- Diversity, multiculturality, gender sensitivity

**Code 2.2: Inklusion & Partizipation** (12 keywords)
- Inclusion, integration, participation, belonging

**Code 2.3: Individuelle Förderung & Differenzierung** (23 keywords)
- Individual support, differentiation, strengths-based approaches

**Code 2.4: Abbau von Benachteiligung & Diskriminierung** (39 keywords)
- Problem recognition: disadvantage, discrimination, inequality
- Transformative action: empowerment, structural change

**Code 2.5: Bildungspartnerschaft & Sozialraumorientierung** (11 keywords)
- Educational partnerships, networking, community orientation

**Code 2.6: Sprachliche Bildung & Mehrsprachigkeit** (15 keywords)
- Language education, multilingualism, literacy

**Code 2.7: Professionelle Haltung & Ethik** (20 keywords)
- Professional attitude, ethics, reflection, values

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

See [DEPLOYMENT_ERFOLG.md](DEPLOYMENT_ERFOLG.md) for complete step-by-step instructions.

**Quick summary:**
1. Upload files via "Files" tab
2. Ensure virtual environment: `/home/bsteiner/trace-equity/venv`
3. Install dependencies: `pip install Flask PyPDF2 pandas openpyxl`
4. Configure WSGI file
5. Link virtualenv path in Web tab
6. Reload app

**Production URL:** http://bsteiner.pythonanywhere.com

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
REQUIREMENTS.md → WAS? Funktionale + nicht-funktionale Anforderungen
```

**USING WHAT? (Optional)**
```
DATA.md → WOMIT? Datenstrukturen, APIs, Beispiele
Kodiermanual.md → Keywords und Code-Definitionen
```

**HOW? (Je nach Bedarf)**
```
DEPLOYMENT_ERFOLG.md → Deployment-Anleitung
WIE_STARTE_ICH_DIE_APP.md → Lokale Entwicklung
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

- **[README.md](README.md)** - Project overview
- **[REQUIREMENTS.md](REQUIREMENTS.md)** - Original requirements (Version A fully implemented)
- **[Kodiermanual.md](Kodiermanual.md)** - Coding manual with all keywords
- **[DEPLOYMENT_ERFOLG.md](DEPLOYMENT_ERFOLG.md)** - PythonAnywhere deployment (tested & working)
- **[WIE_STARTE_ICH_DIE_APP.md](WIE_STARTE_ICH_DIE_APP.md)** - Local development guide
- **[abstract.md](abstract.md)** - Research abstract
- **[forschungsmethode.md](forschungsmethode.md)** - Methodology details

---

## Contact & Collaboration

**Project Lead:** Babsi
**Institution:** Master Elementarpädagogik, 3. Semester
**Research Team:** Working group analyzing multiple PH curricula
**Production URL:** http://bsteiner.pythonanywhere.com
