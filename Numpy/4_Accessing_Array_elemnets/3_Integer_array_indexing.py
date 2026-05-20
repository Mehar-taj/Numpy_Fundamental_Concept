'''Integer array indexing: returns specific elements or only one element from the array based on their index numbers

Integer array slicing: returns specific elements or only one element from the array based on their index numbers

'''

#Integer array indexing
import numpy as np
arr1=np.array([1,2,3,4,5])
              #0,1,2,3,4
#Access only 2 from the given array
print(arr1[1])
#Access only 5 from the given array
print(arr1[4])
print(arr1[[0,2,4]])# this is integer array indexing
arr2=np.array([[1,2,3,4,5],  #indexing value is 0
               [6,7,8,9,10]])#indexing value is 0
#Access only 2 from the given array
print(arr2[0,1])# indexing
#Access only 9 from the given array
print(arr2[1,3])# indexing

# this is slicing because it will return the portion of the array
arr3 = np.array([[1,2,3],
                 [4,5,6]])

print(arr3[:,1:])