#
import numpy as np
arr = np.arange(20)
print(arr)
reshaped_arr = arr.reshape(2,2,5)# rows, columns, inner array and 2*2*5=20
print(reshaped_arr)