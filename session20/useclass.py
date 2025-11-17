from dbmanager import DbManager

dbm = DbManager()

# columns = {
#     "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
#     "name": "TEXT",
#     "price": "REAL",
#     "stock": "INTEGER"
# }

# dbm.create_table('product', columns)

columns = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "firstname": "TEXT",
    "lastname": "TEXT",
    "email": "TEXT",
    "password": "TEXT",
  
}

dbm.create_table('user', columns)