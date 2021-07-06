import numpy as np
arr1=np.array([1,2,3,4,5,6,7,8])

#1-D to 2-D
new1=arr1.reshape(2,4)
#print(new1)

#1-D to 3-D
new2=arr1.reshape(1,2,4)#outermost array contains 2 arrays which  contains 4 arrays each
print(new2)

#multidimensional to 1-D
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
new=arr2.reshape(-1)
print(new)