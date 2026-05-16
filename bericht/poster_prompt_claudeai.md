# Claude.ai-Prompt für das TRACE-Equity-Poster (A0, Artifact)

> **Verwendung:** Auf claude.ai neuen Chat öffnen, die Datei
> `ergebnisse/visualisierungen_vergleich/levinson_heatmap_poster.png`
> an die Nachricht anhängen, dann den **gesamten Block unter „PROMPT"**
> hineinkopieren und absenden. Schritt-für-Schritt-Anleitung: siehe
> `poster_konzept.md` / Chat.

---

## PROMPT

Du bist Grafik- und Informationsdesigner:in für wissenschaftliche
Konferenzposter. Erstelle ein **einzelnes, in sich geschlossenes
HTML-Artifact** (HTML + CSS inline, keine externen Abhängigkeiten) für
ein wissenschaftliches Poster.

### Format & Technik
- **A0 Hochformat**, exakt 841 mm breit × 1189 mm hoch. Setze den
  Poster-Container auf `width: 841mm; height: 1189mm;` und ergänze
  `@page { size: A0 portrait; margin: 0; }` sowie passende
  `print-color-adjust: exact;`-Regeln, damit Hintergrundfarben beim
  PDF-Export erhalten bleiben.
- Innenrand (Padding) ca. 30 mm.
- Schrift: serifenlose Familie (System-Stack:
  `-apple-system, "Segoe UI", Roboto, sans-serif`). Fließtext
  ≥ 24 pt, Abschnitts-Headlines 48–60 pt, Take-home-Banner ~40 pt,
  Haupttitel ≥ 80 pt. Alles muss aus 1,5 m lesbar sein.
- Farbpalette reduziert: Akzentfarbe **#4B3F8C** (Violett), Text
  **#222**, Flächen weiß / sehr helles Grau (#F4F2FA). Keine bunten
  Spielereien — seriös, akademisch.
- Oben rechts und oben links je ein leerer Platzhalter-Kasten
  (gestrichelter Rahmen, Text „Logo Uni Graz") für späteres Logo.

### Layout (klassisch-wissenschaftlich, von oben nach unten)
1. **Titelband** (volle Breite): Titel groß, darunter Untertitel,
   darunter Autorinnen/Affiliation. Logo-Platzhalter links & rechts.
2. **Take-home-Banner** (volle Breite, Akzentfarbe hinterlegt, weiße
   fette Schrift, zentriert).
3. **Zweispaltiger Korpus:**
   - Linke Spalte: „1 Hintergrund & Problem", „2 Forschungsfrage",
     „3 Methode".
   - Rechte Spalte: „4 Ergebnisse" mit den drei Unterblöcken D1, D2, D3.
4. **Levinson-Heatmap** (volle Breite, größtes Einzelelement): das an
   diese Nachricht angehängte Bild einbetten. Falls kein Bild
   vorhanden ist, baue die Heatmap als HTML/CSS-Gitter aus den Daten
   im Abschnitt „Heatmap-Daten" nach (3 Zeilen × 4 Spalten, Zellen
   nach Wert von hellgelb→rot eingefärbt, Prozentzahl in jeder Zelle).
   Bildunterschrift darunter.
5. **Zweispaltig:** linke Spalte „5 Fazit", rechte Spalte
   „6 Handlungsempfehlungen" (E1/E2/E3).
6. **Fußzeile** (volle Breite, kleiner): „Literatur (Auswahl)" links,
   „Kontakt" rechts, dazu ein Platzhalter-Quadrat „QR".

Nummerierte Abschnitts-Headlines mit Akzentfarbe. Großzügige
Weißräume, klare Trennlinien. Der Methode-Block (3) soll als
**horizontales Pfeil-Flussdiagramm** gestaltet sein, nicht als
Fließtext.

### Inhalte (wörtlich übernehmen)

**Titel:** TRACE-Equity

**Untertitel:** Curriculare Verankerung von Chancengerechtigkeit in
der österreichischen Elementarpädagogik-Ausbildung

**Autorinnen/Affiliation:** Laura König · Barbara Steiner —
Universität Graz · Institut für Bildungsforschung und
PädagogInnenbildung · Projektseminar zur Elementarpädagogik
(LV-Leitung: Ass.-Prof. Dr. phil. Eva Pölzl-Stefanec)

**Take-home-Banner:** Österreichs Elementarpädagogik-Curricula bleiben
überwiegend auf formaler Gleichheit stehen — Chancengerechtigkeit als
*transformatives* Leitprinzip ist die curriculare Leerstelle.

**1 Hintergrund & Problem:** Mit der Akademisierung der
Elementarpädagogik (Bachelor seit 2018) stellt sich die Frage, ob die
neuen Curricula den OECD-Anspruch auf *Educational Equity* (OECD,
2018) einlösen — also Chancengerechtigkeit strukturell sichern oder
bei formaler Gleichheitsrhetorik bleiben. Für den österreichischen
Raum fehlte dazu eine systematische Untersuchung. TRACE-Equity
schließt diese Lücke.

**2 Forschungsfrage — Hauptforschungsfrage:** Inwiefern gehen die
Curricula der Bachelorstudiengänge Elementarpädagogik österreichischer
Hochschulen über formale Chancengleichheit hinaus und verankern
Chancengerechtigkeit als pädagogisches Leitprinzip?
*Drei Dimensionen:* D1 — Explizit vs. Implizit (Begriffsnennung oder
Operationalisierung über Handlungskompetenzen?); D2 — Konzeptuelle
Tiefe (welche Gerechtigkeitsstufe nach Levinson et al. 2022
dominiert?); D3 — Komparativer Vergleich (Unterschiede zwischen
Clustern, PH vs. FH?).

