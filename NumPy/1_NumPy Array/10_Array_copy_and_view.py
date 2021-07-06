import numpy as np
#copy()
arr=np.array([1,2,3])
x=arr.copy()
arr[0]=5
print(arr)
print(x)

#view()
arr2=np.array([4,5,6])
y=arr2.view()
arr2[0]=10
print(arr2)
print(y)

#Check if array owns it's data
print(x.base)