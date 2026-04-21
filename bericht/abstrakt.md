---
title: "TRACE-Equity — Abstrakt"
subtitle: "Methodenskizze, theoretische Perspektive und methodische Herangehensweise"
author:
  - Barbara Steiner
  - Laura König
date: "SS 2026"
lang: de
papersize: a4
fontsize: 11pt
geometry:
  - margin=2.5cm
linestretch: 1.3
---

<!--
Arbeitsauftrag (LV 420.810 Forschungsmethoden, Moser, WS25/SS26):
Maximal 3 Seiten. Methodenskizze (zentrale Begriffe), Literaturreferenzen
zur theoretischen Perspektive und eine Skizze der methodischen
Herangehensweise der Aufbereitung der Daten und der Auswertung der Daten.
Keine Ergebnisse.

Seitenbudget:
- § 1 Theoretische Perspektive + Literatur ~500 W. / 1 S.
- § 2 Methodenskizze + zentrale Begriffe ~500 W. / 1 S.
- § 3 Datenaufbereitung + Auswertung ~500 W. / 1 S.
- Literaturverzeichnis: außerhalb des 3-Seiten-Budgets

Reihenfolge: Theorie → Methode → Operation (sinnvoller als die
Auftragsreihenfolge, da § 2 auf § 1 aufbaut). Falls die LV strikt
die Auftragsreihenfolge verlangt → vor Abgabe umordnen.
-->

# 1. Theoretische Perspektive

<!--
Ziel: Die theoretische Rahmung, auf der das Projekt ruht, in ~500 W.
skizzieren und die zentralen Referenzen setzen. KEINE Methoden,
KEINE Ergebnisse.

Bausteine:
- Gegenstand und Forschungslücke: Bachelorisierung der österreichischen
  Elementarpädagogik ab 2018 (Vollmann & Fageth, 2022) — normative
  Rahmensetzung ohne systematische empirische Curriculum-Analyse
  zum Themenfeld Chancengerechtigkeit.
- Begriffliche Spannung Chancengleichheit vs. Chancengerechtigkeit:
  formale Zugangsgleichheit vs. substantielle Gerechtigkeit im
  Bildungssystem (Stojanov, 2011). Anerkennungstheoretische
  Perspektive als normativer Vorrang.
- Educational Equity als bildungspolitischer Begriff (OECD, 2018):
  Potential statt Herkunft als Determinante des Bildungsweges.
- Theoretisches Leitraster: Levinson, Geron & Brighouse (2022) mit
  der Progression equality → equity → liberation. In TRACE-Equity
  adaptiert zu einer dreistufigen Typologie: formale Gleichheit,
  kompensatorische Gerechtigkeit, transformative Gerechtigkeit.
  Ehrlichkeitsformel „in Anlehnung an".
- Anschlusslinien im deutschsprachigen Diskurs: Gomolla & Radtke
  (2009) zu institutioneller Diskriminierung; Prengel zu inklusiver
  Pädagogik; Fröhlich-Gildhoff zur Professionalisierung (optional,
  falls Platz).
- Hauptforschungsfrage: Inwiefern gehen die Curricula der
  österreichischen Bachelorstudiengänge Elementarpädagogik über
  formale Chancengleichheit hinaus und verankern Chancengerechtigkeit
  als pädagogisches Leitprinzip?
-->

# 2. Methodenskizze — zentrale Begriffe

<!--
Ziel: Die methodische Grundorientierung und die zentralen Begriffe
der Auswertungsstrategie in ~500 W. einführen. Keine Operation
(das kommt in § 3), sondern die konzeptuelle Ebene.

Bausteine:
- Qualitative Inhaltsanalyse (QCA) nach Kuckartz & Rädiker (2022)
  als methodisches Rückgrat: strukturiert, regelgeleitet,
  intersubjektiv nachvollziehbar.
- Deduktives Kategoriensystem aus dem Kodiermanual:
  8 Codes (Code 1.1 direkte Nennung; Codes 2.1–2.7 pädagogische
  Handlungskompetenzen). 233 Keywords.
- Single-Source-of-Truth-Prinzip: `knowledge/coding_manual.md` ist
  die einzige Quelle der Keyword-Liste; Analyse-App und
  Auswertungsskripte greifen dynamisch darauf zu.
- Critical Expert in the Loop (CEiL): Jede keywordbasiert generierte
  Fundstelle wird von beiden Kodiererinnen manuell validiert
  (Relevanz + Code-Bestätigung/-Korrektur). Trennung zwischen
  automatischer Vor-Codierung (`code`) und expertenvalidiertem
  Endbefund (`confirmed_code`).
