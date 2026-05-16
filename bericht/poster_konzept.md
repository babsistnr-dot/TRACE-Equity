# TRACE-Equity — Poster-Konzept (A0 Hochformat, klassisch-wissenschaftlich)

> Konzept + abgabefertige Textbausteine. Visuelle Umsetzung in
> PowerPoint / Affinity / LaTeX-beamerposter durch das Team.
> Format: **A0 Hochformat** (841 × 1189 mm), Leseabstand ~1,5 m.

---

## 1. Layout-Raster (A0 Hochformat, 2-Spalten-Korpus)

```
┌───────────────────────────────────────────────────────────┐
│  LOGO Uni Graz        TITEL + UNTERTITEL        LOGO/leer   │  ~12 %
│              Autorinnen · Institut · LV                     │
├───────────────────────────────────────────────────────────┤
│  ┃ TAKE-HOME-BOTSCHAFT (volle Breite, farbig hinterlegt) ┃ │  ~7 %
├──────────────────────────────┬────────────────────────────┤
│ 1  HINTERGRUND & PROBLEM      │ 4  ERGEBNISSE              │
│                               │    D1 — Explizit/Implizit  │
│ 2  FORSCHUNGSFRAGE            │                            │  ~30 %
│    HFF + D1/D2/D3             │    D2 — Konzeptuelle Tiefe │
│                               │                            │
│ 3  METHODE (Mini-Flow)        │    D3 — Komparativ         │
├──────────────────────────────┴────────────────────────────┤
│   ABBILDUNG: LEVINSON-HEATMAP (volle Breite, dominant)     │  ~22 %
│   Verteilung der 3 Gerechtigkeitsstufen je Cluster         │
├──────────────────────────────┬────────────────────────────┤
│ 5  FAZIT (Antwort auf HFF)    │ 6  HANDLUNGSEMPFEHLUNGEN   │  ~17 %
│                               │    E1 · E2 · E3            │
├──────────────────────────────┴────────────────────────────┤
│  LITERATUR (Auswahl)                      Kontakt · QR     │  ~12 %
└───────────────────────────────────────────────────────────┘
```

**Lesefluss:** Titel → Take-home → linke Spalte (Hintergrund→Frage→
Methode) → rechte Spalte (Ergebnisse D1–D3) → Heatmap als Beleg →
Fazit + Empfehlungen → Fußzeile. Klassische Z-Führung.

**Designhinweise**
- Schrift: serifenlose Headlines (z. B. Source Sans / Calibri),
  Fließtext min. 24 pt @ A0, Headlines 60–72 pt, Titel ≥ 90 pt.
- Farbpalette reduziert: 1 Akzentfarbe (Heatmap-konsistent) +
  Dunkelgrau-Text. Nicht alle 8 Code-Farben aufs Poster.
- Take-home-Banner in Akzentfarbe hinterlegt, weiße Schrift.
- Die Heatmap ist das größte Einzelelement — nicht verkleinern.
- **Druckfertige Grafik:**
  `ergebnisse/visualisierungen_vergleich/levinson_heatmap_poster.png`
  (5702 × 3100 px, 600 dpi-Export; ~193 dpi @ A0-Vollbreite,
  300 dpi bis 483 mm Breite — für 1,5 m Leseabstand scharf).
  Reproduzierbar via `python analyse_levinson_mapping.py --poster`
  (aus `scripts/`). Die 150-dpi-Version `levinson_heatmap.png` bleibt
  für den Bericht reserviert.

---

## 2. Abgabefertige Textbausteine

### Titelband

**Titel:**
TRACE-Equity

**Untertitel:**
Curriculare Verankerung von Chancengerechtigkeit in der
österreichischen Elementarpädagogik-Ausbildung

**Autorinnen / Affiliation:**
Laura König · Barbara Steiner
Universität Graz · Institut für Bildungsforschung und
PädagogInnenbildung · Projektseminar zur Elementarpädagogik
(LV-Leitung: Ass.-Prof. Dr. phil. Eva Pölzl-Stefanec)

---

### Take-home-Botschaft (Banner, volle Breite)

> **Österreichs Elementarpädagogik-Curricula bleiben überwiegend auf
> formaler Gleichheit stehen — Chancengerechtigkeit als *transformatives*
> Leitprinzip ist die curriculare Leerstelle.**

---

### 1 · Hintergrund & Problem

Mit der Akademisierung der Elementarpädagogik (Bachelor seit 2018)
stellt sich die Frage, ob die neuen Curricula den OECD-Anspruch auf
*Educational Equity* (OECD, 2018) einlösen — also Chancengerechtigkeit
strukturell sichern oder bei formaler Gleichheitsrhetorik bleiben.
Für den österreichischen Raum fehlte dazu eine systematische
Untersuchung. **TRACE-Equity schließt diese Lücke.**

---

### 2 · Forschungsfrage

**Hauptforschungsfrage**
Inwiefern gehen die Curricula der Bachelorstudiengänge
Elementarpädagogik österreichischer Hochschulen über formale
Chancengleichheit hinaus und verankern Chancengerechtigkeit als
pädagogisches Leitprinzip?

