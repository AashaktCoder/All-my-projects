# Program to find the sum of all self powers till 1000

s = 0
for i in range(1, 1001):
    s += i**i
print(s)