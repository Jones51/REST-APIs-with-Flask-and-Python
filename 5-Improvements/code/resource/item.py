from multiprocessing import connection
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    #by using the reparse we limit the elements to be updated
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required = True,
        help ='This field cannot be left blank'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': "item not found"}, 400

    def post(self, name):
        #checking first if the item already exist
        if ItemModel.find_by_name(name):
            return {'message': f"An item with the name {name} already exists"}, 400
        
        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {'message': "Error while trying to inser the item"},500

        return item,201 #201 is for created
    
    def delete(self, name):
        #Checking if the item indeed exist in the database
        if ItemModel.find_by_name(name):
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (name,))

            connection.commit()
            connection.close()

            return {'message': f"Item {name} deleted"}, 200
        
        #In case the item doesnt exist
        return {'message': 'There is no item with that name in the database'}, 400

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item == None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error ocurred when trying to insert the new item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error ocurred when trying to update the new item"}, 500
        
        return updated_item


class Items(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0],'price': row[1]})

        connection.commit()
        connection.close()

        return {'items': items}