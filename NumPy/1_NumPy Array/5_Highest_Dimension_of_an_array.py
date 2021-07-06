'''
    An array can have any number of dimensions.

    When the array is created, we can define the number of dimensions by using 'ndmin' argument.
'''
import numpy as np
arr=np.array([1,2,3],ndmin=3)
print(arr)