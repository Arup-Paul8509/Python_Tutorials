'''
    To check the dimension of an array we have an attribute 'ndim'
'''
import numpy as np 
arr1=np.array(42)
print(arr1.ndim)
arr2=np.array([1,2,3])
print(arr2.ndim)
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3.ndim)
arr4=np.array([[[1,2,3],[4,5,6]],[[3,2,1],[7,8,9]]])
print(arr4.ndim)
