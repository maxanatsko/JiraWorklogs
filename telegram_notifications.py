import datetime
import telegram
from config_reader import read_config
import logging
import os

## Read configuration
config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
config = read_config(config_file)
bot_token = config.get('Telegram', 'bot_token')
chat_id = config.get('Telegram', 'chat_id')

bot = telegram.Bot(token=bot_token)

def send_telegram_message(msg_text):
    """Sends a message to the Telegram chat with the provided text."""
    try:
        message = f"*{datetime.datetime.now():%Y-%m-%d %H:%M}:* `{msg_text}`"
        bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        logging.info("Message sent to Telegram")
    except Exception as e:
        logging.error(f"Failed to send message to Telegram: {e}")

# Example usage: send_telegram_message("Hello from Max!")