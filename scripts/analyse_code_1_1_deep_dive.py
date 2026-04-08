"""
TRACE-Equity Analyse Script
Analyse 2: Code 1.1 "Direkte Nennung" - Qualitative Tiefenanalyse

Untersucht die explizite Verankerung von Chancengleichheit in den Curricula.
Beantwortet Dimension 1 der Forschungsfrage:
  "Erschöpft sich die curriculare Verankerung in expliziten Begriffsnennungen
   oder wird Chancengerechtigkeit über pädagogische Handlungskompetenzen
   operationalisiert?"

Verwendung:
    python analyse_code_1_1_deep_dive.py mitte
    python analyse_code_1_1_deep_dive.py fh_wien
    python analyse_code_1_1_deep_dive.py --alle
"""

import sys
import pandas as pd
from utils import (load_cluster, load_all_clusters, relevante, nicht_relevante,
                   output_dir, CLUSTER_NAMEN, CLUSTER_PATHS, ERGEBNISSE_DIR)


def analyse_cluster(cluster_name):
    """Führt die Code-1.1-Tiefenanalyse für einen einzelnen Cluster durch."""

    report_file = ERGEBNISSE_DIR / f'cluster_{cluster_name}' / 'analyse_code_1_1_deep_dive.md'
    label = CLUSTER_NAMEN[cluster_name]

    print("=" * 80)
    print(f"TRACE-EQUITY ANALYSE 2: CODE 1.1 DEEP DIVE")
    print(f"{label}")
    print("=" * 80)
    print()

    # Lade Daten
    print("Lade Daten...")
    df = load_cluster(cluster_name)
    relevant_df = relevante(df)
    print(f"[OK] {len(df)} Findings geladen, {len(relevant_df)} relevant")
    print()

    # ==================================================================
    # 1. CODE 1.1 FINDINGS EXTRAHIEREN
    # ==================================================================

    code_1_1_all = df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung']
    code_1_1_relevant = relevant_df[relevant_df['confirmed_code'] == 'Code 1.1: Direkte Nennung']
    implizit_count = len(relevant_df) - len(code_1_1_relevant)

    print(f"Code 1.1 Findings:")
    print(f"  - Total: {len(code_1_1_all)}")
    print(f"  - Relevant: {len(code_1_1_relevant)}")
    print(f"  - Implizite Findings (Code 2.x): {implizit_count}")

    if len(code_1_1_relevant) > 0:
        ratio = f"{implizit_count / len(code_1_1_relevant):.0f}:1"
    else:
        ratio = "nur implizit (kein einziges Code-1.1-Finding)"

    print(f"  - Verhältnis implizit:explizit: {ratio}")
    print()

    # ==================================================================
    # 2. KEYWORD-ANALYSE (nur wenn Findings vorhanden)
    # ==================================================================

    keyword_analysis = {}
    if len(code_1_1_relevant) > 0:
        print("Analysiere Keywords...")
        for keyword in code_1_1_relevant['keyword'].unique():
            findings = code_1_1_relevant[code_1_1_relevant['keyword'] == keyword]
            keyword_analysis[keyword] = {
                'count': len(findings),
                'pages': sorted(int(p) for p in findings['page'].unique().tolist()),
                'contexts': findings['context'].tolist()
            }

        for kw, data in sorted(keyword_analysis.items(), key=lambda x: x[1]['count'], reverse=True):
            print(f"  - {kw}: {data['count']}x auf Seiten {data['pages']}")
        print()

    # ==================================================================
    # 3. KONTEXTANALYSE (nur wenn Findings vorhanden)
    # ==================================================================

    kontexte = {
        'Normativ (Leitprinzip)': [],
        'Beschreibend (Modulinhalte)': [],
        'Kompetenzbezogen (Fähigkeiten)': [],
        'Organisatorisch (Strukturen)': []
    }

    if len(code_1_1_relevant) > 0:
        print("Analysiere Verwendungskontexte...")
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

        for kategorie, items in kontexte.items():
            if len(items) > 0:
                print(f"  - {kategorie}: {len(items)} Findings")
        print()

    # ==================================================================
    # 4. MARKDOWN-REPORT
    # ==================================================================

    print("Erstelle Report...")

    report = f"""# TRACE-Equity Analyse 2: Code 1.1 "Direkte Nennung" — Deep Dive

**Curriculum:** {label}
**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** {len(df)} validierte Findings, davon {len(relevant_df)} relevant

---

## 1. Übersicht

**Code 1.1 — Direkte Nennung** erfasst die explizite Nennung von Begriffen wie
"Chancengleichheit", "Chancengerechtigkeit", "Bildungsgerechtigkeit" oder "Equity"
im Curriculum.

| Kennzahl | Wert |
|---|---|
| Findings gesamt | {len(df)} |
| Relevante Findings | {len(relevant_df)} |
| Code 1.1 (explizit) | {len(code_1_1_relevant)} |
| Code 2.x (implizit) | {implizit_count} |
| Verhältnis implizit:explizit | {ratio} |
"""

    if len(code_1_1_relevant) > 0:
        # Relevanz-Ratio
        if len(code_1_1_all) > 0:
            relevanz_ratio = f"{len(code_1_1_relevant) / len(code_1_1_all) * 100:.1f}%"
        else:
            relevanz_ratio = "—"

        report += f"""
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
                report += f"**Anzahl:** {len(items)} Findings\n\n"

        report += f"""
