from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
users = {
    "1": {"id": "1", "name": "Alice"},
    "2": {"id": "2", "name": "Bob"}
}

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
