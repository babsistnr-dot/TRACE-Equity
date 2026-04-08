"""
TRACE-Equity: Shared Utilities
Gemeinsame Funktionen und Konstanten für alle Analyse-Scripts.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ============================================================================
# PFADE
# ============================================================================

# Scripts liegen in scripts/, Daten in ergebnisse/ — eine Ebene höher
BASE_DIR = Path(__file__).resolve().parent.parent
ERGEBNISSE_DIR = BASE_DIR / 'ergebnisse'

CLUSTER_PATHS = {
    'west':     ERGEBNISSE_DIR / 'cluster_west'    / 'export_clean.csv',
    'mitte':    ERGEBNISSE_DIR / 'cluster_mitte'   / 'export_clean.csv',
    'suedost':  ERGEBNISSE_DIR / 'cluster_suedost' / 'export_clean.csv',
    'fh_wien':  ERGEBNISSE_DIR / 'cluster_fh_wien' / 'export_clean.csv',
}

CLUSTER_NAMEN = {
    'west':    'Cluster West (Tirol, Vorarlberg, Edith Stein)',
    'mitte':   'Cluster Mitte (OÖ, Linz, Salzburg)',
    'suedost': 'Cluster SüdOst (Burgenland, Kärnten, Steiermark)',
    'fh_wien': 'FH Campus Wien',
}

# ============================================================================
# FARBEN (konsistent mit der Web-App)
# ============================================================================

CODE_FARBEN = {
    'Code 1.1': '#e74c3c',   # Rot
    'Code 2.1': '#3498db',   # Blau
    'Code 2.2': '#2ecc71',   # Grün
    'Code 2.3': '#f39c12',   # Orange
    'Code 2.4': '#9b59b6',   # Lila
    'Code 2.5': '#1abc9c',   # Türkis
    'Code 2.6': '#e67e22',   # Dunkelorange
    'Code 2.7': '#34495e',   # Dunkelgrau
}

# Farbliste in Code-Reihenfolge (für Balkendiagramme)
FARBEN_LISTE = list(CODE_FARBEN.values())

# ============================================================================
# LEVINSON-MAPPING (aus Exposé Tabelle 2)
# ============================================================================

LEVINSON_MAPPING = {
    'Code 1.1: Direkte Nennung': 'Explizite Nennung',
    'Code 2.1: Diversität & Heterogenität': 'Formale Gleichheit',
    'Code 2.2: Inklusion & Partizipation': 'Formale Gleichheit',
    'Code 2.3: Individuelle Förderung & Differenzierung': 'Kompensatorische Gerechtigkeit',
    'Code 2.6: Sprachliche Bildung & Mehrsprachigkeit': 'Kompensatorische Gerechtigkeit',
    'Code 2.4: Abbau von Benachteiligung & Diskriminierung': 'Transformative Gerechtigkeit',
    'Code 2.5: Bildungspartnerschaft & Sozialraumorientierung': 'Querschnitt (Systemebene)',
    'Code 2.7: Professionelle Haltung & Ethik': 'Querschnitt (Professionalisierung)',
}

LEVINSON_FARBEN = {
    'Explizite Nennung': '#e74c3c',
    'Formale Gleichheit': '#3498db',
    'Kompensatorische Gerechtigkeit': '#f39c12',
    'Transformative Gerechtigkeit': '#9b59b6',
    'Querschnitt (Systemebene)': '#1abc9c',
    'Querschnitt (Professionalisierung)': '#34495e',
}

# Reihenfolge für konsistente Darstellung
LEVINSON_REIHENFOLGE = [
    'Explizite Nennung',
    'Formale Gleichheit',
    'Kompensatorische Gerechtigkeit',
    'Transformative Gerechtigkeit',
    'Querschnitt (Systemebene)',
    'Querschnitt (Professionalisierung)',
]

# ============================================================================
# FUNKTIONEN
# ============================================================================

def load_cluster(name):
    """Lädt einen Cluster-Export als DataFrame.

    Args:
        name: 'west', 'mitte', oder 'suedost'

    Returns:
        pandas DataFrame mit allen Findings
    """
    if name not in CLUSTER_PATHS:
        raise ValueError(f"Unbekannter Cluster: '{name}'. Verfügbar: {list(CLUSTER_PATHS.keys())}")

    path = CLUSTER_PATHS[name]
    if not path.exists():
        raise FileNotFoundError(f"CSV nicht gefunden: {path}")

    return pd.read_csv(path, encoding='utf-8')


def load_all_clusters():
    """Lädt alle verfügbaren Cluster und gibt ein Dict zurück.

    Returns:
        Dict mit {name: DataFrame} für alle vorhandenen Cluster
    """
    clusters = {}
    for name in CLUSTER_PATHS:
        try:
            clusters[name] = load_cluster(name)
        except FileNotFoundError:
            print(f"  [SKIP] {name}: CSV nicht gefunden")
    return clusters


def relevante(df):
    """Filtert auf relevante Findings (relevant == 'ja')."""
    return df[df['relevant'] == 'ja']


def nicht_relevante(df):
    """Filtert auf nicht-relevante Findings (relevant == 'nein')."""
    return df[df['relevant'] == 'nein']


def add_levinson(df):
    """Fügt eine 'levinson' Spalte basierend auf confirmed_code hinzu."""
    df = df.copy()
    df['levinson'] = df['confirmed_code'].map(LEVINSON_MAPPING)
    return df


def setup_plots():
    """Konfiguriert Matplotlib/Seaborn für konsistente Darstellung."""
    plt.switch_backend('Agg')
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 11


def output_dir(cluster_name, subdir='visualisierungen'):
    """Erstellt und gibt den Output-Ordner für einen Cluster zurück."""
    path = ERGEBNISSE_DIR / f'cluster_{cluster_name}' / subdir
    path.mkdir(parents=True, exist_ok=True)
    return path
