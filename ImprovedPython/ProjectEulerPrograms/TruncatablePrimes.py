def CheckPrime(n):
    n = int(n)
    isPrime = False
    c = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            c += 1
            if n//i != i: c += 1
    if c <= 2 and n != 1: isPrime = True
    return isPrime

def FindTruncatable(n):
    n = str(n)
    isTruncatable = True
    for i in range(len(n)):
        if not CheckPrime(n[i:]): isTruncatable = False
        if not CheckPrime(n[:i+1]): isTruncatable = False

    return isTruncatable

TruncatableNumbers = []
i = 11
while len(TruncatableNumbers) < 11:
    i += 1
    if FindTruncatable(i): TruncatableNumbers.append(i)
    print(i)

print(TruncatableNumbers)
