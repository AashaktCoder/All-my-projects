def SumOfPrimes(n):
    
    primeCount = 0

    Sum = 0

    for i in range(n):

        for j in range(i):

            if j > 1 and i > 1:

                if i%j == 0: primeCount += 1

        if primeCount < 1 and i > 1:

            Sum += i

        primeCount = 0

    return Sum

print(SumOfPrimes(10))
