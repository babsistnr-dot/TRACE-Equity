"""
TRACE-Equity Analyse Script
Analyse 2: Code 1.1 "Direkte Nennung" - Qualitative Tiefenanalyse

Untersucht die explizite Verankerung von Chancengleichheit im Curriculum.
"""

import pandas as pd
import json
from pathlib import Path

# Konfiguration
CSV_FILE = 'ergebnisse/TRACE_Equity_Export_20251118_173805_cleaned.csv'
REPORT_FILE = 'ergebnisse/analyse_2_code_1_1_deep_dive.md'
ZITATE_FILE = 'ergebnisse/analyse_2_zitate.md'

print("="*80)
print("TRACE-EQUITY ANALYSE 2: CODE 1.1 DEEP DIVE")
print("="*80)
print()

# Lade Daten
print("Lade Daten...")
df = pd.read_csv(CSV_FILE)
print(f"[OK] {len(df)} Findings geladen")
print()

# ============================================================================
# 1. DATEN EXTRAHIEREN
# ============================================================================

print("Extrahiere Code 1.1 Findings...")

# Alle Code 1.1 Findings
code_1_1_all = df[df['code'] == 'Code 1.1: Direkte Nennung']
code_1_1_relevant = code_1_1_all[code_1_1_all['relevant'] == 'ja']

print(f"[OK] Code 1.1 Findings:")
print(f"     - Total: {len(code_1_1_all)}")
print(f"     - Relevant: {len(code_1_1_relevant)}")
print(f"     - Nicht relevant: {len(code_1_1_all) - len(code_1_1_relevant)}")
print()

# ============================================================================
# 2. KEYWORD-ANALYSE
# ============================================================================

print("Analysiere Keywords...")

keyword_analysis = {}
for keyword in code_1_1_relevant['keyword'].unique():
    findings = code_1_1_relevant[code_1_1_relevant['keyword'] == keyword]
    keyword_analysis[keyword] = {
        'count': len(findings),
        'pages': sorted(findings['page'].unique().tolist()),
        'contexts': findings['context'].tolist()
    }

print(f"[OK] {len(keyword_analysis)} verschiedene Keywords gefunden:")
for kw, data in sorted(keyword_analysis.items(), key=lambda x: x[1]['count'], reverse=True):
    print(f"     - {kw}: {data['count']}x auf Seiten {data['pages']}")
print()

# ============================================================================
# 3. KONTEXTANALYSE
# ============================================================================

print("Analysiere Verwendungskontexte...")

# Manuelle Kategorisierung nach Durchsicht der Contexte
# (Diese Kategorien müssten bei mehr Findings iterativ entwickelt werden)

kontexte = {
    'Normativ (Leitprinzip)': [],
    'Beschreibend (Modulinhalte)': [],
    'Kompetenzbezogen (Fähigkeiten)': [],
    'Organisatorisch (Strukturen)': []
}

# Für jedes relevante Finding
for idx, row in code_1_1_relevant.iterrows():
    context_lower = row['context'].lower()

    # Heuristik zur Kategorisierung (kann manuell verfeinert werden)
    if any(word in context_lower for word in ['leitbild', 'grundsatz', 'prinzip', 'wert', 'ziel']):
        kontexte['Normativ (Leitprinzip)'].append(row)
    elif any(word in context_lower for word in ['kompetenz', 'fähigkeit', 'können', 'befähigt']):
        kontexte['Kompetenzbezogen (Fähigkeiten)'].append(row)
    elif any(word in context_lower for word in ['modul', 'lehrveranstaltung', 'inhalt', 'thema']):
        kontexte['Beschreibend (Modulinhalte)'].append(row)
    else:
        kontexte['Organisatorisch (Strukturen)'].append(row)

print("[OK] Kontextkategorisierung:")
for kategorie, items in kontexte.items():
    print(f"     - {kategorie}: {len(items)} Findings")
