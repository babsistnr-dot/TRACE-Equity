"""
TRACE-Equity Analyse Script
Analyse 3: Levinson-Mapping — Konzeptuelle Tiefe (Dimension 2)

Beantwortet Dimension 2 der Forschungsfrage:
  "Welches Gerechtigkeitsverständnis dominiert in den Curricula —
   formale Gleichheit, kompensatorische oder transformative Gerechtigkeit?"

Fokussiert auf die 3 Levinson-Stufen (Formale Gleichheit, Kompensatorische
Gerechtigkeit, Transformative Gerechtigkeit). Querschnittscodes (2.5, 2.7)
und Explizite Nennung (1.1) werden transparent ausgewiesen, aber aus der
Hauptauswertung ausgeschlossen (orthogonal zur 3-Stufen-Typologie).

Verwendung:
    python analyse_levinson_mapping.py mitte
    python analyse_levinson_mapping.py fh_wien
    python analyse_levinson_mapping.py --alle
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import (load_cluster, load_all_clusters, relevante, add_levinson,
                   setup_plots, output_dir, CLUSTER_NAMEN, CLUSTER_PATHS,
                   ERGEBNISSE_DIR, LEVINSON_FARBEN)


# Die 3 Levinson-Stufen (orthogonale Kategorien werden separat behandelt)
DREI_STUFEN = [
    'Formale Gleichheit',
    'Kompensatorische Gerechtigkeit',
    'Transformative Gerechtigkeit',
]

# Kategorien, die nicht zu den 3 Stufen gehören (transparent ausweisen)
ORTHOGONAL = [
    'Explizite Nennung',
    'Querschnitt (Systemebene)',
    'Querschnitt (Professionalisierung)',
]


def berechne_verteilung(cluster_name):
    """Berechnet die Levinson-Verteilung für einen Cluster.

    Returns:
        dict mit: total, drei_stufen_df, orthogonal_df, verteilung (Series),
                  prozent (Series), abdeckung (float)
    """
    df = add_levinson(relevante(load_cluster(cluster_name)))
    total = len(df)

    drei_df = df[df['levinson'].isin(DREI_STUFEN)]
    ortho_df = df[df['levinson'].isin(ORTHOGONAL)]

    # Reindex stellt sicher, dass fehlende Stufen mit 0 erscheinen
    verteilung = drei_df['levinson'].value_counts().reindex(DREI_STUFEN, fill_value=0)

    n = len(drei_df)
    prozent = (verteilung / n * 100) if n > 0 else verteilung * 0.0

    return {
        'cluster': cluster_name,
        'label': CLUSTER_NAMEN[cluster_name],
        'total': total,
        'drei_df': drei_df,
        'ortho_df': ortho_df,
        'n_drei': n,
        'verteilung': verteilung,
        'prozent': prozent,
        'abdeckung': (n / total * 100) if total > 0 else 0.0,
    }


def stacked_bar_cluster(ergebnis):
    """Erstellt Stacked Bar Chart für einen einzelnen Cluster."""
    setup_plots()
    fig, ax = plt.subplots(figsize=(10, 3))

    left = 0
    for stufe in DREI_STUFEN:
        wert = ergebnis['prozent'][stufe]
        if wert > 0:
            ax.barh(0, wert, left=left, color=LEVINSON_FARBEN[stufe],
                    label=f'{stufe} ({wert:.1f}%)')
            if wert > 5:
                ax.text(left + wert / 2, 0, f'{wert:.1f}%',
                        ha='center', va='center', color='white',
                        fontweight='bold', fontsize=11)
            left += wert

    ax.set_xlim(0, 100)
    ax.set_ylim(-0.5, 0.5)
    ax.set_yticks([])
    ax.set_xlabel('Anteil (%)')
    ax.set_title(f'Levinson-Stufen: {ergebnis["label"]}\n'
                 f'(n = {ergebnis["n_drei"]} Findings, '
                 f'Abdeckung {ergebnis["abdeckung"]:.1f}% der relevanten Findings)')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=3, frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    out_path = output_dir(ergebnis['cluster']) / 'levinson_verteilung.png'
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    return out_path


def heatmap_vergleich(ergebnisse):
    """Erstellt die Kern-Heatmap: 3 Stufen × 4 Cluster."""
    setup_plots()

    # Matrix bauen: Zeilen = Stufen, Spalten = Cluster
    data = {e['label']: [e['prozent'][s] for s in DREI_STUFEN] for e in ergebnisse}
    df = pd.DataFrame(data, index=DREI_STUFEN)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(df, annot=True, fmt='.1f', cmap='YlOrRd',
                cbar_kws={'label': 'Anteil in %'},
                linewidths=0.5, linecolor='white',
                vmin=0, vmax=100, ax=ax)

    ax.set_title('Levinson-Stufen: Cluster-Vergleich (Dimension 2)\n'
                 'Prozentwerte normalisiert über die 3 Stufen pro Cluster',
                 pad=15)
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Abdeckungsraten als Untertitel
    abdeckungen = '   '.join(f"{e['label'].split(' (')[0]}: {e['abdeckung']:.1f}%"
                             for e in ergebnisse)
    fig.text(0.5, -0.02, f'Abdeckungsraten (3 Stufen / relevante Findings):\n{abdeckungen}',
             ha='center', fontsize=9, style='italic')

    plt.xticks(rotation=20, ha='right')
    plt.yticks(rotation=0)

    out_dir = ERGEBNISSE_DIR / 'visualisierungen_vergleich'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'levinson_heatmap.png'
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    return out_path


def grouped_bar_vergleich(ergebnisse):
    """Erstellt Grouped Bar Chart: 4 Cluster × 3 Stufen."""
    setup_plots()

    cluster_labels = [e['label'].split(' (')[0] for e in ergebnisse]
    data = {s: [e['prozent'][s] for e in ergebnisse] for s in DREI_STUFEN}
    df = pd.DataFrame(data, index=cluster_labels)

    fig, ax = plt.subplots(figsize=(12, 6))
    df.plot(kind='bar', ax=ax,
            color=[LEVINSON_FARBEN[s] for s in DREI_STUFEN],
            width=0.8)

    ax.set_title('Levinson-Stufen: Grouped Bar Vergleich')
    ax.set_ylabel('Anteil (%)')
    ax.set_xlabel('')
    ax.set_ylim(0, 100)
    ax.legend(title='Levinson-Stufe', loc='upper right', frameon=True)
    plt.xticks(rotation=0)
    ax.grid(axis='y', alpha=0.3)

    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', padding=3, fontsize=9)

    out_dir = ERGEBNISSE_DIR / 'visualisierungen_vergleich'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / 'levinson_grouped_bar.png'
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    return out_path


def cluster_report(ergebnis):
    """Schreibt den Markdown-Report für einen einzelnen Cluster."""
    e = ergebnis
    report_file = ERGEBNISSE_DIR / f'cluster_{e["cluster"]}' / 'analyse_levinson.md'

    # Dominante Stufe identifizieren
    if e['n_drei'] > 0:
        dominant = e['prozent'].idxmax()
        dom_prozent = e['prozent'].max()
    else:
        dominant = None
        dom_prozent = 0

    # Orthogonale Aufschlüsselung
    ortho_counts = e['ortho_df']['levinson'].value_counts().reindex(ORTHOGONAL, fill_value=0)

    report = f"""# TRACE-Equity Analyse 3: Levinson-Mapping — {e['label']}

