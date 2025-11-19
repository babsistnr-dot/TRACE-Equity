"""
TRACE-Equity Analyse Script
Analyse 1: Code-Verteilungs-Analyse (Quantitativ)

Erstellt deskriptive Statistiken und Visualisierungen zur Verteilung
der Chancengleichheits-Dimensionen im analysierten Curriculum.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

# Konfiguration
CSV_FILE = 'ergebnisse/TRACE_Equity_Export_20251118_173805_cleaned.csv'
OUTPUT_DIR = 'ergebnisse/analyse_1_visualisierungen'
REPORT_FILE = 'ergebnisse/analyse_1_code_verteilung.md'

# Erstelle Output-Ordner
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Setze Matplotlib auf nicht-interaktiv für Hintergrund-Rendering
plt.switch_backend('Agg')

# Style-Konfiguration
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

print("="*80)
print("TRACE-EQUITY ANALYSE 1: CODE-VERTEILUNGS-ANALYSE")
print("="*80)
print()

# Lade Daten
print("Lade Daten...")
df = pd.read_csv(CSV_FILE)
print(f"[OK] {len(df)} Findings geladen (alle validiert)")
print()

# ============================================================================
# 1. GRUNDLEGENDE STATISTIKEN
# ============================================================================

print("Berechne Statistiken...")

# Alle Findings
code_counts_all = df['code'].value_counts()
code_pct_all = (code_counts_all / len(df) * 100).round(1)

# Nur relevante Findings
relevant_df = df[df['relevant'] == 'ja']
code_counts_relevant = relevant_df['code'].value_counts()
code_pct_relevant = (code_counts_relevant / len(relevant_df) * 100).round(1)

# Nicht-relevante Findings
not_relevant_df = df[df['relevant'] == 'nein']
code_counts_not_relevant = not_relevant_df['code'].value_counts()

# Relevanz-Ratio pro Code
relevanz_ratio = {}
for code in code_counts_all.index:
    total = code_counts_all[code]
    relevant = code_counts_relevant.get(code, 0)
    ratio = (relevant / total * 100) if total > 0 else 0
    relevanz_ratio[code] = ratio

# ============================================================================
# 2. VISUALISIERUNG 1: CODE-VERTEILUNG (ALLE FINDINGS)
# ============================================================================

print("Erstelle Visualisierung 1: Code-Verteilung (alle Findings)...")

fig, ax = plt.subplots(figsize=(14, 8))
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c', '#e67e22', '#34495e']

bars = ax.barh(range(len(code_counts_all)), code_counts_all.values, color=colors)
ax.set_yticks(range(len(code_counts_all)))
ax.set_yticklabels([code.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                     for code in code_counts_all.index])
ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
ax.set_title('Code-Verteilung im Curriculum\n(Alle 516 validierten Findings)',
             fontsize=14, fontweight='bold', pad=20)

# Werte an Balken
for i, (bar, count, pct) in enumerate(zip(bars, code_counts_all.values, code_pct_all.values)):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'{count} ({pct}%)', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/01_code_verteilung_alle.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"  [OK] Gespeichert: {OUTPUT_DIR}/01_code_verteilung_alle.png")

# ============================================================================
# 3. VISUALISIERUNG 2: CODE-VERTEILUNG (NUR RELEVANTE)
# ============================================================================

print("Erstelle Visualisierung 2: Code-Verteilung (nur relevante Findings)...")

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(range(len(code_counts_relevant)), code_counts_relevant.values, color=colors)
ax.set_yticks(range(len(code_counts_relevant)))
ax.set_yticklabels([code.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                     for code in code_counts_relevant.index])
ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
ax.set_title('Code-Verteilung im Curriculum\n(Nur relevante Findings: n=259)',
             fontsize=14, fontweight='bold', pad=20)

for i, (bar, count, pct) in enumerate(zip(bars, code_counts_relevant.values, code_pct_relevant.values)):
    ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height()/2,
            f'{count} ({pct}%)', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/02_code_verteilung_relevant.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"  [OK] Gespeichert: {OUTPUT_DIR}/02_code_verteilung_relevant.png")

# ============================================================================
# 4. VISUALISIERUNG 3: RELEVANZ-RATIO (PIE CHART)
# ============================================================================

print("Erstelle Visualisierung 3: Relevanz-Ratio...")

fig, ax = plt.subplots(figsize=(10, 8))
sizes = [len(relevant_df), len(not_relevant_df)]
labels = [f'Relevant (ja)\n{len(relevant_df)} Findings\n({len(relevant_df)/len(df)*100:.1f}%)',
          f'Nicht relevant (nein)\n{len(not_relevant_df)} Findings\n({len(not_relevant_df)/len(df)*100:.1f}%)']
colors_pie = ['#2ecc71', '#e74c3c']
explode = (0.05, 0)

ax.pie(sizes, explode=explode, labels=labels, colors=colors_pie, autopct='%1.1f%%',
       shadow=True, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax.set_title('Relevanz-Verteilung der validierten Findings',
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/03_relevanz_ratio.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"  [OK] Gespeichert: {OUTPUT_DIR}/03_relevanz_ratio.png")

# ============================================================================
# 5. VISUALISIERUNG 4: TOP KEYWORDS
# ============================================================================

print("Erstelle Visualisierung 4: Top 15 Keywords...")

keyword_counts = df['keyword'].value_counts().head(15)

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(range(len(keyword_counts)), keyword_counts.values, color='#3498db')
ax.set_yticks(range(len(keyword_counts)))
ax.set_yticklabels([kw.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                     for kw in keyword_counts.index])
ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
ax.set_title('Top 15 häufigste Keywords im Curriculum',
             fontsize=14, fontweight='bold', pad=20)

for bar, count in zip(bars, keyword_counts.values):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            str(count), va='center', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/04_top_keywords.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"  [OK] Gespeichert: {OUTPUT_DIR}/04_top_keywords.png")

# ============================================================================
# 6. MARKDOWN-REPORT ERSTELLEN
# ============================================================================

print()
print("Erstelle Markdown-Report...")

report = f"""# TRACE-Equity Analyse 1: Code-Verteilungs-Analyse

