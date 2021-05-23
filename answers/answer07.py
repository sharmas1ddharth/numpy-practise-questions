import numpy as np

arr = np.array([[1, 2, 3],
                [4, 1, 2],
                [1, 8, 2]])

sequence_to_count = '1, 2'
sequence_count = repr(arr).count(sequence_to_count)

print(f"number of times the sequence {sequence_to_count} comes in original array is : {sequence_count}")