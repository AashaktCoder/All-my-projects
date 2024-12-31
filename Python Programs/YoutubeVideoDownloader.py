from tkinter import *
from pytube import YouTube

WIN = Tk()
WIN.geometry("200x100")
WIN.minsize(200, 100)
WIN.maxsize(200, 100)
WIN.title("Download Video")

def Submit(Link):
    file = YouTube(Link)
    mp4 = file.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
    mp4.download("C:\MyFolder", ".mp4", "YoutubePython")

L = StringVar()

L1 = Label(WIN, text="Link: ")
L1.place(x=5, y=20)
E1 = Entry(WIN, textvariable=L)
E1.place(x=50, y=20)
B1 = Button(WIN, text="Download", command=lambda: Submit(L.get()))
B1.place(x=65, y=60)

WIN.mainloop()