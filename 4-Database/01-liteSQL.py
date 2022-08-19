import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rose', '123'),
    (3, 'joao', '1234')
]

cursor.executemany(insert_query, users)
select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

#saving the insert
connection.commit()

connection.close()