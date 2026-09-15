from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Buy groceries", "description": "Milk, bread, eggs"},
    {"id": 2, "name": "Finish homework", "description": "Maths assignment"},
    {"id": 3, "name": "Read a book", "description": "Data Science notes"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"

# GET: Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# POST: Create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Invalid request, 'name' required"}), 400

    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item), 201  # 201 Created

if __name__ == "__main__":
    app.run(debug=True)
