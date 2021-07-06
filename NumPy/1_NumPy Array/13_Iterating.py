import numpy as np
#iterating 1D Array
arr1=np.array([1,2,3])
for x in arr1:
    print(x)

#iterating 2D Array
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
for x in arr2:
    print(x)
#iterate each scaler elements
for x in arr2:
    for y in x:
        print(y)

#iterating 3d array
arr3=np.array([
                [[1,2,3],
                [4,5,6]],
                [[7,8,9],
                [10,11,12]]
             ])
for x in arr3:
    print(x)
#iterating each scaler elements
for x in arr3:
    for y in x:
        for z in y:
            print(z)

'''
    nditer() function is used to print each scalar elements of an multidimentional array using one for loop
'''
for x in np.nditer(arr3):
    print(x)

#Iterating array with different datatypes
arr4=np.array([1,2,3])
for x in np.nditer(arr4,flags=['buffered'],op_dtypes=['S']):
    print(x)
    #numpy does not change elements in-place, so it needs some other space called buffer so we have to pass flags=['buffered']

#Iterating with different step size
arr5=np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr5[:, ::30]):
    print(x)

#Enumerated iteration using ndenumerate()
'''
    Enumeration means mentioning sequence number of somethings one by one.
    ndenumerate() method can be used for those usercases.
'''
arr6=np.array([1,2,3])
for idx,x in np.ndenumerate(arr6):
    print(idx,x)
arr7=np.array([[1,2,3],[4,5,6]])
for idx,x in np.ndenumerate(arr7):
    print(idx,x)