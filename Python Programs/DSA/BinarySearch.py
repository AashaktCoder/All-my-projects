NumList = [0, 1, 3, 4, 5, 9, 11]
NumToFind = 9
tries = 0

def FindNum(List, Num, tries):
    if Num > List[(len(List) - 1) // 2]:
        for i in range(0, List[((len(List) - 1) // 2)]):
            if List[i] == Num:
                return 1
            else:
                tries += 1  
    elif Num < List[(len(List) - 1) // 2]:
        for i in range(List[((len(List) - 1) // 2)], len(List)):
            if List[i] == Num:
                return 1
            else:
                tries += 1  
    else:
        return 1 

    print("The number of tries were: ", tries)    

FindNum(NumList, NumToFind, tries)