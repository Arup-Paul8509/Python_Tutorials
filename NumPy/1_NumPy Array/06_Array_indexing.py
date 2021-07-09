import numpy as np 

#1-D Array
arr1=np.array([1,2,3])
print(arr1[0])#1
print(arr1[2])#3
print(arr1[-1])#3

#2-D Array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2[0,0])#1
print(arr2[1,1])#5

#3-D Array
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]])
print(arr3[0,0,0])#1
print(arr3[1,1,0])#0