**Curriculum:** Cluster Mitte_OÖ_Linz, Salzburg.pdf
**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** 516 validierte Findings (100% validiert, semantische Duplikate entfernt)

---

## 1. Übersicht

### Validierungsstatus
- **Total Findings:** {len(df)}
- **Relevante Findings:** {len(relevant_df)} ({len(relevant_df)/len(df)*100:.1f}%)
- **Nicht-relevante Findings:** {len(not_relevant_df)} ({len(not_relevant_df)/len(df)*100:.1f}%)

---

## 2. Code-Verteilung (alle Findings)

| Code | Anzahl | Prozent | Relevant | Nicht-relevant | Relevanz-Ratio |
|------|--------|---------|----------|----------------|----------------|
"""

for code in code_counts_all.index:
    total = code_counts_all[code]
    pct = code_pct_all[code]
    rel = code_counts_relevant.get(code, 0)
    not_rel = code_counts_not_relevant.get(code, 0)
    ratio = relevanz_ratio[code]
    report += f"| {code} | {total} | {pct}% | {rel} | {not_rel} | {ratio:.1f}% |\n"

report += f"""
**Interpretation:**

- **Größte Kategorie:** {code_counts_all.index[0]} ({code_counts_all.iloc[0]} Findings, {code_pct_all.iloc[0]}%)
- **Kleinste Kategorie:** {code_counts_all.index[-1]} ({code_counts_all.iloc[-1]} Findings, {code_pct_all.iloc[-1]}%)

---

## 3. Code-Verteilung (nur relevante Findings, n={len(relevant_df)})

| Code | Anzahl | Prozent |
|------|--------|---------|
"""

for code in code_counts_relevant.index:
    count = code_counts_relevant[code]
    pct = code_pct_relevant[code]
    report += f"| {code} | {count} | {pct}% |\n"

report += f"""
---

