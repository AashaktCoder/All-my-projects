# Program to find palindrome made by product of two three digit numbers

maxNum = 0
for i in range(1000):
    for j in range(1000):
        if int(str(i*j)) == int(str(i*j)[::-1]):
            if i*j > maxNum: maxNum = i*j

print(maxNum)