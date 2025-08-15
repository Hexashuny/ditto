# 🚀 Ditto: Twitter Infographic Scraper

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Ditto is a Python script that **scrapes infographics from Twitter** and sends them to a **Discord channel** via a webhook. It automates sharing visual content from Twitter to your community.

---

## ✨ Features

- 🖼️ **Infographic Scraping**: Extract images and media from Twitter posts.
- 🤖 **Discord Integration**: Send scraped content automatically using webhooks.
- ⏱️ **Automatic Posting**: Continuously monitors Twitter for new content and posts it.

---

## 🛠️ Prerequisites

- **Python 3.10+**
- Required libraries:
  - `requests`
  - `python-dotenv`
  - `tweepy`
  - `Pillow`

Install all dependencies:

```bash
pip install -r requirements.txt

⚙️ Setup
1️⃣ Clone the Repository
git clone https://github.com/Hexashuny/ditto.git
cd ditto

2️⃣ Create a .env File
# Twitter API credentials
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

# Discord webhook URL
DISCORD_WEBHOOK_URL=your_discord_webhook_url

# Optional: Check interval in seconds
CHECK_INTERVAL=60


Replace the placeholders with your actual credentials.

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Usage

Run the script:

python ditto.py


The bot will continuously check for new Twitter posts and send them to your Discord channel.

📜 License

This project is licensed under the MIT License.
You are free to use and modify it, but you cannot sell it and must give credit to the original author.

💬 Support

For questions or feedback, join our Discord community.
