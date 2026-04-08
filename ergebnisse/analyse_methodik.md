# TRACE-Equity: Analyse-Methodik

**Stand:** April 2026
**Zweck:** Dokumentation der Analyseschritte für das Forschungsteam (Babsi + Laura)

---

## Was dieses Dokument ist

Dieses Dokument erklärt **Schritt für Schritt**, welche Analysen wir durchführen,
warum wir sie so machen, und wie die Ergebnisse zu lesen sind. Es dient als
Nachschlagewerk für beide Teammitglieder und als methodische Grundlage für den
Forschungsbericht.

---

## Überblick: 3 Analyse-Dimensionen

Unsere Hauptforschungsfrage lautet:

> *"Wie ist Chancengerechtigkeit in den Curricula der österreichischen
> Elementarpädagogik-Bachelorstudiengänge verankert?"*

Diese beantworten wir über **drei Dimensionen**, die jeweils einer eigenen
Analyse entsprechen:

| Dimension | Forschungsfrage | Script | Output |
|---|---|---|---|
| **D1** | Explizit vs. Implizit — Erschöpft sich die Verankerung in Begriffsnennungen? | `analyse_code_1_1_deep_dive.py` | Cluster-Reports + Vergleich |
| **D2** | Konzeptuelle Tiefe — Welches Gerechtigkeitsverständnis dominiert? | `analyse_levinson_mapping.py` | Levinson-Heatmap + Reports |
| **D3** | Cluster-Vergleich — Gibt es systematische Unterschiede? | `analyse_vergleich_cluster.py` | Vergleichstabellen + Visualisierungen |

---

## Datenbasis

### Korpora

| Cluster | Hochschulen | Findings | Relevant | Relevanz-Rate |
|---|---|---|---|---|
| West | PH Tirol, PH Vorarlberg, KPH Edith Stein | 468 | 347 | 74,1% |
| Mitte | PH OÖ, PH Linz, PH Salzburg | 516 | 259 | 50,2% |
| SüdOst | PH Burgenland, PH Kärnten, PH Steiermark | 272 | 192 | 70,6% |
| FH Wien | FH Campus Wien | 370 | 263 | 71,1% |
| **Gesamt** | **N=4 Cluster** | **1.626** | **1.061** | **65,3%** |

### Wichtige Begriffe

- **Finding:** Eine Textstelle im Curriculum, die ein Keyword aus dem Kodiermanual enthält
- **Relevant:** Von der Forscherin im CEiL-Verfahren als thematisch relevant eingestuft (ja/nein)
- **confirmed_code:** Der finale, Expert-validierte Code (kann vom automatisch zugewiesenen abweichen)
- **Code 1.1 (Explizit):** Direkte Nennung von "Chancengleichheit", "Equity" etc.
- **Code 2.x (Implizit):** Thematisch verwandte Konzepte (Diversität, Inklusion, Sprachbildung etc.)

### CEiL-Verfahren (Critical Expert in the Loop)

Jedes Finding wurde manuell überprüft:
1. **Keyword-Suche:** Automatische Identifikation durch die Web-App (233 Keywords)
2. **Relevanz-Bewertung:** Forscherin entscheidet: Ist diese Textstelle thematisch relevant?
3. **Code-Bestätigung:** Forscherin bestätigt oder korrigiert die automatische Codezuordnung
4. **Qualitative Anmerkungen:** Optional Notizen zur Interpretation

---

## Dimension 1: Explizit vs. Implizit (Code 1.1 Deep Dive)

### Was wird untersucht?

Wir unterscheiden zwischen:
- **Explizite Verankerung (Code 1.1):** Das Curriculum verwendet Begriffe wie
  "Chancengleichheit", "Chancengerechtigkeit", "Bildungsgerechtigkeit", "Equity"
  oder "Teilhabegerechtigkeit"
- **Implizite Verankerung (Codes 2.1–2.7):** Das Curriculum thematisiert verwandte
  Konzepte wie Diversität, Inklusion oder Sprachbildung, ohne den übergeordneten
  Begriff zu nennen

### Warum ist das wichtig?

Die Unterscheidung zeigt, ob Chancengerechtigkeit als **eigenständiges Leitkonzept**
in den Curricula sichtbar ist, oder ob es nur **indirekt** über Teilaspekte
behandelt wird. Ein Curriculum, das "Inklusion" und "Diversität" thematisiert
ohne jemals "Chancengerechtigkeit" zu sagen, hat eine andere curriculare Logik
als eines, das den Begriff explizit als Leitprinzip formuliert.

### Wie liest man die Ergebnisse?

- **Ratio implizit:explizit** — z.B. "31:1" bedeutet: Auf jede explizite Nennung
  kommen 31 implizite Findings. Je höher die Zahl, desto stärker die implizite
  Dominanz.
- **"nur implizit"** — Kein einziges Code-1.1-Finding, trotzdem viele implizite
  Findings vorhanden. Das ist der extremste Fall.

### Script-Verwendung

