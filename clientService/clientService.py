import requests
from flask import Flask, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")  # Change if using a remote database 
db = client["microservices_db"]
user_collection = db["users"]
orders_collection = db["orders"]
products_collection = db["products"]

@app.route('/orders/<user_id>', methods=['GET'])
def get_user_order_details(user_id):
    # Fetch user details
    user_data = users_collection.find_one({"user_id": user_id}, {"_id": 0})
    # Check if user exists
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    # Fetch orders for the user
    orders = list(orders_collection.find({"user_id": user_id}, {"_id": 0}))
    # Check if orders exist
    if not orders:
        return jsonify({"error": "No orders found for this user"}), 404

    # Fetch product details for each order
    for order in orders:
        product_data = products_collection.find_one({"product_id": order["product_id"]}, {"_id": 0})
        if product_data:
            order["product_details"] = product_data
    # Consolidate data
    response_data = {
        "user": user_data,
        "orders": orders
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=5003)
