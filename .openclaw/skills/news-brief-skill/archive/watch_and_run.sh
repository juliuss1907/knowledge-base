#!/bin/bash
# Watch browser installation and auto-run scraper when ready

set -e

echo "👀 Watching browser installation..."
echo "============================================================"

VENV_PATH="/home/julius/julius-workspace/.hermes/skills/news-brief-skill/venv-3.11"
PYTHON_PATH="$VENV_PATH/bin/python"
SKILL_DIR="/home/julius/julius-workspace/.hermes/skills/news-brief-skill"

cd "$SKILL_DIR"

# Function to check browser
check_browser() {
    "$PYTHON_PATH" -m playwright show-browsers 2>/dev/null | grep -q "chromium"
}

# Wait for browser
while ! check_browser; do
    echo "  ⏳ Browser not ready yet... checking again in 10s"
    sleep 10
done

echo "✅ Browser installation complete!"
echo ""
echo "============================================================"
echo "🚀 Starting scraper..."
echo ""

# Run scraper
"$PYTHON_PATH" scrape.py

echo ""
echo "============================================================"
echo "✅ Scrape complete!"
echo ""
echo "Next: Run synthesize with:"
echo "  ./venv-3.11/bin/python synthesize.py"
echo "============================================================"
