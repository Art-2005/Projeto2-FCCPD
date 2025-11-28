from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://service-a:5001")

@app.route("/report")
def report():
    try:
        r = requests.get(f"{SERVICE_A_URL}/users", timeout=3)
        r.raise_for_status()
        users = r.json()
    except Exception as e:
        return jsonify({"error": "falha ao obter usuários", "detail": str(e)}), 500

    report_lines = []
    for u in users:
        report_lines.append(f"Usuário {u['name']} — ativo desde {u['active_since']}")

    return "<br>".join(report_lines) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
