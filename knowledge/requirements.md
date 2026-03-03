# Anforderungen: TRACE-Equity Analyseplattform

## Muss-Kriterien (Core Features)

### F1: PDF-Textextraktion
- Das System muss Curriculum-PDFs einlesen können
- Automatische Extraktion von Text aus den Dokumenten
- Erhalt der Dokumentstruktur (Kapitel, Abschnitte)

### F2: LLM-basierte Vor-Codierung
- Automatische Identifikation relevanter Textstellen zu "Chancengleichheit"
- Nutzung von Large Language Models (z.B. Gemini 2.5 Pro) mit großem Context Window
- Kategorisierung nach thematischer Dichte und Schlüsselbegriffen

### F3: Expert-Validierung Interface (CEiL)
- Darstellung der automatisch identifizierten Textstellen
- Möglichkeit zur manuellen Überprüfung: "Relevant" / "Nicht relevant"
- Zweifache menschliche Validierung (fachpraktisch + curriculumtheoretisch)
- Transparente Anzeige der LLM-Begründung für jede Codierung

### F4: Hochschulvergleich
- Vergleichende Analyse über alle Curricula hinweg
- Quantitative Auswertung (Häufigkeiten, Gewichtung)
- Qualitative Auswertung (konzeptuelle Rahmungen)
- Export als strukturierte Tabelle

### F5: Nachvollziehbarkeit & Dokumentation
- Logging aller Analyseschritte (Promptotyping-Journal)
- Speicherung aller Zwischenschritte
- Export der Ergebnisse in maschinenlesbarem Format (CSV/JSON)

## Nicht-funktionale Anforderungen

### NF1: Benutzerfreundlichkeit
- **Einfache Bedienung** für Personen ohne Programmierkenntnisse
- Klare, verständliche Benutzeroberfläche
- Schritt-für-Schritt-Führung durch den Analyseprozess

### NF2: Genauigkeit
- Hohe Präzision bei der Identifikation relevanter Textstellen
- Minimierung von False Positives/Negatives
- Validierung durch Expert*innen-Konsens

### NF3: Nachvollziehbarkeit
- Alle Entscheidungen müssen transparent sein
- Erklärungen der LLM-Codierungen einsehbar
- Audit-Trail aller Änderungen und Validierungen

### NF4: Skalierbarkeit
- Verarbeitung mehrerer PDF-Dokumente (mind. 10 Curricula)
- Effiziente Verarbeitung großer Textmengen

## Kann-Kriterien (Nice-to-have)

### P1: Visualisierung
- Grafische Darstellung der Ergebnisse (Diagramme, Heatmaps)
- Vergleichsvisualisierung zwischen Hochschulen

### P2: Erweiterte Suchfunktionen
- Volltextsuche in allen Curricula
- Filterung nach Hochschule, Kategorie, Relevanz

### P3: Export-Formate
- PDF-Report-Generierung
- Direkte Integration mit Excel/Google Sheets

## Nicht-Ziele (Bewusst ausgeschlossen)

- ❌ Automatische Interpretation ohne menschliche Validierung
- ❌ Quantitative Inhaltsanalyse (Wortfrequenzen ohne Kontext)
- ❌ Bearbeitung oder Änderung der Original-PDFs
- ❌ Automatische Kausalitäts-Schlussfolgerungen
- ❌ Veröffentlichung sensibler Hochschuldaten

## Technische Präferenzen

- **LLM**: Gemini 2.5 Pro (großes Context Window für lange Curricula)
- **Programmiersprache**: Python (Standard für Data Science)
- **Interface**: Einfach und zugänglich (z.B. Jupyter Notebook oder Streamlit Web-App)
- **Datenformat**: PDF (Input), CSV/JSON (Output)

---

*Priorisierung: Muss-Kriterien (F1-F5) zuerst, dann Kann-Kriterien (P1-P3)*
