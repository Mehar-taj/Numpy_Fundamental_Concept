#Create 3D array using the random library
import numpy as np
from numpy import random
x=random.randint(10,size=(2,3,5))#Inner 2inner arrays, row, Column
arr=np.array(x)
print(arr)
print(arr.ndim)#for finding the dimension of the array