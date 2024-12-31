NumList = [0, 1, 3, 4, 5, 9, 11]
NumToFind = 9
tries = 0

def FindNum(List, Num, tries):
    for nums in List:
        if nums == Num:
            print("The no. of tries to find the number were ", tries)
            return 1
        else:
            tries += 1      

FindNum(NumList, NumToFind, tries)