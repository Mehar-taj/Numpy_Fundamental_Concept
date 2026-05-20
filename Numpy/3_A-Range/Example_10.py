 #Convert 2d array into 1d array
import numpy as np
x=np.array([[0,1],
            [2,3],
            [4,5],
            [6,7],
            [8,9]])
print('Original array',x)
reshape=x.reshape(10)
print(reshape)