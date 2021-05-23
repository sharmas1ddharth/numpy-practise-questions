import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

array_to_find = [1, 2, 3, 4]
array_to_find2 = [1, 2, 5, 6]

print(array_to_find in arr.tolist())
print(array_to_find2 in arr.tolist())