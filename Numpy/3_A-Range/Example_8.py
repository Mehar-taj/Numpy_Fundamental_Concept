# reshaping the dimension of array for prime numbers
import numpy as np
arr = np.arange(11)
print(arr)
'''
No. of elements inside the array=11
Factor of 11
11*1
1*11
'''
reshape_arr = arr.reshape(11,1)# it will reshape the array into 11 rows and 1 column
print(reshape_arr)