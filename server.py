from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "938657265"

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:8080"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return response

@app.route("/verify", methods=["POST", "OPTIONS"])
def verify():
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json(silent=True) or {}
    key = data.get("api_key", "")

    if key == API_KEY:
        return jsonify({
            "success": True,
            "message": "Access granted"
        })

    return jsonify({
        "success": False,
        "message": "Invalid API key"
    }), 401

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
