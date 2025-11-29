from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

USERS_URL = os.getenv("USERS_URL", "http://service-users:5001")
ORDERS_URL = os.getenv("ORDERS_URL", "http://service-orders:5002")

@app.route("/users")
def users():
    r = requests.get(f"{USERS_URL}/users")
    return jsonify(r.json())

@app.route("/orders")
def orders():
    r = requests.get(f"{ORDERS_URL}/orders")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
    