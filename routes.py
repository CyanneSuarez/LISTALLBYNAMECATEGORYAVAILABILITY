# service/routes.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data
items = [
    {"id": 1, "name": "Item 1", "category": "Electronics", "availability": "In Stock"},
    {"id": 2, "name": "Item 2", "category": "Electronics", "availability": "Out of Stock"},
    {"id": 3, "name": "Item 3", "category": "Furniture", "availability": "In Stock"},
]

@app.route('/items', methods=['GET'])
def list_all_items():
    return jsonify(items), 200

@app.route('/items/name/<string:name>', methods=['GET'])
def list_by_name(name):
    filtered_items = [item for item in items if item['name'] == name]
    if filtered_items:
        return jsonify(filtered_items), 200
    else:
        return jsonify({"error": "Item not found"}), 404

@app.route('/items/category/<string:category>', methods=['GET'])
def list_by_category(category):
    filtered_items = [item for item in items if item['category'] == category]
    if filtered_items:
        return jsonify(filtered_items), 200
    else:
        return jsonify({"error": "Category not found"}), 404

@app.route('/items/availability/<string:availability>', methods=['GET'])
def list_by_availability(availability):
    filtered_items = [item for item in items if item['availability'] == availability]
    if filtered_items:
        return jsonify(filtered_items), 200
    else:
        return jsonify({"error": "No items with given availability"}), 404

if __name__ == "__main__":
    app.run(debug=True)
