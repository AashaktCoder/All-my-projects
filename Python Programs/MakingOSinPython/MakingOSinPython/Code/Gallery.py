from tkinter import *
from os import listdir

class Gallery:
    def __init__(self, WIN, AppList):
        self.WIN = WIN
        self.AppList = AppList

        self.FileList = listdir("Storage")
        self.ImgList = []

        for i in self.FileList:
            if ".png" in i: self.ImgList.append(i)

        self.imgCount = -1
    
    def GoBack(self):
        self.GalleryCanvas.pack_forget()
        self.AppList.pack(side=LEFT, fill=BOTH, expand=True)

    def NextImg(self):
        self.imgCount += 1
        self.FileList = listdir("Storage")
        lst = []
        for i in self.FileList:
            if ".png" in i: 
                lst.append(i)
        self.ImgList = lst

        NewImg = PhotoImage(file=f"Storage/{self.ImgList[self.imgCount]}")
        self.img.configure(image=NewImg, height=200, width=200)
        self.img.image = NewImg

    def PreviousImg(self):
        self.imgCount -= 1
        self.FileList = listdir("Storage")
        lst = []
        for i in self.FileList:
            if ".png" in i: 
                lst.append(i)
        self.ImgList = lst

        NewImg = PhotoImage(file=f"Storage/{self.ImgList[self.imgCount]}")
        self.img.configure(image=NewImg, height=200, width=200)
        self.img.image = NewImg

    def MakeWidgets(self):
        self.GalleryCanvas = Canvas()

        self.title = Label(self.GalleryCanvas, text="Gallery", font="Aerial 35")

        self.NextButton = Button(self.GalleryCanvas, text="Next", font="Aerial 20", command=self.NextImg)
        self.PrevButton = Button(self.GalleryCanvas, text="Prev", font="Aerial 20", command=self.PreviousImg)

        self.img = Label(self.GalleryCanvas, image=None, height=10, width=10)

        self.BackButton = Button(self.GalleryCanvas, text="Back", font="Aerial 20", command=self.GoBack)

    def PlaceWidgets(self):
        self.GalleryCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.title.place(x=120, y=0)

        self.PrevButton.place(x=10, y=180)
        self.NextButton.place(x=310, y=180)

        self.img.place(x=100, y=100)

        self.BackButton.place(x=5, y=340)

    def Update(self):
        self.MakeWidgets()
        self.PlaceWidgets()