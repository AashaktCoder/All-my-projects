# This is a program to find the number of distinct prime factors for a number and finding 4 consecutive numbers with 4 distinct prime factors.

def CheckPrime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0: 
            return False
    return True

def FindPrimeFactors(n):
    factorList = []
    for i in range(2, int(n**0.5)):
        if n%i == 0:
            if CheckPrime(i): factorList.append(i)
            if CheckPrime(n//i): factorList.append(n//i)
    return factorList

run = True
i = 0
while run:
    i += 1
    print(i)
    if len(FindPrimeFactors(i)) == 4 and (len(FindPrimeFactors(i+1)) == 4 and len(FindPrimeFactors(i+2)) == 4):
        if len(FindPrimeFactors(i+3)) == 4:
            print(i, i+1, i+2, i+3)
            run = False