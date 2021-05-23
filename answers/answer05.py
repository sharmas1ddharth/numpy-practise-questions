import numpy as np

arr = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, np.nan, np.nan]
                ])

array_without_non_numeric_values = arr[~np.isnan(arr).any(axis=1)]

print(f"original array:\n {arr}\n")
print(f"array without non-numeric values:\n {array_without_non_numeric_values}")