import pandas as pd
import numpy as np


data = np.array(['a', 'b', 'c', 'd', 'e'])
data1 = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
s = pd.Series(data, dtype='str')
s1 = pd.Series(data1)
s2 = pd.Series(data1, index=['a', 'b', 'f', 'e', 'c', 'd'])
s3 = pd.Series(5, index=[0, 1, 2])
print(s)
print(s1)
print(s2)
print(s3)

print("===========")

s4 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s4)
print(s4.iloc[0])   #index location
print(s4['a'])  #索引访问
print(s4[['a', 'c']])
print(s4[:2])

print("============")

s5 = pd.Series(np.random.randn(5))
print(s5)
print(s5.axes)  #返回索引
print(s5.index) #返回一个RangeIndex对象，用来描述索引的取值范围。
print(s5.values)
print(s5.ndim)

print("=========")

s5 = pd.Series(np.random.randn(6))
print(s5.head())    #查看前(n=5)行数据
print(s5.tail())    #查看后(n=5)行数据

print("==========")

s6 = pd.Series([1, 2, None, 4])
print(pd.isnull(s6))    #检测 Series 中的缺失值,若不存在或缺失,return True
print(pd.notnull(s6))   #检测 Series 中的缺失值,若不存在或缺失,return False

