# ✅ TRACE-Equity auf PythonAnywhere - Erfolgreiche Deployment-Anleitung

## 🎉 Diese Anleitung hat funktioniert!

Erfolgreich deployed am: **21. Oktober 2025**
Live-URL: **http://bsteiner.pythonanywhere.com**

---

## 📋 Voraussetzungen

### Dateien die du brauchst (lokal auf deinem Computer):

```
C:\Users\Babsi\Documents\Master Elementarpädagogik\3. Semester\SE Forschungsmethoden\TRACE-Equity\
├── app.py                    (8.9 KB)
├── requirements.txt          (73 Bytes)
├── Kodiermanual.md          (7.7 KB)
├── README.md                 (2.5 KB)
└── templates/
    └── index.html            (11.7 KB)
```

**NICHT hochladen:**
- `Daten/` Ordner (PDFs bleiben lokal)
- Test-Skripte (test_*.py, search_*.py)
- `uploads/` und `ergebnisse/` (werden automatisch erstellt)

---

## 🚀 Schritt-für-Schritt Anleitung (GETESTET & FUNKTIONIERT)

### **Schritt 1: PythonAnywhere Account erstellen**

1. Gehe zu: https://www.pythonanywhere.com
2. Klicke **"Pricing & signup"**
3. Wähle **"Create a Beginner account"** (kostenlos)
4. Fülle Formular aus:
   - Username: `bsteiner` (oder dein Wunschname)
   - Email
   - Passwort
5. Bestätige Email

✅ **Ergebnis:** Account aktiv

---

### **Schritt 2: Dateien hochladen**

#### **2a) Hauptdateien hochladen**

1. Logge dich ein auf PythonAnywhere
2. Gehe zu **"Files"** Tab
3. Du bist in: `/home/bsteiner/`
4. Klicke **"New directory"**
5. Name: `trace-equity`
6. Enter drücken
7. **Klicke auf** `trace-equity` Ordner
8. **Upload jede Datei einzeln:**
   - Klicke **"Upload a file"**
   - Wähle von deinem Computer:
     ```
     C:\Users\Babsi\Documents\Master Elementarpädagogik\3. Semester\SE Forschungsmethoden\TRACE-Equity\app.py
     ```
   - Warte bis Upload fertig (grünes Häkchen)
   - **Wiederhole für:**
     - `requirements.txt`
     - `Kodiermanual.md`
     - `README.md`

#### **2b) Templates-Ordner erstellen**

1. Du bist in: `/home/bsteiner/trace-equity/`
2. Klicke **"New directory"**
3. Name: `templates` (klein geschrieben!)
4. Enter
5. **Klicke auf** `templates/` Ordner
6. **Upload:**
   - `index.html` von deinem Computer

✅ **Ergebnis:**
```
/home/bsteiner/trace-equity/
├── app.py               (8.9 KB - wichtig!)
├── requirements.txt
├── Kodiermanual.md
├── README.md
└── templates/
    └── index.html       (11.7 KB)
```

**⚠️ WICHTIG:** Prüfe dass `app.py` **8-9 KB** groß ist (nicht 186 Bytes!)

---

### **Schritt 3: Virtual Environment erstellen**

**⚠️ KRITISCH:** Ohne virtualenv funktionieren die Pakete nicht!

1. Gehe zu **"Consoles"** Tab
2. Klicke **"Bash"**
3. Bash Console öffnet sich

**Tippe diese Befehle ein (einzeln, mit Enter nach jedem):**

#### **Befehl 1: In Projektordner wechseln**
```bash
cd /home/bsteiner/trace-equity
```

#### **Befehl 2: Virtual Environment erstellen**
```bash
python3.10 -m venv venv
```
⏳ Dauert ~1-2 Minuten (einfach warten!)

#### **Befehl 3: Virtual Environment aktivieren**
```bash
source venv/bin/activate
```
✅ Du solltest jetzt sehen: `(venv) ~/trace-equity $`

#### **Befehl 4: Python-Pakete installieren**
```bash
pip install Flask PyPDF2 pandas openpyxl
```
⏳ Dauert ~2-3 Minuten

✅ **Ergebnis:**
```
Successfully installed Flask-3.1.2 PyPDF2-3.0.1 pandas-2.3.3 openpyxl-3.1.5 (und viele mehr)
```

**⚠️ WICHTIG:** Installiere **OHNE Versionsnummern** (nicht wie in requirements.txt!)

---

### **Schritt 4: Web App einrichten**

