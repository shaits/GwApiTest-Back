from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow all origins — useful for local/frontend dev

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from backend!"})

@app.route("/api/ping")
def ping():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