```bash
cd scripts/
python analyse_code_1_1_deep_dive.py --alle    # Alle Cluster + Vergleichsreport
python analyse_code_1_1_deep_dive.py mitte     # Nur ein Cluster
```

### Outputs

- `ergebnisse/cluster_*/analyse_code_1_1_deep_dive.md` — Report pro Cluster
- `ergebnisse/analyse_code_1_1_vergleich.md` — Cross-Cluster-Vergleich

---

## Dimension 2: Konzeptuelle Tiefe (Levinson-Mapping)

*Wird in Schritt 6 implementiert.*

### Was wird untersucht?

Die 8 Codes werden nach dem Levinson-Modell (2015) in Gerechtigkeitsstufen
eingeordnet:

| Levinson-Stufe | Codes | Handlungslogik |
|---|---|---|
| Explizite Nennung | Code 1.1 | Direkte Begriffnennung |
| Formale Gleichheit | Code 2.1, 2.2 | Zugang + Anerkennung für alle |
| Kompensatorische Gerechtigkeit | Code 2.3, 2.6 | Gezielte Förderung von Benachteiligten |
| Transformative Gerechtigkeit | Code 2.4 | Machtkritik + strukturelle Veränderung |
| Querschnitt (Systemebene) | Code 2.5 | Vernetzung + Sozialraumorientierung |
| Querschnitt (Professionalisierung) | Code 2.7 | Professionelle Haltung + Ethik |

### Warum ist das wichtig?

Die Stufen bilden eine zunehmende **Tiefe des Gerechtigkeitsverständnisses** ab:
- **Formale Gleichheit** = alle bekommen dasselbe (Gleichbehandlung)
- **Kompensatorische Gerechtigkeit** = Benachteiligte bekommen mehr (Ausgleich)
- **Transformative Gerechtigkeit** = die Strukturen selbst werden hinterfragt

Ein Curriculum, das hauptsächlich auf der Stufe "Formale Gleichheit" bleibt,
hat ein weniger tiefes Gerechtigkeitsverständnis als eines, das auch
transformative Elemente enthält.

### Mapping-Quelle

Das Mapping stammt aus dem **Exposé, Tabelle 2** und basiert auf:
- Levinson, M. (2015). *Moral injury and the ethics of educational injustice.*
  Harvard Educational Review, 85(2), 203–228.

---

## Dimension 3: Cluster-Vergleich

*Wird in Schritt 7 implementiert.*

### Was wird untersucht?

Systematische Unterschiede zwischen den 4 Clustern:
- Code-Verteilung (normalisiert, da unterschiedliche Cluster-Größen)
- Levinson-Profile im Vergleich
- PH-Aggregat (West + Mitte + SüdOst) vs. FH Wien

### Warum ist das wichtig?

Unterschiede zwischen Clustern können auf unterschiedliche **curriculare
Schwerpunkte** oder **institutionelle Traditionen** hinweisen. Der PH-vs-FH-
Vergleich ist besonders relevant, weil die FH Campus Wien als einzige
Fachhochschule einen anderen institutionellen Hintergrund hat.

---

## Qualitätssicherung

### Intercoder-Reliabilität (ICR)

- **Kalibrierungsphase:** Cluster Mitte gemeinsam kodiert
- **Unabhängige Kodierung:** Cluster SüdOst doppelt kodiert
- **Ergebnis:** κ = 0,71 (Relevanz), κ = 0,83 (Codezuordnung)
- **Interpretation:** Substanzielle bis fast perfekte Übereinstimmung
  (Landis & Koch, 1977)
- **Details:** `ergebnisse/intercoder_reliability.md`

### Regressionstests

Die Testsuite (`tests/test_scripts.py`, 49 Tests) stellt sicher:
- Alle 4 CSV-Dateien sind vorhanden und ladbar
- Keine NaN-Werte in `relevant` oder `confirmed_code`
- Nur `ja`/`nein` als Relevanz-Werte
- Exakte Finding-Zahlen stimmen (Regressionstests gegen bekannte Werte)
- Levinson-Mapping ist vollständig (alle Codes werden gemappt)

```bash
# Tests ausführen (aus Projekt-Root):
python -m pytest tests/ -v
```

---

## Allgemeine Script-Verwendung

Alle Scripts liegen in `scripts/` und verwenden `utils.py` als zentrale
Konfiguration (Pfade, Farben, Levinson-Mapping, Ladefunktionen).

```bash
cd scripts/

# Analyse 1: Quantitative Code-Verteilung
python analyse_code_verteilung.py --alle

# Analyse 2: Code 1.1 Deep Dive (Dimension 1)
python analyse_code_1_1_deep_dive.py --alle

# Analyse 3: Levinson-Mapping (Dimension 2) — kommt als nächstes
# Analyse 4: Cross-Cluster-Vergleich (Dimension 3) — kommt danach
```

---

**Erstellt:** April 2026
**Für:** Babsi + Laura (TRACE-Equity Forschungsteam)
