---
title: "TRACE-Equity — Curriculare Verankerung von Chancengerechtigkeit in der österreichischen Elementarpädagogik-Ausbildung"
subtitle: "Forschungsbericht"
author:
  - Barbara Steiner
  - Laura König
date: "Juni 2026"
lang: de
papersize: a4
fontsize: 11pt
geometry:
  - margin=2.5cm
linestretch: 1.3
---

# 1. Einleitung und Forschungsfragen

Mit der Einführung der Bachelorstudiengänge Elementarpädagogik im Jahr
2018 vollzog Österreich einen historischen Professionalisierungsschritt
(Vollmann & Fageth, 2022). Zeitgleich identifiziert die OECD (2018)
Educational Equity als zentralen Qualitätsfaktor früher Bildung: Nicht
die Herkunft, sondern das Potential eines Kindes soll den Bildungsweg
bestimmen. Für die Ausbildung folgt daraus die Frage, ob die neuen
Curricula diesen Anspruch einlösen. Eine systematische empirische
Untersuchung fehlt für den österreichischen Raum. TRACE-Equity schließt
diese Lücke durch eine qualitative Inhaltsanalyse aller österreichischen
Bachelor-Curricula auf Hochschulebene.

**Hauptforschungsfrage:** Inwiefern gehen die Curricula der
Bachelorstudiengänge Elementarpädagogik österreichischer Hochschulen
über formale Chancengleichheit hinaus und verankern Chancengerechtigkeit
als pädagogisches Leitprinzip?

Die Hauptforschungsfrage wird in drei analytische Dimensionen
ausdifferenziert:

- **D1 — Explizit vs. Implizit:** Erschöpft sich die curriculare
  Verankerung in expliziten Begriffsnennungen, oder wird Chancen-
  gerechtigkeit über pädagogische Handlungskompetenzen operationalisiert?
- **D2 — Konzeptuelle Tiefe:** Welches Gerechtigkeitsverständnis nach
  Levinson et al. (2022) dominiert — formale Gleichheit, kompensatorische
  oder transformative Gerechtigkeit?
- **D3 — Komparativer Vergleich:** Lassen sich systematische Unterschiede
  zwischen den vier Clustern identifizieren, insbesondere zwischen
  Pädagogischen Hochschulen und Fachhochschule?

# 2. Methodik

## 2.1 Datenkorpus

Das Sample umfasst N = 4 Curricula, was einer Vollerhebung der
österreichischen Bachelor-Curricula für Elementarpädagogik im öffentlichen
Sektor entspricht. Die Pädagogischen Hochschulen sind in
Entwicklungsverbünde organisiert, sodass ein Curriculum jeweils mehrere
Standorte abdeckt. Insgesamt sind elf Pädagogische Hochschulen und die FH
Campus Wien abgedeckt (vgl. Tabelle 1 in Abschnitt 3.1). Die Validität
des Samples wurde anhand der vier Kriterien nach Morgan (2022) geprüft:
Authentizität (offiziell akkreditierte Originaldokumente),
Glaubwürdigkeit (rechtlich bindende Studienpläne), Repräsentativität
(Vollerhebung durch Cluster-Struktur) und Bedeutung (Curricula definieren
den normativen Rahmen der Ausbildung).

## 2.2 Kategoriensystem

Das Kategoriensystem umfasst acht Codes, denen insgesamt 233 Keywords
zugeordnet sind. Code 1.1 erfasst die direkte Nennung von
Gerechtigkeitsbegriffen (z. B. *Chancengleichheit*, *Bildungsgerechtigkeit*).
Die Codes 2.1–2.7 operationalisieren pädagogische Handlungskompetenzen
(Diversität, Inklusion, individuelle Förderung, Abbau von Benachteiligung,
Bildungspartnerschaft, sprachliche Bildung, professionelle Haltung).

