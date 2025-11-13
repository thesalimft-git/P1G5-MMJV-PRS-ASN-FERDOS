# module    ==>(single file) json, datetime, math, random
# library   ==> (some file in a folders) bs4
# framework ==> (some folders and libraries) django


# import requests
# import time

# path = 'https://apiv2.nobitex.ir/v3/orderbook/USDTIRT'
# result = requests.get(path)

# last_price = result.json().get('lastTradePrice')
# last_price = float(last_price)

# print('last_price: ', last_price)

# while True:
#     time.sleep(2)
#     result = requests.get(path)
#     new_price = result.json().get('lastTradePrice')
#     new_price = float(new_price)
#     print('new_price: ', new_price)
    
#     if new_price > last_price * 1.01:
#         print('market alert')
        
        
#     if new_price < last_price * 0.99:
#         print('market alert')
        
#     last_price = new_price
    