---

## 4. Zitate

"""
        for keyword in sorted(keyword_analysis.keys()):
            report += f"### Keyword: \"{keyword}\"\n\n"
            findings = code_1_1_relevant[code_1_1_relevant['keyword'] == keyword]
            for idx, row in findings.iterrows():
                context_clean = row['context'].replace(
                    '<strong style="background-color: #e74c3c; color: white; padding: 2px 4px; border-radius: 3px;">', '**'
                ).replace('</strong>', '**')
                report += f"**Seite {int(row['page'])}:**\n"
                report += f"> {context_clean}\n\n"

    else:
        report += f"""
---

## 2. Befund: Keine explizite Nennung

Im Curriculum von {label} wurde **kein einziger** expliziter Begriff für
Chancengleichheit oder Chancengerechtigkeit gefunden.

Das bedeutet nicht, dass das Thema fehlt — im Gegenteil: Es gibt
**{implizit_count} relevante Findings** in den impliziten Codes (2.1–2.7).
Die Verankerung erfolgt ausschließlich über pädagogische Handlungsfelder
wie Diversität, Inklusion, Sprachbildung etc., ohne das Konzept beim Namen
zu nennen.

Dies ist ein zentraler Befund für Dimension 1 der Forschungsfrage.
"""

    report += f"""
---

## Interpretation (Dimension 1)

{f"Mit {len(code_1_1_relevant)} expliziten Nennungen und {implizit_count} impliziten Findings (Verhältnis {ratio}) zeigt {label}, dass die curriculare Verankerung von Chancengerechtigkeit weit über bloße Begriffsnennungen hinausgeht." if len(code_1_1_relevant) > 0 else f"Die vollständige Abwesenheit expliziter Begriffsnennungen bei gleichzeitig {implizit_count} impliziten Findings zeigt: {label} verankert Chancengerechtigkeit ausschließlich über pädagogische Handlungskompetenzen, ohne das Konzept explizit zu benennen."}

---

**Erstellt mit:** Python (pandas)
**Methodik:** Qualitative Content Analysis (QCA) + Critical Expert in the Loop (CEiL)
"""

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"[OK] Report: {report_file}")
    print()
    return {
        'cluster': cluster_name,
        'label': label,
        'total': len(df),
        'relevant': len(relevant_df),
        'code_1_1': len(code_1_1_relevant),
        'implizit': implizit_count,
        'ratio': ratio,
        'keywords': keyword_analysis,
    }


def vergleichs_report(ergebnisse):
    """Erstellt den Cross-Cluster-Vergleichsreport für Code 1.1."""

    report_file = ERGEBNISSE_DIR / 'analyse_code_1_1_vergleich.md'

    gesamt_relevant = sum(e['relevant'] for e in ergebnisse)
    gesamt_c11 = sum(e['code_1_1'] for e in ergebnisse)
    gesamt_implizit = sum(e['implizit'] for e in ergebnisse)

    if gesamt_c11 > 0:
        gesamt_ratio = f"{gesamt_implizit / gesamt_c11:.0f}:1"
    else:
        gesamt_ratio = "nur implizit"

    report = f"""# TRACE-Equity: Code 1.1 — Cross-Cluster-Vergleich

**Analysedatum:** {pd.Timestamp.now().strftime('%d.%m.%Y')}
**Datenbasis:** {sum(e['total'] for e in ergebnisse)} validierte Findings aus {len(ergebnisse)} Clustern
**Forschungsfrage D1:** Erschöpft sich die curriculare Verankerung in expliziten
Begriffsnennungen oder wird Chancengerechtigkeit über pädagogische
Handlungskompetenzen operationalisiert?

---

## 1. Übersicht: Explizit vs. Implizit

