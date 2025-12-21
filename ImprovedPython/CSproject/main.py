from pickle import load, dump
import os

os.chdir(os.path.dirname("C:\MyFolder\PythonProgramming\All-my-projects\ImprovedPython\CSproject"))

level = []
with open("currentlevel.dat", "rb") as f:
    level = load(f)
    
wd = 2

c = ' '

px = 4
py = 4

wl = ["-", "|"]

bml = ['.', '1']

win = False
pause = True

def Draw(level):
    print("")
    for i in level: print((' ' * wd).join(i))

def Move(c, level):
    global px, py

    for i in range(len(level)):
        if "0" in level[i]: 
            px = i
            py = level[i].index("0")

    if c == "w" and (level[px - 1][py] not in wl):

        if level[px - 1][py] == "#" and level[px-2][py] in bml: 
            level[px - 2][py] = "#"
            level[px - 1][py] = "."

        if level[px - 1][py] == ".":
            level[px][py] = '.'
            px -= 1
            level[px][py] = '0'

    if c == "s" and (level[px + 1][py] not in wl):

        if level[px + 1][py] == "#" and level[px + 2][py] in bml: 
            level[px + 2][py] = "#"
            level[px + 1][py] = "."

        if level[px + 1][py] == ".":
            level[px][py] = '.'
            px += 1
            level[px][py] = '0'

    if c == "d" and (level[px][py + 1] not in wl):

        if level[px][py + 1] == "#" and level[px][py + 2] in bml: 
            level[px][py + 2] = "#"
            level[px][py + 1] = "."

        if level[px][py + 1] == ".":
            level[px][py] = '.'
            py += 1
            level[px][py] = '0'
            
    if c == "a" and (level[px][py - 1] not in wl):

        if level[px][py - 1] == "#" and level[px][py - 2] in bml: 
            level[px][py - 2] = "#"
            level[px][py - 1] = "."

        if level[px][py - 1] == ".":
            level[px][py] = '.'
            py -= 1
            level[px][py] = '0'


while c != '0':

    if pause: 
        print("\nBLOCK GAME")
        print("Enter 1 to Resume Game")
        print("Enter 2 to load level")
        print("Enter 3 to read instructions")
        print("Enter 0 to Exit Game")

        c = input("")

        if c == "1": pause = False
        
        if c == "2":
            ln = int(input("\nEnter level number to load (0 to 4) : "))
            
            with open("levels.dat", "rb") as f:

                while True:
                    try:
                        obj = load(f)
                        try:
                            if obj[0] == ln:
                                level = obj[1]
                        except: pass

                    except EOFError: break

            pause = False

        if c == "3":
            print("\nINSTRUCTIONS")
            print("1. The player (0) is controlled by w (up), a (left), s (down), d (right), keys")
            print("2. The player cannot pass through -, | and 1 symbols")
            print("3. The # symbol represent boxes which can be pushed by player")
            print("4. The goal of the game is to cover all the 1's with the boxes (#)")
            print("5. The game can be paused by entering x and progress will be saved")
            print("6. The game has 5 built in levels with increasing difficulty")
            print("7. The levels can be loaded from load level screen by entering respective numbers")
            c = input("\nPress enter to return to main menu: ")
            pause = True

    if not pause:

        Draw(level)

        try: c = input("\nEnter key: ")
        except: c = " "

        Move(c, level)

        if c == "x":

            with open("currentlevel.dat", "wb") as f:
                dump(level, f)

            pause = True

        for i in level:
            if '1' in i: win = False
            
        if win: 
            print("\nYOU WIN!!\n")
            pause = True

        win = True
