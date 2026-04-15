# Cross-Cluster-Vergleich (Dimension 3)

**Forschungsfrage:** Gibt es systematische Unterschiede zwischen den vier Clustern?

Basis: Nur relevante Findings (`relevant == 'ja'`, Spalte `confirmed_code`). Alle Cluster getrennt ausgewiesen.

## 1. Summary-Tabelle

| Cluster | Findings gesamt | Relevant | Relevanzrate | Code 1.1 |
|---|---:|---:|---:|---:|
| West | 468 | 347 | 74.1% | 0 |
| Mitte | 516 | 259 | 50.2% | 8 |
| SüdOst | 272 | 192 | 70.6% | 0 |
| FH Wien | 370 | 263 | 71.1% | 1 |
| **Alle** | **1626** | **1061** | **65.3%** | **9** |

## 2. Code-Verteilung — prozentual (je Cluster auf 100%)

| Code | West | Mitte | SüdOst | FH Wien |
|---|---:|---:|---:|---:|
| Code 1.1 | 0.0% | 3.1% | 0.0% | 0.4% |
| Code 2.1 | 32.3% | 35.1% | 39.1% | 18.3% |
| Code 2.2 | 11.2% | 15.1% | 8.9% | 6.5% |
| Code 2.3 | 8.9% | 3.9% | 8.9% | 12.9% |
| Code 2.4 | 2.6% | 8.1% | 4.7% | 5.7% |
| Code 2.5 | 8.6% | 5.4% | 13.0% | 6.1% |
| Code 2.6 | 9.8% | 7.7% | 7.3% | 7.2% |
| Code 2.7 | 26.5% | 21.6% | 18.2% | 43.0% |

## 3. Code-Verteilung — absolut

| Code | West | Mitte | SüdOst | FH Wien |
|---|---:|---:|---:|---:|
| Code 1.1 | 0 | 8 | 0 | 1 |
| Code 2.1 | 112 | 91 | 75 | 48 |
| Code 2.2 | 39 | 39 | 17 | 17 |
| Code 2.3 | 31 | 10 | 17 | 34 |
| Code 2.4 | 9 | 21 | 9 | 15 |
| Code 2.5 | 30 | 14 | 25 | 16 |
| Code 2.6 | 34 | 20 | 14 | 19 |
| Code 2.7 | 92 | 56 | 35 | 113 |
| **Summe** | 347 | 259 | 192 | 263 |

## 4. Spannweite je Code (Min/Max über die 4 Cluster)

| Code | Min | Max | Differenz | Max-Cluster | Min-Cluster |
|---|---:|---:|---:|---|---|
| Code 1.1 | 0.0% | 3.1% | 3.1 pp | Mitte | West |
| Code 2.1 | 18.3% | 39.1% | 20.8 pp | SüdOst | FH Wien |
| Code 2.2 | 6.5% | 15.1% | 8.6 pp | Mitte | FH Wien |
| Code 2.3 | 3.9% | 12.9% | 9.1 pp | FH Wien | Mitte |
| Code 2.4 | 2.6% | 8.1% | 5.5 pp | Mitte | West |
| Code 2.5 | 5.4% | 13.0% | 7.6 pp | SüdOst | Mitte |
| Code 2.6 | 7.2% | 9.8% | 2.6 pp | West | FH Wien |
| Code 2.7 | 18.2% | 43.0% | 24.7 pp | FH Wien | SüdOst |

## 5. Interpretation

### 5.1 Relevanzraten-Varianz

Die Relevanzraten schwanken zwischen 50.2% (Mitte) und 74.1% (West). Diese Varianz ist methodisch relevant: Ein niedriger Wert deutet darauf hin, dass ein größerer Anteil der Keyword-Treffer im CEiL-Verfahren als nicht einschlägig bewertet wurde — z.B. weil Begriffe wie 'Entwicklung' oder 'Bildung' in generischen Kontexten auftreten, ohne Bezug zu Chancengerechtigkeit. Die Varianz ist kein inhaltlicher Befund über Chancengerechtigkeit, sondern ein Hinweis auf Unterschiede in der curricularen Sprache.

### 5.2 Auffällige Code-Unterschiede zwischen Clustern

Die drei Codes mit der größten Spannweite zwischen den Clustern:

- **Code 2.7** (Spannweite 24.7 Prozentpunkte): FH Wien 43.0% vs. SüdOst 18.2%.
- **Code 2.1** (Spannweite 20.8 Prozentpunkte): SüdOst 39.1% vs. FH Wien 18.3%.
- **Code 2.3** (Spannweite 9.1 Prozentpunkte): FH Wien 12.9% vs. Mitte 3.9%.

### 5.3 FH Wien im Vergleich zu den PH-Clustern

Die FH Campus Wien zeigt ein systematisch anderes Profil als die drei Pädagogischen Hochschulen: deutlich geringerer Anteil bei Code 2.1 (Diversität & Heterogenität: 18.3% vs. 32.3–39.1% bei den PHs), dafür deutlich höherer Anteil bei Code 2.3 (Individuelle Förderung: 12.9%) und Code 2.7 (Professionelle Haltung & Ethik: 43.0%). Dieses Muster ist konsistent mit dem Levinson-Befund aus Schritt 6, in dem die FH Wien den deutlichsten Anteil kompensatorischer Gerechtigkeit zeigte.

### 5.4 Limitationen

- N=1 Institution pro Cluster — keine statistische Generalisierung möglich.
- Keine Signifikanztests: Unterschiede sind deskriptiv, nicht inferentiell.
- Relevanzraten variieren (siehe 5.1); der direkte Prozent-Vergleich gleicht diese Varianz durch Normalisierung aus, nivelliert aber unterschiedliche absolute Datenvolumina.

## 6. Visualisierungen

- `visualisierungen_vergleich/code_verteilung_grouped_bar.png`
- `visualisierungen_vergleich/code_verteilung_heatmap.png`

Die Kernvisualisierung des Forschungsberichts bleibt die Levinson-Heatmap aus Schritt 6; die hier erzeugten Grafiken dienen dem Anhang und der Postersession.
