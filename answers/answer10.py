import numpy as np

array_1 = np.array([1, 2])
array_2 = np.array([4, 5])

print(np.array(np.meshgrid(array_1, array_2)).T.reshape(-1, 2))
