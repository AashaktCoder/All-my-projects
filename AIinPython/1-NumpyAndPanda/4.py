import numpy as np

a = np.array([[34, 67, 90, 12], 
              [29, 5, 21, 72], 
              [83, 45, 7, 95]])

# Basic arithemtic operators on array
print(a + 2)
print(a - 4)
print(a * 10)
print(a / 5)

b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(b ** 2)

print(np.sin(b)) # performs sine function over all elements of an array
print(np.cos(b)) # cosine function
print(np.tan(b)) # tan function

c = np.full([3, 3], 5)
d = np.full([3, 3], 8)

print(np.matmul(c, d)) # multiplies two matrices

e = np.identity(5)
# linalg stands for linear algebra and det is determinant
print(np.linalg.det(e)) 

# Functions relatedf to statistics

print(np.min(a), np.max(a)) # maximum and minimum element in a function
print(np.sum(a)) # Finds sum of all elements in the array
print(np.mean(a)) # Find the mean of all elements in array
print(np.median(a))