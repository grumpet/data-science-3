import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#4
#a
df = pd.read_csv('Bridges.csv')
bins = [0, 1900, 1960, np.inf]

labels = ['very old', 'old', 'modern']

new_df = df.copy()

new_df['ERECTED'] = pd.cut(df['ERECTED'], bins=bins, labels=labels)


#b
cols_to_keep = ['LANES', 'T-OR-D', 'MATERIAL']
cols_to_drop = df.columns.difference(cols_to_keep)

df_b = df.drop(columns=cols_to_drop)

df_b = pd.get_dummies(df_b, columns=['T-OR-D', 'MATERIAL'])
