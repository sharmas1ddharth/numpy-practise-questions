import numpy as np

arr = np.array([1, 2, 3, 4, 5, 1, 2, 2, 9])

most_frequent_element = np.bincount(arr)

print(f"most frequent element is '{most_frequent_element.argmax()}' with total count of {max(most_frequent_element)}")
