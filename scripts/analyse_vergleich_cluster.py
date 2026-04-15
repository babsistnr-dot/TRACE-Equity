"""
TRACE-Equity Analyse Script
Analyse 3: Cross-Cluster-Vergleich (Dimension 3)

Beantwortet Forschungsdimension 3:
  "Gibt es systematische Unterschiede zwischen den vier Clustern?"

Vergleich erfolgt auf Code-Ebene (8 Codes × 4 Cluster), getrennt nach
Cluster, nur relevante Findings (relevant == 'ja').

Verwendung:
    python analyse_vergleich_cluster.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from utils import (
    load_cluster, relevante, setup_plots,
    CLUSTER_PATHS, CLUSTER_NAMEN, ERGEBNISSE_DIR,
)

# Reihenfolge für Tabellen und Grafiken
CODE_REIHENFOLGE = [
    'Code 1.1: Direkte Nennung',
    'Code 2.1: Diversität & Heterogenität',
    'Code 2.2: Inklusion & Partizipation',
    'Code 2.3: Individuelle Förderung & Differenzierung',
    'Code 2.4: Abbau von Benachteiligung & Diskriminierung',
    'Code 2.5: Bildungspartnerschaft & Sozialraumorientierung',
    'Code 2.6: Sprachliche Bildung & Mehrsprachigkeit',
    'Code 2.7: Professionelle Haltung & Ethik',
]

CODE_KURZ = {
    'Code 1.1: Direkte Nennung': 'Code 1.1',
    'Code 2.1: Diversität & Heterogenität': 'Code 2.1',
    'Code 2.2: Inklusion & Partizipation': 'Code 2.2',
    'Code 2.3: Individuelle Förderung & Differenzierung': 'Code 2.3',
    'Code 2.4: Abbau von Benachteiligung & Diskriminierung': 'Code 2.4',
    'Code 2.5: Bildungspartnerschaft & Sozialraumorientierung': 'Code 2.5',
    'Code 2.6: Sprachliche Bildung & Mehrsprachigkeit': 'Code 2.6',
    'Code 2.7: Professionelle Haltung & Ethik': 'Code 2.7',
}

CLUSTER_REIHENFOLGE = ['west', 'mitte', 'suedost', 'fh_wien']
CLUSTER_KURZ = {
    'west': 'West',
    'mitte': 'Mitte',
    'suedost': 'SüdOst',
    'fh_wien': 'FH Wien',
}

# Eine Farbe pro Cluster für Grouped Bar
CLUSTER_FARBEN = {
    'west':    '#3498db',
    'mitte':   '#2ecc71',
    'suedost': '#f39c12',
    'fh_wien': '#9b59b6',
}


def sammle_daten():
    """Lädt alle 4 Cluster und gibt eine Auswertungs-Struktur zurück."""
    summary_rows = []
    abs_matrix = {}   # {cluster: {code: n}}
    pct_matrix = {}   # {cluster: {code: %}}
    total_abs = {code: 0 for code in CODE_REIHENFOLGE}

    gesamt_findings = 0
    gesamt_relevant = 0
    gesamt_code_1_1 = 0

    for name in CLUSTER_REIHENFOLGE:
        df = load_cluster(name)
        rel = relevante(df)
        n_rel = len(rel)
        vc = rel['confirmed_code'].value_counts().to_dict()
        abs_matrix[name] = {code: vc.get(code, 0) for code in CODE_REIHENFOLGE}
        pct_matrix[name] = {
            code: (abs_matrix[name][code] / n_rel * 100) if n_rel else 0.0
            for code in CODE_REIHENFOLGE
        }
        code_1_1 = abs_matrix[name]['Code 1.1: Direkte Nennung']

        summary_rows.append({
            'cluster': name,
            'label': CLUSTER_NAMEN[name],
            'findings': len(df),
            'relevant': n_rel,
            'rate': n_rel / len(df) * 100 if len(df) else 0.0,
            'code_1_1': code_1_1,
        })

        gesamt_findings += len(df)
        gesamt_relevant += n_rel
        gesamt_code_1_1 += code_1_1
        for code in CODE_REIHENFOLGE:
            total_abs[code] += abs_matrix[name][code]

    return {
        'summary': summary_rows,
        'abs': abs_matrix,
        'pct': pct_matrix,
        'total_abs': total_abs,
        'gesamt_findings': gesamt_findings,
        'gesamt_relevant': gesamt_relevant,
        'gesamt_code_1_1': gesamt_code_1_1,
    }


def grouped_bar(data, out_path):
    """Grouped Bar: 8 Codes auf X, je 4 Balken pro Cluster."""
    codes = [CODE_KURZ[c] for c in CODE_REIHENFOLGE]
    x = np.arange(len(codes))
    width = 0.2

    fig, ax = plt.subplots(figsize=(14, 7))
    for i, name in enumerate(CLUSTER_REIHENFOLGE):
        werte = [data['pct'][name][code] for code in CODE_REIHENFOLGE]
        ax.bar(x + (i - 1.5) * width, werte, width,
               label=CLUSTER_KURZ[name], color=CLUSTER_FARBEN[name])

    ax.set_ylabel('Anteil an relevanten Findings (%)')
    ax.set_title('Code-Verteilung je Cluster (nur relevante Findings, normalisiert)')
    ax.set_xticks(x)
    ax.set_xticklabels(codes, rotation=0)
    ax.legend(title='Cluster')
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  [OK] Grouped Bar: {out_path.name}")


def heatmap(data, out_path):
    """Heatmap: 8 Codes × 4 Cluster, prozentual."""
    matrix = []
    for code in CODE_REIHENFOLGE:
        matrix.append([data['pct'][c][code] for c in CLUSTER_REIHENFOLGE])
    df = pd.DataFrame(
        matrix,
        index=[CODE_KURZ[c] for c in CODE_REIHENFOLGE],
        columns=[CLUSTER_KURZ[c] for c in CLUSTER_REIHENFOLGE],
    )

    fig, ax = plt.subplots(figsize=(9, 7))
    sns.heatmap(df, annot=True, fmt='.1f', cmap='YlOrRd', ax=ax,
                cbar_kws={'label': 'Anteil (%)'})
    ax.set_title('Code-Verteilung: 8 Codes × 4 Cluster\n(nur relevante Findings, normalisiert pro Cluster)')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  [OK] Heatmap:     {out_path.name}")


def schreibe_report(data, out_path):
    """Erzeugt den Cross-Cluster-Vergleichs-Report als Markdown."""
    lines = []
    lines.append('# Cross-Cluster-Vergleich (Dimension 3)')
    lines.append('')
    lines.append('**Forschungsfrage:** Gibt es systematische Unterschiede '
                 'zwischen den vier Clustern?')
    lines.append('')
    lines.append('Basis: Nur relevante Findings (`relevant == \'ja\'`, '
                 'Spalte `confirmed_code`). Alle Cluster getrennt ausgewiesen.')
    lines.append('')

    # Summary-Tabelle
    lines.append('## 1. Summary-Tabelle')
    lines.append('')
    lines.append('| Cluster | Findings gesamt | Relevant | Relevanzrate | Code 1.1 |')
    lines.append('|---|---:|---:|---:|---:|')
    for row in data['summary']:
        lines.append(
            f"| {CLUSTER_KURZ[row['cluster']]} | {row['findings']} | "
            f"{row['relevant']} | {row['rate']:.1f}% | {row['code_1_1']} |"
        )
    rate_gesamt = data['gesamt_relevant'] / data['gesamt_findings'] * 100
    lines.append(
        f"| **Alle** | **{data['gesamt_findings']}** | "
        f"**{data['gesamt_relevant']}** | **{rate_gesamt:.1f}%** | "
        f"**{data['gesamt_code_1_1']}** |"
    )
    lines.append('')

    # Tabelle A: Prozentual
    lines.append('## 2. Code-Verteilung — prozentual (je Cluster auf 100%)')
    lines.append('')
    header = '| Code | ' + ' | '.join(CLUSTER_KURZ[c] for c in CLUSTER_REIHENFOLGE) + ' |'
    sep = '|---|' + '---:|' * len(CLUSTER_REIHENFOLGE)
    lines.append(header)
    lines.append(sep)
    for code in CODE_REIHENFOLGE:
        werte = ' | '.join(f"{data['pct'][c][code]:.1f}%" for c in CLUSTER_REIHENFOLGE)
        lines.append(f"| {CODE_KURZ[code]} | {werte} |")
    lines.append('')

    # Tabelle B: Absolut
    lines.append('## 3. Code-Verteilung — absolut')
    lines.append('')
    lines.append(header)
    lines.append(sep)
    for code in CODE_REIHENFOLGE:
        werte = ' | '.join(str(data['abs'][c][code]) for c in CLUSTER_REIHENFOLGE)
        lines.append(f"| {CODE_KURZ[code]} | {werte} |")
    summe_zeile = ' | '.join(str(sum(data['abs'][c][code] for code in CODE_REIHENFOLGE))
                             for c in CLUSTER_REIHENFOLGE)
    lines.append(f"| **Summe** | {summe_zeile} |")
    lines.append('')

    # Tabelle C: Spannweite
    lines.append('## 4. Spannweite je Code (Min/Max über die 4 Cluster)')
    lines.append('')
    lines.append('| Code | Min | Max | Differenz | Max-Cluster | Min-Cluster |')
    lines.append('|---|---:|---:|---:|---|---|')
    for code in CODE_REIHENFOLGE:
        werte = {c: data['pct'][c][code] for c in CLUSTER_REIHENFOLGE}
        min_c = min(werte, key=werte.get)
        max_c = max(werte, key=werte.get)
        diff = werte[max_c] - werte[min_c]
        lines.append(
            f"| {CODE_KURZ[code]} | {werte[min_c]:.1f}% | {werte[max_c]:.1f}% | "
            f"{diff:.1f} pp | {CLUSTER_KURZ[max_c]} | {CLUSTER_KURZ[min_c]} |"
        )
    lines.append('')

    # Interpretation
    lines.append('## 5. Interpretation')
    lines.append('')
    lines.append('### 5.1 Relevanzraten-Varianz')
    lines.append('')
    raten = {row['cluster']: row['rate'] for row in data['summary']}
    lines.append(
        f"Die Relevanzraten schwanken zwischen {min(raten.values()):.1f}% "
        f"({CLUSTER_KURZ[min(raten, key=raten.get)]}) und "
        f"{max(raten.values()):.1f}% ({CLUSTER_KURZ[max(raten, key=raten.get)]}). "
        "Diese Varianz ist methodisch relevant: Ein niedriger Wert deutet darauf "
        "hin, dass ein größerer Anteil der Keyword-Treffer im CEiL-Verfahren als "
        "nicht einschlägig bewertet wurde — z.B. weil Begriffe wie 'Entwicklung' "
        "oder 'Bildung' in generischen Kontexten auftreten, ohne Bezug zu "
        "Chancengerechtigkeit. Die Varianz ist kein inhaltlicher Befund über "
        "Chancengerechtigkeit, sondern ein Hinweis auf Unterschiede in der "
        "curricularen Sprache."
    )
    lines.append('')

    lines.append('### 5.2 Auffällige Code-Unterschiede zwischen Clustern')
    lines.append('')
    # Top-3 Spannweiten
    spannweiten = []
    for code in CODE_REIHENFOLGE:
        werte = {c: data['pct'][c][code] for c in CLUSTER_REIHENFOLGE}
        diff = max(werte.values()) - min(werte.values())
        spannweiten.append((code, diff, werte))
    spannweiten.sort(key=lambda t: t[1], reverse=True)
    lines.append('Die drei Codes mit der größten Spannweite zwischen den Clustern:')
    lines.append('')
    for code, diff, werte in spannweiten[:3]:
        hoch = max(werte, key=werte.get)
        tief = min(werte, key=werte.get)
        lines.append(
            f"- **{CODE_KURZ[code]}** (Spannweite {diff:.1f} Prozentpunkte): "
            f"{CLUSTER_KURZ[hoch]} {werte[hoch]:.1f}% vs. "
            f"{CLUSTER_KURZ[tief]} {werte[tief]:.1f}%."
        )
    lines.append('')

    lines.append('### 5.3 FH Wien im Vergleich zu den PH-Clustern')
    lines.append('')
    lines.append(
        "Die FH Campus Wien zeigt ein systematisch anderes Profil als die drei "
        "Pädagogischen Hochschulen: deutlich geringerer Anteil bei Code 2.1 "
        f"(Diversität & Heterogenität: {data['pct']['fh_wien']['Code 2.1: Diversität & Heterogenität']:.1f}% "
        f"vs. {data['pct']['west']['Code 2.1: Diversität & Heterogenität']:.1f}–"
        f"{data['pct']['suedost']['Code 2.1: Diversität & Heterogenität']:.1f}% bei den PHs), "
        "dafür deutlich höherer Anteil bei Code 2.3 (Individuelle Förderung: "
        f"{data['pct']['fh_wien']['Code 2.3: Individuelle Förderung & Differenzierung']:.1f}%) "
        "und Code 2.7 (Professionelle Haltung & Ethik: "
        f"{data['pct']['fh_wien']['Code 2.7: Professionelle Haltung & Ethik']:.1f}%). "
        "Dieses Muster ist konsistent mit dem Levinson-Befund aus Schritt 6, "
        "in dem die FH Wien den deutlichsten Anteil kompensatorischer "
        "Gerechtigkeit zeigte."
    )
    lines.append('')

    lines.append('### 5.4 Limitationen')
    lines.append('')
    lines.append(
        '- N=1 Institution pro Cluster — keine statistische Generalisierung möglich.\n'
        '- Keine Signifikanztests: Unterschiede sind deskriptiv, nicht inferentiell.\n'
        '- Relevanzraten variieren (siehe 5.1); der direkte Prozent-Vergleich '
        'gleicht diese Varianz durch Normalisierung aus, nivelliert aber '
        'unterschiedliche absolute Datenvolumina.'
    )
    lines.append('')

    lines.append('## 6. Visualisierungen')
    lines.append('')
    lines.append('- `visualisierungen_vergleich/code_verteilung_grouped_bar.png`')
    lines.append('- `visualisierungen_vergleich/code_verteilung_heatmap.png`')
    lines.append('')
    lines.append('Die Kernvisualisierung des Forschungsberichts bleibt die '
                 'Levinson-Heatmap aus Schritt 6; die hier erzeugten Grafiken '
                 'dienen dem Anhang und der Postersession.')
    lines.append('')

    out_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  [OK] Report:      {out_path.name}")


def main():
    setup_plots()
    print("=" * 80)
    print("TRACE-EQUITY ANALYSE 3: CROSS-CLUSTER-VERGLEICH (DIMENSION 3)")
    print("=" * 80)
    print()

    data = sammle_daten()

    # Übersichtlicher Konsolen-Output
    print("Summary:")
    for row in data['summary']:
        print(f"  {CLUSTER_KURZ[row['cluster']]:8s}: "
              f"{row['findings']:4d} Findings, {row['relevant']:4d} relevant "
              f"({row['rate']:.1f}%), Code 1.1: {row['code_1_1']}")
    print(f"  Gesamt  : {data['gesamt_findings']} Findings, "
          f"{data['gesamt_relevant']} relevant")
    print()

    viz_dir = ERGEBNISSE_DIR / 'visualisierungen_vergleich'
    viz_dir.mkdir(parents=True, exist_ok=True)

    grouped_bar(data, viz_dir / 'code_verteilung_grouped_bar.png')
    heatmap(data, viz_dir / 'code_verteilung_heatmap.png')

    schreibe_report(data, ERGEBNISSE_DIR / 'analyse_vergleich_cluster.md')

    print()
    print("Fertig.")


if __name__ == '__main__':
    main()
