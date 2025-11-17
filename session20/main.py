# sql --> crud
# create,read,update, delete
# mysql, postgress, sqlite
# python sqlite3

# 1- conection
# 2- cursor
# 3- command
# 4- execute command
# 5- commit

# create: CREATE TABLE <tablename>(field1, filed2, filed3)
import sqlite3
con = sqlite3.connect("test.db")
cur = con.cursor()

# create Table
# -----------------------------------------
# command = """
#     CREATE TABLE product(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         price REAL,
#         stock INTEGER
# )
# """
# cur.execute(command)


# command = "CREATE TABLE IF NOT EXISTS user(id, first_name, last_name, username, password)"
# cur.execute(command)

# command = "CREATE TABLE orders(id, user_id, product_id)"
# cur.execute(command)


# command = """
#     INSERT INTO user VALUES
#         (1, 'ali', 'akbari', 'ali@gmail.com', '1234'),
#         (2, 'reza', 'akbari', 'reza@gmail.com', '9876')
# """

# cur.execute(command)
# con.commit()
