import numpy as np

# todo numpy arrays also very similar to vector and have
# todo many buitin,useful functions

# creat an numpy array
arr0 = np.array([0, 1, 2, 3])

# creating an numpy matrix of zeros and ones
#! note the double brackets

arr1 = np.zeros((4, 3))
print(arr1)
arr2 = np.ones((4, 3))
print(arr2)

# creating a linspace for use
arr3 = np.linspace(1, 10, 10)
print(arr3)
# using shape
#! note the lack of paranthesis

# attribute of numpy arr
n = arr2.shape
print(n)

# * operations:

# summing the elements of an arr
sum = np.sum(arr3)
#
