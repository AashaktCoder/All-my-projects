# Program to find sum of all numbers which can be written as the sum of the fifth powers of their digits

ts = 0
s = 0
for i in range(2, 1000000):
    for j in str(i):
        s += int(j)**5

    if s == i: 
        ts += i
    s = 0

print(ts)