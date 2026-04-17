from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    token_ok = "yes" if BOT_TOKEN else "no"
    chat_ok = "yes" if CHAT_ID else "no"
    return f"Bot is live | BOT_TOKEN loaded: {token_ok} | CHAT_ID loaded: {chat_ok}", 200

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}

    message = data.get("message", "No message received")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    r = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return (r.text, r.status_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
