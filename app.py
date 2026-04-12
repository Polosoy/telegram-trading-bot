from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8494992296:AAHphD4LulAA2dZ_0L0xtN7NRliIWeHe-Xk")
CHAT_ID = os.environ.get("357177171")

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}

    message = f"""{data.get('side')} {data.get('symbol')}
Entry: {data.get('entry')}
SL: {data.get('sl')}
TP: {data.get('tp')}"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return ("ok", 200) if r.ok else (r.text, 500)

@app.route("/", methods=["GET"])
def home():
    return "Bot is live", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))