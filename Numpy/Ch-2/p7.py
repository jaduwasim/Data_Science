# Creating object type array:
# Object is the parent of all int,float,bool,complex and str.
# Here the elements are looks like Hetrogeneous. But the datatype of element id 'object'

import numpy as np 
arr = np.array([10,'Krishna',10.5,True, 10+20j], dtype='object')
print(f'Array: {arr}')
print(f'Data type of elements of array a ==> {arr.dtype}')