Für die Auswertung zu Dimension 2 werden diese Codes über das Mapping aus
Levinson et al. (2022) den drei Gerechtigkeitsstufen zugeordnet: Formale
Gleichheit (Codes 2.1, 2.2), kompensatorische Gerechtigkeit (Codes 2.3,
2.6) und transformative Gerechtigkeit (Code 2.4). Die Codes 2.5
(Bildungspartnerschaft) und 2.7 (professionelle Haltung) werden als
Querschnittskategorien separat ausgewiesen, da sie orthogonal zu den drei
Stufen liegen. Das Kodiermanual dient als *Single Source of Truth*: Sowohl
die Analyse-App als auch die späteren Auswertungsskripte greifen
dynamisch auf dieselbe Keyword-Liste zu.

## 2.3 Keyword-basierte Analyse mit Expertenvalidierung (CEiL)

Die Analyse erfolgt in zwei Stufen. In einem ersten, automatisierten
Schritt extrahiert eine eigens entwickelte Flask-Webapplikation alle
Textstellen aus den Curriculum-PDFs, in denen ein Keyword des
Kategoriensystems auftritt. Jedes Finding wird mit einem Kontextfenster
von ±200 Zeichen und einer vorläufigen Code-Zuordnung versehen.

Der zweite Schritt ist die Expertenvalidierung durch beide
Kodiererinnen (*Critical Expert in the Loop*). Über die Web-App wird pro
Finding (a) die Relevanz (ja/nein) und (b) der bestätigte oder korrigierte
Code entschieden. Die explizite Trennung zwischen automatischer
Vor-Codierung (`code`) und expertenvalidiertem Endbefund (`confirmed_code`)
gewährleistet Transparenz und Reproduzierbarkeit. Auf eine
LLM-gestützte Codierung wurde verzichtet, da generative KI komplexe
Kontextbedeutungen tendenziell auf dekontextualisierte Kategorien
reduziert und latente Bedeutungen oder Machtstrukturen häufig nicht
erfasst (Tai et al., 2024).

## 2.4 Gütekriterien und Intercoder-Reliabilität

Vor der unabhängigen Kodierung wurde anhand des Clusters Mitte eine
Kalibrierungsphase durchgeführt, in der geteilte Entscheidungsregeln
formuliert wurden. Die Intercoder-Reliabilität wurde am Cluster SüdOst
(n = 272 Findings) bestimmt: Beide Kodiererinnen validierten alle
Findings unabhängig voneinander.

Die Übereinstimmung liegt für die Relevanz-Entscheidung bei κ = 0,71
(87,1 % Übereinstimmung) und für die Code-Zuordnung bei κ = 0,83
(89,7 %) und damit im Bereich *gut* bis *sehr gut* (Landis & Koch, 1977).
Die höhere Übereinstimmung bei der Code-Zuordnung spiegelt die stärkere
Strukturiertheit der Kategorien gegenüber der stärker interpretativen
Relevanz-Entscheidung. Die 52 nicht-übereinstimmenden Fälle wurden in
einer Konsenskonferenz bereinigt; die Ergebnisse flossen in das Feld
`confirmed_code` ein. Details finden sich in Anhang A.2.

# 3. Ergebnisse

## 3.1 Datenübersicht

**Tabelle 1.** *Zusammensetzung des Datenkorpus und Umfang der Analyse*

| Cluster | Hochschulen | Findings | Relevant | Relevanzrate | Code 1.1 |
|---|---|---:|---:|---:|---:|
| West | PH Tirol, PH Vorarlberg, KPH Edith Stein | 468 | 347 | 74,1 % | 0 |
| Mitte | PH OÖ, PH Linz, PH Salzburg | 516 | 259 | 50,2 % | 8 |
| SüdOst | PH Burgenland, PH Kärnten, PH Steiermark | 272 | 192 | 70,6 % | 0 |
| FH Wien | FH Campus Wien | 370 | 263 | 71,1 % | 1 |
| **Gesamt** | N = 4 Cluster | **1.626** | **1.061** | **65,3 %** | **9** |

