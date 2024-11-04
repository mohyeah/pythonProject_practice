import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

np.save("my_array.npy", arr1)
load_data = np.load("my_array.npy")

print(load_data)