print()

# ============================================================================
# 4. KONZEPTUELLE RAHMUNG
# ============================================================================

print("Analysiere konzeptuelle Rahmungen...")

# Analysiere sprachliche Nuancen
nuancen = {
    'Chancengleichheit': 'Formale Gleichheit der Möglichkeiten',
    'Chancengerechtigkeit': 'Substanzielle Gerechtigkeit (kompensatorisch)',
    'Equality': 'Englisch: Gleichheit',
    'Equity': 'Englisch: Gerechtigkeit/Fairness',
    'Educational Equity': 'Bildungsgerechtigkeit (international)',
    'Bildungsgerechtigkeit': 'Gerechtigkeit im Bildungskontext',
    'Teilhabegerechtigkeit': 'Gerechte Partizipation'
}

print("[OK] Semantische Differenzierung der Begriffe:")
for keyword in keyword_analysis.keys():
    if keyword in nuancen:
        print(f"     - {keyword}: {nuancen[keyword]}")
print()

# ============================================================================
# 5. MARKDOWN-REPORT ERSTELLEN
# ============================================================================

print("Erstelle Markdown-Report...")

report = f"""# TRACE-Equity Analyse 2: Code 1.1 "Direkte Nennung" - Deep Dive

**Curriculum:** Cluster Mitte_OÖ_Linz, Salzburg.pdf
**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Fokus:** Explizite Verankerung von Chancengleichheit im Curriculum

---

## 1. Übersicht

**Code 1.1: Direkte Nennung**
- **Definition:** Explizite Nennung von Chancengleichheit/Chancengerechtigkeit oder verwandten Begriffen
- **Total Findings:** {len(code_1_1_all)}
- **Relevante Findings:** {len(code_1_1_relevant)}
- **Relevanz-Ratio:** {len(code_1_1_relevant)/len(code_1_1_all)*100:.1f}%

---

## 2. Keyword-Verteilung

| Keyword | Anzahl | Seiten |
|---------|--------|--------|
"""

for kw, data in sorted(keyword_analysis.items(), key=lambda x: x[1]['count'], reverse=True):
    pages_str = ', '.join(map(str, data['pages']))
    report += f"| {kw} | {data['count']} | {pages_str} |\n"

report += f"""
---

## 3. Semantische Differenzierung

Die verwendeten Begriffe unterscheiden sich in ihrer konzeptuellen Bedeutung:

| Begriff | Konzeptuelle Rahmung | Theoretischer Bezug |
|---------|---------------------|---------------------|
| Chancengleichheit | Formale Gleichheit der Ausgangsbedingungen | Liberal-egalitärer Ansatz |
| Chancengerechtigkeit | Substanzielle Gerechtigkeit (Kompensation) | Capability Approach (Sen) |
| Equity | Fairness durch Berücksichtigung unterschiedlicher Ausgangslagen | International: Educational Equity |
| Bildungsgerechtigkeit | Gerechtigkeit spezifisch im Bildungskontext | Kritische Bildungstheorie |

**Interpretation:**

Die Begriffswahl im Curriculum ist nicht zufällig:
- **"Chancengleichheit"** betont formale Gleichbehandlung
- **"Chancengerechtigkeit"** impliziert kompensatorische/transformative Ansätze
- **"Equity" vs. "Equality"** international etablierte Unterscheidung

---

## 4. Verwendungskontexte

Die explizite Nennung von Chancengleichheit erfolgt in unterschiedlichen curricularen Kontexten:

"""

