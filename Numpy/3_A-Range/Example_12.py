#Convert 2d array into 3d array
import numpy as np
x=np.array([[0,1],
            [2,3],
            [4,5],
            [6,7],
            [8,9]])
print('Original array',x)
print('Dimensions of original array:',x.ndim)
reshape=x.reshape(2,1,5)
print('Reshaped array:',reshape)
print('Dimensions of reshaped array:',reshape.ndim)