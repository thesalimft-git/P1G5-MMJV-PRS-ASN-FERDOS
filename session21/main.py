from dbmanager import DbManager

dbm = DbManager()


# products = {
#             "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
#             "name": "TEXT",
#             "price": "REAL",
#             "stock": "INTEGER"
# }

# dbm.create_table('product', products)


# data = {"name": "Phone", "price": 1100, "stock": 20}
# dbm.insert('product', data)



# data = {"stock": 5, 'name': 'new phone'}
# where = {"id": 1}
# dbm.update('product', data, where)


# result = dbm.get_one('product', {"id": 1})
# print(list(result))



# result = dbm.get_many('product', {"id <": 4})
# for item in result:
#     print(list(item))



# where = {"id =": 3}
# x = dbm.delete('product', where)
# print(x)

