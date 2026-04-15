"""
TRACE-Equity: Test Suite

Testet utils.py und alle Analyse-Scripts.
Ausführen aus dem Projekt-Root:
    python -m pytest tests/ -v
"""

import sys
import pytest
import pandas as pd
from pathlib import Path

# Scripts-Ordner zum Pfad hinzufügen
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from utils import (
    load_cluster, load_all_clusters, relevante, nicht_relevante,
    add_levinson, output_dir, CLUSTER_PATHS, CLUSTER_NAMEN,
    LEVINSON_MAPPING, CODE_FARBEN, FARBEN_LISTE
)


# ============================================================================
# utils.py — Datenpfade & Konfiguration
# ============================================================================

class TestKonfiguration:

    def test_alle_cluster_pfade_vorhanden(self):
        """Alle 4 Cluster-CSVs existieren auf der Festplatte."""
        for name, path in CLUSTER_PATHS.items():
            assert path.exists(), f"CSV fehlt: {name} → {path}"

    def test_alle_cluster_haben_namen(self):
        """Jeder Cluster-Key hat einen Anzeigenamen."""
        for name in CLUSTER_PATHS:
            assert name in CLUSTER_NAMEN, f"Kein Name für Cluster: {name}"

    def test_levinson_mapping_vollstaendig(self):
        """Alle 8 Codes sind im Levinson-Mapping vorhanden."""
        assert len(LEVINSON_MAPPING) == 8

    def test_farben_vollstaendig(self):
        """Alle 8 Codes haben eine Farbe."""
        assert len(CODE_FARBEN) == 8
        assert len(FARBEN_LISTE) == 8


# ============================================================================
# utils.py — Ladefunktionen
# ============================================================================

class TestLadefunktionen:

    def test_load_cluster_west(self):
        df = load_cluster('west')
        assert len(df) > 0
        assert 'confirmed_code' in df.columns

    def test_load_cluster_mitte(self):
        df = load_cluster('mitte')
        assert len(df) > 0

    def test_load_cluster_suedost(self):
        df = load_cluster('suedost')
        assert len(df) > 0

    def test_load_cluster_fh_wien(self):
        df = load_cluster('fh_wien')
        assert len(df) > 0

    def test_load_unbekannter_cluster_wirft_fehler(self):
        with pytest.raises(ValueError):
            load_cluster('xyz')

    def test_load_all_clusters_gibt_alle_vier(self):
        clusters = load_all_clusters()
        assert set(clusters.keys()) == {'west', 'mitte', 'suedost', 'fh_wien'}


# ============================================================================
# Datenqualität — alle Cluster
# ============================================================================

class TestDatenqualitaet:

    @pytest.fixture(params=['west', 'mitte', 'suedost', 'fh_wien'])
    def df(self, request):
        return load_cluster(request.param)

    def test_keine_nan_in_relevant(self, df):
        assert df['relevant'].isna().sum() == 0, "NaN-Werte in 'relevant'"

    def test_keine_nan_in_confirmed_code(self, df):
        assert df['confirmed_code'].isna().sum() == 0, "NaN-Werte in 'confirmed_code'"

    def test_alle_validated(self, df):
        # export_clean sollte nur validierte Findings enthalten
        assert df['validated'].isin([True, 'True']).all(), "Nicht-validierte Findings in export_clean"

    def test_relevant_nur_ja_nein(self, df):
        assert set(df['relevant'].unique()).issubset({'ja', 'nein'}), \
            f"Ungültige Werte in 'relevant': {df['relevant'].unique()}"

    def test_pflicht_spalten_vorhanden(self, df):
        pflicht = ['pdf_name', 'page', 'code', 'keyword', 'context',
                   'validated', 'relevant', 'confirmed_code']
        for col in pflicht:
            assert col in df.columns, f"Spalte fehlt: {col}"

    def test_mindestens_100_findings(self, df):
        assert len(df) >= 100, f"Zu wenige Findings: {len(df)}"


# ============================================================================
# Filter-Funktionen
# ============================================================================

class TestFilterFunktionen:

    def test_relevante_nur_ja(self):
        df = load_cluster('mitte')
        rel = relevante(df)
        assert (rel['relevant'] == 'ja').all()

    def test_nicht_relevante_nur_nein(self):
        df = load_cluster('mitte')
        nein = nicht_relevante(df)
        assert (nein['relevant'] == 'nein').all()

    def test_relevante_plus_nicht_relevante_gleich_gesamt(self):
        df = load_cluster('west')
        assert len(relevante(df)) + len(nicht_relevante(df)) == len(df)


# ============================================================================
# Levinson-Mapping
# ============================================================================

class TestLevinsonMapping:

    def test_add_levinson_spalte(self):
        df = load_cluster('mitte')
        df = add_levinson(df)
        assert 'levinson' in df.columns

    def test_kein_nan_in_levinson(self):
        df = load_cluster('mitte')
        df = add_levinson(relevante(df))
        unmapped = df[df['levinson'].isna()]['confirmed_code'].unique()
        assert len(unmapped) == 0, f"Nicht gemappte Codes: {unmapped}"

    def test_levinsonn_vollstaendig(self):
        """Alle 4 Hauptstufen kommen in den Daten vor."""
        df = add_levinson(relevante(load_cluster('mitte')))
        stufen = set(df['levinson'].unique())
        for stufe in ['Formale Gleichheit', 'Kompensatorische Gerechtigkeit', 'Transformative Gerechtigkeit']:
            assert stufe in stufen, f"Levinson-Stufe fehlt: {stufe}"


# ============================================================================
# Bekannte Zahlen — Regressions-Tests
# ============================================================================

