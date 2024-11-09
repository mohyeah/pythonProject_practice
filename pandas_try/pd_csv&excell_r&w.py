import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('F:/PyCharm code/PycharmProjects/pythonProject_practice/pandas_try/pd_csv_try.csv')
print(df)

df2 = pd.read_csv('F:/PyCharm code/PycharmProjects/pythonProject_practice/pandas_try/pd_csv_try.csv',
                  names=['a', 'b', 'c', 'd', 'e'], skiprows=1)
info = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
csv_data = info.to_csv('F:/PyCharm code/PycharmProjects/pythonProject_practice/pandas_try/pd_to_csv_try.csv', index=True, sep=',')

