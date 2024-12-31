from tkinter import *
from random import Random, choice

score = 0
ComputerScore = 0

WIN = Tk()

WIN.geometry("500x500")
WIN.maxsize(500,500)
WIN.minsize(500,500)
WIN.title("Rock, Paper, Scissor, By Aashakt")

def Choose():
    OptionList = ["Rock", "Paper", "Scissor"]
    RandomChoice = choice(OptionList)
    return RandomChoice

def CheckWin(): 
    global score  
    global ComputerScore

    if score >= 5:
        L5.configure(text="User Won The Game !!")

    if ComputerScore >= 5:
        L5.configure(text="Computer Won The Game !!")    

def B1func():
    global score
    global ComputerScore
    Choice = Choose()

    if (Choice == "Rock"):
        L1.configure(text="Computer chose Rock")
        L2.configure(text="Draw")  
    if (Choice == "Paper"):
        L1.configure(text="Computer chose Paper")
        L2.configure(text="Computer Won")
        ComputerScore += 1
        L4.configure(text=f"Computer Score: {ComputerScore}")

    if (Choice == "Scissor"):
        L1.configure(text="Computer chose Scissor")
        L2.configure(text="User Won") 
        score += 1
        L3.configure(text=f"Score: {score}")
    CheckWin()    

def B2func():
    global score
    global ComputerScore
    Choice = Choose()

    if (Choice == "Rock"):
        L1.configure(text="Computer chose Rock")
        L2.configure(text="User Won")  
        score += 1
        L3.configure(text=f"Score: {score}")
    if (Choice == "Paper"):
        L1.configure(text="Computer chose Paper")
        L2.configure(text="Draw")   
    if (Choice == "Scissor"):
        L1.configure(text="Computer chose Scissor")
        L2.configure(text="Computer Won")
        ComputerScore += 1
        L4.configure(text=f"Computer Score: {ComputerScore}") 
    CheckWin()    

def B3func():
    global score
    global ComputerScore
    Choice = Choose()

    if (Choice == "Rock"):
        L1.configure(text="Computer chose Rock")
        L2.configure(text="Computer Won")  
        ComputerScore += 1
        L4.configure(text=f"Computer Score: {ComputerScore}")
    if (Choice == "Paper"):
        L1.configure(text="Computer chose Paper")
        L2.configure(text="User Won")  
        score += 1
        L3.configure(text=f"Score: {score}")
    if (Choice == "Scissor"):
        L1.configure(text="Computer chose Scissor")
        L2.configure(text="Draw") 
    CheckWin()              

B1 = Button(WIN, font=("Aerial", 30), text="Rock", bg='#5ca3ff', command=B1func)
B1.place(x=10, y=100)
B2 = Button(WIN, font=("Aerial", 30), text="Paper", bg='#19ff75', command=B2func)
B2.place(x=160, y=100)
B3 = Button(WIN, font=("Aerial", 30), text="Scissor", bg='#ffc338', command=B3func)
B3.place(x=320, y=100)

L1 = Label(WIN, text="Rock Paper Scissor", font=("Aerial", 30))
L1.place(x=0, y=250)
L2 = Label(WIN, text="Win or Loose", font=("Aerial", 30))
L2.place(x=0, y=320)
L3 = Label(WIN, text=f"Score: {score}", font=("Aerial", 25))
L3.place(x=0, y=0)
L4 = Label(WIN, text=f"Computer Score: {ComputerScore}", font=("Aerial", 25))
L4.place(x=180, y=0)
L5 = Label(WIN, text="", font=("Aerial", 26))
L5.place(x=0, y=420)

WIN.mainloop()