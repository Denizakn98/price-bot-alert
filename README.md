# price-bot-alert# Bitcoin Price Alert Bot

A simple Telegram bot that monitors Bitcoin (BTC) and Ethereum (ETH) prices and sends price alerts to users.

## Features

- Monitors BTC and ETH prices using the CoinGecko API
- Sends alerts to your Telegram when the price crosses your threshold
- Supports multiple users and custom alert levels

## Requirements

- Python 3.8+
- `requests`, `python-telegram-bot` libraries (`pip install requests python-telegram-bot`)
- A Telegram Bot Token (from BotFather on Telegram)

## Setup

1. Clone this repository.
2. Install requirements:
   ```
   pip install requests python-telegram-bot
   ```
3. Set your Telegram bot token as an environment variable or directly in the code.
4. Start the bot:
   ```
   python bot.py
   ```
5. On Telegram, search for your bot and start chatting!
6. Use `/setbtc 40000` or `/seteth 2500` to set price alerts.

## Example Commands

- `/start` — Start the bot
- `/setbtc <price>` — Set BTC price alert
- `/seteth <price>` — Set ETH price alert

**Note:** This is for educational use. Do not use for trading.
