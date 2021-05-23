import numpy as np

one_dimensional_array = np.arange(6)
two_dimensional_array = np.arange(12).reshape(2, 6)

for x, y in np.nditer([one_dimensional_array, two_dimensional_array]):
    print(f"[{x}, {y}]")

