from tkinter import *
import tkinter.font as font

# Setting up the main Window
WIN = Tk()
WIN.geometry("320x400")
WIN.maxsize(320, 400)
WIN.minsize(320, 400)
WIN.title("Calculator")
IconImage = PhotoImage(file='CalculatorIcon.png')
WIN.iconphoto(False, IconImage)

# Variables
ButtonFont = font.Font(size=30)
Etext = StringVar()
FirstNum = 0
SecondNum = 0
OperationNum = 0

# Functions
def WriteNumber(Number):
    Etext.set(int(str(Etext.get()) + Number))

def ClearText(): Etext.set("")    

def AddNumber():
    global FirstNum
    global OperationNum
    FirstNum = float(Etext.get())
    Etext.set("") 
    OperationNum = 0

def SubNumber():
    global FirstNum
    global OperationNum
    FirstNum = float(Etext.get())
    Etext.set("") 
    OperationNum = 1

def MultiNumber():
    global FirstNum
    global OperationNum
    FirstNum = float(Etext.get())
    Etext.set("") 
    OperationNum = 2

def DivideNumber():
    global FirstNum
    global OperationNum
    FirstNum = float(Etext.get())
    Etext.set("") 
    OperationNum = 3

def DisplayResult():
    SecondNum = Etext.get()
    if OperationNum == 0:
        Etext.set(str(FirstNum + int(SecondNum)))
    if OperationNum == 1:
        Etext.set(str(FirstNum - int(SecondNum)))
    if OperationNum == 2:
        Etext.set(str(FirstNum * int(SecondNum)))
    if OperationNum == 3:
        Etext.set(str(float(FirstNum / float(SecondNum))))                        

# All the widgets
E1 = Entry(WIN, width=14, font="Aerial 50", textvariable=Etext)
E1.place(x=0, y=0)

B1 = Button(WIN, width=3, height=1, font=ButtonFont, text="1", command=lambda: WriteNumber("1"))
B1.place(x=0, y=80)
B2 = Button(WIN, width=3, height=1, font=ButtonFont, text="2", command=lambda: WriteNumber("2"))
B2.place(x=80, y=80)
B3 = Button(WIN, width=3, height=1, font=ButtonFont, text="3", command=lambda: WriteNumber("3"))
B3.place(x=160, y=80)
B4 = Button(WIN, width=3, height=1, font=ButtonFont, text="4", command=lambda: WriteNumber("4"))
B4.place(x=0, y=160)
B5 = Button(WIN, width=3, height=1, font=ButtonFont, text="5", command=lambda: WriteNumber("5"))
B5.place(x=80, y=160)
B6 = Button(WIN, width=3, height=1, font=ButtonFont, text="6", command=lambda: WriteNumber("6"))
B6.place(x=160, y=160)
B7 = Button(WIN, width=3, height=1, font=ButtonFont, text="7", command=lambda: WriteNumber("7"))
B7.place(x=0, y=240)
B8 = Button(WIN, width=3, height=1, font=ButtonFont, text="8", command=lambda: WriteNumber("8"))
B8.place(x=80, y=240)
B9 = Button(WIN, width=3, height=1, font=ButtonFont, text="9", command=lambda: WriteNumber("9"))
B9.place(x=160, y=240)
B0 = Button(WIN, width=3, height=1, font=ButtonFont, text="0", command=lambda: WriteNumber("0"))
B0.place(x=80, y=320)
B11 = Button(WIN, width=3, height=1, font=ButtonFont, text="C", command=ClearText)
B11.place(x=0, y=320)
B12 = Button(WIN, width=3, height=1, font=ButtonFont, text="=", command=DisplayResult)
B12.place(x=160, y=320)
B13 = Button(WIN, width=3, height=1, font=ButtonFont, text="+", command=AddNumber)
B13.place(x=240, y=80)
B14 = Button(WIN, width=3, height=1, font=ButtonFont, text="-", command=SubNumber)
B14.place(x=240, y=160)
B15 = Button(WIN, width=3, height=1, font=ButtonFont, text="x", command=MultiNumber)
B15.place(x=240, y=240)
B16 = Button(WIN, width=3, height=1, font=ButtonFont, text="÷", command=DivideNumber)
B16.place(x=240, y=320)

WIN.mainloop()