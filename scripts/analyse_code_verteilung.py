"""
TRACE-Equity Analyse Script
Analyse 1: Code-Verteilungs-Analyse (Quantitativ)

Verwendung:
    python analyse_code_verteilung.py west
    python analyse_code_verteilung.py mitte
    python analyse_code_verteilung.py suedost
    python analyse_code_verteilung.py --alle
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
from utils import (load_cluster, relevante, nicht_relevante, setup_plots,
                   output_dir, FARBEN_LISTE, CLUSTER_NAMEN, CLUSTER_PATHS,
                   ERGEBNISSE_DIR)


def analyse_cluster(cluster_name):
    """Führt die komplette Code-Verteilungs-Analyse für einen Cluster durch."""

    vis_dir = output_dir(cluster_name)
    report_file = ERGEBNISSE_DIR / f'cluster_{cluster_name}' / 'analyse_code_verteilung.md'
    label = CLUSTER_NAMEN[cluster_name]

    print("=" * 80)
    print(f"TRACE-EQUITY ANALYSE 1: CODE-VERTEILUNGS-ANALYSE")
    print(f"{label}")
    print("=" * 80)
    print()

    # Lade Daten
    print("Lade Daten...")
    df = load_cluster(cluster_name)
    print(f"[OK] {len(df)} Findings geladen (alle validiert)")
    print()

    # ==================================================================
    # 1. GRUNDLEGENDE STATISTIKEN
    # ==================================================================

    print("Berechne Statistiken...")

    code_counts_all = df['confirmed_code'].value_counts()
    code_pct_all = (code_counts_all / len(df) * 100).round(1)

    relevant_df = relevante(df)
    code_counts_relevant = relevant_df['confirmed_code'].value_counts()
    code_pct_relevant = (code_counts_relevant / len(relevant_df) * 100).round(1)

    not_relevant_df = nicht_relevante(df)
    code_counts_not_relevant = not_relevant_df['confirmed_code'].value_counts()

    relevanz_ratio = {}
    for code in code_counts_all.index:
        total = code_counts_all[code]
        rel = code_counts_relevant.get(code, 0)
        ratio = (rel / total * 100) if total > 0 else 0
        relevanz_ratio[code] = ratio

    # ==================================================================
    # 2. VISUALISIERUNG 1: CODE-VERTEILUNG (ALLE FINDINGS)
    # ==================================================================

    print("Erstelle Visualisierung 1: Code-Verteilung (alle Findings)...")

    fig, ax = plt.subplots(figsize=(14, 8))
    bars = ax.barh(range(len(code_counts_all)), code_counts_all.values,
                   color=FARBEN_LISTE[:len(code_counts_all)])
    ax.set_yticks(range(len(code_counts_all)))
    ax.set_yticklabels([c.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                        for c in code_counts_all.index])
    ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
    ax.set_title(f'Code-Verteilung: {label}\n(Alle {len(df)} validierten Findings)',
                 fontsize=14, fontweight='bold', pad=20)

    for bar, count, pct in zip(bars, code_counts_all.values, code_pct_all.values):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                f'{count} ({pct}%)', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{vis_dir}/01_code_verteilung_alle.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [OK] Gespeichert: {vis_dir}/01_code_verteilung_alle.png")

    # ==================================================================
    # 3. VISUALISIERUNG 2: CODE-VERTEILUNG (NUR RELEVANTE)
    # ==================================================================

    print("Erstelle Visualisierung 2: Code-Verteilung (nur relevante Findings)...")

    fig, ax = plt.subplots(figsize=(14, 8))
    bars = ax.barh(range(len(code_counts_relevant)), code_counts_relevant.values,
                   color=FARBEN_LISTE[:len(code_counts_relevant)])
    ax.set_yticks(range(len(code_counts_relevant)))
    ax.set_yticklabels([c.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                        for c in code_counts_relevant.index])
    ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
    ax.set_title(f'Code-Verteilung: {label}\n(Nur relevante Findings: n={len(relevant_df)})',
                 fontsize=14, fontweight='bold', pad=20)

    for bar, count, pct in zip(bars, code_counts_relevant.values, code_pct_relevant.values):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                f'{count} ({pct}%)', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{vis_dir}/02_code_verteilung_relevant.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [OK] Gespeichert: {vis_dir}/02_code_verteilung_relevant.png")

    # ==================================================================
    # 4. VISUALISIERUNG 3: RELEVANZ-RATIO (PIE CHART)
    # ==================================================================

    print("Erstelle Visualisierung 3: Relevanz-Ratio...")

    fig, ax = plt.subplots(figsize=(10, 8))
    sizes = [len(relevant_df), len(not_relevant_df)]
    labels = [f'Relevant (ja)\n{len(relevant_df)} Findings\n({len(relevant_df)/len(df)*100:.1f}%)',
              f'Nicht relevant (nein)\n{len(not_relevant_df)} Findings\n({len(not_relevant_df)/len(df)*100:.1f}%)']
    colors_pie = ['#2ecc71', '#e74c3c']

    ax.pie(sizes, explode=(0.05, 0), labels=labels, colors=colors_pie,
           autopct='%1.1f%%', shadow=True, startangle=90,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax.set_title(f'Relevanz-Verteilung: {label}',
                 fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(f'{vis_dir}/03_relevanz_ratio.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [OK] Gespeichert: {vis_dir}/03_relevanz_ratio.png")

    # ==================================================================
    # 5. VISUALISIERUNG 4: TOP KEYWORDS
    # ==================================================================

    print("Erstelle Visualisierung 4: Top 15 Keywords...")

    keyword_counts = df['keyword'].value_counts().head(15)

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(range(len(keyword_counts)), keyword_counts.values, color='#3498db')
    ax.set_yticks(range(len(keyword_counts)))
    ax.set_yticklabels([kw.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
                        for kw in keyword_counts.index])
    ax.set_xlabel('Anzahl Findings', fontsize=12, fontweight='bold')
    ax.set_title(f'Top 15 Keywords: {label}',
                 fontsize=14, fontweight='bold', pad=20)

    for bar, count in zip(bars, keyword_counts.values):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                str(count), va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{vis_dir}/04_top_keywords.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  [OK] Gespeichert: {vis_dir}/04_top_keywords.png")

    # ==================================================================
    # 6. MARKDOWN-REPORT
    # ==================================================================

    print()
    print("Erstelle Markdown-Report...")

    report = f"""# TRACE-Equity Analyse 1: Code-Verteilungs-Analyse

