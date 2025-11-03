from flask import Flask, request, jsonify
app = Flask(__name__)

MODEL = {
    "hi": "Hello! How can I help you today?",
    "what is your name": "I am TestBot, your testing assistant.",
    "default": "Sorry, I didn't understand that. Could you rephrase?"
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = (data.get("message") or "").strip().lower()
    # simple matching
    response = MODEL.get(message, MODEL["default"])
    return jsonify({
        "message": message,
        "response": response,
        "metadata": {"matched": message in MODEL}
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
