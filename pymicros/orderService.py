from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
orders = [
    {"order_id": "101", "user_id": "1", "product_id": "1001"},
    {"order_id": "102", "user_id": "1", "product_id": "1002"},
    {"order_id": "103", "user_id": "2", "product_id": "1003"}
]

@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    user_orders = [order for order in orders if order["user_id"] == user_id]
    return jsonify(user_orders)

if __name__ == '__main__':
    app.run(port=5001)
