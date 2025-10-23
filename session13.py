users = [
    {'name' : 'ali1', 'age': 21, 'city': 'Tehran'},
    {'name' : 'ali2', 'age': 22, 'city': 'Tehran'},
    {'name' : 'ali3', 'age': 23, 'city': 'Karaj'},
    {'name' : 'ali4', 'age': 24, 'city': 'Tehran'},
    {'name' : 'ali5', 'age': 25, 'city': 'Rasht'},
]
# map, filter, zip
# iterable : list,dict,tuple,string
# map(1, 2)

# def func(x):
#     return x ** 2

# anonymous, callback, 

# y = lambda x: x ** 2

# print(y(3))


# def get_name_by_age(a):
#     for item in users:
#         if item['age'] == a:
#             print(item['name'])
#             break
#     else:
#         print('can not find')

# get_name_by_age(27)

# get the number of user in users
# print(len(users))

# def show_users():
#     for item in users:
#         print(
#                 item.get('name'),
#                 item.get('age'),
#                 item.get('city'),
#                 sep = " - " 
#                 )

def show_users(li):
    for item in li:
        for v in item.values():
            print(v, end = " - ")
        print()

# [ali - tehran - 2004]
# show_users(users)
    
# user = {'name' : 'ali1', 'age': 21, 'city': 'Tehran'},
 
# user.pop('age')
# user.update({'birthday' : 2004})

# def add_birthday():
#     for user in users:
#         user.update({'birthday' : 2025 - user.get('age')})
#         user['birthday'] : 
#         user.pop('age')
#     show_users(users)

# add_birthday()

result = map(lambda item : item.get('name'), users)
print(list(result))

# y = list(result).copy()