**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** {e['total']} relevante Findings

Diese Analyse beantwortet **Dimension 2** der Forschungsfrage: Welches
Gerechtigkeitsverständnis dominiert? Fokus auf die 3 Levinson-Stufen
(Formale Gleichheit, Kompensatorische Gerechtigkeit, Transformative
Gerechtigkeit). Orthogonale Kategorien (Querschnitt, Explizite Nennung)
werden separat ausgewiesen.

---

## 1. Hauptauswertung: 3 Levinson-Stufen

**Abdeckungsrate:** {e['abdeckung']:.1f}% der relevanten Findings
({e['n_drei']} von {e['total']}) fallen in die 3 Levinson-Stufen.

| Levinson-Stufe | Anzahl | Prozent (über 3 Stufen) |
|---|---:|---:|
"""
    for stufe in DREI_STUFEN:
        report += f"| {stufe} | {e['verteilung'][stufe]} | {e['prozent'][stufe]:.1f}% |\n"

    report += f"| **Summe** | **{e['n_drei']}** | **100,0%** |\n"

    report += f"""
---

## 2. Separate Ausweisung: Orthogonale Kategorien

Diese Kategorien gehören nicht zu den 3 Levinson-Stufen und wurden aus der
Hauptauswertung ausgeschlossen — werden aber transparent ausgewiesen.

| Kategorie | Anzahl | Anteil (von {e['total']}) |
|---|---:|---:|
"""
    for kat in ORTHOGONAL:
        anzahl = int(ortho_counts[kat])
        prozent = (anzahl / e['total'] * 100) if e['total'] > 0 else 0
        report += f"| {kat} | {anzahl} | {prozent:.1f}% |\n"

    # Prüfsumme
    pruefsumme = e['n_drei'] + int(ortho_counts.sum())
    report += f"| **Summe (3 Stufen + Orthogonal)** | **{pruefsumme}** | **{pruefsumme/e['total']*100:.1f}%** |\n"

    report += f"""
---

## 3. Interpretation

