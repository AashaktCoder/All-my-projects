from tkinter import *
from tkinter import messagebox as msg
from random import randint

WIN = Tk()
WIN.geometry("300x370")
WIN.minsize(300, 370)
WIN.maxsize(300, 370)
WIN.title("Log In")

Email = StringVar()
Password = StringVar()
otp = IntVar()

def Submit():
    global Otp
    with open("C:\MyFolder\PythonProgramming\OTPverification\EmailDetails.txt", "r") as f:
        EmailList = f.readlines()
        for i in range(len(EmailList)):
            if EmailList[i].removesuffix("\n") == Email.get(): 
                if EmailList[i+1].removesuffix("\n") == Password.get():
                    L5.config(text="Correct Email")
                    Otp = randint(0, 10000)
                    msg.showinfo("OTP", f"{Otp} is your OTP")
            else:
                L5.config(text="Incorrect Email")  

def SubmitOTP():
    if otp.get() == Otp:
        L6.config(text="You Have Succsessfully Logged In")

L1 = Label(WIN, text="Login", font="Aerial 40 bold").place(x=70, y=0)

L2 = Label(WIN, text="Email:", font="Aerial 15").place(x=0, y=90)
E2 = Entry(WIN, textvariable=Email)
E2.place(x=100, y=95)

L3 = Label(WIN, text="Password:", font="Aerial 15").place(x=0, y=130)
E3 = Entry(WIN, textvariable=Password)
E3.place(x=100, y=135)

L4 = Label(WIN, text="Enter OTP:", font="Aerial 14").place(x=0, y=260)
E4 = Entry(WIN, textvariable=otp)
E4.place(x=100, y=260)

L5 = Label(WIN, text="", font="Aerial 15")
L5.place(x=85, y=223)

B1 = Button(WIN, text="Submit", font="Aerial 15", command=Submit)
B1.place(x=110, y=175)

B2 = Button(WIN, text="Submit OTP", font="Aerial 15", command=SubmitOTP)
B2.place(x=95, y=290)

L6 = Label(WIN, text="", font="Aerial 14")
L6.place(x=0, y=335)

WIN.mainloop()