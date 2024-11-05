import pandas as pd
import numpy as np

data = [['Apple', 10], ['Beta', 20], ['Charlie', 30]]
data1 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
data2 = [{'a':1, 'b':2}, {'a':3, 'b':4, 'c':5}]
data3 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
         'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
data4 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
         'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
data5 = {'three' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data, columns=['Squads', 'Num'], dtype=str)
df1 = pd.DataFrame(data1, index=['rank1', 'rank2', 'rank3', 'rank4'], columns=['Age', 'Name', 'Squads'])
df2 = pd.DataFrame(data2, index=['first', 'second'], columns=['a', 'b', 'c','d'])
df3 = pd.DataFrame(data3, dtype=int)
df4 = pd.DataFrame(data4)
df5 = pd.DataFrame(data5)
df6 = pd.DataFrame({'a_data': [40, 28, 39, 32, 18],
                    'b_data': [20, 37, 41, 35, 45],
                    'c_data': [22, 17, 11, 25, 15]})


#print(df2)
#print(df2['a'])

# 列操作
'''
df3['three'] = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
df3['four'] = df3['one'] + df3['two']
df3.insert(1, column='1.5', value=np.array([1, 2, 3, 4], dtype=float))
print(df3)
print(df3.pop('1.5'))   #
del df3['four']    #删除列
'''

# 行操作
print(df4)
print(df4.loc['a', 'one'])  #仅接受[ 行, 列 ]标签索引
print(df4.iloc[0])  #取行
print(df4[1:3]) # 行切片, 左闭右开
# 使用 pd.concat([df, df2]) 函数将两个 DataFrame 沿着行的方向（axis=0，默认行为）进行合并。
# 合并后的 DataFrame 会有重复的索引（0 和 1），如果你希望重新设置索引，可以使用 ignore_index=True

df5 = pd.concat([df4, df5], axis=1, ignore_index=False) #axis = 0:按行合并
                                                              #axis = 1:按列合并
                                                              #ignore_index:由于可能导致索引重复,故选择是否忽略

print(df5)
print(df4.drop('a', axis=0))

print("==============")
print(df4.T)
print(df4.axes)
print(df4.dtypes)   #返回每列数据类型
'''
print(df4.shape)
print(df4.size)
print(df4.empty)
print(df4.isnull())  ==  print(df4.isna())
print(df4.head())
print(df4.tail())   #默认前/后5行
'''

print(df6.shift(periods=2, axis=0,))