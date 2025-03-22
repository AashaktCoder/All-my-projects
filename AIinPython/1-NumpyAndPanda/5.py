import numpy as np

# Reorganization of arrays

a = np.array([[34, 67, 90, 12], 
              [29, 5, 21, 72], 
              [83, 45, 7, 95]])

print(a.reshape((12, 1))) # Changes the shape of array but keeping the no.
print(a.reshape((6, 2))) # of elements the same in the array
print(a.reshape((3, 2, 2)))

b = np.array([1, 2, 3, 4, 5])
c = np.array([6, 7, 8, 9, 10])

# Vertical Stack
print(np.vstack([b, b, c, c, c, c])) # Stacks arrays onto each other 

# Horizontal Stack
print(np.hstack([b, c])) # Stacks array side by side