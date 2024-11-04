import numpy as np

data = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
data2 = np.zeros(shape=(3, 3))
data3 = np.ones(shape=(3, 3))
data4 = np.arange(10, 16, 2)
data5 = np.linspace(1, 10, 10)  #创建有连续间隔的数组
data6 = np.random.rand(3, 4)
data7 = np.random.randint(2, 5, size=(3, 3))
data8 = np.reshape(data, shape=(4, 2))
data9 = data8.T #转置
print(data)
print(data.shape)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data7)
print(data8)
print(data9)
