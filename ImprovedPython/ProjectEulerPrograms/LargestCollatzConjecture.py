# Program to find a number under one million which has the longest collatz conjecture chain

def CollatzConjecture(n):

    terms = 0

    if n > 1:
        while n != 1:

            if n%2 == 0:
                n = n//2
                terms += 1

            else: 
                n = (3*n) + 1
                terms += 1

    return terms

maxNum = 0
maxTerms = 0

'''
for i in range(1000000):
        
    print(CollatzConjecture(i))

    if maxTerms < CollatzConjecture(i):
        maxTerms = CollatzConjecture(i)
        maxNum = i
        

print(CollatzConjecture(837799))
'''

# The Answer to the question is 837799
