import numpy as np

arr_2d = np.array([[1,2,3],
                  [3,4,5]])
# print(arr_2d.shape) #(2,3)
# print(arr_2d.size) #6
# print(arr_2d.dtype) #int64
# print(arr_2d.ndim)

arr = np.array([1.2,2.5,30.5,4.0])
#arr.astype(datatype) # data type could be int,str,float etc

int_arr = arr.astype(int)
print(int_arr)

# mathmatical operation on numpy arrays : --