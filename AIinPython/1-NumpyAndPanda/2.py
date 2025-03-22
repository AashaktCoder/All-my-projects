import numpy as np

a = np.array([[23, 15, 46, 61, 5], [79, 34, 12, 92, 85]])

print(a[1, 2]) # to access an element in the array [row, column]

print(a[0, :]) # To access an entire row
print(a[:, 3]) # To access an entire column

print(a[0, 2:5]) # to slice the row
print(a[1, 1:5:2]) # to slice the row with stepsize as 2
# negative values can also be entered as stepsize of start and end index

a[1, 2] = 56
print(a) # there was 12 at row 1 and column 2 and it got replaced by 56

a[:, 4] = [49, 22] # the 4th index column had 5 and 85 that are replaced by
print(a) # 49 and 22 so a column can be changed

a[0, 2:5] = [62, 17, 39] # a slice of the row is changed from [46, 61, 5]
print(a) # to the new [62, 17, 39]

# Advanced Indexing

print(a[0, [1, 4]]) # access many elements from row 0 using a list index

print(a[[0, 1, 0, 1, 0], [0, 1, 2, 3, 4]])