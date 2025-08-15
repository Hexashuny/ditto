Ditto: Twitter Infographic Scraper

Ditto is a Python script that scrapes infographics from Twitter and sends them to a Discord channel via a webhook. It's designed to automate the process of sharing visual content from Twitter to your Discord community.

Features

Infographic Scraping: Extracts images and media from Twitter posts.

Discord Integration: Sends scraped content to a specified Discord channel using webhooks.

Automatic Posting: Continuously monitors Twitter for new infographics and posts them to Discord.

Prerequisites

Python 3.10+

Required Python libraries:

requests

python-dotenv

tweepy

Pillow

You can install the necessary libraries using:

pip install -r requirements.txt

Setup

Clone the Repository

git clone https://github.com/Hexashuny/ditto.git
cd ditto


Create a .env File

In the project root, create a .env file with the following content:

# Twitter API credentials
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

# Discord webhook URL
DISCORD_WEBHOOK_URL=your_discord_webhook_url

# Optional: Check interval in seconds
CHECK_INTERVAL=60


Replace the placeholders with your actual Twitter API credentials and Discord webhook URL.

Install Dependencies

Ensure all required libraries are installed:

pip install -r requirements.txt

Usage

Run the script to start scraping Twitter for infographics and posting them to your Discord channel:

python ditto.py


The script will continue running, checking for new content at the interval specified in the .env file.

License

This project is licensed under the MIT License.
