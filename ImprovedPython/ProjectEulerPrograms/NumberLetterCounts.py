# Program to convert numbers into their words and then counting the no. of letters in the words, and counting the total letters in the combined words of numbers from 1 to 1000

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tenToTwenty = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def FindLetterNum(n):
    word = ""
    n = str(n)

    if len(n) >= 3:
        if n[-1]+n[-2] != "00": 
            word += ones[int(n[-3])-1] + "hundredand"

        else: word += ones[int(n[-3])-1] + "hundred"

        if n[-2] == "0" and n[-1]+n[-2] != "00":
            word += ones[int(n[-1])-1]

    if len(n) >= 2:
        try:
            if n[-2]+n[-1] == "10":
                word += "ten"

            if 10 < int(n[-2]+n[-1]) < 20:
                word += tenToTwenty[int(n[-1])-1]

            if 1 < int(n[-2]) < 10:
                word += tens[int(n[-2])-2]
                if int(n[-1]) != 0:
                    word += ones[int(n[-1])-1]
                    
        except: pass
    
    if len(n) == 1: word += ones[int(n[-1])-1]

    return word

TotalString = ""

for i in range(1, 1000):
    TotalString += FindLetterNum(i)

TotalString += "onethousand"

print(len(TotalString))