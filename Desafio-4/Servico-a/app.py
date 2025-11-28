from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Ana", "active_since": "2021-04-10"},
    {"id": 2, "name": "Bruno", "active_since": "2022-01-15"},
    {"id": 3, "name": "Carla", "active_since": "2020-09-03"}
]

@app.route("/users")
def users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    