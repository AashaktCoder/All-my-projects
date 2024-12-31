from random import choice

LegalColor = ["R", "G", "B", "Y", "W", "P"]

RandomCombo = []
for i in range(4): RandomCombo.append(choice(LegalColor))

print("Guess The 4 digit Color Combo\n")

def GuessColor(Lis):
    RightPos = 0
    color = input("Legal colors R, G, B, Y, W, P: ")
    color = color + "     "

    for i in range(len(Lis)):
        if Lis[i] == color[i]:
            RightPos += 1

    return RightPos

def MainGame():
    YouWin = False
    Turns = 0

    while not(YouWin):
        RightPos = GuessColor(RandomCombo)
        if RightPos == 4:
            Turns += 1
            print("\nYou Win")
            print("Number of turns", Turns)  
            YouWin = True    
        else:
            print("Try Again, no of right guess", RightPos, "\n")
            Turns += 1       

MainGame()