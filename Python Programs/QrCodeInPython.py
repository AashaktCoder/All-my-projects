import qrcode
from tkinter import *
from PIL import Image
import webbrowser

WIN = Tk()
WIN.geometry("200x200")
WIN.minsize(200, 200)
WIN.maxsize(200, 200)
WIN.title("QR code")

image = Image.open("some_file.png")
image = image.resize((120, 120))
image.save("some_file.png")

QRCodeImage = PhotoImage(file="some_file.png")

def GetQRcode():
    global QRcodeImg
    MainText = E1.get()
    QRCodeImage = qrcode.make(MainText)
    QRCodeImage.save("some_file.png")
    image = Image.open("some_file.png")
    image = image.resize((120, 120))
    image.save("some_file.png")
    QRCodeImage = PhotoImage(file="some_file.png")
    L2.configure(image=QRCodeImage)
    if ("https://" in E1.get()):
        webbrowser.open(E1.get())

L1 = Label(WIN, text="Text: ").place(x=0, y=0)

E1 = Entry(WIN)
E1.place(x=50, y=0)

B1 = Button(WIN, text="Submit", command=GetQRcode)
B1.place(x=75, y=25)

L2 = Label(WIN, image=QRCodeImage, width=200, height=100)
L2.place(x=0, y=75)

WIN.mainloop()