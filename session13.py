# users = [
#     {'name' : 'ali1', 'age': 21, 'city': 'tehran'},
#     {'name' : 'ali2', 'age': 22, 'city': 'tehran'},
#     {'name' : 'ali3', 'age': 23, 'city': 'karaj'},
#     {'name' : 'ali4', 'age': 24, 'city': 'tehran'},
#     {'name' : 'ali5', 'age': 25, 'city': 'rasht'},
# ]

# def get_name_by_age(a):
#     for item in users:
#         if item['age'] == a:
#             print(item['name'])
#             break
#     else:
#         print('can not find')  
#   
# get_name_by_age(230)


# print(len(users))


# def show_users():
#     for item in users:
#         print(
#             item.get('name'),
#             item.get('age'),
#             item.get('city'),
#             sep= ' - '
#               )

# def show_users(li):
#     for item in li:
#         for v in item.values():
#             print(v, end=' - ')
#         print()

# goal = ['ali1 - tehran - 2004]
# show_users(users)


# user = {'name' : 'ali4', 'age': 24, 'city': 'tehran'}


# user.pop('age')
# user.update({'birthday' : 2004})

# def add_birthday():
#     for user in users:
#         # user.update({'birthday': 2025 - user.get('age')})
#         user['birthday'] = 2024 - user
#         user.pop('age')
#     show_users(users)

# add_birthday()


users = [
    {'name' : 'ali1', 'age': 21, 'city': 'tehran'},
    {'name' : 'ali2', 'age': 22, 'city': 'tehran'},
    {'name' : 'ali3', 'age': 23, 'city': 'karaj'},
    {'name' : 'ali4', 'age': 24, 'city': 'tehran'},
    {'name' : 'ali5', 'age': 25, 'city': 'rasht'},
]


# y = lambda x: x ** 2
# print(y(3))

res = list(map(lambda item: item.get('name'), users))
print(res)

# print(list(res))


