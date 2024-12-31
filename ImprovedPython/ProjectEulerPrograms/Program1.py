# To find sum of all multiples of 3 or 5 under 1000
'''s = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        s += i
print(s)'''

# Program to find sum of even numbered fibonacci sequence till 4 million
'''
n1 = 1
n2 = 2

s = 0

while n2 < 4000000:
    
    if n2%2 == 0:
        s += n2

    a = n2
    n2 = n1+n2
    n1 = a
print(s)'''

# To find largest prime factor of a number
'''
def FindLargestPrimeFactor(n):
    m = 0
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            for j in range(1, int(i**0.5) + 1):
                if i%j == 0: c += 1
            if i > m and c == 1: m = i
            c = 0
    return m

print(FindLargestPrimeFactor(600851475143))'''