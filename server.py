import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY","")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/verify", methods=["POST"])
def verify():
    data = request.get_json(silent=True) or {}
    key = data.get("api_key", "")

    if key and key == API_KEY:
        return jsonify({
            "success": True,
            "message": "Access granted"
        })

    return jsonify({
        "success": False,
        "message": "Invalid API key"
    }), 401

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