**Drei analytische Dimensionen**
- **D1 — Explizit vs. Implizit:** Begriffsnennung oder Operationali-
  sierung über Handlungskompetenzen?
- **D2 — Konzeptuelle Tiefe:** Welche Gerechtigkeitsstufe nach
  Levinson et al. (2022) dominiert?
- **D3 — Komparativer Vergleich:** Systematische Unterschiede
  zwischen den Clustern (PH vs. FH)?

---

### 3 · Methode

**Mini-Flow (als Diagramm setzen):**

```
Vollerhebung           Qualitative              Critical Expert
N = 4 Cluster-      →   Inhaltsanalyse      →    in the Loop
Curricula              (Kuckartz &               1.626 Findings
(9 PH + FH Wien)       Rädiker, 2022)            → 1.061 relevant
                       233 Keywords / 8 Codes    κ = 0,71 / 0,83
                                                       │
                                                       ▼
                            Levinson-Typologie (3 Stufen):
                       formale Gleichheit → kompensatorisch
                                → transformativ
```

Deduktives Kategoriensystem, keine LLM-Codierung (Validität latenter
Bedeutungen). Intercoder-Reliabilität: κ = 0,71 (Relevanz),
κ = 0,83 (Code) — *gut* bis *sehr gut* (Landis & Koch, 1977).

---

### 4 · Ergebnisse

**D1 — Explizit vs. Implizit**
Nur **9 von 1.061** relevanten Findings (**0,8 %**) nennen
Gerechtigkeit explizit. Verhältnis **117 : 1** zugunsten impliziter
Operationalisierung. Zwei Cluster (West, SüdOst) ganz ohne Begriff.
→ Die Verankerung liegt in den Kompetenzen, nicht in den Begriffen.

**D2 — Konzeptuelle Tiefe**
Formale Gleichheit dominiert in **allen** Clustern (**48,9–71,8 %**).
Transformative Gerechtigkeit bleibt durchgängig schwach
(**4,0–11,6 %**). → Die Progression *equality → equity → liberation*
bricht nach der zweiten Stufe ab (vgl. Heatmap).

**D3 — Komparativer Vergleich**
Die **FH Campus Wien** weicht systematisch ab: weniger formale
Gleichheit, mehr kompensatorische Gerechtigkeit (**39,8 %**) und
professionelle Haltung (Code 2.7: **43,0 %**). Die institutionelle
Differenz **PH vs. FH** ist das dominante Strukturmerkmal.

---

### 5 · Fazit

Die Curricula gehen **punktuell** über formale Gleichheit hinaus —
durch kompensatorische Förderung und Haltungsbildung —, verankern
Chancengerechtigkeit aber **nicht systematisch transformativ**.
Die Schwäche ist präzise lokalisierbar: curricular im
unterrepräsentierten Code 2.4, institutionell vor allem bei den
Pädagogischen Hochschulen, diskursiv in der fehlenden Begriffsführung.
Theoretisch bestätigt sich die *Gleichbehandlung von Ungleichen*
(Gomolla & Radtke, 2009).

---

### 6 · Handlungsempfehlungen

- **E1 — Begriff verankern:** Chancengerechtigkeit explizit auf
  Programmebene setzen (Qualifikationsprofile, Modulüberschriften).
- **E2 — Machtkritik ausbauen:** Lerngelegenheiten zu institutioneller
  Diskriminierung, Bildungsprivilegien und vorurteilsbewussten
  Ansätzen institutionalisieren.
- **E3 — Transfer-Signal nutzen:** FH-Wien-Profil als Referenzpunkt
  im hochschulübergreifenden Dialog.

---

### Fußzeile — Literatur (Auswahl)

Gomolla, M., & Radtke, F.-O. (2009). *Institutionelle Diskriminierung*.
VS Verlag. · Kuckartz, U., & Rädiker, S. (2022). *Qualitative
Inhaltsanalyse* (5. Aufl.). Beltz Juventa. · Levinson, M., Geron, T.,
& Brighouse, H. (2022). Conceptions of educational equity. *AERA Open,
8*. · OECD. (2018). *Equity in education*. OECD Publishing. ·
Stojanov, K. (2011). *Bildungsgerechtigkeit*. VS Verlag.

**Kontakt:** laura.koenig@edu.uni-graz.at ·
barbara.steiner@edu.uni-graz.at — [QR-Code: Link zu Bericht/Repo]

---

## 3. Was bewusst NICHT aufs Poster kommt

- Vollständige Code-Tabellen (A.3.4 / A.3.5) — nur Heatmap.
- ICR-Detailtabelle — eine κ-Zeile in der Methode genügt.
- Theorie-Herleitung Stojanov/Levinson im Detail — nur Kurzbezug.
- Limitationen-Block — auf Poster verzichtbar (im mündlichen
  Gespräch an der Postersession adressieren).

## 4. Offene Punkte vor Druck

1. Uni-Graz-Poster-Vorlage/Logo bei LV-Leitung anfragen?
2. ~~Heatmap in Druckauflösung~~ ✅ erledigt — `levinson_heatmap_poster.png`
   (600 dpi) liegt unter `ergebnisse/visualisierungen_vergleich/`.
3. QR-Ziel festlegen (öffentliches Repo? PDF des Berichts?).