| Cluster | Relevante Findings | Code 1.1 (explizit) | Code 2.x (implizit) | Verhältnis |
|---|---|---|---|---|
"""
    for e in ergebnisse:
        report += f"| {e['label']} | {e['relevant']} | {e['code_1_1']} | {e['implizit']} | {e['ratio']} |\n"

    report += f"| **Gesamt** | **{gesamt_relevant}** | **{gesamt_c11}** | **{gesamt_implizit}** | **{gesamt_ratio}** |\n"

    report += f"""
---

## 2. Zentrale Befunde

### Befund 1: Marginale explizite Verankerung

Von **{gesamt_relevant}** relevanten Findings über alle 4 Cluster hinweg enthalten
nur **{gesamt_c11} ({gesamt_c11/gesamt_relevant*100:.1f}%)** eine explizite Nennung von
Chancengleichheit oder verwandten Begriffen (Code 1.1). Das Verhältnis von
impliziter zu expliziter Verankerung beträgt **{gesamt_ratio}**.

### Befund 2: Cluster-Unterschiede

"""
    # Cluster mit Findings
    mit_c11 = [e for e in ergebnisse if e['code_1_1'] > 0]
    ohne_c11 = [e for e in ergebnisse if e['code_1_1'] == 0]

    if ohne_c11:
        namen = " und ".join(e['label'] for e in ohne_c11)
        report += f"- **{len(ohne_c11)} von {len(ergebnisse)} Clustern** ({namen}) enthalten "
        report += f"**keine einzige** explizite Begriffnennung — trotz substanzieller impliziter Verankerung "
        implizit_str = ', '.join(str(e['implizit']) + ' Findings' for e in ohne_c11)
        report += f"({implizit_str}).\n"

    if mit_c11:
        for e in mit_c11:
            report += f"- **{e['label']}** hat {e['code_1_1']} explizite Nennungen "
            report += f"(Verhältnis {e['ratio']})"
            if e['keywords']:
                kws = ', '.join(f'"{kw}" ({d["count"]}x)' for kw, d in
                                sorted(e['keywords'].items(), key=lambda x: x[1]['count'], reverse=True))
                report += f": {kws}"
            report += ".\n"

    report += f"""
### Befund 3: Dominanz der impliziten Verankerung

Über alle Cluster hinweg wird Chancengerechtigkeit primär über **pädagogische
Handlungskompetenzen** operationalisiert (Codes 2.1–2.7), nicht über explizite
Begriffsnennungen. Dies beantwortet Dimension 1 der Forschungsfrage eindeutig:

> Die curriculare Verankerung erschöpft sich **nicht** in expliziten
> Begriffsnennungen. Im Gegenteil: {gesamt_c11/gesamt_relevant*100:.1f}% expliziten Nennungen
> stehen {gesamt_implizit/gesamt_relevant*100:.1f}% implizite Verankerungen gegenüber.
> Chancengerechtigkeit wird als **Querschnittsthema** behandelt, das sich in
> konkreten pädagogischen Handlungsfeldern manifestiert.

---

## 3. Methodische Anmerkung

Die Analyse basiert auf dem Feld `confirmed_code` (Expert-validierte Codezuordnung).
Alle Findings wurden im CEiL-Verfahren (Critical Expert in the Loop) manuell
validiert und ggf. umkodiert. Die Unterscheidung explizit/implizit folgt dem
Kodiermanual: Code 1.1 erfasst ausschließlich direkte Begriffsnennungen,
Codes 2.1–2.7 erfassen thematisch verwandte pädagogische Konzepte.

---

**Erstellt mit:** Python (pandas)
**Methodik:** Qualitative Content Analysis (QCA) + Critical Expert in the Loop (CEiL)
"""

    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"[OK] Vergleichsreport: {report_file}")


# ======================================================================
# MAIN
# ======================================================================

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Verwendung:")
        print("  python analyse_code_1_1_deep_dive.py mitte")
        print("  python analyse_code_1_1_deep_dive.py fh_wien")
        print("  python analyse_code_1_1_deep_dive.py --alle")
        sys.exit(1)

    if sys.argv[1] == '--alle':
        ergebnisse = []
        for name in CLUSTER_PATHS:
            ergebnisse.append(analyse_cluster(name))
        print()
        vergleichs_report(ergebnisse)
    elif sys.argv[1] in CLUSTER_PATHS:
        analyse_cluster(sys.argv[1])
    else:
        print(f"Unbekannter Cluster: '{sys.argv[1]}'")
        print(f"Verfügbar: {', '.join(CLUSTER_PATHS.keys())}, --alle")
        sys.exit(1)
