users = [
    {'name' : 'ali1', 'age': 21, 'city': 'Tehran'},
    {'name' : 'ali2', 'age': 22, 'city': 'Tehran'},
    {'name' : 'ali3', 'age': 23, 'city': 'Karaj'},
    {'name' : 'ali4', 'age': 24, 'city': 'Tehran'},
    {'name' : 'ali5', 'age': 25, 'city': 'Rasht'},
]

# list comprehension
# names = [item.get('name') for item in users]
# print(names)

# cities = [lambda item: len('item')]

# map = get or create a value from iterator

# m = map(lambda item: item.get('name'), users)
# print(list(m))

# # who's from tehran
# f = filter(lambda item: item.get('city') == 'Tehran', users)
# print(list(f))

# whose age is more than 23
# f = filter(lambda item: item.get('age') > 23 , users)
# print(list(f))

# list a name of who's from tehran
# f = filter(lambda item: item.get('city') == 'Tehran', users)
# m = map(lambda item: item.get('name'), f)
# print(list(m))


# m = map(lambda item: item.get('name'),
#             filter(lambda item: item.get('city') == 'Tehran', users)
#             )
# m = m.copy
# print(m)
# print(m)
# print(m)

# sort
# li = ['a', 's', 'z', 'b']
# li.sort(reverse= True)
# print(li)

# sorted
# s = sorted(users, key= lambda item: item.get('city'))
# print(s)

# m = map(lambda item: item.get('name'),
#         sorted(users, key= lambda item: item.get('city'))
#     )
# print(list(m))