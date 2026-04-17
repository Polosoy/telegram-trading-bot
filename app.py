from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Webhook is live", 200


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}

    # 🔍 Debug (optional - remove later)
    print("Incoming data:", data)

    # ✅ Get TradingView message directly
    message = data.get("message")

    # Fallback (in case TradingView sends raw text differently)
    if not message:
        message = str(data)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return jsonify({"status": "ok", "telegram": response.text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
