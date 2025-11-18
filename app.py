"""
TRACE-Equity PDF Analyse Web-App
Version A: Keyword-basierte Suche mit manueller Validierung
"""

from flask import Flask, render_template, request, jsonify, send_file
from PyPDF2 import PdfReader
import pandas as pd
import os
from datetime import datetime
import json
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Erstelle uploads Ordner falls nicht vorhanden
os.makedirs('uploads', exist_ok=True)
os.makedirs('ergebnisse', exist_ok=True)

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_keywords_from_kodiermanual(filepath=None):
    """
    Parst Keywords direkt aus dem Kodiermanual.md
    Single Source of Truth - keine Duplikation mehr!
    """
    # Default to Knowledge/Kodiermanual.md relative to app.py location
    if filepath is None:
        filepath = os.path.join(BASE_DIR, 'Knowledge', 'Kodiermanual.md')

    keywords = {}

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Finde alle Code-Definitionen
        # Split by code sections (##### Code X.X: Name)
        code_sections = re.split(r'(?=##### Code [\d\.]+: )', content)

        for section in code_sections:
            if not section.strip():
                continue

            # Extract code number and name
            code_match = re.match(r'##### Code ([\d\.]+): ([^\n]+)', section)
            if not code_match:
                continue

            code_num = code_match.group(1)
            code_name = code_match.group(2).strip()

            # Find all keyword sections (could be multiple for Code 2.4)
            # Pattern: **Keywords und Phrasen** or **Keywords und Phrasen (...):**
            keyword_sections = re.findall(
                r'\*\*Keywords und Phrasen[^:]*:\*\*\n((?:- [^\n]+\n?)+)',
                section,
                re.DOTALL
            )

            # Collect all keywords from all sections
            keyword_list = []
            for keywords_text in keyword_sections:
                for line in keywords_text.split('\n'):
                    line = line.strip()
                    if line.startswith('- '):
                        keyword = line[2:].strip()
                        # Entferne Klammern-Kommentare wie "(im Bildungskontext)"
                        keyword = re.sub(r'\s*\([^)]+\)\s*$', '', keyword)
                        if keyword:
                            keyword_list.append(keyword)

            # Erstelle vollständigen Code-Namen
            full_code_name = f"Code {code_num}: {code_name}"
            keywords[full_code_name] = keyword_list

            print(f"[OK] Parsed {full_code_name}: {len(keyword_list)} keywords")

        # Validierung
        if len(keywords) != 8:
            print(f"[WARNING] Expected 8 codes, found {len(keywords)}")

        total_keywords = sum(len(v) for v in keywords.values())
        print(f"[OK] Total keywords loaded: {total_keywords}")

        return keywords

    except FileNotFoundError:
        print("="*80)
        print(f"CRITICAL ERROR: Kodiermanual.md not found")
        print("="*80)
        print(f"Looked for file at: {filepath}")
        print(f"App directory (BASE_DIR): {BASE_DIR}")
        print("")
        print("The application CANNOT run without the Kodiermanual.md file.")
        print("This file is the Single Source of Truth for all keywords.")
        print("")
        print("If deploying to PythonAnywhere:")
        print(f"1. Ensure file exists at: {filepath}")
        print("2. Check that the 'Knowledge' folder is in the same directory as app.py")
        print("3. Reload the web app")
        print("="*80)
        raise SystemExit("FATAL: Kodiermanual.md not found - cannot continue")
    except Exception as e:
        print("="*80)
        print(f"CRITICAL ERROR parsing Kodiermanual.md: {str(e)}")
        print("="*80)
        import traceback
        traceback.print_exc()
        print("")
        print("The application CANNOT run with a corrupted Kodiermanual.md file.")
        print("Please check the file format and try again.")
        print("="*80)
        raise SystemExit(f"FATAL: Cannot parse Kodiermanual.md - {str(e)}")

# Keywords aus Kodiermanual.md laden (Single Source of Truth!)
KEYWORDS = parse_keywords_from_kodiermanual()

def extract_pdf_text(pdf_path):
    """Extrahiert Text aus PDF seitenweise"""
    reader = PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        pages.append({
            'page_num': i + 1,
            'text': text
        })
    return pages

