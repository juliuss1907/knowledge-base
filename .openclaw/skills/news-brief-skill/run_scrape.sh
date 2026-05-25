#!/bin/bash
# Launcher script for news brief scraper using Python 3.11 virtualenv

set -e

echo "🚀 Starting News Brief Scraper (Python 3.11)"
echo "============================================================"

# Activate virtualenv
cd "$(dirname "$0")"
source venv-3.11/bin/activate

# Run scraper
echo "📊 Running scrape.py..."
python scrape.py

echo ""
echo "============================================================"
echo "✅ Scraper completed!"
echo ""
echo "Next: Run synthesize"
echo "  ./run_synthesize.sh"