1. Gehe zu **"Web"** Tab
2. Klicke **"Add a new web app"**
3. Klicke **"Next"**
4. Wähle **"Flask"**
5. Wähle **"Python 3.10"**
6. **Path ändern zu:**
   ```
   /home/bsteiner/trace-equity/app.py
   ```
   (Ersetze den Standard-Pfad!)
7. Klicke **"Next"**

✅ **Ergebnis:** Web app erstellt

---

### **Schritt 5: WSGI-Konfiguration**

1. Auf der **Web** Tab, scrolle zu **"Code:"**
2. Klicke auf **"WSGI configuration file"** (blauer Link)
3. **LÖSCHE ALLES** in der Datei
4. **Füge NUR das ein:**

```python
import sys

path = '/home/bsteiner/trace-equity'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

5. Klicke **"Save"** (grüner Button oben rechts)

✅ **Ergebnis:** WSGI konfiguriert

---

### **Schritt 6: Virtual Environment verknüpfen**

**⚠️ KRITISCH:** Ohne diesen Schritt findet Python die Pakete nicht!

1. Bleibe auf **"Web"** Tab
2. Scrolle zu **"Virtualenv:"**
3. Klicke auf das Eingabefeld: **"Enter path to a virtualenv, if desired"**
4. Trage ein:
   ```
   /home/bsteiner/trace-equity/venv
   ```
5. Enter drücken

✅ **Ergebnis:** Du siehst jetzt: **"Virtualenv: /home/bsteiner/trace-equity/venv"**

---

### **Schritt 7: App starten!**

1. Bleibe auf **"Web"** Tab
2. Scrolle ganz nach oben
3. Klicke den großen grünen Button: **"Reload bsteiner.pythonanywhere.com"**
4. Warte ~10 Sekunden
5. Klicke auf: **http://bsteiner.pythonanywhere.com**

🎉 **Deine App läuft jetzt!**

---

## 🔍 Fehlerbehebung (falls etwas nicht klappt)

### Problem: "Hello from Flask!" statt TRACE-Equity App

**Ursache:** WSGI-Pfad falsch oder app.py zu klein

**Lösung:**
1. Files Tab → Prüfe `app.py` Größe (muss 8-9 KB sein!)
2. Falls zu klein: Lösche und lade nochmal hoch
3. Web Tab → Reload

---

### Problem: "ModuleNotFoundError: No module named 'PyPDF2'"

**Ursache:** Virtual Environment nicht verknüpft

**Lösung:**
1. Web Tab → "Virtualenv:" Feld
2. Trage ein: `/home/bsteiner/trace-equity/venv`
3. Reload

---

### Problem: Pandas Installation schlägt fehl

**Lösung:** Installiere OHNE Versionsnummern!

```bash
# FALSCH:
pip install pandas==2.0.3

# RICHTIG:
pip install pandas
```

---

### Problem: "Console limit reached"

**Lösung:**
1. Consoles Tab
2. Schließe alte Consoles (rotes X)
3. Neue Console öffnen

---

## 🔒 Passwortschutz einrichten (WICHTIG!)

### Nach erfolgreichem Deployment:

1. **Web** Tab
2. Scrolle zu **"Password protection"**
3. Klicke **"Set up password protection"**
4. Username: `trace-equity` (oder dein Wunsch)
5. Passwort: `[sicheres Passwort wählen]`
6. Speichern

✅ **Ergebnis:** App ist passwortgeschützt

---

## 📊 Wichtige Infos für später

### **App-URLs:**
- **Live-App:** http://bsteiner.pythonanywhere.com
- **Dashboard:** https://www.pythonanywhere.com/user/bsteiner/

### **Dateien auf PythonAnywhere:**
- **Projekt:** `/home/bsteiner/trace-equity/`
- **Virtual Env:** `/home/bsteiner/trace-equity/venv/`
- **WSGI Config:** `/var/www/bsteiner_pythonanywhere_com_wsgi.py`

### **Logs prüfen:**
- Web Tab → **"Error log"** (bei Problemen)
- Web Tab → **"Server log"** (für Access-Logs)

---

## 🔄 Updates hochladen

### Wenn du app.py ändern willst:

1. **Files** Tab
2. Navigiere zu `/home/bsteiner/trace-equity/`
3. Klicke auf `app.py`
4. Klicke **"Delete"** (bestätigen)
5. **Upload** neue `app.py` von deinem Computer
6. **Web** Tab → **Reload** Button

### Wenn du templates/index.html ändern willst:

1. **Files** Tab → `/home/bsteiner/trace-equity/templates/`
2. Lösche alte `index.html`
3. Upload neue `index.html`
4. **Web** Tab → **Reload**

---

## 💰 Kosten & Limits (Free Account)

### **Was ist kostenlos:**
✅ 1 Web-App
✅ 512 MB Speicher
✅ HTTPS automatisch
✅ Unbegrenzte Requests (fair use)

### **Limits:**
⚠️ App "schläft" nach 3 Monaten Inaktivität (reaktivierbar)
⚠️ Max. 2 Bash Consoles gleichzeitig
⚠️ Keine Custom Domain

### **Upgrade (optional):**
- **Hacker Plan:** $5/Monat
  - Kein Auto-Sleep
  - Mehr Speicher
  - Custom Domain möglich

---

## 📱 URL mit Forschungsgruppe teilen

### **Email-Vorlage:**

```
Hallo Team,

