# RSS to Discord Bot

A Python bot that fetches posts from an RSS feed and sends them to a Discord channel with role mentions and embedded images. Ideal for updates, announcements, and news feeds.

## Features

- Fetches the latest posts from an RSS feed.
- Sends messages as Discord embeds with optional images.
- Adds a role mention at the top of each post.
- Normalizes text to prevent duplicate lines.
- Configurable check interval.
- Keeps track of already posted content.

## Prerequisites

- Python 3.10+
- `requests`
- `feedparser`
- `python-dotenv`

Install dependencies:

```bash
pip install -r requirements.txt
Setup

Clone the repository:

git clone https://github.com/yourusername/your-repo.git
cd your-repo


Create a .env file in the root directory with the following placeholders:

# Discord
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_here
DISCORD_ROLE_ID=your_role_id_here
DISCORD_LINK=https://discord.gg/your_invite_here

# RSS feed
RSS_FEED_URL=https://your_rss_feed_here.xml

# Optional
CHECK_INTERVAL=60


Place normalize_text.py in the same folder as the main script.

Usage

Run the bot:

python scrapper.py


The bot will continuously check the RSS feed at the interval set in .env and post new entries to Discord.
