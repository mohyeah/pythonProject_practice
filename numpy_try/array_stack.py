import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

stacked_vertically = np.vstack((arr1, arr2))    #垂直堆叠
stacked_horizontally = np.hstack((arr1, arr2))  #水平堆叠
print(stacked_vertically)
print(stacked_horizontally)