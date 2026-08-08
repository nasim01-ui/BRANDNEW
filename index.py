from flask import Flask, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__)

ROOT = Path(__file__).resolve().parent.parent

@app.route("/")
def home():
    return send_from_directory(ROOT / "public", "index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "running",
        "app": "BrandOS AKIJ"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
