import numpy as np
# list contains heterogenous elements
l = [10,20,30.5, 'washim']
a = np.array(l) # upcasting to float
print(f'a :: {a}')
print(f'data type of elements of a ==> {a.dtype}')