"""
    if dominant:
        report += f"""**Dominantes Gerechtigkeitsverständnis:** {dominant} ({dom_prozent:.1f}%)

"""
        # Narrative Interpretation
        formal = e['prozent']['Formale Gleichheit']
        komp = e['prozent']['Kompensatorische Gerechtigkeit']
        trans = e['prozent']['Transformative Gerechtigkeit']

        report += f"Von den {e['n_drei']} Findings, die den 3 Levinson-Stufen zugeordnet "
        report += f"wurden, entfallen **{formal:.1f}%** auf formale Gleichheit, "
        report += f"**{komp:.1f}%** auf kompensatorische Gerechtigkeit und nur "
        report += f"**{trans:.1f}%** auf transformative Gerechtigkeit.\n\n"

        if formal > 60:
            report += "Das Curriculum bleibt damit überwiegend auf der Ebene der **formalen "
            report += "Gleichheit** — Zugang, Nicht-Diskriminierung und Anerkennung von "
            report += "Heterogenität stehen im Vordergrund.\n\n"
        elif komp > formal:
            report += "Das Curriculum betont **kompensatorische Gerechtigkeit** stärker als "
            report += "formale Gleichheit — gezielte Förderung Benachteiligter nimmt eine "
            report += "prominente Rolle ein.\n\n"

        if trans < 10:
            report += f"**Transformative Gerechtigkeit** — die kritische Hinterfragung von "
            report += f"Machtstrukturen und systemischer Ungleichheit — ist mit {trans:.1f}% "
            report += f"deutlich unterrepräsentiert.\n"
    else:
        report += "*Keine Findings in den 3 Levinson-Stufen — Interpretation nicht möglich.*\n"

    report += f"""
---

## 4. Visualisierung

![Levinson-Verteilung]({e["cluster"]}/visualisierungen/levinson_verteilung.png)

*Datei:* `visualisierungen/levinson_verteilung.png`

---

**Erstellt mit:** Python (pandas, matplotlib, seaborn)
**Methodik:** Qualitative Content Analysis (QCA) + Levinson-Typologie (2022)
**Mapping-Quelle:** Exposé Tabelle 2 (in Anlehnung an Levinson et al., 2022)
"""

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    return report_file


def vergleich_report(ergebnisse):
    """Schreibt den Cross-Cluster-Vergleichsreport."""
    report_file = ERGEBNISSE_DIR / 'analyse_levinson_vergleich.md'

    report = f"""# TRACE-Equity: Levinson-Mapping — Cross-Cluster-Vergleich

**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** {sum(e['total'] for e in ergebnisse)} relevante Findings aus {len(ergebnisse)} Clustern
**Forschungsfrage D2:** Welches Gerechtigkeitsverständnis dominiert in den
Curricula — formale Gleichheit, kompensatorische oder transformative Gerechtigkeit?

---

## Konzeptuelle Einordnung

Diese Analyse fokussiert auf die **3 Levinson-Stufen** (Formale Gleichheit,
Kompensatorische Gerechtigkeit, Transformative Gerechtigkeit). Orthogonale
Kategorien (Querschnitt-Codes 2.5/2.7, Explizite Nennung 1.1) werden
transparent ausgewiesen, aber nicht in die Hauptauswertung einbezogen.
Prozentwerte sind jeweils normalisiert über die 3 Stufen pro Cluster.

---

## 1. Hauptauswertung: Prozentuale Verteilung (über 3 Stufen)

| Cluster | Formale Gleichheit | Kompensatorische Gerechtigkeit | Transformative Gerechtigkeit |
|---|---:|---:|---:|
"""
    for e in ergebnisse:
        name = e['label'].split(' (')[0]
        report += f"| {name} | {e['prozent']['Formale Gleichheit']:.1f}% | "
        report += f"{e['prozent']['Kompensatorische Gerechtigkeit']:.1f}% | "
        report += f"{e['prozent']['Transformative Gerechtigkeit']:.1f}% |\n"

    report += """
---

## 2. Absolute Zahlen (3 Levinson-Stufen)

| Cluster | Formale Gleichheit | Kompensatorische Gerechtigkeit | Transformative Gerechtigkeit | Summe |
|---|---:|---:|---:|---:|
"""
    for e in ergebnisse:
        name = e['label'].split(' (')[0]
        f_n = int(e['verteilung']['Formale Gleichheit'])
        k_n = int(e['verteilung']['Kompensatorische Gerechtigkeit'])
        t_n = int(e['verteilung']['Transformative Gerechtigkeit'])
        report += f"| {name} | {f_n} | {k_n} | {t_n} | {f_n+k_n+t_n} |\n"

    report += """
---

## 3. Abdeckungsraten

Wie viel Prozent der relevanten Findings fallen in die 3 Levinson-Stufen?

