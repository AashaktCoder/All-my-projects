def SumSquareDiff(n):

    SumOfSquare = 0
    SquareOfSum = 0

    for i in range(n):
        SumOfSquare += (i+1)**2

        SquareOfSum += (i+1)
    
    return (((SquareOfSum)**2) - SumOfSquare)

print(SumSquareDiff(100))