**3 Methode (als Pfeil-Flow):** Vollerhebung N = 4 Cluster-Curricula
(9 PH + FH Campus Wien) → Qualitative Inhaltsanalyse (Kuckartz &
Rädiker, 2022), deduktiv, 233 Keywords / 8 Codes → Critical Expert in
the Loop: 1.626 Findings → 1.061 relevant (κ = 0,71 Relevanz;
κ = 0,83 Code) → Levinson-Typologie (3 Stufen): formale Gleichheit →
kompensatorisch → transformativ. Zusatz klein darunter: Keine
LLM-Codierung (Validität latenter Bedeutungen); κ-Werte *gut* bis
*sehr gut* (Landis & Koch, 1977).

**4 Ergebnisse:**
- *D1 — Explizit vs. Implizit:* Nur 9 von 1.061 relevanten Findings
  (0,8 %) nennen Gerechtigkeit explizit. Verhältnis 117 : 1 zugunsten
  impliziter Operationalisierung. Zwei Cluster (West, SüdOst) ganz
  ohne Begriff. → Die Verankerung liegt in den Kompetenzen, nicht in
  den Begriffen.
- *D2 — Konzeptuelle Tiefe:* Formale Gleichheit dominiert in allen
  Clustern (48,9–71,8 %). Transformative Gerechtigkeit bleibt
  durchgängig schwach (4,0–11,6 %). → Die Progression equality →
  equity → liberation bricht nach der zweiten Stufe ab (siehe
  Heatmap).
- *D3 — Komparativer Vergleich:* Die FH Campus Wien weicht
  systematisch ab: weniger formale Gleichheit, mehr kompensatorische
  Gerechtigkeit (39,8 %) und professionelle Haltung (Code 2.7:
  43,0 %). Die institutionelle Differenz PH vs. FH ist das dominante
  Strukturmerkmal.

**Bildunterschrift Heatmap:** Verteilung der drei Gerechtigkeitsstufen
je Cluster (relevante Findings, normalisiert über die drei Stufen pro
Cluster).

**5 Fazit:** Die Curricula gehen punktuell über formale Gleichheit
hinaus — durch kompensatorische Förderung und Haltungsbildung —,
verankern Chancengerechtigkeit aber nicht systematisch transformativ.
Die Schwäche ist präzise lokalisierbar: curricular im
unterrepräsentierten Code 2.4, institutionell vor allem bei den
Pädagogischen Hochschulen, diskursiv in der fehlenden Begriffsführung.
Theoretisch bestätigt sich die *Gleichbehandlung von Ungleichen*
(Gomolla & Radtke, 2009).

**6 Handlungsempfehlungen:**
- E1 — Begriff verankern: Chancengerechtigkeit explizit auf
  Programmebene setzen (Qualifikationsprofile, Modulüberschriften).
- E2 — Machtkritik ausbauen: Lerngelegenheiten zu institutioneller
  Diskriminierung, Bildungsprivilegien und vorurteilsbewussten
  Ansätzen institutionalisieren.
- E3 — Transfer-Signal nutzen: FH-Wien-Profil als Referenzpunkt im
  hochschulübergreifenden Dialog.

**Literatur (Auswahl):** Gomolla, M., & Radtke, F.-O. (2009).
*Institutionelle Diskriminierung*. VS Verlag. · Kuckartz, U., &
Rädiker, S. (2022). *Qualitative Inhaltsanalyse* (5. Aufl.). Beltz
Juventa. · Levinson, M., Geron, T., & Brighouse, H. (2022).
Conceptions of educational equity. *AERA Open, 8*. · OECD. (2018).
*Equity in education*. OECD Publishing. · Stojanov, K. (2011).
*Bildungsgerechtigkeit*. VS Verlag.

**Kontakt:** laura.koenig@edu.uni-graz.at ·
barbara.steiner@edu.uni-graz.at

### Heatmap-Daten (nur Fallback, falls kein Bild angehängt)
Zeilen = Stufen, Spalten = Cluster, Werte in %:
- Formale Gleichheit: West 67,1 · Mitte 71,8 · SüdOst 69,7 · FH Wien 48,9
- Kompensatorische Gerechtigkeit: West 28,9 · Mitte 16,6 · SüdOst 23,5 · FH Wien 39,8
- Transformative Gerechtigkeit: West 4,0 · Mitte 11,6 · SüdOst 6,8 · FH Wien 11,3

### Ausgabe
Gib **nur** das fertige HTML-Artifact aus. Optimiere es so, dass
„Drucken → Als PDF speichern → Papierformat A0" ein randloses,
korrekt proportioniertes Poster ergibt.

---

## Iterations-Befehle (nach der ersten Version an Claude.ai schicken)

- „Die rechte Spalte ist zu textlastig — kürze D1–D3 auf je maximal
  drei Zeilen und mache die Kernzahlen (0,8 %, 117:1, 48,9–71,8 %,
  4,0–11,6 %, 39,8 %, 43,0 %) groß und farbig."
- „Mach den Methode-Block kompakter und klar als Pfeilkette erkennbar."
- „Mehr Weißraum zwischen den Abschnitten; Trennlinien dünner."
- „Das Take-home-Banner soll das visuell stärkste Element nach dem
  Titel sein."
- „Heatmap größer ziehen, sodass sie ca. ein Viertel der Posterhöhe
  einnimmt."
- „Erstelle eine Querformat-Variante zum Vergleich." (optional)
