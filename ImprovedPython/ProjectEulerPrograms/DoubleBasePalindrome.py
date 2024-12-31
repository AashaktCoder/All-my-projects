# This is a program to check if a number is a palindrome (is the same from left ot right and right to left) in both base 10 and in binary (base 2).

def ChangeToBinary(n):
    num = n
    binaryNum = ""
    while num != 0:
        if num%2 == 0: 
            binaryNum += '0'
            num = num//2
        else:
            binaryNum += '1'
            num = num//2
    return binaryNum[::-1]

def CheckDoubleBasePalindrome(n):
    num = str(n)
    binaryNum = ChangeToBinary(n)
    if num == num[::-1] and binaryNum == binaryNum[::-1]:
        return True
    else: return False

s = 0
#for i in range(1, 1000000):
    #if CheckDoubleBasePalindrome(i): s += i

print(s)