'''
    We use array_split() for spliting arrays,
    we pass it the array we want to split and the number of splits.
'''
import numpy as np
arr1=np.array([1,2,3,4,5,6])
print(arr1)
newarr1=np.array_split(arr1,3)
print(newarr1)
#Access the splitted array
print(newarr1[1])

#Splitting 2D Array
arr2=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr2=np.array_split(arr2,3)
print(newarr2)

#splitting 2D arrays along rows
newarr2=np.array_split(arr2,3,axis=1)#np.hsplit(arr2,3)
print(newarr2)