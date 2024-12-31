# In this program we need to find the sum of digits of factorial of a number, example: 10! = 3628800 and 3+0+6+8+8+0+0 = 27.

def FindFactorial(n):
    f = 1
    for i in range(1, n): f += (f * i)
    return f

def SumOfDigits(n):
    s = 0
    for num in str(n):
        s += int(num)
    return s

print(SumOfDigits(FindFactorial(100)))