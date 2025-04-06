from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
products = {
    "1001": {"id": "1001", "name": "Laptop", "price": 1200},
    "1002": {"id": "1002", "name": "Smartphone", "price": 800},
    "1003": {"id": "1003", "name": "Tablet", "price": 600}
}

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)
