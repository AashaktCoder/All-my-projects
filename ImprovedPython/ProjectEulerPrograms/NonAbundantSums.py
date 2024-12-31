# Program to find sum of all non abundant numbers (numbers with sum of their divisors being greater than the number) below 28123

def FindSumOfDivisors(n):
    s = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0: 
            s += i
            if n//i != i: s += (n//i)
    return s - n

AbundantNumLis = set()

for i in range(1, 28124):

    if i < FindSumOfDivisors(i):
        AbundantNumLis.add(i)

NonAbundantSumList = []
AbundantSum = False
for i in range(1, 28124):
    AbundantSum = False
    for num in AbundantNumLis:
        if (i - num) in AbundantNumLis:
            AbundantSum = True
            break

    if not AbundantSum:
        NonAbundantSumList.append(i)

s = 0
for i in NonAbundantSumList:
    s += i
print(s)