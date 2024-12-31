# This is a program to find amicable numbers, if the sum of divisors of a number n = the sum of divisors of that sum then the numbers are amicable pairs.

def FindDivisorsSum(n):
    Sum = 0

    for i in range(1, int(n**0.5) + 1):
        
        if n != i and i != 1:

            if n%i == 0: 
                Sum += i

                if n//i != i: Sum += (n // i)

    return Sum + 1

def AmicableNumbers(r):
    Sum = 0

    for i in range(r):
        
        a = FindDivisorsSum(i)

        if FindDivisorsSum(a) == i and i != a:
            Sum += i
    
    return Sum