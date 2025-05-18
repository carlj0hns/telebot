import os
from flask import Flask, request
import telegram

# ✅ Get bot token from environment variable
TOKEN = os.environ.get("7770774968:AAF6P4G9OfnQdwZyqjpDR_5KXMv-btvH3BY")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables!")

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Telegram webhook handler
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Simple reply
    bot.sendMessage(chat_id=chat_id, text=f"You said: {text}")
    return "OK"

# Root route (optional)
@app.route("/", methods=["GET"])
def home():
    return "Telegram bot is running!"

if __name__ == "__main__":
    app.run(port=5000)
