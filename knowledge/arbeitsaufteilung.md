# Arbeitsaufteilung SS2026 — Wer macht was?

## Laura
1. **FH Campus Wien fertig machen** — PDF beschaffen, durch die App laufen lassen, alle Findings validieren (CEiL), CSV exportieren
2. **Bericht gegenlesen** — Claudes Entwurf mit Babsi gemeinsam reviewen und finalisieren
3. **Poster erstellen** — Nach Abschluss der Analyse ein Poster für die Postersession (26.06.) gestalten

## Babsi + Claude
1. **Daten bereinigen** — SüdOst NaN-Werte fixen, confirmed_code-Problem lösen
2. **Alle Analyse-Scripts erstellen und ausführen** — Levinson-Mapping, Cross-Cluster-Vergleich, Code 1.1 Deep Dive, Zitate-Sammlung, ICR-Dokumentation
3. **Mit Chris besprechen** — Ergebnisse und Methodik reviewen, prüfen ob die Forschungsfragen so sinnvoll beantwortet werden können
4. **Forschungsbericht schreiben** — Claude erstellt den Entwurf (8 Seiten + Anhang), Babsi überarbeitet

## Realistische Einschätzung
Claude übernimmt den Großteil der technischen Arbeit (Scripts, Analysen, Visualisierungen, Berichts-Entwurf). Die manuelle Arbeit liegt bei Laura (FH Wien Validierung ~8-12h, Poster) und Babsi (Review, Feinschliff, Chris-Abstimmung). Die Analyse-Scripts und der Berichts-Entwurf können in wenigen Sessions mit Claude erledigt werden.

## Reihenfolge
```
Laura: FH Wien validieren ──────────────────────┐
                                                 │
Babsi + Claude: Schritte 0-3 (Bereinigung,       │
  ICR-Doku, utils.py) ──→ Schritte 5-8          │
  (Analysen) ──→ Besprechung mit Chris ──→       │
  Schritt 9 (Bericht) ◄─────────────────────────┘

Laura + Babsi: Bericht gegenlesen + finalisieren
Laura: Poster erstellen ──→ 26.06. Postersession
Team: Bericht finalisieren ──→ 29.06. Abgabe
```
