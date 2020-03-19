### classes start with capital (convention)
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

stores = [
    {
        "name": "my wonderful store",
        "items": [
            {
             "name": "Item One",
             "price": 15.99   
            }
        ]
    }
]

# POST - used to receive data (from the webserver perspective)
# GET - used to send data back only (from the webserver perspective)


# POST /store data: {name: }
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"]
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route("/store/<string:name>") # "http://127.0.0.1:5000/store/some_name"
def get_store(name):
    # iterate over stores and find the one with the name
    for store in stores
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "not found"})

# GET /store
@app.route("/store")
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            request_data = request.get_json()
            new_item = {
                "name": request_data["item"]
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})

    
    request_data = request.get_json()
    new_item = {
        "name": request_data["name"]
        "items": request["item"]
    }
    stores.append(new_store)
    return jsonify(new_item)

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"message": "store not found"})


@app.route("/") # 'http call on some page'
# decorator always acts on a method
def home():
    return "Hello, world!"

app.run(port=5000)