for kategorie, items in kontexte.items():
    if len(items) > 0:
        report += f"\n### 4.{list(kontexte.keys()).index(kategorie) + 1} {kategorie}\n\n"
        report += f"**Anzahl Findings:** {len(items)}\n\n"
        report += "**Charakteristik:**\n"

        if kategorie == 'Normativ (Leitprinzip)':
            report += "- Chancengleichheit als übergeordneter Wert oder Grundsatz\n"
            report += "- Meist in Präambeln, Leitbildern oder Zielsetzungen\n"
            report += "- Normative Verpflichtung der Institution\n\n"
        elif kategorie == 'Kompetenzbezogen (Fähigkeiten)':
            report += "- Chancengleichheit als zu erwerbende Kompetenz\n"
            report += "- Studierende sollen Chancengleichheit fördern KÖNNEN\n"
            report += "- Handlungsorientierung\n\n"
        elif kategorie == 'Beschreibend (Modulinhalte)':
            report += "- Chancengleichheit als Modulinhalt oder Thema\n"
            report += "- Didaktische Verankerung in Lehrveranstaltungen\n"
            report += "- Wissensvermittlung\n\n"
        else:
            report += "- Organisatorische oder strukturelle Kontexte\n\n"

report += """
---

## 5. Interpretation: Capability Approach Mapping

Gemäß dem theoretischen Rahmen (Sen, Nussbaum) lassen sich die Findings in drei Kategorien einordnen:

### 5.1 Formale Chancengleichheit
- **Fokus:** Gleiche Ausgangsbedingungen, Nicht-Diskriminierung
- **Begriffe:** Primär "Chancengleichheit", "Equality"
- **Limitation:** Ignoriert strukturelle Ungleichheiten

### 5.2 Substanzielle Chancengerechtigkeit
- **Fokus:** Kompensation unterschiedlicher Ausgangslagen
- **Begriffe:** "Chancengerechtigkeit", "Equity", "Bildungsgerechtigkeit"
- **Ansatz:** Ressourcenorientiert, kompensatorisch

### 5.3 Transformative Gerechtigkeit
- **Fokus:** Strukturelle Veränderung, Empowerment
- **Begriffe:** "Teilhabegerechtigkeit" (am nächsten)
- **Ansatz:** Kritisch-emanzipatorisch

**Befund:**

Die explizite Verankerung von Chancengleichheit im Curriculum ist **gering**:
- Nur {len(code_1_1_relevant)} relevante Findings
- Bedeutet: Chancengleichheit wird primär **implizit** (über Codes 2.1-2.7) behandelt

**Kritische Frage:**
- Ist implizite Verankerung ausreichend für professionelle Habitusbildung?
- Oder braucht es mehr explizite normative Verpflichtung?

---

## 6. Vergleich mit anderen Codes

**Code 1.1 (Direkte Nennung):** {len(code_1_1_relevant)} Findings
**Code 2.1-2.7 (Implizite Dimensionen):** {len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)} Findings

**Verhältnis:**
- Implizite zu explizite Verankerung: {(len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)) / len(code_1_1_relevant):.1f}:1

**Interpretation:**
- Chancengleichheit wird primär über **Diversität, Inklusion, Sprache etc.** thematisiert
- Explizite Benennung als Leitprinzip ist selten
- Mögliche Erklärung: "Hidden Curriculum" vs. Manifest Curriculum

---

## 7. Methodenkritische Reflexion

**Limitation der Keyword-Suche:**
- Nur 7 Keywords für Code 1.1
- Mögliche weitere Begriffe: "Gerechtigkeit", "Fairness", "gleiche Bildungschancen"
- Trade-off: Spezifität vs. Sensitivität

**Stärke:**
- Präzise Erfassung expliziter Nennungen
- Hohe Relevanz-Ratio ({len(code_1_1_relevant)/len(code_1_1_all)*100:.1f}%)

---

## Siehe auch

- **Zitate-Sammlung:** `analyse_2_zitate.md`
- **Quantitative Übersicht:** `analyse_1_code_verteilung.md`

---

**Erstellt mit:** Python (pandas)
**Methodik:** Reflexive Thematic Analysis (RTA) + Critical Expert in the Loop (CEiL)
"""

with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"[OK] Report gespeichert: {REPORT_FILE}")
print()

