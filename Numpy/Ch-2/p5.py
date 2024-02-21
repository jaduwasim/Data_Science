# if Array contains different type of elements
import numpy as np 
arr = np.array([10,20,30.5])
print(arr)
print(arr.dtype)
'''
If list contains heterogenous elements, and while creating the array upcasting
will be performed.

Output:
=======
[10.  20.  30.5]
float64
'''