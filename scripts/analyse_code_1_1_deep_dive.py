"""
TRACE-Equity Analyse Script
Analyse 2: Code 1.1 "Direkte Nennung" - Qualitative Tiefenanalyse

Untersucht die explizite Verankerung von Chancengleichheit im Curriculum.
"""

import pandas as pd
from utils import load_cluster, ERGEBNISSE_DIR

# Konfiguration
CLUSTER = 'mitte'
REPORT_FILE = ERGEBNISSE_DIR / f'cluster_{CLUSTER}' / 'analyse_code_1_1_deep_dive.md'
ZITATE_FILE = ERGEBNISSE_DIR / f'cluster_{CLUSTER}' / 'zitate.md'

print("=" * 80)
print("TRACE-EQUITY ANALYSE 2: CODE 1.1 DEEP DIVE")
print("=" * 80)
print()

# Lade Daten
print("Lade Daten...")
df = load_cluster(CLUSTER)
print(f"[OK] {len(df)} Findings geladen")
print()

# ============================================================================
# 1. DATEN EXTRAHIEREN
# ============================================================================

print("Extrahiere Code 1.1 Findings...")

code_1_1_all = df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung']
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

kontexte = {
    'Normativ (Leitprinzip)': [],
    'Beschreibend (Modulinhalte)': [],
    'Kompetenzbezogen (Fähigkeiten)': [],
    'Organisatorisch (Strukturen)': []
}

for idx, row in code_1_1_relevant.iterrows():
    context_lower = row['context'].lower()

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
# 4. MARKDOWN-REPORT ERSTELLEN
# ============================================================================

print("Erstelle Markdown-Report...")

report = f"""# TRACE-Equity Analyse 2: Code 1.1 "Direkte Nennung" - Deep Dive

**Curriculum:** Cluster Mitte (OÖ, Linz, Salzburg)
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

## 3. Verwendungskontexte

"""

for kategorie, items in kontexte.items():
    if len(items) > 0:
        report += f"### {kategorie}\n\n"
        report += f"**Anzahl Findings:** {len(items)}\n\n"

report += f"""
---

## 4. Explizit vs. Implizit

**Code 1.1 (Direkte Nennung):** {len(code_1_1_relevant)} Findings
**Code 2.1–2.7 (Implizite Dimensionen):** {len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)} Findings

**Verhältnis Implizit zu Explizit:** {(len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)) / max(len(code_1_1_relevant), 1):.1f}:1

---

**Erstellt mit:** Python (pandas)
**Methodik:** Reflexive Thematic Analysis (RTA) + Critical Expert in the Loop (CEiL)
"""

with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"[OK] Report gespeichert: {REPORT_FILE}")
print()

# ============================================================================
# 5. ZITATE-SAMMLUNG ERSTELLEN
# ============================================================================

print("Erstelle Zitate-Sammlung...")

zitate = f"""# TRACE-Equity Analyse 2: Zitate-Sammlung (Code 1.1)

**Curriculum:** Cluster Mitte (OÖ, Linz, Salzburg)
**Code:** 1.1 Direkte Nennung
**Anzahl relevanter Findings:** {len(code_1_1_relevant)}

---

"""

for keyword in sorted(keyword_analysis.keys()):
    zitate += f"\n## Keyword: \"{keyword}\"\n\n"
    zitate += f"**Anzahl:** {keyword_analysis[keyword]['count']}\n\n"

    findings = code_1_1_relevant[code_1_1_relevant['keyword'] == keyword]

    for idx, row in findings.iterrows():
        context_clean = row['context'].replace('<strong style="background-color: #e74c3c; color: white; padding: 2px 4px; border-radius: 3px;">', '**')
        context_clean = context_clean.replace('</strong>', '**')

        zitate += f"### Seite {row['page']}\n\n"
        zitate += f"> {context_clean}\n\n"
        zitate += "---\n\n"

with open(ZITATE_FILE, 'w', encoding='utf-8') as f:
    f.write(zitate)

print(f"[OK] Zitate gespeichert: {ZITATE_FILE}")
print()

print("=" * 80)
print("ANALYSE 2 ABGESCHLOSSEN")
print("=" * 80)
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
