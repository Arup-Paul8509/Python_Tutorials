import numpy as np 
'''
    [start,end]
    [start,end,step]
'''
#Slicing 1-D Array
arr1=np.array([1,2,3,4,5])
print(arr1[1:3])#[2,3]
print(arr1[-3:-1])#[3,4]
print(arr1[0::2])#[1,3,5]

#Slicing 2-D Array
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[1,1:4])#[7,8,9]
print(arr2[0:2,1])#[2,7]
print(arr2[0:2,1:4])#[[2,3,4],[7,8,9]]
