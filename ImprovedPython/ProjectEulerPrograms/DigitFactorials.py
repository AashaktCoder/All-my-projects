# Program to find sum of all numbers which can be written as the sum of the factorials of their digits
from math import factorial

s = 0
for i in range(3, 20000):
    for j in str(i):
        s += factorial(int(j))
    if i == s: print(i)
    s = 0