import sqlite3

class UserModel:
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