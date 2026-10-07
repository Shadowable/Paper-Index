from flask import Flask, jsonify, render_template

app = Flask(__name__)

ITEMS = [
    {"id": 1, "name": "Notebook"},
    {"id": 2, "name": "Pen"},
]


@app.get("/")
def home():
    return render_template("index.html", items=ITEMS)


@app.get("/items/<int:item_id>")
def item_page(item_id):
    item = next((item for item in ITEMS if item["id"] == item_id), None)
    if item is None:
        return render_template("item.html", item=None), 404
    return render_template("item.html", item=item)


@app.get("/api/items")
def list_items():
    return jsonify(ITEMS)


@app.get("/api/items/<int:item_id>")
def get_item(item_id):
    item = next((item for item in ITEMS if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


if __name__ == "__main__":
    app.run(debug=True)