Aus den vier Curricula resultierten insgesamt 1.626 Keyword-Treffer, von
denen 1.061 (65,3 %) im CEiL-Verfahren als inhaltlich relevant
klassifiziert wurden. Die deutliche Varianz der Relevanzraten zwischen
50,2 % (Mitte) und 74,1 % (West) wird in Abschnitt 3.4 eigens aufgegriffen.

## 3.2 Dimension 1 — Explizit vs. Implizit

**Tabelle 2.** *Verhältnis expliziter zu impliziter Verankerung je Cluster*

| Cluster | Code 1.1 (explizit) | Relevant implizit | Verhältnis |
|---|---:|---:|---:|
| West | 0 | 347 | nur implizit |
| Mitte | 8 | 251 | 31 : 1 |
| SüdOst | 0 | 192 | nur implizit |
| FH Wien | 1 | 262 | 262 : 1 |
| **Gesamt** | **9** | **1.052** | **117 : 1** |

Die explizite Verankerung von Chancengerechtigkeit ist über alle Cluster
hinweg marginal: Nur 9 von 1.061 relevanten Findings (0,8 %) nennen
Begriffe wie *Chancengleichheit*, *Chancengerechtigkeit* oder
*Bildungsgerechtigkeit* direkt. Zwei der vier Cluster verzichten
vollständig auf die Begriffe. Auf jede explizite Nennung kommen 117
Findings, in denen Chancengerechtigkeit *implizit* — über pädagogische
Handlungskompetenzen — operationalisiert wird.

Nur das Curriculum des Clusters Mitte führt den Begriff in der Einleitung
programmatisch ein:

> „Die Forderung nach Bildungsgerechtigkeit, die in der österreichischen
> Bundesverfassung in Bezug auf Chancengleichheit und Teilhabegerechtigkeit
> als Ziele genannt werden, bildet die Basis." (Cluster Mitte, S. 10)

Die übrigen Code-1.1-Findings in Mitte verweisen auf diese einleitende
Rahmung; sie repräsentieren also keine systematische Durchdringung des
Curriculums, sondern einen diskursiven Rahmen. Die zentrale Erkenntnis der
ersten Dimension ist somit ein **Implementierungsspalt zwischen
bildungspolitischem Labeling und curricularer Substanz**: Die Curricula
nennen Chancengerechtigkeit kaum beim Namen, adressieren sie aber
über ein breites Spektrum pädagogischer Kompetenzen.

## 3.3 Dimension 2 — Konzeptuelle Tiefe (Levinson-Mapping)

