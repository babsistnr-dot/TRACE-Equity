"""
TRACE-Equity Analyse Script
Schritt 8: Zitate-Sammlung pro Code pro Cluster

Sammelt repräsentative Textstellen (bis zu N pro Code) aus den validierten
relevanten Findings, für die Verwendung im Forschungsbericht und auf dem
Poster. HTML-Tags aus den Kontexten werden entfernt.

Verwendung:
    python zitate_sammlung.py            # alle Cluster
    python zitate_sammlung.py west       # einzelner Cluster
"""

import re
import sys
import pandas as pd

from utils import (
    load_cluster, relevante,
    CLUSTER_PATHS, CLUSTER_NAMEN, ERGEBNISSE_DIR,
)

# Maximale Anzahl Zitate pro Code pro Cluster
MAX_PRO_CODE = 5

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

TAG_RE = re.compile(r'<[^>]+>')
WS_RE = re.compile(r'\s+')


def clean_context(text):
    """Entfernt HTML-Tags und normalisiert Whitespace."""
    if not isinstance(text, str):
        return ''
    text = TAG_RE.sub('', text)
    text = WS_RE.sub(' ', text).strip()
    return text


def finde_zitate(df_rel, code, max_n=MAX_PRO_CODE):
    """Wählt die längsten / informativsten Zitate für einen Code aus."""
    subset = df_rel[df_rel['confirmed_code'] == code].copy()
    if subset.empty:
        return []
    subset['context_clean'] = subset['context'].apply(clean_context)
    # Längere Kontexte sind meist informativer; sortiere absteigend.
    subset['len'] = subset['context_clean'].str.len()
    subset = subset.sort_values('len', ascending=False).head(max_n)
    return subset[['page', 'keyword', 'context_clean', 'notes']].to_dict('records')


def report_fuer_cluster(name):
    """Erzeugt einen Zitate-Report für einen Cluster."""
    df = load_cluster(name)
    rel = relevante(df)

    lines = []
    lines.append(f'# Zitate-Sammlung: {CLUSTER_NAMEN[name]}')
    lines.append('')
    lines.append(f'Basis: {len(rel)} relevante Findings (`relevant == \'ja\'`, '
                 'Spalte `confirmed_code`). HTML-Tags aus den Kontexten '
                 'wurden entfernt. Pro Code bis zu '
                 f'{MAX_PRO_CODE} Zitate, sortiert nach Kontext-Länge '
                 '(informativere Textstellen zuerst).')
    lines.append('')

    for code in CODE_REIHENFOLGE:
        zitate = finde_zitate(rel, code)
        lines.append(f'## {code}')
        lines.append('')
        if not zitate:
            lines.append('_Keine relevanten Findings in diesem Code._')
            lines.append('')
            continue

        for i, z in enumerate(zitate, 1):
            seite = int(z['page']) if pd.notna(z['page']) else '–'
            keyword = z['keyword'] if isinstance(z['keyword'], str) else ''
            ctx = z['context_clean']
            lines.append(f'**Zitat {i}** (S. {seite}, Keyword: _{keyword}_)')
            lines.append('')
            lines.append(f'> {ctx}')
            lines.append('')
            if isinstance(z['notes'], str) and z['notes'].strip():
                lines.append(f'*Anmerkung Codierung:* {z["notes"].strip()}')
                lines.append('')

    out_path = ERGEBNISSE_DIR / f'cluster_{name}' / 'zitate.md'
    out_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"  [OK] {name:8s} -> {out_path.relative_to(ERGEBNISSE_DIR)}")


def main():
    print("=" * 80)
    print("TRACE-EQUITY SCHRITT 8: ZITATE-SAMMLUNG")
    print("=" * 80)
    print()

    if len(sys.argv) > 1:
        ziel = sys.argv[1]
        if ziel not in CLUSTER_PATHS:
            print(f"Unbekannter Cluster: {ziel}. Verfügbar: {list(CLUSTER_PATHS.keys())}")
            sys.exit(1)
        cluster_list = [ziel]
    else:
        cluster_list = list(CLUSTER_PATHS.keys())

    for name in cluster_list:
        report_fuer_cluster(name)

    print()
    print("Fertig.")


if __name__ == '__main__':
    main()
