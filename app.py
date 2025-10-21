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

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Erstelle uploads Ordner falls nicht vorhanden
os.makedirs('uploads', exist_ok=True)
os.makedirs('ergebnisse', exist_ok=True)

# Keywords aus Kodiermanual.md (VOLLSTÄNDIGE Liste)
KEYWORDS = {
    "Code 1.1: Direkte Nennung": [
        "Chancengleichheit",
        "Chancengerechtigkeit"
    ],
    "Code 2.1: Diversität & Heterogenität": [
        "Diversität", "Diversity", "Vielfalt", "Heterogenität",
        "kulturell", "Interkulturalität", "Interreligiosität", "multireligiös",
        "Geschlecht", "Gender", "geschlechtssensibel", "sozioökonomisch",
        "ethnisch", "Familienkonstellationen", "Pädagogik der Vielfalt",
        "Diversitätsansprüche", "Diversitätsbedingungen", "multikulturell"
    ],
    "Code 2.2: Inklusion & Partizipation": [
        "Inklusion", "inklusive Pädagogik", "inklusives Setting", "inklusiv",
        "Integration", "Segregation", "Partizipation", "Teilhabe",
        "Zugehörigkeit", "barrierefrei", "inklusive Lernumgebungen",
        "inklusiven Settings"
    ],
    "Code 2.3: Individuelle Förderung & Differenzierung": [
        "individuelle Förderung", "individuelle Lernprozesse", "individuelle Lernphasen",
        "Individualisierung", "Differenzierung", "Stärkenorientierung", "stärkenorientiert",
        "Ressourcenorientierung", "ressourcenorientiert", "Potenzialanalyse",
        "Potenziale erkennen", "Fördermaßnahmen", "Begabung", "Begabungsförderung",
        "Behinderung", "spezifische Lern- und Entwicklungsschwierigkeiten",
        "individuelle Lebensrealität", "individuelle Entwicklung",
        "individuelle Entwicklungs- und Bildungsprozesse",
        "individuelle Entwicklungs- und Bildungsverläufe",
        "besondere Bedarfe", "individuelle Lernausgangslagen",
        "Förderplanung", "Lernprozessbegleitung"
    ],
    "Code 2.4: Abbau von Benachteiligung & Diskriminierung": [
        # Problemerkennung & Analyse
        "Benachteiligung", "Ungleichheit", "Gleichheit", "soziale Ungerechtigkeit",
        "Diskriminierung", "diskriminierungskritisch", "Vorurteile", "vorurteilsbewusst",
        "Stereotype", "soziale Stratifizierung", "soziale Herkunft",
        "soziale Lebensbedingungen", "soziale Benachteiligung", "Gleichstellung",
        "Gleichstellungspädagogik", "Bildungsgerechtigkeit",
        "Bedingungen und Auswirkungen von Ungleichheit", "sensibel wahrnehmen",
        "Zugang", "Zugang zu Bildung", "Bildungszugang", "Barrieren",
        # Transformatives Handeln
        "Empowerment", "entgegenwirken", "bekämpfen", "verändern", "transformieren",
        "kritisch hinterfragen", "Machtverhältnisse", "Machtstrukturen",
        "strukturelle Veränderung", "strukturell", "emanzipatorisch",
        "Selbstbestimmung fördern", "Selbstbestimmung stärken", "Teilhabe ermöglichen",
        "ko-konstruktiv", "auf Empowerment ausgerichtet", "in die Handlungen miteinzubeziehen"
    ],
    "Code 2.5: Bildungspartnerschaft & Sozialraumorientierung": [
        "Bildungspartnerschaft", "Erziehungspartnerschaft",
        "Zusammenarbeit mit Erziehungsberechtigten", "Kooperation mit externen Partnern",
        "Netzwerkarbeit", "Vernetzung", "Sozialraum", "multiprofessionelle Teams",
        "interdisziplinäre Zusammenarbeit", "Kooperation mit Eltern bzw. Erziehungsberechtigten",
        "Kooperation mit Netzwerkorganisationen", "sozialräumliche Programme"
    ],
    "Code 2.6: Sprachliche Bildung & Mehrsprachigkeit": [
        "Sprachliche Bildung", "Sprachförderung", "alltagsintegrierte Sprachbildung",
        "Mehrsprachigkeit", "Erstspracherwerb", "Zweitspracherwerb", "Literacy",
        "Family Literacy", "Sprachstandsbeobachtung", "Sprachstandsdiagnostik",
        "sprachsensibel", "sprachbezogen", "Deutsch als Erst- bzw. Zweitsprache",
        "Fremdspracherwerb", "Mehrsprachendidaktik"
    ],
    "Code 2.7: Professionelle Haltung & Ethik": [
        "Professionelle Haltung", "pädagogischer Habitus", "Berufsethos",
        "Werte", "Werthaltung", "Wertebildung", "Haltung", "Grundhaltung",
        "Selbstreflexion", "ethisch", "Ethik", "Menschenbild", "Kinderbild",
        "Reflexionskompetenz", "Vorbildwirkung", "wissenschaftlich-reflektierender Habitus",
        "forschend reflexiver Habitus", "persönlichkeitsorientierte Professionsentwicklung",
        "lösungsorientierte Grundhaltung", "kritische Distanz"
    ]
}

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

    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump({
            'pdf_name': filename,
            'timestamp': session_id,
            'total_results': len(results),
            'results': results
        }, f, ensure_ascii=False, indent=2)

    return jsonify({
        'success': True,
        'pdf_name': filename,
        'total_results': len(results),
        'session_id': session_id,
        'results': results  # ALLE Ergebnisse anzeigen
    })

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
    results_file = os.path.join('ergebnisse', f'analyse_{session_id}.json')

    if not os.path.exists(results_file):
        return jsonify({'error': 'Session nicht gefunden'}), 404

    with open(results_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Als DataFrame
    df = pd.DataFrame(data['results'])

    # Sortiere Spalten für bessere Übersicht
    column_order = ['pdf_name', 'page', 'code', 'keyword', 'context', 'validated', 'relevant', 'confirmed_code', 'notes']
    # Nur Spalten verwenden die existieren
    column_order = [col for col in column_order if col in df.columns]
    df = df[column_order]

    # CSV speichern
    csv_file = os.path.join('ergebnisse', f'export_{session_id}.csv')
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')

    return send_file(csv_file, as_attachment=True, download_name=f'TRACE_Equity_Export_{session_id}.csv')

if __name__ == '__main__':
    print("="*80)
    print("TRACE-Equity PDF Analyse Tool")
    print("="*80)
    print("\nÖffne deinen Browser und gehe zu: http://localhost:5000")
    print("\nZum Beenden: Strg+C drücken")
    print("="*80)
    app.run(debug=True, port=5000)
