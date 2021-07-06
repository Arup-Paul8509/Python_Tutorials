'''
concatenate() method along with the axis is used to joint two or more arrays in single array
'''
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

#join two 2D arrays along rows(axis=1)
print('join two 2D arrays along rows(axis=1)')
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

#joining arrays using stack() functions
print('joining arrays using stack() functions')
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.stack((arr1,arr2),axis=1)
print(arr)

#stacking along rows
print('stacking along rows')
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.hstack((arr1,arr2))
print(arr)

#stacking along columns
print('stacking along columns')
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.vstack((arr1,arr2))
print(arr)

#stacking along height(depth)
print('stacking along height(depth)')
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.dstack((arr1,arr2))
print(arr)