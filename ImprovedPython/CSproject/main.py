from pickle import load, dump

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
        print("Enter 0 to Exit Game")

        c = input("")

        if c == "1": pause = False
        
        if c == "2":
            ln = int(input("\nEnter level number to load: "))
            
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