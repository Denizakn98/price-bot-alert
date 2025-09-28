import os
import time
import threading
import requests
from telegram.ext import Updater, CommandHandler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") or "PASTE_YOUR_BOT_TOKEN_HERE"

user_alerts = {}  # chat_id -> {'btc': price, 'eth': price}

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    r = requests.get(url)
    data = r.json()
    return data[symbol]['usd']

def start(update, context):
    update.message.reply_text(
        "Welcome to the Bitcoin/Ethereum Price Alert Bot!\n"
        "Use /setbtc <price> or /seteth <price> to set alerts."
    )

def set_btc(update, context):
    try:
        price = float(context.args[0])
        chat_id = update.effective_chat.id
        user_alerts.setdefault(chat_id, {})['btc'] = price
        update.message.reply_text(f"BTC alert set at ${price}")
    except Exception:
        update.message.reply_text("Usage: /setbtc <price>")

def set_eth(update, context):
    try:
        price = float(context.args[0])
        chat_id = update.effective_chat.id
        user_alerts.setdefault(chat_id, {})['eth'] = price
        update.message.reply_text(f"ETH alert set at ${price}")
    except Exception:
        update.message.reply_text("Usage: /seteth <price>")

def check_prices(context):
    while True:
        for chat_id, alerts in user_alerts.items():
            if 'btc' in alerts:
                btc_price = get_price('bitcoin')
                if (btc_price >= alerts['btc']):
                    context.bot.send_message(chat_id, f"BTC price alert!\nCurrent price: ${btc_price}")
                    del alerts['btc']
            if 'eth' in alerts:
                eth_price = get_price('ethereum')
                if (eth_price >= alerts['eth']):
                    context.bot.send_message(chat_id, f"ETH price alert!\nCurrent price: ${eth_price}")
                    del alerts['eth']
        time.sleep(60)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("setbtc", set_btc))
    dp.add_handler(CommandHandler("seteth", set_eth))

    # Start price checking in a thread
    threading.Thread(target=check_prices, args=(updater.bot,), daemon=True).start()
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
