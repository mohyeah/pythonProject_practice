import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#创建包含时间序列的数据
df = pd.DataFrame(np.random.randn(8,4),index=pd.date_range('2/1/2020',periods=8), columns=list('ABCD'))
df.plot(kind='bar', stacked=True)
#plt.show()

df2 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
print(df2)
df2.plot(kind='barh', stacked=True) #水平柱状图
plt.show()