def get_color_for_code(code_name):
    """Gibt eine Farbe für jeden Code zurück"""
    colors = {
        "Code 1.1": "#e74c3c",  # Rot
        "Code 2.1": "#3498db",  # Blau
        "Code 2.2": "#2ecc71",  # Grün
        "Code 2.3": "#f39c12",  # Orange
        "Code 2.4": "#9b59b6",  # Lila
        "Code 2.5": "#1abc9c",  # Türkis
        "Code 2.6": "#e67e22",  # Dunkelorange
        "Code 2.7": "#34495e"   # Dunkelgrau
    }
    # Hole die Code-Nummer (z.B. "Code 1.1" aus "Code 1.1: Direkte Nennung")
    code_prefix = code_name.split(':')[0].strip()
    return colors.get(code_prefix, "#95a5a6")

def search_keywords_in_text(pages, context_chars=200):
    """Sucht Keywords in den PDF-Seiten"""
    results = []

    for page in pages:
        text = page['text']
        text_lower = text.lower()
        page_num = page['page_num']

        # Für jeden Code
        for code_name, keywords in KEYWORDS.items():
            # Für jedes Keyword im Code
            for keyword in keywords:
                keyword_lower = keyword.lower()

                # Finde alle Vorkommen
                start = 0
                while True:
                    pos = text_lower.find(keyword_lower, start)
                    if pos == -1:
                        break

                    # Kontext extrahieren
                    context_start = max(0, pos - context_chars)
                    context_end = min(len(text), pos + len(keyword) + context_chars)
                    context = text[context_start:context_end]

                    # Keyword im Kontext hervorheben
                    color = get_color_for_code(code_name)
                    # Finde das Keyword im Kontext (case-insensitive)
                    context_lower = context.lower()
                    keyword_pos = context_lower.find(keyword_lower)

                    if keyword_pos != -1:
                        # Erhalte das Original-Keyword mit der richtigen Schreibweise
                        original_keyword = context[keyword_pos:keyword_pos + len(keyword)]
                        # Erstelle HTML-Hervorhebung
                        highlighted_keyword = f'<strong style="background-color: {color}; color: white; padding: 2px 4px; border-radius: 3px;">{original_keyword}</strong>'
                        # Ersetze im Kontext
                        highlighted_context = context[:keyword_pos] + highlighted_keyword + context[keyword_pos + len(keyword):]
                    else:
                        highlighted_context = context

                    results.append({
                        'pdf_name': os.path.basename(page['pdf_path']) if 'pdf_path' in page else 'unknown',
                        'page': page_num,
                        'code': code_name,
                        'keyword': keyword,
                        'context': highlighted_context.strip(),
                        'position': pos,
                        'validated': False,
                        'relevant': None,
                        'notes': ''
                    })

                    start = pos + 1

    return results

