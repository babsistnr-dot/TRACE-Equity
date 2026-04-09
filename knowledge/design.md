# TRACE-Equity: Design-Entscheidungen

Dokumentation der Visualisierungs- und Darstellungsentscheidungen.

---

## Grundsätze

1. **Forschungsfragengetrieben** — Jede Visualisierung muss eine
   Forschungsfrage beantworten. Rein deskriptive Häufigkeitsdiagramme
   ohne theoretischen Bezug werden nicht erstellt.
2. **Eine Kernvisualisierung** — Der 8-Seiten-Bericht hat Platz für
   maximal 1–2 Abbildungen im Hauptteil. Alles andere gehört in den Anhang.
3. **Tabellen vor Diagrammen** — Wo exakte Zahlen wichtiger sind als
   visuelle Muster, verwenden wir Markdown-Tabellen statt Grafiken.

---

## Verworfene Darstellungsformen

| Darstellungsform | Warum verworfen |
|---|---|
| **Pie Charts** | In der Wissenschaft generell kritisch gesehen — schwer zu lesen, verzerren Proportionen. Ein Satz wie "347 von 468 (74,1%)" ist präziser. |
| **Top-Keywords-Diagramme** | Kein Erkenntnisgewert für die Forschungsfrage. Die Häufigkeit einzelner Keywords sagt nichts über Gerechtigkeitsverständnisse aus. |
| **Separate Balkendiagramme pro Cluster** | Nicht vergleichbar ohne Normalisierung. Die Levinson-Heatmap leistet dasselbe besser. |
| **Deskriptive Code-Häufigkeits-Balken** | Waren die erste Analyse (WS 2025). Zeigen nur "wie viel von was" ohne theoretische Einordnung. Ersetzt durch Levinson-Mapping. |

---

## Gewählte Darstellungsformen

### Levinson-Heatmap (Kernvisualisierung — Schritt 6)

**Beantwortet:** D2 (Konzeptuelle Tiefe) + D3 (Cluster-Vergleich) gleichzeitig

**Aufbau:**
- Zeilen: Levinson-Stufen (Formale Gleichheit, Kompensatorische Gerechtigkeit,
  Transformative Gerechtigkeit, Querschnitt)
- Spalten: 4 Cluster
- Zellen: Prozentuale Verteilung (normalisiert pro Cluster auf 100%)
- Farbskala: Sequentiell (hell = wenig, dunkel = viel)

**Warum Prozent statt absolut:** Cluster haben unterschiedliche Größen
(192–347 relevante Findings). Absolute Zahlen wären nicht vergleichbar.

**Warum Heatmap statt Grouped Bar:** Bei 4 Clustern × 6 Levinson-Stufen
hat ein Grouped Bar 24 Balken — unübersichtlich. Die Heatmap zeigt
Muster auf einen Blick (z.B. "alle Cluster stark bei Formaler Gleichheit,
schwach bei Transformativer Gerechtigkeit").

### Explizit:Implizit-Ratio (Schritt 5)

**Beantwortet:** D1 (Explizit vs. Implizit)

**Darstellung:** Tabelle mit Verhältniszahlen, keine Visualisierung nötig.
Die Zahlen sind so eindeutig (117:1 über alle Cluster), dass ein Diagramm
keinen Mehrwert bieten würde.

### Summary-Tabelle (Schritt 7)

**Beantwortet:** Deskriptive Übersicht (Tabelle 1 im Bericht)

**Darstellung:** Markdown-Tabelle mit: Cluster, Findings gesamt, relevant,
Relevanz-Rate, Code-1.1-Anteil. Dient als Orientierung für Lesende.

---

## Farbschema

Konsistent mit der Web-App (definiert in `scripts/utils.py`):

| Element | Farbe | Hex |
|---|---|---|
| Code 1.1 (Direkte Nennung) | Rot | #e74c3c |
| Code 2.1 (Diversität) | Blau | #3498db |
| Code 2.2 (Inklusion) | Grün | #2ecc71 |
| Code 2.3 (Förderung) | Orange | #f39c12 |
| Code 2.4 (Benachteiligung) | Lila | #9b59b6 |
| Code 2.5 (Partnerschaft) | Türkis | #1abc9c |
| Code 2.6 (Sprachbildung) | Dunkelorange | #e67e22 |
| Code 2.7 (Haltung) | Dunkelgrau | #34495e |

Levinson-Stufen verwenden eigene Farben (definiert in `LEVINSON_FARBEN`),
um Verwechslung mit Code-Farben zu vermeiden.

---

## Umlaute in Visualisierungen

Matplotlib kann Umlaute korrekt darstellen, wenn der Font sie unterstützt.
Wir verwenden die System-Standardschrift und ersetzen Umlaute **nicht**
(kein `ä→ae`). Falls ein Font Probleme macht, wird auf DejaVu Sans
gewechselt (`plt.rcParams['font.family'] = 'DejaVu Sans'`).