# ============================================================================
# 6. ZITATE-SAMMLUNG ERSTELLEN
# ============================================================================

print("Erstelle Zitate-Sammlung...")

zitate = f"""# TRACE-Equity Analyse 2: Zitate-Sammlung (Code 1.1)

**Curriculum:** Cluster Mitte_OÖ_Linz, Salzburg.pdf
**Code:** 1.1 Direkte Nennung
**Anzahl relevanter Findings:** {len(code_1_1_relevant)}

---

## Hinweise zur Verwendung

Diese Sammlung enthält alle relevanten Textstellen mit expliziter Nennung von Chancengleichheit/Chancengerechtigkeit.
Die Zitate sind nach Keywords gruppiert und können direkt für wissenschaftliche Arbeiten verwendet werden.

**Format:**
- **Seite:** Seitenzahl im Curriculum-PDF
- **Keyword:** Gefundenes Schlagwort
- **Kontext:** Textausschnitt mit Hervorhebung

---

"""

for keyword in sorted(keyword_analysis.keys()):
    zitate += f"\n## Keyword: \"{keyword}\"\n\n"
    zitate += f"**Anzahl:** {keyword_analysis[keyword]['count']}\n\n"

    findings = code_1_1_relevant[code_1_1_relevant['keyword'] == keyword]

    for idx, row in findings.iterrows():
        # Entferne HTML-Tags für saubere Zitate
        context_clean = row['context'].replace('<strong style="background-color: #e74c3c; color: white; padding: 2px 4px; border-radius: 3px;">', '**')
        context_clean = context_clean.replace('</strong>', '**')

        zitate += f"### Zitat {findings.index.tolist().index(idx) + 1} (Seite {row['page']})\n\n"
        zitate += f"> {context_clean}\n\n"
        zitate += f"**Verwendungskontext:** "

        context_lower = row['context'].lower()
        if any(word in context_lower for word in ['leitbild', 'grundsatz', 'prinzip']):
            zitate += "Normativ (Leitprinzip)\n\n"
        elif any(word in context_lower for word in ['kompetenz', 'fähigkeit']):
            zitate += "Kompetenzbezogen\n\n"
        elif any(word in context_lower for word in ['modul', 'lehrveranstaltung']):
            zitate += "Beschreibend (Modulinhalt)\n\n"
        else:
            zitate += "Sonstiger Kontext\n\n"

        zitate += "---\n\n"

zitate += """
## Nutzungshinweise

Diese Zitate können für folgende Zwecke verwendet werden:

1. **Wissenschaftliche Arbeiten**
   - Direkte Belege für curriculare Verankerung
   - Beispiele für konzeptuelle Rahmungen

2. **Komparative Analyse**
   - Vergleich mit anderen Hochschul-Curricula
   - Typologiebildung

3. **Präsentationen**
   - Illustrative Beispiele
   - Evidenz für Argumentationen

**Zitierweise:**
- Quelle: [Curriculum-Name], Seite [X]
- Als indirekte Paraphrase oder direktes Zitat nutzbar

---

**Erstellt:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
"""

with open(ZITATE_FILE, 'w', encoding='utf-8') as f:
    f.write(zitate)

print(f"[OK] Zitate gespeichert: {ZITATE_FILE}")
print()

print("="*80)
print("ANALYSE 2 ABGESCHLOSSEN")
print("="*80)
print()
print("Outputs:")
print(f"  - Report: {REPORT_FILE}")
print(f"  - Zitate: {ZITATE_FILE}")
print()
print(f"Zentrale Befunde:")
print(f"  - {len(code_1_1_relevant)} relevante Findings mit expliziter Nennung")
print(f"  - {len(keyword_analysis)} verschiedene Keywords verwendet")
print(f"  - Implizite zu explizite Verankerung: {(len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)) / max(len(code_1_1_relevant), 1):.1f}:1")
print()
