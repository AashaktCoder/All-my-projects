Bnum = input("Enter a binary number: ")
MainNum = 0

def ConvertNum(Num, Res):
    j = 0
    for i in Num[::-1]:
        Res += int(i) * (2 ** j)
        j += 1
    print(Res)

ConvertNum(Bnum, MainNum)