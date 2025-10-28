users = [
    {'name': 'ali1', 'age': 21, 'city': 'tehran'},
    {'name': 'ali2', 'age': 22, 'city': 'tehran'},
    {'name': 'ali3', 'age': 23, 'city': 'karaj'},
    {'name': 'ali4', 'age': 24, 'city': 'tehran'},
    {'name': 'ali5', 'age': 25, 'city': 'rasht'},
]

def func1():
    print('hello')
# map, filter, zip

# def get_name_by_age(a):
#     for item in users:
#         if item['age'] == a:
#             print(item['name'])
#             break
#     else:
#         print('can not fine')

# get_name_by_age(230)



# # get the number of user in users
# print(len(users))




# line by line print [ali1 - 21 - tehran ]
# def show_users(li):
#     for item in li:
#         for v in item.values():
#             print(v, end=" - ")
#         print()
        
# show_users(users)

# goal: [ ali1 - tehran - 2004 ]
# user = {'name': 'ali1', 'age': 21, 'city': 'tehran'}

# remove key value from dict
# user.pop('age')

# add birthday
# user.update({'birthday': 2004})



# a function that remove age, and ass birthday
# def add_birthday():
#     for user in users:
#         user.update({'birthday': 2025 - user.get('age') })
#         # user['birthday'] = 2024
        
#         user.pop('age')
#     show_users(users)


# add_birthday()






# def func(x):
#     return x ** 2

# anonymous, callback, lambda function
# y = lambda x: x ** 2
# print(y(3))


# map, sorted, filter: iterable [list, set, tuple, dict, string]
# def func():
#     pass

# result = map(lambda item: item.get('name'), users)
# y = list(result).copy()

# print(y)


