list = [90, 765, 3, 325, 45, 12, 78, 123, 90, 32]

# Program to swap first and last element in a list
'''
first = list[0]
list[0] = list[len(list) - 1]
list[len(list) - 1] = first
'''

# Program to swap two elements in a list
'''
def Swap(list, a, b):
    first = list[a]
    list[a] = list[b]
    list[b] = first
    return list
'''

# Program to check if element in list
'''
def IsElementThere(list, a):
    for i in list:
        if i == a:
            return "Element is in the list"
    return "Element is not in the list"
'''

# Program to count number of duplicates in a list
'''
list = [3, 4, 7, 12, 45, 3, 67, 4, 23, 7, 12, 3]
def CountDuplicate(list, a):
    count = 0
    for i in list:
        if i == a:
            count += 1
    return f"{a} repeats {count-1} times in the list"    
'''

# Program to count sum and average of all elements in a list
'''
def FindSumAverage(list):
    sum = 0
    for i in list:
        sum += i
    return sum, sum/len(list)   
'''    

# Program to count positive and negative numbers in a list
'''
list = [-1, -2, -3, -4, -5, -6, 1, 2, 3, 4]
def CountInteger(list):
    pCount = 0
    nCount = 0
    for i in list:
        if i > 0:
            pCount += 1
        elif i < 0:
            nCount += 1
    return pCount, nCount
'''    