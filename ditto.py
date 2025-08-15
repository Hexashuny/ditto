# -*- coding: utf-8 -*-
import os
import time
import logging
import requests
import feedparser
from dotenv import load_dotenv
from normalize_text import normalize_line  # helper for safe UTF-8 normalization
import re

# Load environment variables
load_dotenv()
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")            # Discord webhook URL
RSS_FEED_URL = os.getenv("RSS_FEED_URL")                  # RSS feed URL
ROLE_ID = os.getenv("DISCORD_ROLE_ID")                    # Discord role ID to mention
DISCORD_LINK = os.getenv("DISCORD_LINK")                  # Clickable link text
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))     # Check interval in seconds

if not WEBHOOK_URL or not RSS_FEED_URL or not ROLE_ID or not DISCORD_LINK:
    raise ValueError("Please set all required environment variables in .env")

POSTED_IDS_FILE = "posted_ids.txt"

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

# Load already posted IDs
if os.path.exists(POSTED_IDS_FILE):
    with open(POSTED_IDS_FILE, "r", encoding="utf-8") as f:
        POSTED_IDS = set(f.read().splitlines())
else:
    POSTED_IDS = set()

def save_posted_ids():
    with open(POSTED_IDS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(POSTED_IDS))

def format_blockquote(text):
    """Format text for Discord blockquote with exactly one > per line."""
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join([f"> {line}" for line in cleaned_lines])

def send_to_discord_embed(text, media_urls=[]):
    """Send text + first image inside a single Discord embed with role mention and clickable link."""
    role_mention = f"<@&{ROLE_ID}>"
    clickable_link = f"[{DISCORD_LINK}]({DISCORD_LINK})"
    
    text = text.replace('\\', '').strip()
    blockquote_text = format_blockquote(text)
    
    embed = {"description": blockquote_text}
    if media_urls:
        embed["image"] = {"url": media_urls[0]}

    payload = {
        "content": f"{role_mention}\n{clickable_link}",
        "embeds": [embed]
    }

    try:
        r = requests.post(WEBHOOK_URL, json=payload)
        if r.status_code in (200, 201, 204):
            logging.info("Embed sent successfully.")
        else:
            logging.error(f"Discord embed error {r.status_code}: {r.text}")
    except Exception as e:
        logging.error(f"Error sending Discord embed: {e}")

def fetch_posts(limit=5):
    """Fetch last N posts from RSS feed using only the title."""
    feed = feedparser.parse(RSS_FEED_URL)
    if not feed.entries:
        logging.info("No entries found in feed.")
        return []

    posts = []

    for entry in feed.entries[:limit]:
        text_lines = []

        # Only use title lines
        title_lines = entry.title.splitlines()
        text_lines.extend([line.strip() for line in title_lines if line.strip()])

        # Remove author signature like "— G47IX (@g47ix)"
        text_lines = [re.sub(r'\u2014\s*\S+\s*\(@\S+\)', '', line).strip() for line in text_lines]

        # Remove URLs
        text_lines = [re.sub(r'http\S+', '', line).strip() for line in text_lines]

        # Remove duplicate or similar lines
        seen_normalized = set()
        unique_lines = []
        for line in text_lines:
            normalized = normalize_line(line)
            if normalized and normalized not in seen_normalized:
                seen_normalized.add(normalized)
                unique_lines.append(line)

        cleaned_text = "\n".join(unique_lines)

        # Skip if already posted
        if cleaned_text in POSTED_IDS:
            continue

        # Extract media URLs
        media_urls = []
        if "media_content" in entry:
            for media in entry.media_content:
                if "url" in media:
                    media_urls.append(media["url"])

        posts.append({"id": cleaned_text, "text": cleaned_text, "media": media_urls})

    return posts

def main():
    logging.info("===== SCRAPPER STARTED =====")
    while True:
        try:
            posts = fetch_posts(limit=5)
            for post in reversed(posts):
                send_to_discord_embed(post["text"], post["media"])
                POSTED_IDS.add(post["id"])
            save_posted_ids()
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
