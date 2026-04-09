# Anforderungen: TRACE-Equity

## Teil A: Web-App (WS 2025 — abgeschlossen)

### F1: PDF-Textextraktion
- Curriculum-PDFs einlesen, Text seitenweise extrahieren
- 233 Keywords aus Kodiermanual automatisch suchen (Single Source of Truth)

### F2: Keyword-basierte Vor-Codierung
- Automatische Zuordnung zu 8 Code-Kategorien anhand der Keywords
- Farbcodierte Hervorhebung im Kontext (±200 Zeichen)
- *Anmerkung:* LLM-basierte Analyse (Version B) wurde bewusst nicht
  umgesetzt — Keyword-Ansatz bietet Transparenz und Reproduzierbarkeit

### F3: Expert-Validierung Interface (CEiL)
- Relevanz-Bewertung (ja/nein) pro Finding
- Code-Bestätigung oder -Korrektur per Dropdown
- Notizfeld für qualitative Anmerkungen
- Automatische Speicherung, Fortschrittsanzeige

### F4: Session-Management
- Mehrere PDFs parallel analysierbar
- Sessions persistent (localStorage), fortsetzbar, löschbar

### F5: Datenexport
- CSV-Export mit allen Validierungen (BytesIO, UTF-8 mit BOM)
- Spalten: pdf_name, page, keyword, context, validated, relevant,
  confirmed_code, notes

---

## Teil B: Analyse-Scripts (SS 2026 — in Arbeit)

### A1: Datenintegrität sicherstellen
- Alle CSVs verwenden `confirmed_code` (Expert-validiert), nicht `code`
- Keine NaN-Werte in `relevant` oder `confirmed_code`
- Nur validierte Findings (`validated == True`)
- Regressionstests sichern bekannte Zahlen gegen versehentliche Änderung
- *Erfolgskriterium:* 53/53 Tests bestehen (`python -m pytest tests/ -v`)

### A2: Dimension 1 — Explizit vs. Implizit (Code 1.1 Deep Dive)
- Pro Cluster: Anzahl Code-1.1-Findings und implizite Findings bestimmen
- Verhältnis implizit:explizit berechnen
- Cross-Cluster-Vergleich als Markdown-Report
- *Erfolgskriterium:* Forschungsfrage D1 beantwortbar mit konkreten Zahlen

### A3: Dimension 2 — Konzeptuelle Tiefe (Levinson-Mapping)
- Codes auf Levinson-Stufen mappen (Exposé Tabelle 2)
- Verteilung der Stufen pro Cluster berechnen (nur relevante Findings)
- Heatmap: Levinson-Stufe × Cluster (normalisiert auf Prozent)
- *Erfolgskriterium:* Dominantes Gerechtigkeitsverständnis pro Cluster
  identifizierbar

### A4: Dimension 3 — Cross-Cluster-Vergleich
- Summary-Tabelle aller 4 Cluster (Findings, relevant, Relevanz-Rate)
- Code-Verteilung normalisiert (prozentual) für Vergleichbarkeit
- PH-Aggregat (West + Mitte + SüdOst) vs. FH Wien
- *Erfolgskriterium:* Systematische Unterschiede beschreibbar

### A5: Zitate-Sammlung
- Pro Code und Cluster: repräsentative Textstellen für den Bericht
- HTML-Tags aus Kontexten entfernen
- *Erfolgskriterium:* Mindestens 1 Zitat pro Code pro Cluster (wo vorhanden)

### A6: Forschungsbericht
- Max. 8 Seiten + Anhang, PDF-Abgabe bis 29.06.2026
- Struktur: Einleitung, Methodik, Ergebnisse (D1–D3), Diskussion, Limitationen
- 1 Kernvisualisierung im Hauptteil (Levinson-Heatmap)
- *Erfolgskriterium:* Alle 3 Dimensionen + Hauptforschungsfrage beantwortet

### A7: Poster
- 10-Minuten-Postersession am 26.06.2026
- Forschungsfrage, Methode, Kernbefunde, Levinson-Heatmap, Fazit
- *Erfolgskriterium:* Zentrale Ergebnisse auf einen Blick erfassbar

---

## Nicht-funktionale Anforderungen

### NF1: Wissenschaftlichkeit
- Alle Analyseschritte nachvollziehbar und dokumentiert
- Intercoder-Reliabilität dokumentiert (κ-Werte)
- Theoretischer Bezugsrahmen (Levinson) konsequent angewandt

### NF2: Reproduzierbarkeit
- Scripts wiederholbar ausführbar mit identischen Ergebnissen
- Daten versioniert (git), Regressionstests vorhanden
- Single Source of Truth für Keywords (Kodiermanual)

### NF3: Verständlichkeit
- Dokumentation für beide Teammitglieder verständlich (Master-Niveau)
- Methodik-Dokumentation erklärt jede Analyse für Nicht-Programmiererinnen

---

## Nicht-Ziele

- Automatische Interpretation ohne menschliche Validierung
- Kausalitäts-Schlussfolgerungen
- LLM-basierte Analyse (Version B) — bewusste Entscheidung für Transparenz
- Veröffentlichung sensibler Hochschuldaten
