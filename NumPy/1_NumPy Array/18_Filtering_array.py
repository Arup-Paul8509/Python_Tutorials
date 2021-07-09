'''
    In NumPy, you  filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.
'''
import numpy as np
arr=np.array([41,42,43,44])
x=[True,False,True,False]
newarr=arr[x]
print(newarr)

#Creating the Filter Array
filter_arr=[]
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)

#Creating filter directly from array
filter_arr=arr > 42
newarr=arr[filter_arr]
print(newarr)