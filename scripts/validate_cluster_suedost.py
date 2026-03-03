"""
TRACE-Equity Validation Script
Validierung des Cluster SüdOst CSV-Exports

Analysiert Validierungsstatus und prüft auf semantische Duplikate.
"""

import pandas as pd
from pathlib import Path

CSV_FILE = 'ergebnisse/TRACE_Equity_Export_ClusterSüdOst.csv'
CLEANED_FILE = 'ergebnisse/TRACE_Equity_Export_ClusterSüdOst_cleaned.csv'

print("="*80)
print("CLUSTER SÜDOST - CSV VALIDATION")
print("="*80)
print()

# Lade Daten
print("Lade Daten...")
df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')
print(f"[OK] {len(df)} Findings geladen")
print()

# ============================================================================
# 1. GRUNDLEGENDE STATISTIKEN
# ============================================================================

print("="*80)
print("1. VALIDIERUNGSSTATUS")
print("="*80)

total = len(df)
validated = df['validated'].sum()
not_validated = total - validated

print(f"Total Findings: {total}")
print(f"Validiert: {validated} ({validated/total*100:.1f}%)")
print(f"Nicht validiert: {not_validated} ({not_validated/total*100:.1f}%)")
print()

# ============================================================================
# 2. RELEVANZ-ANALYSE (NUR VALIDIERTE)
# ============================================================================

print("="*80)
print("2. RELEVANZ-ANALYSE (nur validierte Findings)")
print("="*80)

validated_df = df[df['validated'] == True]
relevant = len(validated_df[validated_df['relevant'] == 'ja'])
not_relevant = len(validated_df[validated_df['relevant'] == 'nein'])
relevance_ratio = (relevant / validated * 100) if validated > 0 else 0

print(f"Relevant (ja): {relevant} ({relevant/validated*100:.1f}%)")
print(f"Nicht relevant (nein): {not_relevant} ({not_relevant/validated*100:.1f}%)")
print()

# ============================================================================
# 3. CODE-VERTEILUNG (ALLE FINDINGS)
# ============================================================================

print("="*80)
print("3. CODE-VERTEILUNG (alle Findings)")
print("="*80)

code_counts_all = df['code'].value_counts()
for code, count in code_counts_all.items():
    pct = count / total * 100
    print(f"{code}: {count} ({pct:.1f}%)")
print()

# ============================================================================
# 4. CODE-VERTEILUNG (NUR RELEVANTE)
# ============================================================================

print("="*80)
print("4. CODE-VERTEILUNG (nur relevante Findings)")
print("="*80)

relevant_df = validated_df[validated_df['relevant'] == 'ja']
code_counts_relevant = relevant_df['code'].value_counts()
for code, count in code_counts_relevant.items():
    pct = count / len(relevant_df) * 100
    print(f"{code}: {count} ({pct:.1f}%)")
print()

# ============================================================================
# 5. VERGLEICH MIT CLUSTER MITTE
# ============================================================================

print("="*80)
print("5. VERGLEICH MIT CLUSTER MITTE")
print("="*80)

print("Cluster Mitte (OÖ Linz, Salzburg):")
print("  - 516 validierte Findings")
print("  - 259 relevant (50.2%)")
print("  - 257 nicht relevant (49.8%)")
print()
print("Cluster SüdOst (Burgenland, Kärnten, Steiermark):")
print(f"  - {validated} validierte Findings")
print(f"  - {relevant} relevant ({relevance_ratio:.1f}%)")
print(f"  - {not_relevant} nicht relevant ({not_relevant/validated*100:.1f}%)")
print()

# ============================================================================
# 6. ANALYSE NICHT-VALIDIERTER FINDINGS
# ============================================================================

print("="*80)
print("6. NICHT-VALIDIERTE FINDINGS (potenzielle Duplikate)")
print("="*80)

not_validated_df = df[df['validated'] == False]
print(f"Total nicht-validiert: {len(not_validated_df)}")
print()

if len(not_validated_df) > 0:
    print("Code-Verteilung (nicht-validiert):")
    nv_codes = not_validated_df['code'].value_counts()
    for code, count in nv_codes.items():
        print(f"  {code}: {count}")
    print()

    # Semantische Duplikat-Analyse
    print("Semantische Duplikat-Analyse:")
    print("(Überprüfung auf Kontext-Überlappung mit validierten Findings)")
    print()

    # Einfache Heuristik: Gleiche Seite + gleiches Keyword = wahrscheinlich Duplikat
    duplicate_count = 0
    for idx, nv_row in not_validated_df.iterrows():
        # Finde validierte Findings mit gleichem Keyword und gleicher Seite
        same_page_keyword = validated_df[
            (validated_df['page'] == nv_row['page']) &
            (validated_df['keyword'] == nv_row['keyword'])
        ]
        if len(same_page_keyword) > 0:
            duplicate_count += 1

    print(f"Findings mit gleicher Seite & Keyword wie validierte: {duplicate_count}/{len(not_validated_df)}")
    print(f"Wahrscheinlich semantische Duplikate: {duplicate_count}")
    print()

# ============================================================================
# 7. VALIDITÄTS-CHECK
# ============================================================================

print("="*80)
print("7. DATENQUALITÄT")
print("="*80)

# Prüfe auf fehlende Werte
print("Fehlende Werte:")
print(df.isnull().sum())
print()

# Prüfe Struktur
print("CSV-Struktur:")
print(f"  Spalten: {list(df.columns)}")
print(f"  Erwartete Spalten: ['pdf_name', 'page', 'code', 'keyword', 'context', 'validated', 'relevant', 'confirmed_code', 'notes']")
print()

# ============================================================================
# 8. EMPFEHLUNG
# ============================================================================

print("="*80)
print("8. EMPFEHLUNG")
print("="*80)

if not_validated > 0:
    print(f"WARNUNG: {not_validated} Findings sind nicht validiert ({not_validated/total*100:.1f}%)")
    print()
    print("Mögliche Gründe:")
    print("  1. Validierung noch nicht abgeschlossen")
    print("  2. Semantische Duplikate (gleiche Keywords auf gleichen Seiten)")
    print()
    print("Empfehlung:")
    print("  - Validierung fortsetzen ODER")
    print("  - Nicht-validierte Findings als Duplikate entfernen")
    print()

    user_input = input("Sollen nicht-validierte Findings entfernt werden? (ja/nein): ")

    if user_input.lower() == 'ja':
        print()
        print("Erstelle bereinigte CSV-Datei...")
        cleaned_df = df[df['validated'] == True]
        cleaned_df.to_csv(CLEANED_FILE, index=False, encoding='utf-8-sig')
        print(f"[OK] Bereinigte Datei gespeichert: {CLEANED_FILE}")
        print(f"[OK] {len(cleaned_df)} Findings (nur validierte)")
        print()
    else:
        print()
        print("Keine Bereinigung durchgeführt.")
        print()
else:
    print("[OK] Alle Findings sind validiert!")
    print("Keine Bereinigung notwendig.")
    print()

print("="*80)
print("VALIDATION ABGESCHLOSSEN")
print("="*80)
