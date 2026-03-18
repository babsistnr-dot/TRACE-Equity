# Ergebnisse / Results

Analyseergebnisse des TRACE-Equity Projekts, geordnet nach Cluster.

## Übersicht

| Cluster | Findings | Relevant | Relevanz-Ratio | Code 1.1 |
|---------|----------|----------|----------------|----------|
| **West** | 468 | 347 | 74.1% | 0 |
| **Mitte** | 516 | 259 | 50.2% | 8 |
| **SüdOst** | 272 | 192 | 70.6% | 0 |
| **FH Wien** | — | — | — | ausstehend |

Alle `export_clean.csv` sind 100% validiert, 0 NaN-Werte.

---

## Struktur

```
ergebnisse/
├── intercoder_reliability.md     # ICR-Dokumentation
├── cluster_west/
│   ├── export_raw.csv            # Roh-Export aus App
│   ├── export_clean.csv          # 468 Findings (bereinigt)
│   ├── analyse_code_verteilung.md
│   └── visualisierungen/         # 4 PNGs
├── cluster_mitte/
│   ├── export_raw.csv
│   ├── export_clean.csv          # 516 Findings (bereinigt)
│   ├── analyse_code_verteilung.md
│   ├── analyse_code_1_1_deep_dive.md
│   ├── zitate.md
│   └── visualisierungen/         # 4 PNGs
└── cluster_suedost/
    ├── export_raw.csv
    ├── export_clean.csv          # 272 Findings (bereinigt)
    ├── validation_report.md
    ├── analyse_code_verteilung.md
    └── visualisierungen/         # 4 PNGs
```

## Analyse ausführen

```bash
cd scripts/

# Quantitative Code-Verteilung:
python analyse_code_verteilung.py west       # ein Cluster
python analyse_code_verteilung.py --alle     # alle Cluster

# Code 1.1 Tiefenanalyse:
python analyse_code_1_1_deep_dive.py
```

---

**Projekt:** TRACE-Equity
**Stand:** März 2026
