from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get("7770774968:AAF6P4G9OfnQdwZyqjpDR_5KXMv-btvH3BY")
bot = telegram.Bot(token=TOKEN)
URL_PATH = f"/{TOKEN}"  # Secure path for webhook

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route(URL_PATH, methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message = update.message.text

    if message == "/start":
        bot.send_message(chat_id=chat_id, text="Hello! I am alive with webhooks!")
    else:
        bot.send_message(chat_id=chat_id, text=f"You said: {message}")

    return "ok"
