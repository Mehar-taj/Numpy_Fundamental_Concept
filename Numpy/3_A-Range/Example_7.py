#converting 1d array in 2d array
import numpy as np
arr = np.arange(10)
print(arr)
'''
Array has 10 elements so, possible reshapes must be multipkes of 10:
No. of elements inside the array=10
Factor of 10
1*10
10*1
2*5
5*2
'''

reshape_arr = arr.reshape(2,5)
print(reshape_arr)