**Curriculum:** {label}
**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** {len(df)} validierte Findings

---

## 1. Übersicht

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

## 4. Top 15 Keywords

| Rank | Keyword | Anzahl |
|------|---------|--------|
"""

    for i, (keyword, count) in enumerate(keyword_counts.items(), 1):
        report += f"| {i} | {keyword} | {count} |\n"

    report += """
---

## 5. Visualisierungen

1. `01_code_verteilung_alle.png` — Code-Verteilung (alle Findings)
2. `02_code_verteilung_relevant.png` — Code-Verteilung (nur relevante)
3. `03_relevanz_ratio.png` — Relevanz-Verteilung (Pie Chart)
4. `04_top_keywords.png` — Top 15 Keywords

---

**Erstellt mit:** Python (pandas, matplotlib, seaborn)
**Methodik:** Qualitative Content Analysis (QCA) + Critical Expert in the Loop (CEiL)
"""

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"  [OK] Report gespeichert: {report_file}")
    print()
    print(f"Zentrale Befunde:")
    print(f"  - {len(df)} validierte Findings")
    print(f"  - {len(relevant_df)} relevant ({len(relevant_df)/len(df)*100:.1f}%)")
    print()


# ======================================================================
# MAIN
# ======================================================================

if __name__ == '__main__':
    setup_plots()

    if len(sys.argv) < 2:
        print("Verwendung:")
        print("  python analyse_code_verteilung.py west")
        print("  python analyse_code_verteilung.py mitte")
        print("  python analyse_code_verteilung.py suedost")
        print("  python analyse_code_verteilung.py --alle")
        sys.exit(1)

    if sys.argv[1] == '--alle':
        for name in CLUSTER_PATHS:
            analyse_cluster(name)
    elif sys.argv[1] in CLUSTER_PATHS:
        analyse_cluster(sys.argv[1])
    else:
        print(f"Unbekannter Cluster: '{sys.argv[1]}'")
        print(f"Verfügbar: {', '.join(CLUSTER_PATHS.keys())}, --alle")
        sys.exit(1)
