# This is a program to find if all the circulaar numbers of a numbers are prime or not, example - for 197, the circulars 719, 917 are also primes.

def FindCircularNumbers(n):
    CircularNumbers = []

    n = str(n)

    for i in range(len(n)):
        CircularNumbers.append(int(n[-i:]+n[:-i]))
    
    return CircularNumbers

def CheckPrime(n):
    isPrime = False

    c = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            c += 1
            if n//i != i: c += 1
    if c <= 2: isPrime = True
    return isPrime

isCircularPrime = False

num = 0

for i in range(2, 1000000):
    print(i)
    isCircularPrime = True
    for j in FindCircularNumbers(i):
        if CheckPrime(j) == False: isCircularPrime = False

    if isCircularPrime: num += 1

print(num)
