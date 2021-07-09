'''
A dimension in array is one level of array depth(nested array[an array that have arrays as their elements]).
'''
#0-D Array
'''
    0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
'''
import numpy as np 
arr=np.array(42)
print("0-D Array")
print(arr)

#1-D Array
'''
    An array that has 0-D arrays as its elemtents. It is the most common and basic arrays.
'''
arr=np.array([1,2,3])
print("1-D Array")
print(arr)

#2-D Array
'''
    An array that has 1-D arrays as its elements. This is often used to represent matrix.
    NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
'''
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2-D Array")
print(arr)

#3-D Array
'''
    An array that has 2-D arrays as its elements. This is often used to represent a 3rd order tensor.
'''
arr=np.array([[[1,2,3],[4,5,6]],[[3,2,1],[7,8,9]]])
print("3-D Array")
print(arr)
