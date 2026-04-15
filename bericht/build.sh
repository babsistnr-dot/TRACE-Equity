#!/usr/bin/env bash
# PDF-Export des Forschungsberichts via Pandoc.
# Voraussetzung: pandoc + eine LaTeX-Distribution (TeX Live oder MiKTeX) installiert.
set -e
cd "$(dirname "$0")"
pandoc forschungsbericht.md \
    --output forschungsbericht.pdf \
    --pdf-engine=xelatex \
    --toc --toc-depth=2 \
    --number-sections
echo "Fertig: forschungsbericht.pdf"
