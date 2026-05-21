'''
RANDOM VARIABLES
A random variable in Python means generating values randomly using functions from NumPy’s random module.
'''
import numpy as np
from numpy import random
x = random.randint(10)# generating a random integer between 0 and 10. defaultly generate a single random integer
arr = np.array(x)
print(x)
