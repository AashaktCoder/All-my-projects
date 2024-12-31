# Program to find a sum made from consecutive prime numbers which is itself a prime number

def CheckPrime(n):
    c = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            c += 1
            if n//i != i: c += 1
    if c == 2: return True
    else: return False

def FindConsecutivePrimeSum(n):
    s = 0
    primes = []
    for i in range(2, n):
        if CheckPrime(i):
            if (s + i) < n:
                primes.append(i)
                s += i
            else: break
    while CheckPrime(s) == False:
        s -= primes.pop(0)

    return [s, primes]

print(FindConsecutivePrimeSum(1000000)[0])