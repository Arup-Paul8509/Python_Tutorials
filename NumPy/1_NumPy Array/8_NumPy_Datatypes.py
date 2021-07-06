#Datatypes
'''
    strings- "ABCD"
    integer- 123
    float- 10.256
    boolean- True,False
    complex- 1.0+2.0j
'''
'''
    i-integer
    b-boolean
    u-unsigned integer
    f-float
    c-complex float
    m-timedelta
    M-datetime
    O-object
    S-string
    U-unicode string
    V-fixed chunck of memory for other type(void)
'''
#Checking datatype of an Array
import numpy as np
arr1=np.array([1,2,3])
print(arr1.dtype)
arr2=np.array(['a','b','c'])
print(arr2.dtype)