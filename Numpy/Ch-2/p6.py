# we have to use dtype argument while creating the arrray
import numpy as np 
list_one = [10,20,30]
arr_int = np.array(list_one,dtype='int')
arr_bool = np.array(list_one, dtype='bool')
arr_comp = np.array(list_one, dtype='complex')
arr_float = np.array(list_one, dtype='float')
arr_str = np.array(list_one, dtype='str')
print(arr_int)
print(arr_bool)
print(arr_comp)
print(arr_float)
print(arr_str)
'''
Output:
[10 20 30]
[ True  True  True]
[10.+0.j 20.+0.j 30.+0.j]
[10. 20. 30.]
['10' '20' '30']
'''