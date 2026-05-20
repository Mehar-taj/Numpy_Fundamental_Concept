# creating a 2D array using random variables.
import numpy as np
from numpy import random
x = random.randint(10,size=(3,5))# rows=3, columns=5
arr = np.array(x)
print(arr)