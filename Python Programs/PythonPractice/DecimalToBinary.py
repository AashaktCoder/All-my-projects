from math import floor

num = int(input("Enter a number: "))
binaryString = ""

def ConvertNum(Num, str):
    while Num != 0:
        if Num%2 == 0:
            str = str + "0"
        elif Num%2 == 1:
            str = str + "1"
        Num = Num / 2   
        Num = floor(Num) 
    print("The number in binary is ", str[::-1])

ConvertNum(num, binaryString)