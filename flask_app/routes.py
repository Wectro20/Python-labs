from flask import request, jsonify, abort
from database.database import Item, item_schema, items_schema
from .flask_app import app, db
from marshmallow import ValidationError


# endpoint to create new item
@app.route("/item", methods=["POST"])
def add_item():
    try:
        item = item_schema.load(request.json)
        db.session.add(item)
    except ValidationError as response:
        abort(400, response)

    db.session.commit()

    return jsonify(request.json)


# endpoint to show all items
@app.route("/item", methods=["GET"])
def get_items():
    all_items = Item.query.all()
    result = items_schema.dump(all_items)
    return jsonify(result)


# endpoint to get item detail by id
@app.route("/item/<id>", methods=["GET"])
def item_detail(id):
    item = Item.query.get(id)
    if item is None:
        response = jsonify({
            "Status": 404,
            "Description": "No such an id"
        })
        abort(404, response)
    return item_schema.jsonify(item)


# endpoint to update item
@app.route("/item/<id>", methods=["PUT"])
def item_update(id):
    item_p = Item.query.get(id)
    if item_p is None:
        response = jsonify({
            "Status": 404,
            "Description": "No such an id"
        })
        abort(404, response)
    try:
        item = item_schema.load(request.json)
        item_p.name = item.name
        item_p.price = item.price
        item_p.country = item.country
        item_p.material = item.material
        item_p.brand = item.brand
        item_p.gender = item.gender
        item_p.size = item.size
        item_p.type_of_sport = item.type_of_sport

    except ValidationError as response:
        abort(400, response)

    db.session.commit()
    return item_schema.jsonify(item_p)


# endpoint to delete item
@app.route("/item/<id>", methods=["DELETE"])
def item_delete(id):
    item = Item.query.get(id)
    if item is None:
        response = jsonify({
            "Status": 404,
            "Description": "No such an id"
        })
        abort(404, response)

    db.session.delete(item)
    db.session.commit()

    return item_schema.jsonify(item)
