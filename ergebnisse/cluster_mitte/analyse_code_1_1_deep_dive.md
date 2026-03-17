# TRACE-Equity Analyse 2: Code 1.1 "Direkte Nennung" - Deep Dive

**Curriculum:** Cluster Mitte_OÖ_Linz, Salzburg.pdf
**Analysedatum:** 17.03.2026
**Fokus:** Explizite Verankerung von Chancengleichheit im Curriculum

---

## 1. Übersicht

**Code 1.1: Direkte Nennung**
- **Definition:** Explizite Nennung von Chancengleichheit/Chancengerechtigkeit oder verwandten Begriffen
- **Total Findings:** 8
- **Relevante Findings:** 8
- **Relevanz-Ratio:** 100.0%

---

## 2. Keyword-Verteilung

| Keyword | Anzahl | Seiten |
|---------|--------|--------|
| Bildungsgerechtigkeit | 5 | 10, 16, 49, 50, 53 |
| Chancengleichheit | 1 | 10 |
| Teilhabegerechtigkeit | 1 | 10 |
| Chancengerechtigkeit | 1 | 68 |

---

## 3. Semantische Differenzierung

Die verwendeten Begriffe unterscheiden sich in ihrer konzeptuellen Bedeutung:

| Begriff | Konzeptuelle Rahmung | Theoretischer Bezug |
|---------|---------------------|---------------------|
| Chancengleichheit | Formale Gleichheit der Ausgangsbedingungen | Liberal-egalitärer Ansatz |
| Chancengerechtigkeit | Substanzielle Gerechtigkeit (Kompensation) | Capability Approach (Sen) |
| Equity | Fairness durch Berücksichtigung unterschiedlicher Ausgangslagen | International: Educational Equity |
| Bildungsgerechtigkeit | Gerechtigkeit spezifisch im Bildungskontext | Kritische Bildungstheorie |

**Interpretation:**

Die Begriffswahl im Curriculum ist nicht zufällig:
- **"Chancengleichheit"** betont formale Gleichbehandlung
- **"Chancengerechtigkeit"** impliziert kompensatorische/transformative Ansätze
- **"Equity" vs. "Equality"** international etablierte Unterscheidung

---

## 4. Verwendungskontexte

Die explizite Nennung von Chancengleichheit erfolgt in unterschiedlichen curricularen Kontexten:


### 4.1 Normativ (Leitprinzip)

**Anzahl Findings:** 4

**Charakteristik:**
- Chancengleichheit als übergeordneter Wert oder Grundsatz
- Meist in Präambeln, Leitbildern oder Zielsetzungen
- Normative Verpflichtung der Institution


### 4.2 Beschreibend (Modulinhalte)

**Anzahl Findings:** 1

**Charakteristik:**
- Chancengleichheit als Modulinhalt oder Thema
- Didaktische Verankerung in Lehrveranstaltungen
- Wissensvermittlung


### 4.3 Kompetenzbezogen (Fähigkeiten)

**Anzahl Findings:** 1

**Charakteristik:**
- Chancengleichheit als zu erwerbende Kompetenz
- Studierende sollen Chancengleichheit fördern KÖNNEN
- Handlungsorientierung


### 4.4 Organisatorisch (Strukturen)

**Anzahl Findings:** 2

**Charakteristik:**
- Organisatorische oder strukturelle Kontexte


---

## 5. Interpretation: Capability Approach Mapping

Gemäß dem theoretischen Rahmen (Sen, Nussbaum) lassen sich die Findings in drei Kategorien einordnen:

### 5.1 Formale Chancengleichheit
- **Fokus:** Gleiche Ausgangsbedingungen, Nicht-Diskriminierung
- **Begriffe:** Primär "Chancengleichheit", "Equality"
- **Limitation:** Ignoriert strukturelle Ungleichheiten

### 5.2 Substanzielle Chancengerechtigkeit
- **Fokus:** Kompensation unterschiedlicher Ausgangslagen
- **Begriffe:** "Chancengerechtigkeit", "Equity", "Bildungsgerechtigkeit"
- **Ansatz:** Ressourcenorientiert, kompensatorisch

### 5.3 Transformative Gerechtigkeit
- **Fokus:** Strukturelle Veränderung, Empowerment
- **Begriffe:** "Teilhabegerechtigkeit" (am nächsten)
- **Ansatz:** Kritisch-emanzipatorisch

**Befund:**

Die explizite Verankerung von Chancengleichheit im Curriculum ist **gering**:
- Nur {len(code_1_1_relevant)} relevante Findings
- Bedeutet: Chancengleichheit wird primär **implizit** (über Codes 2.1-2.7) behandelt

**Kritische Frage:**
- Ist implizite Verankerung ausreichend für professionelle Habitusbildung?
- Oder braucht es mehr explizite normative Verpflichtung?

---

## 6. Vergleich mit anderen Codes

**Code 1.1 (Direkte Nennung):** {len(code_1_1_relevant)} Findings
**Code 2.1-2.7 (Implizite Dimensionen):** {len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)} Findings

**Verhältnis:**
- Implizite zu explizite Verankerung: {(len(df[df['relevant'] == 'ja']) - len(code_1_1_relevant)) / len(code_1_1_relevant):.1f}:1

**Interpretation:**
- Chancengleichheit wird primär über **Diversität, Inklusion, Sprache etc.** thematisiert
- Explizite Benennung als Leitprinzip ist selten
- Mögliche Erklärung: "Hidden Curriculum" vs. Manifest Curriculum

---

## 7. Methodenkritische Reflexion

**Limitation der Keyword-Suche:**
- Nur 7 Keywords für Code 1.1
- Mögliche weitere Begriffe: "Gerechtigkeit", "Fairness", "gleiche Bildungschancen"
- Trade-off: Spezifität vs. Sensitivität

**Stärke:**
- Präzise Erfassung expliziter Nennungen
- Hohe Relevanz-Ratio ({len(code_1_1_relevant)/len(code_1_1_all)*100:.1f}%)

---

## Siehe auch

- **Zitate-Sammlung:** `analyse_2_zitate.md`
- **Quantitative Übersicht:** `analyse_1_code_verteilung.md`

---

**Erstellt mit:** Python (pandas)
**Methodik:** Reflexive Thematic Analysis (RTA) + Critical Expert in the Loop (CEiL)
