'''Sclicing: returns a portion of the array.

   Integer array slicing: returns specific elements or only one element from the array based on their index numbers

'''

import numpy as np
arr =np.array([1,2,3,4,5,6,7,8,9])
            #  0 1 2 3 4 5 6 7 8
#slicing the array
#accessing only 2nd element
print(arr[1])
#accessing 5th element
print(arr[4])
arr2=np.array([[1,2,3,4,5],  #indexing value is 0
               [6,7,8,9,10]])#indexing value is 0
#Access only 2 from the given array
print(arr2[0][1])
#Access only 9 from the given array
print(arr2[1][3])
print(arr2[0:1])# this is slicing the array and it will return the portion of the array 
print(arr2[0,1])# this is integer array indexing and it will return the value of the first row and second column of the array