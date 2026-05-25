"""
News Brief Skill Configuration
Generated: 2026-05-25
"""

# Telegram API Credentials
TELEGRAM_API_ID = 35676903
TELEGRAM_API_HASH = 'bd6c6e8b4eeee4d88d210aa29e45601e'

# Telegram Bot Settings
TELEGRAM_BOT_TOKEN = '8813276012:AAFDygfqcMvurKlxGYzFV9asxKcsSTgRBfA'
TELEGRAM_CHAT_ID = '1370258715'

# Output Settings
OUTPUT_SETTINGS = {
    'telegram': {
        'enabled': True,
        'bot_token': TELEGRAM_BOT_TOKEN,
        'chat_id': TELEGRAM_CHAT_ID
    },
    'markdown': {
        'enabled': True,
        'path': '/home/julius/julius-workspace/personal',
        'filename_format': '{date}/{session}.md',
        'keep_days': 30,
        'create_index': True
    }
}

# Global Settings
GLOBAL_SETTINGS = {
    'scraping': {
        'telegram_timeout': 60,
        'thefeed_timeout': 30,
        'rss_timeout': 30
    },
    'time_window': {
        'hours': 48,
        'max_age_days': 2
    },
    'keywords': {
        'tiers': {
            1: 100,
            2: 70,
            3: 40,
            'negative': -50
        }
    },
    'engagement': {
        'telegram_weight': 0.3,
        'thefeed_weight': 0.4,
        'rss_weight': 0.1
    },
    'source_authority': {
        'high': 1.5,
        'medium': 1.0,
        'low': 0.7
    },
    'recency': {
        '3h': 10,
        '6h': 7,
        '12h': 3
    }
}

# Quality Filters
QUALITY_FILTERS = {
    'min_text_length': 200,
    'min_views': 1000,
    'dedup_threshold': 0.85
}

# Topics Configuration
TOPICS = {
    'crypto': {
        'enabled': True,
        'display_name': 'Crypto',
        'icon': '🪙',
        'description': 'Cryptocurrency, DeFi, blockchain',
        
        'sources': {
            'telegram': [
                {'username': 'ahboyashreads', 'name': 'Ah Boy Ash Reads', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'shoalresearch', 'name': 'Shoal Research', 'priority': 'high', 'type': 'research', 'enabled': True},
                {'username': 'DecryptNews', 'name': 'Decrypt News', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'WatcherGuru', 'name': 'Watcher Guru', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'unfolded_defi', 'name': 'Unfolded DeFi', 'priority': 'medium', 'type': 'analysis', 'enabled': True},
                {'username': 'wublockchainenglish', 'name': 'Wu Blockchain English', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'CoinDeskGlobal', 'name': 'CoinDesk Global', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'CoinBureau', 'name': 'Coin Bureau', 'priority': 'medium', 'type': 'education', 'enabled': True}
            ],
            'websites': [
                {'name': 'thefeed.today', 'url': 'https://thefeed.today/crypto', 'priority': 'high', 'type': 'news', 'enabled': True}
            ],
            'rss': []
        },
        
        'keywords': {
            'tier_1': {
                'keywords': ['Trump', 'SEC', 'FED', 'Bitcoin', 'Ethereum', 'Solana', 'Hyperliquid', 'Zcash', 'Polymarket', 'Kashi hack', 'exploit', 'Binance', 'Coinbase', 'Iran', 'America', 'USA', 'a16z', 'stablecoin'],
                'weight': 100
            },
            'tier_2': {
                'keywords': ['DeFi', 'layer-1', 'layer-2', 'perp dex', 'prediction market', 'Lighter', 'Base', 'exchange', 'privacy', 'memecoin', 'tokenized assets'],
                'weight': 70
            },
            'tier_3': {
                'keywords': [],
                'weight': 40
            },
            'negative': {
                'keywords': ['airdrop farming', 'pump and dump'],
                'weight': -50
            }
        },
        
        'selection': {
            'worth_reading': {
                'min': 3,
                'max': 5,
                'min_score': 40
            }
        }
    },
    
    'tech': {
        'enabled': True,
        'display_name': 'Tech & AI',
        'icon': '💻',
        'description': 'Software, AI, technology news',
        
        'sources': {
            'telegram': [
                {'username': 'hackernewslive', 'name': 'Hacker News Live', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'tech', 'name': 'Tech Updates', 'priority': 'medium', 'type': 'news', 'enabled': True}
            ],
            'websites': [
                {'name': 'thefeed.today', 'url': 'https://thefeed.today/tech', 'priority': 'high', 'type': 'news', 'enabled': True}
            ],
            'rss': [
                {'name': 'Hacker News', 'url': 'https://news.ycombinator.com/rss', 'priority': 'high', 'enabled': True},
                {'name': 'TechCrunch', 'url': 'https://techcrunch.com/feed/', 'priority': 'medium', 'enabled': True},
                {'name': 'The Verge', 'url': 'https://www.theverge.com/rss/index.xml', 'priority': 'high', 'enabled': True},
                {'name': 'Ars Technica', 'url': 'https://feeds.arstechnica.com/arstechnica/index', 'priority': 'high', 'enabled': True},
                {'name': 'MIT Tech Review', 'url': 'https://www.technologyreview.com/feed/', 'priority': 'high', 'enabled': True}
            ]
        },
        
        'keywords': {
            'tier_1': {
                'keywords': ['anthropic', 'google', 'deepseek', 'kimi', 'hermes', 'openclaw', 'xai', 'openai', 'nvidia', 'claude', 'minimax', 'chatgpt', 'gemini', 'ollama', 'qwen', 'mistral', 'spacex'],
                'weight': 100
            },
            'tier_2': {
                'keywords': ['robotics', 'physical ai', 'ai', 'chip', 'memory'],
                'weight': 70
            },
            'tier_3': {
                'keywords': [],
                'weight': 40
            },
            'negative': {
                'keywords': ['scam', 'fake'],
                'weight': -50
            }
        },
        
        'selection': {
            'worth_reading': {
                'min': 3,
                'max': 5,
                'min_score': 40
            }
        }
    },
    
    'fundraising': {
        'enabled': True,
        'display_name': 'Fund Raise',
        'icon': '💰',
        'description': 'Venture capital and fundraising news',
        
        'sources': {
            'telegram': [
                {'username': 'cryptorank_fundraising', 'name': 'CryptoRank Fundraising', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'crypto_fundraising', 'name': 'Crypto Fundraising', 'priority': 'high', 'type': 'news', 'enabled': True},
                {'username': 'CryptoRankNews', 'name': 'CryptoRank News', 'priority': 'high', 'type': 'news', 'enabled': True}
            ],
            'websites': [],
            'rss': []
        },
        
        'keywords': {
            'tier_1': {
                'keywords': ['a16z', 'csx', 'coinbase', 'dragonfly', 'spartan', 'founder fund', 'sequoia'],
                'weight': 100
            },
            'tier_2': {
                'keywords': [],
                'weight': 70
            },
            'tier_3': {
                'keywords': [],
                'weight': 40
            },
            'negative': {
                'keywords': [],
                'weight': -50
            }
        },
        
        'selection': {
            'worth_reading': {
                'min': 2,
                'max': 4,
                'min_score': 40
            }
        }
    }
}
