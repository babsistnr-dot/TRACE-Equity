# Intercoder-Reliabilität (ICR): Dokumentation

**Projekt:** TRACE-Equity
**Kodiererinnen:** Babsi (Kodiererin A), Laura (Kodiererin B)
**Datum:** November 2025 – Februar 2026

---

## 1. Kalibrierungsphase

Vor Beginn der unabhängigen Kodierung wurde eine gemeinsame Kalibrierung durchgeführt, um ein geteiltes Verständnis des Kategoriensystems sicherzustellen.

**Vorgehen:**
1. Beide Kodiererinnen studierten das Kodiermanual (233 Keywords, 8 Codes)
2. **Cluster Mitte** (516 Findings) diente als Kalibrierungs-Corpus
3. Die ersten ~50 Findings wurden gemeinsam validiert und diskutiert
4. Bei Uneinigkeit wurden Entscheidungsregeln formuliert und dokumentiert

**Ergebnis der Kalibrierung — ergänzte Kodierregeln:**
- Keywords in Literaturverzeichnissen oder Quellenangaben → generell nicht relevant
- „Ethik" als Modulname (z.B. „Ethik und Gesellschaft") ohne inhaltlichen Equity-Bezug → nicht relevant für Code 2.7
- „kulturell" als allgemeines Adjektiv ohne Diversitätsbezug → nicht relevant für Code 2.1
- Grenzfälle zwischen Code 2.1 (Diversität) und Code 2.4 (Abbau Benachteiligung): Entscheidend ist die **Handlungslogik** — beschreibt die Textstelle Anerkennung von Vielfalt (→ 2.1) oder aktive Veränderung von Strukturen (→ 2.4)?

---

## 2. Unabhängige Kodierung

**Corpus:** Cluster SüdOst (272 Findings nach Bereinigung)

**Vorgehen:**
- Beide Kodiererinnen validierten alle 272 Findings unabhängig voneinander über die TRACE-Equity Web-App
- Für jedes Finding: Relevanz-Entscheidung (ja/nein) und Code-Bestätigung bzw. Umkodierung
- Kein Austausch während der Kodierphase

**Warum Cluster SüdOst als ICR-Corpus?**
- Mittlere Größe (272 Findings) — vollständige Doppelkodierung realistisch
- Enthält alle 7 vorkommenden Codes (Code 1.1 fehlt) → breites Kategoriespektrum
- Wurde nach der Kalibrierungsphase kodiert → Lerneffekt aus Cluster Mitte berücksichtigt

---

## 3. Ergebnisse

### 3.1 Relevanz-Übereinstimmung

| | Kodiererin B: ja | Kodiererin B: nein | Summe |
|---|---|---|---|
| **Kodiererin A: ja** | 165 | 18 | 183 |
| **Kodiererin A: nein** | 17 | 72 | 89 |
| **Summe** | 182 | 90 | 272 |

- **Prozent-Übereinstimmung:** 237/272 = **87.1%**
- **Cohens κ:** **0.71** (gut)

### 3.2 Code-Übereinstimmung

Berechnet für die 165 Findings, die beide Kodiererinnen als relevant bewerteten:

- **Prozent-Übereinstimmung:** 148/165 = **89.7%**
- **Cohens κ:** **0.83** (sehr gut)

### 3.3 Häufigste Abweichungen

| Abweichungstyp | Häufigkeit | Beispiel |
|---|---|---|
| Relevanz: A ja / B nein | 18 | Keywords in allgemeinen Kompetenzbeschreibungen ohne Equity-Bezug |
| Relevanz: A nein / B ja | 17 | Keywords in Modulbeschreibungen mit indirektem Equity-Bezug |
| Code-Zuordnung | 17 | Code 2.1 vs. 2.4 bei Formulierungen zu „Umgang mit Vielfalt" |

---

## 4. Konsenskonferenz

Nach der unabhängigen Kodierung wurden alle 52 nicht-übereinstimmenden Findings gemeinsam besprochen.

**Vorgehen:**
1. Jede Kodiererin erläuterte ihre Entscheidung
2. Rückbezug auf das Kodiermanual und die Kalibrierungsregeln
3. Konsens wurde für alle Fälle erreicht

**Zentrale Erkenntnisse:**
- Die meisten Abweichungen bei der Relevanz betrafen **kontextarme Findings** — Keywords in Aufzählungen oder Tabellen, wo der Equity-Bezug schwer beurteilbar war
- Code-Abweichungen konzentrierten sich auf die Grenze **Code 2.1 ↔ 2.4**: „Diversitätsbewusstsein" als Anerkennung (2.1) oder als Ansatz zur Veränderung (2.4)?
- Ergänzte Regel: Enthält die Textstelle ein **aktives Verb** (fördern, abbauen, verändern) → Code 2.4; beschreibende Formulierung (anerkennen, wahrnehmen, berücksichtigen) → Code 2.1

**Ergebnis:** Die finalen Kodierungen wurden als `confirmed_code` in der Export-CSV gespeichert.

---

## 5. Interpretation

Die ICR-Werte liegen im Bereich **gut bis sehr gut** (Landis & Koch, 1977):

| Maß | Wert | Bewertung |
|---|---|---|
| κ Relevanz | 0.71 | Gut |
| κ Code-Zuordnung | 0.83 | Sehr gut |

Die höhere Übereinstimmung bei der Code-Zuordnung (κ = 0.83) im Vergleich zur Relevanz-Entscheidung (κ = 0.72) lässt sich dadurch erklären, dass die **Relevanzbeurteilung stärker interpretativ** ist — sie erfordert eine Einschätzung des Kontexts —, während die **Code-Zuordnung** durch die klare Struktur des Kodiermanuals stärker standardisiert ist.

Die Kalibrierungsphase an Cluster Mitte hat sich als wirksam erwiesen: Die während der Kalibrierung formulierten Entscheidungsregeln reduzierten systematische Abweichungen.

---

## 6. Anwendung auf Cluster West

Nach der Konsenskonferenz wurde Cluster West (468 Findings) mit den geschärften Kodierregeln validiert. Eine stichprobenartige Gegenkontrolle (10%, n=47) ergab eine Übereinstimmung von 91.5%, was die Stabilität der Kodierung bestätigt.

---

## Literatur

- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.
- Kuckartz, U. & Rädiker, S. (2022). *Qualitative Inhaltsanalyse: Methoden, Praxis, Computerunterstützung* (5. Aufl.). Beltz Juventa.
- Landis, J. R. & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.
- Lombard, M., Snyder-Duch, J. & Bracken, C. C. (2002). Content analysis in mass communication. *Human Communication Research*, 28(4), 587–604.
