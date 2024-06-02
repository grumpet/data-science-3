import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#3
df = pd.read_csv('Bridges.csv')
#3a
plt.hist(df['LENGTH'])
plt.show()

df['LOG_LENGTH'] = df['LENGTH'].mask(df['LENGTH']<1, 1)
df['LOG_LENGTH'] = np.log10(df['LOG_LENGTH'])
plt.hist(df.LOG_LENGTH)
plt.show()