from flask import Flask, jsonify

app = Flask(__name__)

ORDERS = [
    {"order_id": 101, "user_id": 1, "total": 99.90},
    {"order_id": 102, "user_id": 2, "total": 149.50},
    {"order_id": 103, "user_id": 1, "total": 59.99},
]

@app.route("/orders")
def get_orders():
    return jsonify(ORDERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)