## 4. Top 15 Keywords (alle Findings)

| Rank | Keyword | Anzahl |
|------|---------|--------|
"""

for i, (keyword, count) in enumerate(keyword_counts.items(), 1):
    report += f"| {i} | {keyword} | {count} |\n"

report += """
---

## 5. Wissenschaftliche Interpretation

### 5.1 Schwerpunkte

**Dominanz von Code 2.1 (Diversität & Heterogenität):**
- Mit deutlichem Abstand die größte Kategorie
- Deutet auf starken Fokus auf Diversitäts-Diskurse im Curriculum hin
- Kritische Frage: Ist "Diversität" substanziell oder primär diskursiv verankert?

**Starke Präsenz von Code 2.7 (Professionelle Haltung & Ethik):**
- Zweitgrößte Kategorie
- Zeigt Fokus auf Reflexivität und professionelle Habitusbildung
- Verbindung zu Professionalisierungstheorien (Fröhlich-Gildhoff et al.)

### 5.2 Lücken und Unterrepräsentation

**Geringe Präsenz von Code 1.1 (Direkte Nennung):**
- Nur 8 Findings - Chancengleichheit wird selten EXPLIZIT benannt
- Latente vs. manifeste Verankerung im Curriculum
- Kritische bildungssoziologische Frage: Implizite = weniger verbindlich?

**Unterrepräsentation von Code 2.3 & 2.5:**
- Individuelle Förderung (31 Findings) und Bildungspartnerschaft (32 Findings)
- Mögliche Erklärung: Zu spezifische Keywords, oder tatsächliche curriculare Lücke?

### 5.3 Capability Approach Mapping

**Formale Chancengleichheit:**
- Primär in Code 2.1 (Diversität) - oft deskriptiv/anerkennend

**Kompensatorische Ansätze:**
- Code 2.3 (Individuelle Förderung) - unterrepräsentiert
- Code 2.2 (Inklusion) - moderate Präsenz

**Transformative Ansätze:**
- Code 2.4 (Abbau von Benachteiligung) - moderate Präsenz (37 Findings)
- Empowerment und strukturelle Veränderung weniger prominent

---

## 6. Visualisierungen

Siehe Ordner: `ergebnisse/analyse_1_visualisierungen/`

1. `01_code_verteilung_alle.png` - Code-Verteilung (alle Findings)
2. `02_code_verteilung_relevant.png` - Code-Verteilung (nur relevante)
3. `03_relevanz_ratio.png` - Relevanz-Verteilung (Pie Chart)
4. `04_top_keywords.png` - Top 15 Keywords

---

## 7. Methodenkritische Reflexion

### Relevanz-Ratio: 50.2%

**Interpretation:**
- Die Hälfte der automatisch gefundenen Keywords wurde als "nicht relevant" eingestuft
- Dies ist **methodisch wertvoll** für die Reflexion der KI-Assistenz (CEiL-Prinzip)
- Zeigt Notwendigkeit menschlicher Expert*innen-Validierung

**Mögliche Erklärungen für False Positives:**
- Kontextabhängigkeit: Keyword erscheint, aber Bedeutung passt nicht (z.B. "sozial" in "sozial-emotional")
- Überlappende Bedeutungen: Mehrere Keywords im gleichen Textabschnitt
- Zu breite Keywords: "sozial", "Haltung" sind semantisch weit gefasst

---

**Erstellt mit:** Python (pandas, matplotlib, seaborn)
**Methodik:** Qualitative Content Analysis (QCA) + Critical Expert in the Loop (CEiL)
"""

# Speichere Report
with open(REPORT_FILE, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"  [OK] Report gespeichert: {REPORT_FILE}")
print()

print("="*80)
print("ANALYSE 1 ABGESCHLOSSEN")
print("="*80)
print()
print("Outputs:")
print(f"  - Report: {REPORT_FILE}")
print(f"  - Visualisierungen: {OUTPUT_DIR}/")
print()
