# Program to find a pythagorean triplet with a + b + c = 1000.

a, b, c = 0, 0, 0

'''
for i in range(1, 1000):
    a = i
    for j in range(1, 1000):
        b = j
        for k in range(1, 1000):
            c = k
            if (a*a + b*b) == c*c and (a + b + c) == 1000:
                print(a, b, c)
'''

# The result of the code above is a=200, b=375, c=425