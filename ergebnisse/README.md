# Ergebnisse / Results

Analyseergebnisse des TRACE-Equity Projekts, geordnet nach Cluster.

## Struktur

```
ergebnisse/
├── cluster_west/         # Cluster West: Tirol, Vorarlberg, Edith Stein
├── cluster_mitte/        # Cluster Mitte: OÖ, Linz, Salzburg
└── cluster_suedost/      # Cluster SüdOst: Burgenland, Kärnten, Steiermark
```

## Cluster-Übersicht

### cluster_west/
| Datei | Beschreibung |
|---|---|
| `export.csv` | 534 Findings, 476 validiert (89%), 347 relevant |

**Status:** Validierung noch offen (58 Einträge)

---

### cluster_mitte/
| Datei | Beschreibung |
|---|---|
| `export_raw.csv` | 591 Findings (Roh-Export aus App) |
| `export_clean.csv` | 516 Findings (bereinigt, vollständig validiert) |
| `analyse_code_verteilung.md` | Quantitativer Report: Code-Verteilung |
| `analyse_code_1_1_deep_dive.md` | Qualitativer Report: Code 1.1 Direkte Nennung |
| `zitate.md` | Strukturierte Zitate-Sammlung |
| `visualisierungen/` | 4 PNG-Grafiken zur Code-Verteilung |

**Status:** Vollständig analysiert

---

### cluster_suedost/
| Datei | Beschreibung |
|---|---|
| `export_raw.csv` | 319 Findings (Roh-Export aus App) |
| `export_clean.csv` | 276 Findings (bereinigt, vollständig validiert) |
| `validation_report.md` | Validierungsbericht (Duplikate-Analyse) |
| `analyse_code_verteilung.md` | Quantitativer Report: Code-Verteilung |
| `visualisierungen/` | 4 PNG-Grafiken zur Code-Verteilung |

**Status:** Vollständig analysiert

---

## Neue Analyse erstellen

```bash
# 1. App starten (aus Projekt-Root)
python app.py  →  http://localhost:5000

# 2. PDF hochladen, analysieren, validieren, exportieren

# 3. CSV in passenden cluster_*/ Ordner ablegen:
#    export_raw.csv    = direkt aus App exportiert
#    export_clean.csv  = nach Duplikate-Bereinigung

# 4. Analyse-Skripte ausführen (aus Projekt-Root):
python scripts/analyse_code_verteilung.py
python scripts/analyse_code_verteilung_suedost.py
```

---

**Projekt:** TRACE-Equity (Tracking Representations of Access, Chances and Equity)
**Stand:** März 2026
