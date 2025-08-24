# with default values 
#np.zeros(shape)

import numpy as np
zeros_array = np.zeros(3)  # this will create an arrays of zero
print(zeros_array)


# array with ones 

ones_array = np.ones((2,3))
print(ones_array)

# Full Array (custom constant)
#full(shape,custom value) # custom value  is the value by which you want to fill your array

custom_array = np.full((3,3),7) # array will be 3*3 and filled with 7 (shape and value could be anything)

print(custom_array)

# Empty Array (uninitialized, may contain random values in memory)

empty_array = np.empty((2,2))
print(empty_array)

# Identity Matrix (default diagonal = 1)

identity_matrix = np.eye(4) # 4*4 matrix
print(identity_matrix)

custom_identity_matrix = np.eye(2,3)
print(custom_identity_matrix) #2rows, 3columns


# how to change the identity value
arr = np.eye(4) * 5   # Replace diagonal 1s with 5
print(arr)