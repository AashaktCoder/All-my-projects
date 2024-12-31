def TriangularNumbers(n):
    Sum = 0
    for i in range(n+1):
        Sum += i
    
    return Sum

# This is the optimized code to find factors of a number using its square root in th range and not the whole number, the factors of its square root are half the total factors of the number and to find the other half factors we divide the original number by the factors of its square roots, giving us all the factors of the number.
def FindNoOfFactors(n):
    num = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            num += 1
            if n // i != i: num += 1

    return num - 1

i = 0
while FindNoOfFactors(TriangularNumbers(i)) < 500:
    i += 1
print(i, TriangularNumbers(i))