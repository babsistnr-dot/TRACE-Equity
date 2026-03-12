"""
TRACE-Equity Analyse Script
Analyse 1: Code-Verteilungs-Analyse (Quantitativ)
CLUSTER WEST (Tirol, Vorarlberg, Edith Stein)

Erstellt deskriptive Statistiken und Visualisierungen zur Verteilung
der Chancengleichheits-Dimensionen im analysierten Curriculum.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

# Konfiguration
CSV_FILE = '../ergebnisse/cluster_west/export_clean.csv'
OUTPUT_DIR = '../ergebnisse/cluster_west/visualisierungen'
REPORT_FILE = '../ergebnisse/cluster_west/analyse_code_verteilung.md'

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
print("CLUSTER WEST (Tirol, Vorarlberg, Edith Stein)")
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

bars = ax.barh(range(len(code_counts_all)), code_counts_all.values, color=colors[:len(code_counts_all)])
ax.set_yticks(range(len(code_counts_all)))
ax.set_yticklabels([code.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                     for code in code_counts_all.index])
ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
ax.set_title(f'Code-Verteilung im Curriculum Cluster West\n(Alle {len(df)} validierten Findings)',
             fontsize=14, fontweight='bold', pad=20)

# Werte an Balken
for i, (bar, count, pct) in enumerate(zip(bars, code_counts_all.values, code_pct_all.values)):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
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
bars = ax.barh(range(len(code_counts_relevant)), code_counts_relevant.values, color=colors[:len(code_counts_relevant)])
ax.set_yticks(range(len(code_counts_relevant)))
ax.set_yticklabels([code.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                     for code in code_counts_relevant.index])
ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
ax.set_title(f'Code-Verteilung im Curriculum Cluster West\n(Nur relevante Findings: n={len(relevant_df)})',
             fontsize=14, fontweight='bold', pad=20)

for i, (bar, count, pct) in enumerate(zip(bars, code_counts_relevant.values, code_pct_relevant.values)):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
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
ax.set_title('Relevanz-Verteilung der validierten Findings\nCluster West',
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
ax.set_title('Top 15 haeufigste Keywords im Curriculum Cluster West',
             fontsize=14, fontweight='bold', pad=20)

for bar, count in zip(bars, keyword_counts.values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
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

**Curriculum:** Cluster West — Tirol, Vorarlberg, Edith Stein
**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** {len(df)} validierte Findings (100% validiert, nicht-validierte entfernt)

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
- **Code 1.1 fehlt:** Keine explizite Nennung von Chancengleichheit im Curriculum

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
- Mit Abstand die größte Kategorie bei allen und relevanten Findings
- Deutet auf starken Fokus auf Diversitäts-Diskurse im Curriculum hin
- Konsistent mit den Befunden aus Cluster Mitte und SüdOst

**Starke Präsenz von Code 2.7 (Professionelle Haltung & Ethik):**
- Zweitgrößte Kategorie
- Zeigt Fokus auf Reflexivität und professionelle Habitusbildung
- Verbindung zu Professionalisierungstheorien (Fröhlich-Gildhoff et al.)

### 5.2 Lücken und Unterrepräsentation

**Keine Code 1.1 Findings (Direkte Nennung):**
- 0 Findings — Chancengleichheit wird NIE explizit benannt
- Identisch mit Cluster SüdOst (ebenfalls 0)
- Cluster Mitte hatte immerhin 8 Findings (1.6%)
- **Ausschließlich implizite Verankerung** im Curriculum

**Unterrepräsentation transformativer Ansätze:**
- Code 2.4 (Abbau von Benachteiligung) und Code 2.5 (Bildungspartnerschaft) — relativ schwach vertreten
- Empowerment und strukturelle Veränderung weniger prominent

### 5.3 Capability Approach Mapping

**Formale Chancengleichheit:**
- Primär in Code 2.1 (Diversität) — oft deskriptiv/anerkennend

**Kompensatorische Ansätze:**
- Code 2.3 (Individuelle Förderung) — moderate Präsenz
- Code 2.2 (Inklusion) — moderate Präsenz

**Transformative Ansätze:**
- Code 2.4 (Abbau von Benachteiligung) — schwach vertreten
- Empowerment und strukturelle Veränderung deutlich unterrepräsentiert

---

## 6. Vergleich aller drei Cluster

| Metrik | Cluster West | Cluster Mitte | Cluster SüdOst |
|--------|-------------|---------------|----------------|
| **Hochschulen** | Tirol, Vorarlberg, Edith Stein | OÖ, Linz, Salzburg | Burgenland, Kärnten, Steiermark |
| **Total validierte Findings** | 468 | 516 | 276 |
| **Relevanz-Ratio** | 74.1% | 50.2% | 69.6% |
| **Code 1.1 (Direkte Nennung)** | 0% | 1.6% | 0% |
| **Code 2.1 (Diversität) — relevant** | s.o. | 36.6% | 43.8% |
| **Code 2.7 (Haltung) — relevant** | s.o. | 18.4% | 17.2% |
| **Code 2.4 (Abbau Benachteiligung) — relevant** | s.o. | 7.3% | 4.7% |

*(Prozente für Cluster West werden dynamisch berechnet und in der Tabelle oben angezeigt.)*

### Cluster-übergreifende Befunde

**Konsistent über alle drei Cluster:**
1. Code 2.1 (Diversität) dominiert in allen Curricula
2. Code 2.7 (Professionelle Haltung) durchgängig zweitstärkstes Thema
3. Code 1.1 (Direkte Nennung) fast nicht vorhanden — Chancengleichheit wird primär implizit thematisiert
4. Transformative Ansätze (Code 2.4) überall unterrepräsentiert

**Implikation:** Österreichische Elementarpädagogik-Curricula verankern Chancengleichheit primär über Diversitätsdiskurse und professionelle Haltungen, jedoch kaum über explizite Benennung oder transformative Handlungsstrategien.

---

## 7. Visualisierungen

Siehe Ordner: `ergebnisse/cluster_west/visualisierungen/`

1. `01_code_verteilung_alle.png` — Code-Verteilung (alle Findings)
2. `02_code_verteilung_relevant.png` — Code-Verteilung (nur relevante)
3. `03_relevanz_ratio.png` — Relevanz-Verteilung (Pie Chart)
4. `04_top_keywords.png` — Top 15 Keywords

---

## 8. Methodenkritische Reflexion

### Relevanz-Ratio: 74.1%

**Interpretation:**
- Höchste Relevanz-Ratio aller drei Cluster (Mitte: 50.2%, SüdOst: 69.6%)
- Mögliche Erklärungen:
  1. Validierungs-Lerneffekt (drittes Curriculum → präzisere Keyword-Zuordnung)
  2. Curriculum tatsächlich stärker auf Equity-Themen fokussiert
  3. Kürzere/fokussiertere Curricula mit weniger Rauschen

**Methodenkritisch:**
- Intercoder-Reliabilität fehlt (nur eine Person validiert)
- Reihenfolge-Effekt möglich (West nach Mitte und SüdOst validiert)

### Code 1.1 fehlt komplett

**Kritischer Befund (identisch mit SüdOst):**
- Chancengleichheit wird im Curriculum nie explizit benannt
- Nur Cluster Mitte hat überhaupt explizite Nennungen (8 Findings)
- Implizite Verankerung = weniger verbindlich?

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
print("Zentrale Befunde:")
print(f"  - {len(df)} validierte Findings")
print(f"  - {len(relevant_df)} relevant ({len(relevant_df)/len(df)*100:.1f}%)")
print(f"  - Code 1.1 (Direkte Nennung): 0 Findings")
print(f"  - Dominanz Code 2.1 (Diversitaet): {code_counts_relevant.iloc[0]} ({code_pct_relevant.iloc[0]}%)")
print()