class TestBekannteZahlen:
    """Stellt sicher, dass Datenbereinigungen keine Zahlen verändert haben."""

    def test_west_findings(self):
        assert len(load_cluster('west')) == 468

    def test_west_relevant(self):
        assert len(relevante(load_cluster('west'))) == 347

    def test_mitte_findings(self):
        assert len(load_cluster('mitte')) == 516

    def test_mitte_relevant(self):
        assert len(relevante(load_cluster('mitte'))) == 259

    def test_suedost_findings(self):
        assert len(load_cluster('suedost')) == 272

    def test_suedost_relevant(self):
        assert len(relevante(load_cluster('suedost'))) == 192

    def test_fh_wien_findings(self):
        assert len(load_cluster('fh_wien')) == 370

    def test_fh_wien_relevant(self):
        assert len(relevante(load_cluster('fh_wien'))) == 263

    def test_mitte_code_1_1_count(self):
        """Cluster Mitte hat 8 relevante Code-1.1-Findings."""
        df = relevante(load_cluster('mitte'))
        count = len(df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung'])
        assert count == 8

    def test_fh_wien_code_1_1_count(self):
        """FH Wien hat 1 relevantes Code-1.1-Finding."""
        df = relevante(load_cluster('fh_wien'))
        count = len(df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung'])
        assert count == 1

    def test_west_kein_code_1_1(self):
        """Cluster West hat 0 Code-1.1-Findings."""
        df = relevante(load_cluster('west'))
        count = len(df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung'])
        assert count == 0

    def test_suedost_kein_code_1_1(self):
        """Cluster SüdOst hat 0 Code-1.1-Findings."""
        df = relevante(load_cluster('suedost'))
        count = len(df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung'])
        assert count == 0

    def test_gesamt_code_1_1_count(self):
        """Über alle Cluster hinweg gibt es genau 9 Code-1.1-Findings."""
        total = 0
        for name in ['west', 'mitte', 'suedost', 'fh_wien']:
            df = relevante(load_cluster(name))
            total += len(df[df['confirmed_code'] == 'Code 1.1: Direkte Nennung'])
        assert total == 9


# ============================================================================
# Levinson-Verteilung (Schritt 6 — Regression)
# ============================================================================

class TestLevinsonVerteilung:
    """Regressionstests für Levinson-Stufen-Verteilung pro Cluster (nur relevante Findings)."""

    DREI_STUFEN = ['Formale Gleichheit', 'Kompensatorische Gerechtigkeit', 'Transformative Gerechtigkeit']

    def _drei_stufen_counts(self, cluster):
        df = add_levinson(relevante(load_cluster(cluster)))
        df3 = df[df['levinson'].isin(self.DREI_STUFEN)]
        return df3['levinson'].value_counts().to_dict(), len(df3)

    def test_west_levinson(self):
        counts, total = self._drei_stufen_counts('west')
        assert total == 225
        assert counts.get('Formale Gleichheit') == 151
        assert counts.get('Kompensatorische Gerechtigkeit') == 65
        assert counts.get('Transformative Gerechtigkeit') == 9

    def test_mitte_levinson(self):
        counts, total = self._drei_stufen_counts('mitte')
        assert total == 181
        assert counts.get('Formale Gleichheit') == 130
        assert counts.get('Kompensatorische Gerechtigkeit') == 30
        assert counts.get('Transformative Gerechtigkeit') == 21

    def test_suedost_levinson(self):
        counts, total = self._drei_stufen_counts('suedost')
        assert total == 132
        assert counts.get('Formale Gleichheit') == 92
        assert counts.get('Kompensatorische Gerechtigkeit') == 31
        assert counts.get('Transformative Gerechtigkeit') == 9

    def test_fh_wien_levinson(self):
        counts, total = self._drei_stufen_counts('fh_wien')
        assert total == 133
        assert counts.get('Formale Gleichheit') == 65
        assert counts.get('Kompensatorische Gerechtigkeit') == 53
        assert counts.get('Transformative Gerechtigkeit') == 15


# ============================================================================
# Cross-Cluster-Vergleich (Schritt 7 — Regression)
# ============================================================================

class TestClusterVergleich:
    """Regressionstests für Code-Verteilungen je Cluster (nur relevante Findings)."""

    def _counts(self, cluster):
        df = relevante(load_cluster(cluster))
        return df['confirmed_code'].value_counts().to_dict(), len(df)

    def test_gesamt_relevant(self):
        total = sum(len(relevante(load_cluster(c)))
                    for c in ['west', 'mitte', 'suedost', 'fh_wien'])
        assert total == 1061

    def test_west_code_verteilung(self):
        counts, total = self._counts('west')
        assert total == 347
        assert counts.get('Code 2.1: Diversität & Heterogenität') == 112
        assert counts.get('Code 2.7: Professionelle Haltung & Ethik') == 92

    def test_mitte_code_verteilung(self):
        counts, total = self._counts('mitte')
        assert total == 259
        assert counts.get('Code 2.1: Diversität & Heterogenität') == 91
        assert counts.get('Code 2.7: Professionelle Haltung & Ethik') == 56

    def test_suedost_code_verteilung(self):
        counts, total = self._counts('suedost')
        assert total == 192
        assert counts.get('Code 2.1: Diversität & Heterogenität') == 75
        assert counts.get('Code 2.7: Professionelle Haltung & Ethik') == 35

    def test_fh_wien_code_verteilung(self):
        counts, total = self._counts('fh_wien')
        assert total == 263
        assert counts.get('Code 2.1: Diversität & Heterogenität') == 48
        assert counts.get('Code 2.3: Individuelle Förderung & Differenzierung') == 34
        assert counts.get('Code 2.7: Professionelle Haltung & Ethik') == 113
