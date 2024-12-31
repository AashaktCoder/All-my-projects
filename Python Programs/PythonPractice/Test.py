# Function to square all the numbers in a list
'''
def SquareList(List):
    SquaredList = []
    for items in List:
        SquaredList.append(items*items)
    return SquaredList

NormalList = [1, 2, 3, 4, 5]
MainList = SquareList(NormalList)

print(MainList)
'''

# Program to find a duplicate number in a List
'''
MainList = [2, 4, 5, 8, 7, 1, 2, 9, 0]

for i in range(len(MainList)):
    for j in range(i+1, len(MainList)):
        if MainList[i] == MainList[j]:
            print(MainList[i], " is a duplicate number")
            break
'''

# Program to reverse a List
'''
MainList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
ResultList = []

for i in range(len(MainList)):
    ResultList.append(MainList[(len(MainList) - 1) - i])

print(ResultList)
'''

# Program to find the greatest number in a List
'''
MainList = [10, 67, 34, 20, 12, 84, 90]
MaxNumber = 0

for num in MainList:
    if num > MaxNumber:
        MaxNumber = num

print(MaxNumber, " is the largest number")
'''

# Program to sort a list into descending order
'''
MainList = [23, 45, 12, 3, 90, 78, 56]
MaxNumber = 0

ResultList = []

while len(MainList) > 0:
    MaxNumber = 0
    for num in MainList:
        if num > MaxNumber:
            MaxNumber = num
    MainList.remove(MaxNumber)
    ResultList.append(MaxNumber)        

print(ResultList)
# Omg I did it all myself!!!
'''

# Program to sort a list into ascending order
'''
MainList = [23, 45, 12, 3, 90, 78, 56]
MaxNumber = 0

ResultList = []
ascendResultList = []

while len(MainList) > 0:
    MaxNumber = 0
    for num in MainList:
        if num > MaxNumber:
            MaxNumber = num
    MainList.remove(MaxNumber)
    ResultList.append(MaxNumber)

for i in range(len(ResultList)):
    ascendResultList.append(ResultList[(len(ResultList) - 1) - i])

print(ascendResultList)
'''

# Program to check wether an element is in a list or not
'''
num = int(input("Enter a number: "))

MainList = [34, 56, 90, 68, 27, 42, 88]

for i in range(len(MainList)):
    if MainList[i] == num:
        print("The number typed is in the list")
        break
'''