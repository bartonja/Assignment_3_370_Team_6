from flask import Flask, jsonify
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['microservices_db']
users_collection = db['users']


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({"user_id": user_id}, {"_id": 0})
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
