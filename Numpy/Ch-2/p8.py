# np.arange(start,stop,step)

import numpy as np 
arr_one = np.arange(10) #Consider 0-9
arr_two = np.arange(1,11) #consider 0-10
arr_three = np.arange(1,21,2) #Consider 1 to 20 and skip second number Like 1,3,5,7,9,11,13,15,17,19

print(f'{arr_one} Size: {arr_one.size} Shape:{arr_one.shape} Dtype:{arr_one.dtype} Dimention: {arr_one.ndim}')
print(f'{arr_two} Size: {arr_two.size} Shape:{arr_two.shape} Dtype:{arr_two.dtype} Dimention: {arr_two.ndim}')
print(f'{arr_three} Size: {arr_three.size} Shape:{arr_three.shape} Dtype:{arr_three.dtype} Dimention: {arr_one.ndim}')

'''
Output:
[0 1 2 3 4 5 6 7 8 9] Size: 10 Shape:(10,) Dtype:int32 Dimention: 1
[ 1  2  3  4  5  6  7  8  9 10] Size: 10 Shape:(10,) Dtype:int32 Dimention: 1
[ 1  3  5  7  9 11 13 15 17 19] Size: 10 Shape:(10,) Dtype:int32 Dimention: 1
'''