@app.route('/')
def index():
    """Hauptseite"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    """PDF hochladen und analysieren"""
    try:
        if 'pdf' not in request.files:
            return jsonify({'error': 'Keine Datei hochgeladen'}), 400

        file = request.files['pdf']
        if file.filename == '':
            return jsonify({'error': 'Keine Datei ausgewählt'}), 400

        if not file.filename.endswith('.pdf'):
            return jsonify({'error': 'Nur PDF-Dateien erlaubt'}), 400

        # Datei speichern
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # PDF analysieren
        pages = extract_pdf_text(filepath)
        for page in pages:
            page['pdf_path'] = filepath

        results = search_keywords_in_text(pages)

        # Ergebnisse temporär speichern
        session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        results_file = os.path.join('ergebnisse', f'analyse_{session_id}.json')

        # Debug-Ausgabe
        print(f"DEBUG: Versuche JSON zu speichern in: {results_file}")
        print(f"DEBUG: Absolute Path: {os.path.abspath(results_file)}")

        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump({
                'pdf_name': filename,
                'timestamp': session_id,
                'total_results': len(results),
                'results': results
            }, f, ensure_ascii=False, indent=2)

        print(f"DEBUG: JSON erfolgreich gespeichert!")

        return jsonify({
            'success': True,
            'pdf_name': filename,
            'total_results': len(results),
            'session_id': session_id,
            'results': results  # ALLE Ergebnisse anzeigen
        })

    except Exception as e:
        print(f"ERROR in upload_pdf: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Upload fehlgeschlagen: {str(e)}'}), 500

@app.route('/load_session/<session_id>')
def load_session(session_id):
    """Lädt eine existierende Session"""
    results_file = os.path.join('ergebnisse', f'analyse_{session_id}.json')

    if not os.path.exists(results_file):
        return jsonify({'error': 'Session nicht gefunden'}), 404

    with open(results_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return jsonify({
        'success': True,
        'pdf_name': data['pdf_name'],
        'total_results': data['total_results'],
        'session_id': session_id,
        'results': data['results']
    })

@app.route('/save_validation', methods=['POST'])
def save_validation():
    """Speichert eine einzelne Validierung"""
    data = request.json
    session_id = data.get('session_id')
    result_index = data.get('result_index')
    validation_data = data.get('validation')

    results_file = os.path.join('ergebnisse', f'analyse_{session_id}.json')

    if not os.path.exists(results_file):
        return jsonify({'error': 'Session nicht gefunden'}), 404

    # Lade aktuelle Daten
    with open(results_file, 'r', encoding='utf-8') as f:
        file_data = json.load(f)

    # Update Validierung
    if result_index < len(file_data['results']):
        file_data['results'][result_index]['validated'] = True
        file_data['results'][result_index]['relevant'] = validation_data.get('relevant')
        file_data['results'][result_index]['confirmed_code'] = validation_data.get('code')
        file_data['results'][result_index]['notes'] = validation_data.get('notes', '')

    # Speichere zurück
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=2)

    return jsonify({'success': True})

@app.route('/export/<session_id>')
def export_results(session_id):
    """Ergebnisse als CSV exportieren"""
    try:
        from io import BytesIO, StringIO
        from flask import Response

        results_file = os.path.join('ergebnisse', f'analyse_{session_id}.json')

        if not os.path.exists(results_file):
            return jsonify({'error': 'Session nicht gefunden'}), 404

        with open(results_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Prüfe ob Ergebnisse vorhanden sind
        if not data.get('results') or len(data['results']) == 0:
            return jsonify({'error': 'Keine Ergebnisse zum Exportieren vorhanden'}), 400

        # Als DataFrame
        df = pd.DataFrame(data['results'])

        # Entferne HTML-Tags aus dem Kontext für CSV-Export
        if 'context' in df.columns:
            df['context'] = df['context'].str.replace('<strong style="[^"]*">', '', regex=True)
            df['context'] = df['context'].str.replace('</strong>', '', regex=True)

        # Sortiere Spalten für bessere Übersicht
        column_order = ['pdf_name', 'page', 'code', 'keyword', 'context', 'validated', 'relevant', 'confirmed_code', 'notes']
        # Nur Spalten verwenden die existieren
        column_order = [col for col in column_order if col in df.columns]
        df = df[column_order]

        # Debug-Ausgabe
        print(f"DEBUG: Erstelle CSV im Speicher für Session: {session_id}")
        print(f"DEBUG: DataFrame Shape: {df.shape}")

        # CSV im Speicher erstellen (BytesIO für PythonAnywhere-Kompatibilität)
        output = BytesIO()
        # UTF-8 BOM für Excel-Kompatibilität
        output.write('\ufeff'.encode('utf-8'))
        df.to_csv(output, index=False, encoding='utf-8')
        output.seek(0)

        print(f"DEBUG: CSV erfolgreich im Speicher erstellt! Größe: {output.getbuffer().nbytes} bytes")

        # Erstelle Response mit BytesIO
        return Response(
            output.getvalue(),
            mimetype='text/csv',
            headers={
                'Content-Disposition': f'attachment; filename=TRACE_Equity_Export_{session_id}.csv'
            }
        )

    except Exception as e:
        # Logging für Debugging
        print(f"ERROR in export_results: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Export fehlgeschlagen: {str(e)}'}), 500

if __name__ == '__main__':
    print("="*80)
    print("TRACE-Equity PDF Analyse Tool")
    print("="*80)
    print("\nÖffne deinen Browser und gehe zu: http://localhost:5000")
    print("\nZum Beenden: Strg+C drücken")
    print("="*80)
    app.run(debug=True, port=5000)
