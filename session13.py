users = [
    {'name': 'ali1', 'age': 21, 'city': 'tehran'},
    {'name': 'ali2', 'age': 22, 'city': 'tehran'},
    {'name': 'ali3', 'age': 23, 'city': 'karaj'},
    {'name': 'ali4', 'age': 24, 'city': 'tehran'},
    {'name': 'ali5', 'age': 25, 'city': 'rasht'},
]



# def get_name_by_age(age):
#     for item in users:
#      if item ['age'] == a:
#             print(item['name'])
#             break
#      else:
#          print('can not find')


# get_name_by_age(230)


# def show_users():
#     for item in users:
#         print(
#                 item.get('name'),
#                 item.get('age'),
#                 item.get('city'), 
#                 sep=" - "
# #             )
# show_users()

# def show_users(li):
#     for item in li:
#         for v in item.values():
#             print(v, end=" - ")
#         print()

# show_users()

# def add_birthday():
#     for user in users:
#         user.update({'birthday': 2025 - user.get('age')  })
#         user.pop('age')
#     show_users(users)

# add_birthday()
    
        

# y = lambda x: x ** 2
# print(Y(3))

result = map(lambda item: item.get('name'), users)
print(list(result))