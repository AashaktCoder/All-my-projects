import numpy as np

a = np.array([[45, -6, 90], [3, 7, 15]])

print(a)
print(a.shape) # shape of the array
print(a.ndim) # dimension of the array

print(a.size) # number of elements in the array
print(a.itemsize) # size of the elements in bytes
print(a.size * a.itemsize) # net data size of the array

b = np.array([[1, 2], [3, 4], [5, 6]], dtype='int16') # specify the datatype of the array

c = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
# This is a 3d array
print(c.shape, c.ndim)