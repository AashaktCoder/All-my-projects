from tkinter import *

WIN = Tk()
WIN.geometry("300x300")
WIN.minsize(300, 300)
WIN.maxsize(300, 300)
WIN.title("Sign Up")

Email = StringVar()
Password = StringVar()

def MakeAccount():
    with open("C:\MyFolder\PythonProgramming\OTPverification\EmailDetails.txt", "a") as f:
        if len(Password.get()) >= 8:
            f.write("\n" + Email.get() + "\n")
            f.write(Password.get())
            L4.config(text="Account Made Successfully")
        else:
            L4.config(text="Password should have 8 letters")    

L1 = Label(WIN, text="Sign Up", font="Aerial 40 bold").place(x=45, y=0)

L2 = Label(WIN, text="Email:", font="Aerial 15").place(x=0, y=90)
E2 = Entry(WIN, textvariable=Email)
E2.place(x=100, y=95)

L3 = Label(WIN, text="Password:", font="Aerial 15").place(x=0, y=130)
E3 = Entry(WIN, textvariable=Password)
E3.place(x=100, y=135)

B1 = Button(WIN, text="Make Account", font="Aerial 15", command=MakeAccount)
B1.place(x=80, y=185)

L4 = Label(WIN, text="", font="Aerial 15")
L4.place(x=25, y=250)

WIN.mainloop()