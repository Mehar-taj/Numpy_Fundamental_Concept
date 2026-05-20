#coverting 3d array into 1d array
import numpy as np
x=np.array([[[0,1],
 [2,3],
 [4,5],
 [6,7],
 [8,9]]])
print('Original array',x)
print('Dimensions of original array:',x.ndim)
reshape=x.reshape(10)
print(reshape)
print('Dimensions of reshaped array:',reshape.ndim)