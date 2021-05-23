import numpy as np

arr = np.array([[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]])


squeezed_array = np.squeeze(arr)

print(f"original array \n {arr} \n shape of original array {arr.shape}\n")
print(f"squeezed array \n {squeezed_array} \n shape of squeezed array {squeezed_array.shape}")