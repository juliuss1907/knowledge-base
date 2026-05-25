#!/bin/bash
# News Brief Skill - 2-hour cron job
cd /home/julius/knowledge-base/.openclaw/skills/news-brief-skill
./venv-3.12/bin/python scrape.py > /tmp/news_brief_scrape.log 2>&1
./venv-3.12/bin/python synthesize.py > /tmp/news_brief_synth.log 2>&1
