'''Boolean array Indexing: Returns specific elements from the array based on the condition given in the form of boolean values (True or False)
'''
import numpy as np
arr=np.array([[32,5,23,1,43,12,34,34,345,23,23],
              [61,72,83,41,50,95,796,57,80,10,14]])
#Access only the values which are greater than 50
cond = arr>50
print("Extacted values which are greater than 50: ",arr[cond])
# Extacted values which are greater than 50 in 1st row
row_1 = arr[0]
cond = row_1>50
print("Extacted values which are greater than 50 in 1st row: ",row_1[cond])
print("Extacted values which are greater than 50 in 1st row: ",arr[0,cond])
cond = (arr%2!=0)
print("Extracted values which are odd numbers: ",arr[cond])