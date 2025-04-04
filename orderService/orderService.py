from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['microservices_db']
orders_collection = db['orders']


@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    orders = list(orders_collection.find({'user_id': user_id}, {'_id': 0}))
    return jsonify(orders)

if __name__ == '__main__':
    app.run(port=5001)
