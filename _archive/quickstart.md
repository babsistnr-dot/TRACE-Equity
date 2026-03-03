# 🚀 So startest du die TRACE-Equity Web-App

## Schritt 1: Terminal in VSCode öffnen

1. Öffne VSCode
2. Drücke **`Strg + Ö`** (oder gehe oben auf `Terminal` → `New Terminal`)

## Schritt 2: App starten

Im Terminal (unten in VSCode) tippe:

```bash
python app.py
```

Drücke **Enter**.

## Schritt 3: Browser öffnen

Die App startet automatisch! Du siehst im Terminal:

```
TRACE-Equity PDF Analyse Tool
================================================================================

Öffne deinen Browser und gehe zu: http://localhost:5000

Zum Beenden: Strg+C drücken
================================================================================
```

**Gehe zu:** `http://localhost:5000` in deinem Browser

→ Die Web-App öffnet sich! 🎉

---

## ✅ So benutzt du die App:

### 1. PDF hochladen
- Klicke auf **"Datei auswählen"**
- Wähle ein Curriculum-PDF (z.B. aus dem `Daten/` Ordner)
- Die App analysiert es automatisch!

### 2. Ergebnisse ansehen
- Du siehst alle gefundenen Textstellen
- Für jede Textstelle:
  - **Seite** wird angezeigt
  - **Gefundenes Keyword**
  - **Vorgeschlagener Code**
  - **Kontext** (Text darum herum)

### 3. Validieren
- **"Relevant? "** → Wähle "Ja" oder "Nein"
- **"Code bestätigen"** → Ändere den Code falls nötig
- **"Notizen"** → Schreibe deine Gedanken dazu

### 4. Exportieren
- Klicke auf **"Als CSV exportieren"**
- Die Datei wird heruntergeladen
- Öffne sie in Excel!

---

## 🛑 App beenden

Im Terminal (VSCode): Drücke **`Strg + C`**

---

## ❓ Probleme?

### "Fehler: Port already in use"
→ Die App läuft schon! Gehe einfach zu http://localhost:5000

### "ModuleNotFoundError: No module named 'flask'"
→ Installiere Flask:
```bash
python -m pip install flask
```

### PDF wird nicht hochgeladen
→ Prüfe:
- Ist es wirklich eine PDF-Datei?
- Ist die Datei < 50 MB?

---

## 📁 Wo sind meine Ergebnisse?

Alle Analysen werden gespeichert in:

```
TRACE-Equity/
├── uploads/          ← Hochgeladene PDFs
├── ergebnisse/       ← JSON-Dateien mit Analysen
│   ├── analyse_XXXXXX.json
│   └── export_XXXXXX.csv
```

→ Die CSV-Dateien kannst du in Excel öffnen!

---

## 🎨 Features der App:

✅ Schönes, modernes Design
✅ Drag & Drop PDF-Upload
✅ Automatische Keyword-Suche (alle 7 Codes)
✅ Kontext-Anzeige (200 Zeichen vor/nach)
✅ Validierungs-Interface
✅ CSV-Export für Excel
✅ Lokale Speicherung (Datenschutz!)

---

**Viel Erfolg mit deiner Forschung! 🎓✨**
