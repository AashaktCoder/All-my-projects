import numpy as np

# Initializing different types of arrays

print(np.zeros([2, 3])) # Creates an array of a give shape with only 0
print(np.ones([3, 4, 2])) # Creates an array of a shape with only 1

print(np.full([4, 4], 50)) # Fills an array of given shape with some number

a = np.array([[45, 67, 12], [89, 34, 56]])
print(np.full_like(a, 8)) # fills an array with some number

print(np.random.rand(3, 4)) # Fills array of a shape with random decimal
print(np.random.random_sample(a.shape))
print(np.random.randint(0, 10, size=(3, 3))) # fills array of a given size with random integers picked from a start to end point

print(np.identity(5)) # similar to identity matrix in mathematics

# Question to make the following array using the given methods
b = np.ones([5, 5], dtype='int16')
b[1:4, 1:4] = np.zeros([3, 3])
b[2, 2] = 9
print(b)