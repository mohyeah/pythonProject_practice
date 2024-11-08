import pandas as pd
import numpy as np

# 创建字典型series结构
data = {'Name': pd.Series(['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L']),
           'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])
     }

df = pd.DataFrame(data)

print(df)
print(df.sum(axis=0))   #默认axis=0
print('\n', end='')
print((df.iloc[:, 1:]).mean(axis=0))
print('\n', end='')
print((df.iloc[:, 1:]).std(axis=0))
print(df.describe(include='all'))