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
# arr = np.eye(4) * 5   # Replace diagonal 1s with 5
# print(arr)

#arange() --> similar to range function in python here 'a' means array and 'range' is python range
#arange()
#arange(start,end,step)


arr = np.arange(1,10,2)
print(arr)

#linear spacing array :- 
#linspace --> returns a evenly specified numbers over a specified interval
#linspace(start,end,no. of element required )
linspace_arr = np.linspace(1,5,2)
print(linspace_arr)
linspace_arr1 = np.linspace(1,5,100)
print(linspace_arr1)


# random generation function : --

random_arr = np.random.rand(5)  # it will give 5 random array element and values between 0 to 1 (normilization)
print(random_arr)

# randn --> it is base don standardization(gives random numbers between -3 to 3)
#np.random.randn(size)
random_arr1 = np.random.randn(2)
print(random_arr1)

# to get random integer array element
# np.random.randint(start,end,size(no. of elemets req.))

random_arr2 = np.random.randint(10,20,5) # it will give 5 elements betwwn 10 and 20 
# low=10:inclusive (smallest possible value is 10).
# high=20: exclusive (largest possible value is 19).
# size=5: gives 5 random integers.
print(random_arr2)
