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

**Designhinweise (evidenzbasiert — Quellen s. Abschnitt 5)**
- **Schriftgrößen @ A0** (lesbar aus ~1 m, max. 3–4 Größen gesamt):
  Titel **85–100 pt**, Untertitel/Autorinnen ~44 pt,
  Abschnitts-Headlines **50–60 pt**, Fließtext **30–36 pt**
  (nie unter 28 pt), Bildunterschrift/Literatur **22–24 pt**.
- **Schrift:** max. 2 Familien. Empfehlung: eine serifenlose für
  Titel/Headlines + eine gut lesbare für Fließtext. Kein Comic Sans,
  keine schmalen Display-Fonts, **kein Versal-Satz** (GROSSBUCHSTABEN).
- **3-Farben-Regel:** annähernd schwarzer Text (#222), nahezu weißer
  / sehr heller Flächengrund (#F4F2FA), **eine** Akzentfarbe
  (#4B3F8C). Nicht die 8 Code-Farben aufs Poster.
- **Kontrast:** Text/Hintergrund ≥ 4,5:1 (WCAG AA). #222 auf Weiß und
  Weiß auf #4B3F8C erfüllen das.
- **Farbsehschwäche:** ~8 % der Männer rot-grün-blind. Heatmap (YlOrRd,
  Helligkeitsverlauf) ist akzeptabel — vor Druck Graustufen-A4-Test
  + Coblis/Color Oracle gegenprüfen.
- **Weißraum:** großzügig; ≥ 25 mm zwischen Sektionen, ~30 mm
  Außenrand. Weißraum ist Gestaltungsmittel, kein Verlust.
- **Kennzahlen einheitlich:** Stat-Callouts mit gleicher
  Schriftgröße, gleicher Ausrichtung, klar vom Begleittext getrennt
  (z. B. konsistente Kacheln je Dimension) — *nicht* verschieden
  große, frei im Text schwebende Riesenzahlen.
- **Autorinnennamen nur im Kontaktblock**, nicht im Titelband
  (dort nur Institution/LV). Akademische Konvention wäre Namen oben;
  bewusste Abweichung der Verfasserinnen.
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

**Affiliation (Titelband — ohne Autorinnennamen):**
Universität Graz · Institut für Bildungsforschung und
PädagogInnenbildung · Projektseminar zur Elementarpädagogik
(LV-Leitung: Ass.-Prof. Dr. phil. Eva Pölzl-Stefanec)
*Autorinnennamen erscheinen ausschließlich im Kontaktblock.*

---

### Take-home-Botschaft (Banner, volle Breite)

> **Österreichs Elementarpädagogik-Curricula bleiben überwiegend auf
> formaler Gleichheit stehen — Chancengerechtigkeit als *transformatives*
> Leitprinzip ist die curriculare Leerstelle.**

---

### 1 · Hintergrund & Problem

- Akademisierung der Elementarpädagogik — Bachelor seit 2018
- OECD-Anspruch: *Educational Equity* als Qualitätsfaktor (OECD, 2018)
- Offen: sichern die Curricula Chancengerechtigkeit **strukturell**
  oder bleibt es bei Gleichheitsrhetorik?
- Für Österreich bisher keine systematische Untersuchung
  → **TRACE-Equity schließt die Lücke.**

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
  zwischen den vier Clustern (3 PH-Cluster + FH)?

---

### 3 · Methode

**Mini-Flow (als Diagramm setzen):**

```
Vollerhebung          Qualitative          CEiL in eigener
N = 4 Cluster-     →   Inhaltsanalyse   →   Flask-Web-App      →  Levinson-
Curricula             (Kuckartz &           (mit Coding-Agent      Typologie
(9 PH + FH Wien)      Rädiker, 2022)        entwickelt)            (3 Stufen)
                      233 Keywords          1.626 → 1.061       formale Gl. →
                      8 Codes               κ = 0,71 / 0,83     kompens. →
                                                                transformativ
```

Eigens für das Projekt mit einem Coding-Agent entwickelte
Flask-Web-App (Promptotyping) für Keyword-Extraktion + CEiL-
Validierung. Deduktiv · keine LLM-Codierung (Validität latenter
Bedeutungen) · ICR κ = 0,71 / 0,83 — *gut* bis *sehr gut*
(Landis & Koch, 1977).

---

### 4 · Ergebnisse

**D1 — Explizit vs. Implizit**
- Nur **9 / 1.061** Findings (**0,8 %**) nennen Gerechtigkeit explizit
- Verhältnis **117 : 1** zugunsten impliziter Operationalisierung
- West & SüdOst: kein einziger expliziter Begriff
- → Verankerung liegt in den **Kompetenzen**, nicht in Begriffen

**D2 — Konzeptuelle Tiefe**
- Formale Gleichheit dominiert überall: **48,9–71,8 %**
- Transformative Gerechtigkeit durchgängig schwach: **4,0–11,6 %**
- → Progression *equality → equity → liberation* bricht nach
  Stufe 2 ab (vgl. Heatmap)

**D3 — Komparativer Vergleich (alle vier Cluster)**
- **West:** fokussiert professionelle Haltung, niedrigste
  Transformativ-Quote (**4,0 %**)
- **Mitte:** höchste Transformativ-Quote aller Cluster (**11,6 %**)
- **SüdOst:** ausgeglichenstes Profil unter den PHs
- **FH Campus Wien:** Sonderstellung — geringste formale Gleichheit,
  höchste kompensatorische Gerechtigkeit (**39,8 %**), professionelle
  Haltung (Code 2.7: **43,0 %**)
- → PHs untereinander **nicht homogen**; ihre Streuung ist aber
  kleiner als der Abstand zur FH → **PH vs. FH** bleibt das
  dominante Strukturmerkmal

---

### 5 · Fazit

- **Punktuell** über formale Gleichheit hinaus (kompensatorische
  Förderung, Haltungsbildung) — aber **nicht systematisch
  transformativ** verankert
- Schwäche lokalisierbar: curricular (Code 2.4) · institutionell
  (v. a. PHs) · diskursiv (fehlende Begriffsführung)
- Bestätigt die *Gleichbehandlung von Ungleichen*
  (Gomolla & Radtke, 2009)

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

**Kontakt:** Laura König — laura.koenig@edu.uni-graz.at ·
Barbara Steiner — barbara.steiner@edu.uni-graz.at
— [QR-Code: Link zu Bericht/Repo]

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
4. ~~Textumfang straffen~~ ✅ erledigt — Fließtext-Absätze
   (Hintergrund, Ergebnisse D1–D3, Fazit) in Stichpunktstil
   überführt. Verbleibende ~448 W. sind überwiegend nicht kürzbare
   fixe Elemente (HFF wörtlich, Affiliation, 5 Literaturangaben,
   Take-home, Kontakt); der eigentliche Scan-Text ist jetzt
   stichpunktbasiert. Kennzahlen unverändert.

---

## 5. Wissenschaftliche Poster-Richtlinien (Recherche-Synthese)

Evidenzbasis aus Hochschul-Leitfäden (UCLA, Yale, UChicago, Ohio
State, York) und Fachquellen (Mai 2026). Kernregeln, an denen sich
das Konzept oben orientiert:

**Text & Wortzahl**
- *Weniger Text = mehr Betrachtende.* Richtwert 250 W. (aggressiv)
  bis 300–500 W. (typisch), absolute Obergrenze ~800 W.
- Stichpunkte und unvollständige Sätze statt Fließtext; kurze
  Absätze; „Information lebt im Design, nicht im Absatz".
- Methoden als Illustration, Ergebnisse als Grafik statt Tabelle
  (hier: Methoden-Pfeilflow + Levinson-Heatmap — bereits umgesetzt).

**Schriftgrößen @ A0** (lesbar aus ~1 m)
- Titel 85–100 pt · Headlines 50–60 pt · Fließtext 30–36 pt
  (Minimum 28) · Bildunterschrift/Literatur 18–24 pt.
- Maximal 3–4 Schriftgrößen, maximal 2 Schriftfamilien.
- Kein Versal-Satz für Titel/Body; keine Display-/Schmalschriften.

**Farbe & Kontrast**
- 3-Farben-Regel: ~schwarzer Text · heller Grund · *eine*
  Akzentfarbe.
- WCAG AA: Kontrast ≥ 4,5:1 für Fließtext.
- ~8 % der Männer rot-grün-blind → rot-grün-Codierung meiden;
  Graustufen-/Simulator-Test (Coblis, Color Oracle) vor Druck.

**Layout & Lesefluss**
- Spaltenweise von oben links nach unten rechts; Lesepfad muss
  ohne Erklärung erkennbar sein.
- Großzügiger Weißraum (≥ 25 mm zwischen Sektionen); Raster für
  konsistente Ausrichtung; vorab auf Papier skizzieren.
- DACH-Hinweis: Hochformat ist an Uni-Postersessions üblich und
  hier vorgegeben — international wird oft Querformat empfohlen,
  für diesen Abgabekontext aber nicht maßgeblich.

**Häufige Fehler (Checkliste — vor Abgabe prüfen)**
- [ ] Zu viel Text / zu kleine Schrift (< 28 pt Body @ A0)
- [ ] Zu wenig Weißraum, „überladenes" Layout
- [ ] Inkonsistente Ausrichtung (kein Raster)
- [ ] > 3–4 Schriftgrößen oder > 2 Schriftfamilien
- [ ] Mehr als ~3 Farben / rot-grün-Konflikte
- [ ] Versal-Satz, Comic Sans, Display-Schriften
- [ ] Plakatmaße überschritten (Rand fehlt)
- [ ] Unklarer Lesepfad

### Quellen

- UCLA Library — Size, Layout, and Text:
  https://guides.library.ucla.edu/c.php?g=223540&p=1480858
- Ohio State — Scientific Posters: A Learner's Guide:
  https://ohiostate.pressbooks.pub/scientificposterguide/chapter/scientific-posters/
- Molecular Ecologist — 10 Simple Rules for Designing a Scientific Poster:
  https://www.molecularecologist.com/2016/06/03/10-simple-rules-for-designing-a-scientific-poster/
- Animate Your Science — Font sizes for scientific posters:
  https://www.animateyour.science/post/how-to-choose-appropriate-font-sizes-for-your-scientific-poster
- Animate Your Science — Colour-blind-friendly posters:
  https://www.animateyour.science/post/how-to-design-a-colour-blind-friendly-scientific-poster
- Yale Library — Academic Poster Accessibility:
  https://guides.library.yale.edu/academic-poster-resources/accessibility
