users = [
    {'name': 'ali1', 'age': 21, 'city': 'tehran'},
    {'name': 'ali2', 'age': 22, 'city': 'tehran'},
    {'name': 'ali3', 'age': 23, 'city': 'karaj'},
    {'name': 'ali4', 'age': 24, 'city': 'tehran'},
    {'name': 'ali5', 'age': 25, 'city': 'rasht'},
]

# list comprehension
# names = [item.get('name') for item in users]
# print(names)

# map : get or create a value from iterator 
# m = map(lambda item: item.get('name'), users)
# print(list(m))

# who is tehrani
# f = filter(lambda item: item.get('city') == 'tehran' , users)
# print(list(f))

# whose age is more than 23
# f = filter(lambda item: item.get('age') > 23 , users)
# print(list(f))


# list anem of user who are tehrani
# f = filter(lambda item: item.get('city') == 'tehran', users)
# m = map(lambda item: item.get('name'), f)
# print(list(m))



# m = map(lambda item: item.get('name'), 
#             filter(lambda item: item.get('city') == 'tehran', users)
#         )

# m = m.copy()
# print(m)
# print(m)
# print(m)


# li = ['a', 's', 'z', 'b']
# li.sort(reverse=True)
# print(li)

# s = sorted(users, key=lambda item: item.get('city'))
# print(s)




# m = map(lambda item: item.get('name'), 
#         sorted(users, key=lambda item: item.get('city'))
#     )

# print(list(m))





