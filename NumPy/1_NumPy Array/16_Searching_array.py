'''
 To searching an array we will use the where() method
'''
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
#searching for 4
x=np.where(arr==4)
print(x)
#searching for odd values
x=np.where(arr%2!=0)
print(x)

#Search Sorted
'''
    searchsorted() returns the index position of a value 
    should be placed in sorted array
'''
x=np.searchsorted(arr,4)
print(x)

#search sorted from right side
x=np.searchsorted(arr,2,side='right')
print(x)

#multiple values
x=np.searchsorted(arr,[2,3,4])
print(x)