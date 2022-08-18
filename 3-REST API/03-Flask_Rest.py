from flask import Flask, request
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
        data = request.get_json(force=True, silent=True) #force=true disables the header, prevents error if the format is not json, silence=true will not return an error, will simple not run
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item,201 #201 is for created

class Items(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)