![Levinson-Heatmap: Verteilung der drei Gerechtigkeitsstufen je Cluster (nur relevante Findings, normalisiert pro Cluster über die drei Stufen). Abdeckungsraten siehe Tabelle 3.](abbildungen/levinson_heatmap.png){#fig:heatmap width=100%}

**Tabelle 3.** *Levinson-Verteilung numerisch (Anteile über die drei Stufen)*

| Cluster | Formale Gleichheit | Kompensatorisch | Transformativ | Abdeckung |
|---|---:|---:|---:|---:|
| West | 67,1 % | 28,9 % | 4,0 % | 64,8 % |
| Mitte | 71,8 % | 16,6 % | 11,6 % | 69,9 % |
| SüdOst | 69,7 % | 23,5 % | 6,8 % | 68,8 % |
| FH Wien | 48,9 % | 39,8 % | 11,3 % | 50,6 % |

Die Prozentwerte beziehen sich auf die Summe der drei Levinson-Stufen
(= 100 %). Die *Abdeckungsrate* gibt an, welcher Anteil der relevanten
Findings pro Cluster in diese Summe eingeht; die übrigen Findings
entfallen auf die Querschnittscodes 2.5 (Bildungspartnerschaft) und 2.7
(professionelle Haltung) sowie auf Code 1.1 und werden separat
ausgewiesen.

Die Heatmap zeigt ein konsistentes Grundmuster bei gleichzeitig deutlicher
institutioneller Streuung. In allen vier Clustern dominiert die Stufe der
**formalen Gleichheit** mit Anteilen zwischen 48,9 % (FH Wien) und 71,8 %
(Mitte); hier wirken jene Codes, die Diversitätsanerkennung und Inklusion
als Zugangs- und Partizipationsbedingungen thematisieren. Demgegenüber
bleibt die **transformative Gerechtigkeit** durchgängig schwach und
erreicht nur Anteile zwischen 4,0 % (West) und 11,6 % (Mitte);
machtkritische und strukturverändernde Perspektiven — etwa auf
institutionelle Diskriminierung oder Empowerment — sind curricular
unterrepräsentiert. Innerhalb dieses Grundmusters nimmt die FH Campus
Wien eine Sonderstellung ein: Mit 39,8 % weist sie den höchsten Anteil
**kompensatorischer Gerechtigkeit** (individuelle Förderung, sprachliche
Bildung) und zugleich den geringsten Anteil formaler Gleichheit auf.

Die inhaltliche Signatur der transformativen Stufe lässt sich an einem
Finding aus Cluster Mitte illustrieren:

> „Haben umfangreiches Wissen bezüglich Konzepten der vorurteilsbewussten
> Bildung und sind sich der Bedeutung kindlicher Erfahrungen mit Vielfalt
> bewusst." (Cluster Mitte, S. 106)

Solche Formulierungen, die aktive Reflexion und Haltungsbildung gegen
Benachteiligung adressieren, bleiben die Ausnahme. Die curriculare
Schwerlast liegt auf Diversitätsanerkennung und Teilhabe, nicht auf
Machtkritik.

## 3.4 Dimension 3 — Komparativer Vergleich

Der komparative Vergleich bestätigt das Levinson-Muster auf Code-Ebene
und legt ein systematisch abweichendes Profil der FH Campus Wien frei.
Vorangestellt ist ein methodischer Befund: Die Relevanzraten variieren
deutlich zwischen 50,2 % (Mitte) und 74,1 % (West). Diese Varianz
interpretieren wir **nicht** als inhaltlichen Unterschied in der
Verankerung von Chancengerechtigkeit, sondern als Hinweis auf
unterschiedliche curriculare Sprachdichte: Ein niedrigerer Wert deutet
darauf hin, dass ein größerer Anteil der Keyword-Treffer in generischen
Kontexten (z. B. Modulüberschriften, Literaturverzeichnisse) auftritt
und im CEiL-Verfahren als nicht einschlägig klassifiziert wurde.

**Tabelle 4.** *Auszug Code-Verteilung — Codes mit größter Spannweite
zwischen Clustern*

| Code | West | Mitte | SüdOst | FH Wien |
|---|---:|---:|---:|---:|
| 2.1 Diversität & Heterogenität | 32,3 % | 35,1 % | 39,1 % | 18,3 % |
| 2.3 Individuelle Förderung | 8,9 % | 3,9 % | 8,9 % | 12,9 % |
| 2.7 Professionelle Haltung | 26,5 % | 21,6 % | 18,2 % | 43,0 % |

Die FH Campus Wien weist bei Code 2.1 (Diversität & Heterogenität) mit
18,3 % einen deutlich geringeren Anteil als die drei PH-Cluster (32,3 %
bis 39,1 %) auf; umgekehrt ist sie bei Code 2.7 (professionelle Haltung)
mit 43,0 % mehr als doppelt so stark vertreten wie SüdOst (18,2 %) und
erhöht auch bei Code 2.3 (individuelle Förderung) gegenüber Mitte (3,9 %).
Dieses Muster ist konsistent mit dem Levinson-Befund aus Abschnitt 3.3:
Ein höherer Anteil bei Codes 2.3 und 2.7 verschiebt das Profil in
Richtung kompensatorischer und professioneller Handlungslogik, ein
geringerer Anteil bei Code 2.1 reduziert den Bereich formaler Gleichheit.

Die Pädagogischen Hochschulen bleiben untereinander nicht homogen. West
zeigt die stärkste Ausprägung bei Diversität und professioneller Haltung,
Mitte die höchste Transformativ-Quote (11,6 %), SüdOst das ausgeglichenste
Profil zwischen den PHs. Die Streuung ist aber durchweg kleiner als der
Abstand zur FH Wien, sodass sich der institutionelle Unterschied (PH vs.
FH) als **dominantes Strukturmerkmal** der Ausbildungslandschaft
identifizieren lässt.

# 4. Diskussion und Beantwortung der Hauptforschungsfrage

## 4.1 Synthese der drei Dimensionen

Die Befunde der drei Dimensionen ergeben ein konsistentes Gesamtbild.
Die explizite curriculare Verankerung von Chancengerechtigkeit ist
marginal (D1: 0,8 % explizite Nennungen), inhaltlich wird das Konzept
überwiegend auf der Stufe **formaler Gleichheit** adressiert (D2: 49 –
72 % der Levinson-zuordenbaren Findings), während **transformative
Gerechtigkeit** in allen Clustern unterrepräsentiert bleibt (D2: 4 –
12 %). Innerhalb dieses Grundmusters hebt sich die FH Campus Wien als
einziger Cluster mit einem deutlich kompensatorischen Profil ab (D3).

Damit lässt sich die Hauptforschungsfrage präzisiert beantworten: Die
Curricula gehen punktuell über formale Chancengleichheit hinaus —
insbesondere durch kompensatorische Förderkonzepte und durch Elemente
professioneller Haltungsbildung — verankern Chancengerechtigkeit als
pädagogisches Leitprinzip aber **nicht systematisch** im Sinne einer
transformativen Gerechtigkeit. Der von der OECD (2018) formulierte
Anspruch, durch Bildungspolitik soziale Mobilität aktiv zu fördern,
findet in den analysierten Curricula nur punktuell eine Entsprechung in
machtkritischen oder strukturverändernden Lerngelegenheiten — ein
Anspruch, der allerdings über die outcome-orientierte OECD-Rahmung
hinaus eine theoretische Erweiterung im Sinne anerkennungstheoretischer
Gerechtigkeitskonzepte (Stojanov, 2011) voraussetzt.

## 4.2 Einordnung in den Fachdiskurs und Praxisimplikationen

Diese Struktur stützt die empirischen Befunde von Gomolla & Radtke
(2009), wonach formal-neutrale Routinen in Bildungsorganisationen —
*„Gleichbehandlung von Ungleichen"* — ethnische Differenz nicht nur
unbearbeitet lassen, sondern aktiv mit herstellen. Sie verweist zugleich
auf das von Stojanov (2011) rekonstruierte Spannungsfeld zwischen
verteilungs-, teilhabe- und anerkennungsorientierten
Gerechtigkeitsverständnissen, in dem anerkennungstheoretische
Perspektiven einen normativen Vorrang beanspruchen, in der
Bildungspraxis jedoch weniger präsent sind. Das abweichende Profil der
FH Campus Wien — stärker kompensatorisch, stärker
professionalisierungsbezogen — könnte Ausdruck einer unterschiedlichen
institutionellen Tradition sein; eine Einordnung, die quantitative
Dokumentenanalyse nicht leisten kann und die für eine
Anschlussuntersuchung aufzugreifen wäre.

Für die curriculare Weiterentwicklung lassen sich aus diesen Befunden
zwei Ansatzpunkte ableiten, die unterschiedliche Reichweite haben. Auf
sprachlicher Ebene könnte die explizite begriffliche Verankerung
gestärkt werden, um Chancengerechtigkeit als Leitprinzip auch in
Modulüberschriften, Lernergebnissen und Kompetenzbeschreibungen
sichtbar zu machen. Inhaltlich gewichtiger ist jedoch die Erweiterung
des Kategorienrepertoires in Richtung machtkritischer und
strukturreflexiver Lerngelegenheiten (Code 2.4), die über individuelle
Fördermaßnahmen hinausgehen. Dass eine solche Akzentverschiebung
curricular machbar ist, zeigt das Profil der FH Campus Wien.

# 5. Limitationen

Die Befunde unterliegen mehreren methodischen Einschränkungen. Eine
grundsätzliche Grenze betrifft den Gegenstand selbst: Dokumentenanalysen
erschließen nur den schriftlichen Gehalt der Curricula, nicht deren
Umsetzung im Lehrgeschehen — eine in der Curriculumforschung etablierte
Unterscheidung zwischen intendiertem und realisiertem Curriculum. Zu
den generellen Grenzen der Dokumentenanalyse zählt zudem, dass
Dokumente nicht alles abbilden, was in Institutionen tatsächlich
geschieht (Morgan, 2022). Hinzu kommt die Datengrundlage: Mit nur
einem Curriculum pro Cluster (N = 1 pro Institution) bleibt jede
Aussage strikt deskriptiv, statistische Inferenz ist auf dieser Basis
nicht möglich.

Auch das Kategoriensystem stößt an Grenzen. Die drei Levinson-Stufen
lassen sich unterschiedlich gut operationalisieren: Formale Gleichheit
wird über klare Begriffe greifbar, während transformative Gerechtigkeit
häufig in subtileren Formulierungen zum Ausdruck kommt, deren Erfassung
stärkere interpretative Leistung voraussetzt und anfälliger für
Codiervarianz ist. Die prozentuale Normalisierung pro Cluster wiederum
nivelliert Unterschiede im absoluten Datenvolumen und blendet die
Varianz der Relevanzraten im direkten Vergleich aus.

Schließlich ist der Momentaufnahme-Charakter der Erhebung zu
berücksichtigen: Curricula werden periodisch überarbeitet, und eine
Folgeerhebung könnte Veränderungen gegenüber dem hier dokumentierten
Stand 2025/26 sichtbar machen.

# Literaturverzeichnis

- Gomolla, M., & Radtke, F.-O. (2009). *Institutionelle Diskriminierung: Die Herstellung ethnischer Differenz in der Schule* (3. Aufl.). VS Verlag für Sozialwissenschaften.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174.
- Levinson, M., Geron, T., & Brighouse, H. (2022). Conceptions of educational equity. *AERA Open, 8*, 1–14.
- Morgan, H. (2022). Conducting a qualitative document analysis. *The Qualitative Report, 27*(1), 64–77.
- OECD. (2018). *Equity in education: Breaking down barriers to social mobility* (PISA). OECD Publishing.
- Stojanov, K. (2011). *Bildungsgerechtigkeit: Rekonstruktionen eines umkämpften Begriffs*. VS Verlag für Sozialwissenschaften.
- Tai, R. H., Bentley, L. R., Xia, X., Sitt, J. M., Fankhauser, S. C., Chicas-Mosier, A. M., & Monteith, B. G. (2024). An examination of the use of large language models to aid analysis of textual data. *International Journal of Qualitative Methods, 23*, 1–12.
- Vollmann, P., & Fageth, B. (2022). Thesen zum Bachelorstudium Elementarpädagogik an der Pädagogischen Hochschule der Diözese Linz. *Pädagogische Horizonte, 6*(1), 1–20.

# Anhang

## A.1 Kodiermanual-Auszug

Das vollständige Kodiermanual umfasst 233 Keywords, die acht Codes
zugeordnet sind. Der folgende Auszug beschreibt die Codes in
Kurzform; die vollständige Keyword-Liste ist im Projekt-Repository unter
`knowledge/coding_manual.md` dokumentiert.

- **Code 1.1 — Direkte Nennung:** explizite Verwendung von Begriffen wie *Chancengleichheit*, *Chancengerechtigkeit*, *Bildungsgerechtigkeit*, *Equity*.
- **Code 2.1 — Diversität & Heterogenität:** Anerkennung von Vielfalt (Geschlecht, Herkunft, Religion, Familienformen).
- **Code 2.2 — Inklusion & Partizipation:** Zugang, Teilhabe, Barrierefreiheit.
- **Code 2.3 — Individuelle Förderung & Differenzierung:** stärkenorientierte, differenzierte Förderung.
- **Code 2.4 — Abbau von Benachteiligung & Diskriminierung:** Machtkritik, Empowerment, strukturelle Veränderung.
- **Code 2.5 — Bildungspartnerschaft & Sozialraumorientierung:** Vernetzung, multiprofessionelle Teams.
- **Code 2.6 — Sprachliche Bildung & Mehrsprachigkeit:** DaZ, Literacy, Translanguaging.
- **Code 2.7 — Professionelle Haltung & Ethik:** Selbstreflexion, Werteorientierung, pädagogischer Habitus.

## A.2 Intercoder-Reliabilität — Detailtabelle

**ICR-Stichprobe:** Cluster SüdOst, n = 272 Findings, beide Kodiererinnen unabhängig.

| Maß | Wert | Bewertung (Landis & Koch, 1977) |
|---|---:|---|
| Prozent-Übereinstimmung Relevanz | 87,1 % | — |
| Cohens κ Relevanz | 0,71 | gut |
| Prozent-Übereinstimmung Code | 89,7 % | — |
| Cohens κ Code | 0,83 | sehr gut |

Häufigste Abweichungen betrafen (a) kontextarme Findings ohne
eindeutigen Equity-Bezug und (b) die Grenze zwischen Code 2.1 (Anerkennung
von Vielfalt) und Code 2.4 (Abbau von Benachteiligung). Eine
Konsenskonferenz bereinigte alle 52 nicht-übereinstimmenden Fälle. Die
finalen Kodierungen wurden in der Spalte `confirmed_code` gespeichert
und liegen allen Analysen zugrunde.

## A.3 Zusätzliche Visualisierungen

Die folgenden Abbildungen ergänzen Abschnitt 3. Sie sind im
Projekt-Repository unter
`ergebnisse/visualisierungen_vergleich/` und `ergebnisse/cluster_*/visualisierungen/`
abgelegt.

- Code-Verteilungs-Heatmap (8 Codes × 4 Cluster, prozentual)
- Grouped Bar der Code-Verteilung über alle Cluster
- Stacked Bars der Levinson-Verteilung pro Cluster (4 Stück)
- Grouped Bar der Levinson-Verteilung über alle Cluster

## A.4 Code-Verteilung — vollständige Tabelle

**A.4.1** *Prozentuale Verteilung pro Cluster (Summe je Spalte = 100 %)*

| Code | West | Mitte | SüdOst | FH Wien |
|---|---:|---:|---:|---:|
| Code 1.1 | 0,0 % | 3,1 % | 0,0 % | 0,4 % |
| Code 2.1 | 32,3 % | 35,1 % | 39,1 % | 18,3 % |
| Code 2.2 | 11,2 % | 15,1 % | 8,9 % | 6,5 % |
| Code 2.3 | 8,9 % | 3,9 % | 8,9 % | 12,9 % |
| Code 2.4 | 2,6 % | 8,1 % | 4,7 % | 5,7 % |
| Code 2.5 | 8,6 % | 5,4 % | 13,0 % | 6,1 % |
| Code 2.6 | 9,8 % | 7,7 % | 7,3 % | 7,2 % |
| Code 2.7 | 26,5 % | 21,6 % | 18,2 % | 43,0 % |

**A.4.2** *Absolute Zahlen (relevante Findings)*

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
| **Summe** | **347** | **259** | **192** | **263** |