unsere TRACE-Equity PDF Analyse-App ist jetzt online! 🎉

URL: http://bsteiner.pythonanywhere.com

Login (falls aktiviert):
Username: trace-equity
Passwort: [Passwort]

So funktioniert's:
1. PDF-Curriculum hochladen
2. Ergebnisse durchsehen (alle gefundenen Keywords)
3. Validieren: Relevant? Ja/Nein
4. Code bestätigen/ändern
5. CSV exportieren
6. In Excel öffnen und auswerten

Die App durchsucht automatisch alle 138 Keywords aus unserem
Kodiermanual (7 Codes: Chancengleichheit explizit, Diversität,
Inklusion, Individuelle Förderung, Abbau von Benachteiligung,
Bildungspartnerschaft, Sprachliche Bildung, Professionelle Haltung).

Bei Fragen: Einfach melden!

Viele Grüße
```

---

## ✅ Checkliste für erfolgreiches Deployment

- [ ] PythonAnywhere Account erstellt
- [ ] Ordner `trace-equity` erstellt
- [ ] `app.py` hochgeladen (8-9 KB!)
- [ ] `templates/index.html` hochgeladen (11.7 KB)
- [ ] `requirements.txt`, `Kodiermanual.md` hochgeladen
- [ ] Virtual Environment erstellt (`python3.10 -m venv venv`)
- [ ] Virtual Environment aktiviert (`source venv/bin/activate`)
- [ ] Pakete installiert (`pip install Flask PyPDF2 pandas openpyxl`)
- [ ] Web App erstellt (Flask, Python 3.10)
- [ ] WSGI-Config angepasst (Pfad zu app.py)
- [ ] Virtualenv-Pfad eingetragen (`/home/bsteiner/trace-equity/venv`)
- [ ] App neu geladen (Reload Button)
- [ ] App funktioniert (lila-violettes Design sichtbar)
- [ ] Test-PDF hochgeladen
- [ ] CSV-Export getestet
- [ ] Passwortschutz aktiviert
- [ ] URL mit Gruppe geteilt

---

## 🎓 Lessons Learned

### **Was hat NICHT funktioniert:**

❌ `pip install -r requirements.txt` mit Versionsnummern
- Pandas 2.0.3 lässt sich nicht kompilieren auf Python 3.10
- **Lösung:** Ohne Versionsnummern installieren

❌ `pip install --user` in Bash Console
- Pakete landen im falschen Python-Verzeichnis
- **Lösung:** Virtual Environment verwenden

❌ app.py mit 186 Bytes
- Datei wurde nicht vollständig hochgeladen
- **Lösung:** Upload wiederholen, Größe prüfen

### **Was hat funktioniert:**

✅ Virtual Environment (`python3.10 -m venv venv`)
✅ Pakete ohne Versionsnummern (`pip install Flask PyPDF2 pandas openpyxl`)
✅ Virtualenv-Pfad in Web Tab eintragen
✅ Einfache WSGI-Konfiguration (ohne Kommentare)

---

## 🎉 Erfolg!

**Die App ist jetzt live und funktioniert:**
- ✅ PDF-Upload funktioniert
- ✅ Keyword-Suche läuft
- ✅ Alle 138 Keywords aus Kodiermanual werden gefunden
- ✅ Validierungs-Interface funktioniert
- ✅ CSV-Export funktioniert
- ✅ Schönes, professionelles Design

**URL:** http://bsteiner.pythonanywhere.com

**Deployment-Zeit:** ~45 Minuten (inkl. Troubleshooting)

---

*Erstellt am: 21. Oktober 2025*
*Getestet und funktioniert: ✅*
