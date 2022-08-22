from multiprocessing import connection
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

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
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': "item not found"}, 400

    #We could originally use the get method, however it is authenticated by jwt, so we created this class method instead
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone() #getting only the first resuld

        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        #checking first if the item already exist
        if self.find_by_name(name):
            return {'message': f"An item with the name {name} already exists"}, 400
        
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
            self.insert(item)
        except:
            return {'message': "Error while trying to inser the item"},500

        return item,201 #201 is for created

    #for the Put method to work, we can't call the POST method, so we extracted the creation in a class method
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price'],))

        connection.commit()
        connection.close()

    def delete(self, name):
        #Checking if the item indeed exist in the database
        if self.find_by_name(name):
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
        #instead of using data=request.get_json. we use the parse for validation and security
        #Also, using the "Item" in front is necesay since by declaring it above, its now a class method, and we need to use it internally now
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}

        #if the item is none, it doesnt exist, we create id
        if item == None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error ocurred when trying to insert the new item"}, 500
        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error ocurred when trying to update the new item"}, 500
        
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name'],))

        connection.commit()
        connection.close()

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