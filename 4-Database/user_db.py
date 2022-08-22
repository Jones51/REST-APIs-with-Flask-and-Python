from cgitb import text
import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id,username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,)) #(username, ) since the value needs to be a tuple, and a single tuple goes like this
        row = result.fetchone() #get the first result
        if row:
            #creates an user with the database info
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,)) #(_id, ) since the value needs to be a tuple, and a single tuple goes like this
        row = result.fetchone() #get the first result
        if row:
            #creates an user with the database info
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        
        connection.close()
        return user

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required = True,
        help ='This field cannot be left blank'
    )
    parser.add_argument('password',
        type=str,
        required = True,
        help ='This field cannot be left blank'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "An user with that username already exists"}, 400
        

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" #The first one needs to be NULL since it its the id
        cursor.execute(query, (data['username'], data['password'],)) #remember the data needs to be a turple

        connection.commit()
        connection.close()

        return {"message": "User created successfully "}, 201


