import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1
df = pd.read_csv('Bridges.csv')
print('The shape of the dataset is:', df.shape,"\n")
print('The columns of the dataset are:\n', df.dtypes,"\n")
print("general description:\n",df.describe(),'\n')
print('missing values:\n',df.isnull().sum(),'\n')


#2

#a
q_a = df
q_a = df.dropna(thresh=len(df)*0.9, axis=1)
print(q_a)
#b
"""
q_b = df
#q_b['cat_var'].fillna('Unknown', inplace=True)
print(q_b)
#c
q_c = df
q_c['num_var'].fillna(df['num_var'].mean(), inplace=True)
print(q_c)
"""

