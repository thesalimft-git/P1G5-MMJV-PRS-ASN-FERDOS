# Data Analyses, ml, dl, ai

import numpy as np
import pandas as pd


# ar = np.array([[1, 2], [3, 4]])
# print(ar)


df = pd.DataFrame({
    'name':['ali', 'reza', 'sara'],
    'age': [23, 24, 25],
    'weight': [80, 70, 65],
    'height': [180, 170, 165],
    'car': ['sia', '206', 'x']
    })


# print(df['height']/df['weight'])
print(df)

# title,teacher,price
# php,ali,100
# js,reza,200


df.to_csv('students.csv')


