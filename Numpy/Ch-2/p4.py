# 2D Array (Matrix) Creation By using Nested List
import numpy as np 
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(f'The type of {arr} is {type(arr)}')
print(f'The type of element is {arr.dtype}')
print(f'The Dimention of {arr} is {arr.ndim}')
print(f'The Number of Total Element is {arr.size}')
print(f'The Shape of {arr} is {arr.shape}')

'''
Output:
The type of [[10 20 30]
 [40 50 60]
 [70 80 90]] is <class 'numpy.ndarray'>
The type of element is int32
The Dimention of [[10 20 30]
 [40 50 60]
 [70 80 90]] is 2
The Number of Total Element is 9
The Shape of [[10 20 30]
 [40 50 60]
 [70 80 90]] is (3, 3)
'''