import numpy as np

arr = np.random.rand(3, 4)
print(arr)
print('Original:\n', arr)
print('Mean:', np.mean(arr))
print('Transposed:\n', arr.T)