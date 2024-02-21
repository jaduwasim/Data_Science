# np.eye(N, M=None, k=0), for Generate Identity Matrix 
'''
Parameters
    ----------
    N : int
      Number of rows in the output.
    M : int, optional
      Number of columns in the output. If None, defaults to `N`.
    k : int, optional
      Index of the diagonal: 0 (the default) refers to the main diagonal,
'''
import numpy as np
# arr = np.eye(5)
# arr = np.eye(5,5)
arr = np.eye(5,5,-1) #First args for Row, Second for Column and third for diagonal
print(arr)