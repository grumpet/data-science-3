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

missing_percent = df.isnull().sum() / len(df) * 100
colomns_to_drop = []
for  index,value in missing_percent.items():
    if (value < 10 and value > 0):
        colomns_to_drop.append(index)
        
df_drop = df.dropna(subset=colomns_to_drop)

#b
df_change_catagorical = df.copy()
for col in colomns_to_drop:
    df_change_catagorical[col] = df_change_catagorical[col].fillna('missing')
    
#c
df_change_mean = df.copy()
for col in colomns_to_drop:
    df[col].fillna(df[col].mode()[0], inplace=True)
    
    