| Cluster | Relevante Findings | In 3 Stufen | Abdeckungsrate | Orthogonal (Querschnitt + Explizit) |
|---|---:|---:|---:|---:|
"""
    for e in ergebnisse:
        name = e['label'].split(' (')[0]
        ortho_count = e['total'] - e['n_drei']
        report += f"| {name} | {e['total']} | {e['n_drei']} | {e['abdeckung']:.1f}% | {ortho_count} |\n"

    report += f"""
---

## 4. Kernvisualisierung: Heatmap

![Levinson-Heatmap](visualisierungen_vergleich/levinson_heatmap.png)

*Datei:* `visualisierungen_vergleich/levinson_heatmap.png`

Die Heatmap ist die **Kernvisualisierung** für den Forschungsbericht. Sie
zeigt auf einen Blick, welche Levinson-Stufe in welchem Cluster dominiert.

---

## 5. Ergänzende Visualisierung: Grouped Bar

![Grouped Bar](visualisierungen_vergleich/levinson_grouped_bar.png)

*Datei:* `visualisierungen_vergleich/levinson_grouped_bar.png`

---

## 6. Interpretation

"""
    # Dominante Stufe pro Cluster bestimmen
    for e in ergebnisse:
        dom = e['prozent'].idxmax()
        dom_p = e['prozent'].max()
        report += f"- **{e['label']}:** dominant ist *{dom}* ({dom_p:.1f}%)\n"

    # Gesamtbefund
    report += f"""
### Befund D2

Über alle 4 Cluster hinweg dominiert die **formale Gleichheit**. Die
curriculare Verankerung bleibt damit überwiegend auf der niedrigsten
Levinson-Stufe: Zugang, Nicht-Diskriminierung und Anerkennung von
Heterogenität stehen im Vordergrund.

**Transformative Gerechtigkeit** — die kritische Hinterfragung von
Machtstrukturen — ist in allen Clustern deutlich unterrepräsentiert
(zwischen {min(e['prozent']['Transformative Gerechtigkeit'] for e in ergebnisse):.1f}%
und {max(e['prozent']['Transformative Gerechtigkeit'] for e in ergebnisse):.1f}%).

Die **Cluster-Unterschiede** sind der Gegenstand von Dimension 3
(Schritt 7). Auffällig bereits jetzt: Die Verteilungen variieren
substanziell zwischen den Clustern, was eine systematische Analyse
in Schritt 7 rechtfertigt.

---

**Erstellt mit:** Python (pandas, matplotlib, seaborn)
**Methodik:** Qualitative Content Analysis (QCA) + Levinson-Typologie (2022)
**Mapping-Quelle:** Exposé Tabelle 2 (in Anlehnung an Levinson et al., 2022)
"""

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    return report_file


def analyse_cluster(cluster_name):
    """Führt die Levinson-Analyse für einen einzelnen Cluster durch."""
    print(f"=== {CLUSTER_NAMEN[cluster_name]} ===")
    ergebnis = berechne_verteilung(cluster_name)
    print(f"  Relevante Findings: {ergebnis['total']}")
    print(f"  In 3 Stufen: {ergebnis['n_drei']} ({ergebnis['abdeckung']:.1f}% Abdeckung)")
    for stufe in DREI_STUFEN:
        print(f"    {stufe}: {ergebnis['verteilung'][stufe]} ({ergebnis['prozent'][stufe]:.1f}%)")

    png_path = stacked_bar_cluster(ergebnis)
    md_path = cluster_report(ergebnis)
    print(f"  [OK] PNG: {png_path.name}")
    print(f"  [OK] MD:  {md_path.name}")
    print()
    return ergebnis


# ======================================================================
# MAIN
# ======================================================================

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Verwendung:")
        print("  python analyse_levinson_mapping.py mitte")
        print("  python analyse_levinson_mapping.py fh_wien")
        print("  python analyse_levinson_mapping.py --alle")
        sys.exit(1)

    if sys.argv[1] == '--alle':
        ergebnisse = [analyse_cluster(name) for name in CLUSTER_PATHS]
        print("=== Cross-Cluster-Vergleich ===")
        heatmap_path = heatmap_vergleich(ergebnisse)
        grouped_path = grouped_bar_vergleich(ergebnisse)
        vergleich_path = vergleich_report(ergebnisse)
        print(f"  [OK] Heatmap:         {heatmap_path.name}")
        print(f"  [OK] Grouped Bar:     {grouped_path.name}")
        print(f"  [OK] Vergleichs-Doku: {vergleich_path.name}")
    elif sys.argv[1] in CLUSTER_PATHS:
        analyse_cluster(sys.argv[1])
    else:
        print(f"Unbekannter Cluster: '{sys.argv[1]}'")
        print(f"Verfügbar: {', '.join(CLUSTER_PATHS.keys())}, --alle")
        sys.exit(1)
