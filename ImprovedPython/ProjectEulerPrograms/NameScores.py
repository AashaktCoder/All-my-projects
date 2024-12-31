# Program to find sum of index of all alphabets in all the names and then multiplying it by the index of the name in the list.

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

NameList = []

f = open("ProjectEulerPrograms\\NameFile.txt", "r")

NameStr = f.read()
NameList = eval(NameStr)
NameList = sorted(NameList)

f.close()

SumOfNameScores = 0
s = 0

for name in NameList:
    for c in name:
        s += alphabets.index(c) + 1

    SumOfNameScores += (s * (NameList.index(name) + 1))
    s = 0

print(SumOfNameScores)