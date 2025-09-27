from flask import Flask, request, jsonify
from flask_cors import CORS

# Create the app
app = Flask(__name__)
CORS(app)  # allow cross-origin requests (useful in dev)

# Very simple in-memory store (resets if you restart the server)
DATA_STORE = {"messages": []}

@app.route("/ping", methods=["GET"])
def ping():
    """
    Simple health-check endpoint.
    GET /ping  -> returns {"status":"ok","msg":"pong"}
    """
    return jsonify({"status": "ok", "msg": "pong"}), 200

@app.route("/messages", methods=["GET", "POST"])
def messages():
    """
    GET /messages  -> returns list of saved messages
    POST /messages -> accept JSON {"text": "..."} and save it
    """
    if request.method == "GET":
        # Return all saved messages as JSON
        return jsonify(DATA_STORE["messages"]), 200

    # For POST: parse JSON body
    payload = request.get_json(force=True, silent=True)
    if not payload or "text" not in payload:
        # Bad request if JSON missing or "text" key absent
        return jsonify({"error": "missing 'text' field"}), 400

    item = {"text": payload["text"]}
    DATA_STORE["messages"].append(item)
    # Return created item and HTTP 201 (created)
    return jsonify(item), 201

@app.route("/", methods=["GET"])
def home():
    return "Simple GET/POST API running. Use /ping or /messages."


if __name__ == "__main__":
    # Run dev server, 0.0.0.0 binds to all interfaces (useful later for LAN)
    app.run(host="0.0.0.0", port=5000, debug=True)