- Intercoder-Reliabilität (Cohens κ) als Gütekriterium; κ=0,71
  (Relevanz) bzw. κ=0,83 (Code-Zuordnung) — Interpretation nach
  Landis & Koch (1977).
- Verzicht auf LLM-Codierung begründet: Tendenz zur Dekontextuali-
  sierung, Gefahr des Übersehens latenter Machtstrukturen (Tai
  et al., 2024).
- Auswertungsstrategie entlang drei Dimensionen: D1 explizite vs.
  implizite Verankerung, D2 konzeptuelle Tiefe (Levinson-Mapping),
  D3 clusterkomparativer Vergleich. Nur beschreiben, NICHT auswerten.
-->

# 3. Datenaufbereitung und Auswertung

<!--
Ziel: Den Weg von den Quelldokumenten zur Auswertung in ~500 W.
schildern. Wieder: OPERATION, nicht Ergebnis.

Bausteine:
- Korpus: Vollerhebung der N=4 Bachelor-Curricula für Elementar-
  pädagogik im öffentlichen Sektor Österreichs. Pädagogische
  Hochschulen sind in Entwicklungsverbünde organisiert (3 Cluster
  West/Mitte/SüdOst, 11 PHs) plus FH Campus Wien.
- Qualitätsprüfung der Dokumente nach den vier Kriterien nach
  Morgan (2022): Authentizität, Glaubwürdigkeit, Repräsentativität,
  Bedeutung.
- Datenaufbereitung: PDF → Text-Extraktion (Flask-Webapplikation,
  eigens entwickelt) → keywordbasierte Vorsuche → Kontextfenster
  ±200 Zeichen → vorläufige Code-Zuordnung. Ergebnis: N=1.626
  Rohfindings, davon 1.061 nach CEiL als relevant klassifiziert
  (Validierungsquote dokumentiert, ergebnisoffen).
- Auswertungsprozess (zweistufig):
  1. Kalibrierungsphase: Beide Kodiererinnen kodieren gemeinsam
     ein Referenzcluster (Mitte) und entwickeln geteilte
     Entscheidungsregeln, insbesondere zur Unterscheidung von
     Code 2.1 (Anerkennung Diversität) und Code 2.4 (Abbau
     Benachteiligung).
  2. Unabhängige Kodierung der übrigen Cluster; Intercoder-
     Reliabilität am Cluster SüdOst bestimmt; Konsenskonferenz
     zur Klärung der 52 nicht-übereinstimmenden Fälle.
- Dreidimensionale Auswertung:
  - D1 operationalisiert über das Verhältnis Code-1.1- zu
    impliziten Findings pro Cluster.
  - D2 über die an Levinson et al. (2022) angelehnte Zuordnung
    der Codes zu den drei Gerechtigkeitsstufen (formale
    Gleichheit: 2.1/2.2; kompensatorisch: 2.3/2.6; transformativ:
    2.4); Querschnittscodes 2.5/2.7 separat ausgewiesen.
  - D3 über deskriptiv-komparative Profile auf Code-Ebene
    (PH vs. FH, PH untereinander).
- Reproduzierbarkeit: Alle Auswertungsskripte greifen auf dieselbe
  `export_clean.csv` pro Cluster zu; Feld `confirmed_code` ist
  kanonisch; 62 automatisierte Tests sichern Datenkonsistenz.
-->

# Literaturverzeichnis

<!--
Durchgang A: Nur Literatur-Stubs. APA-Formatierung in Durchgang C.
Primärliteratur (im Abstrakt zitiert):
-->

- Gomolla, M., & Radtke, F.-O. (2009). *Institutionelle Diskriminierung*. VS Verlag.
- Kuckartz, U., & Rädiker, S. (2022). *Qualitative Inhaltsanalyse*. Beltz Juventa.
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174.
- Levinson, M., Geron, T., & Brighouse, H. (2022). Conceptions of educational equity. *AERA Open, 8*, 1–14.
- Morgan, H. (2022). Conducting a qualitative document analysis. *The Qualitative Report, 27*(1), 64–77.
- OECD. (2018). *Equity in education: Breaking down barriers to social mobility*. OECD Publishing.
- Stojanov, K. (2011). *Bildungsgerechtigkeit*. VS Verlag.
- Tai, R. H., Bentley, L. R., Xia, X., Sitt, J. M., Fankhauser, S. C., Chicas-Mosier, A. M., & Monteith, B. G. (2024). An examination of the use of large language models to aid analysis of textual data. *International Journal of Qualitative Methods, 23*, 1–12.
- Vollmann, P., & Fageth, B. (2022). Thesen zum Bachelorstudium Elementarpädagogik. *Pädagogische Horizonte, 6*(1), 1–20.
