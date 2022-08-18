from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        
        return({'message': 'Item not found'}, 404) #404 is for not found

    def post(self, name):
        item = {'name': name, 'price': 14.00}
        items.append(item)
        return item,201 #201 is for created

api.add_resource(Item, '/item/<string:name>')

app.run(port=5000, debug=True)