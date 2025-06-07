from tkinter import *
from cv2 import VideoCapture, imshow, waitKey, destroyWindow, imwrite
from os import listdir
from PIL import Image

class Camera:
    def __init__(self, WIN, AppListCanvas):
        self.WIN = WIN
        self.AppListCanvas = AppListCanvas

        self.maxN = 0

    def GoBack(self):
        self.CameraCanvas.pack_forget()
        self.AppListCanvas.pack(side=LEFT, fill=BOTH, expand=True)

    def TurnOnCamera(self):
        for i in listdir('Storage'): 
            if ".png" in i: 
                self.maxN = int(i[6])+1

        cam = VideoCapture(0)
        result, NewImg = cam.read()

        if result:
            imwrite(f"Storage/newImg{self.maxN}.png", NewImg)
            resizeImg = Image.open(f"Storage/newImg{self.maxN}.png")
            resizeImg = resizeImg.resize((200, 200))
            resizeImg.save(f"Storage/newImg{self.maxN}.png")
            image2 = PhotoImage(file=f"Storage/newImg{self.maxN}.png")
            self.ImgLabel.configure(image=image2, height=250, width=250)
            self.ImgLabel.image = image2
            cam = 0

    def MakeWidget(self):
        self.CameraCanvas = Canvas(self.WIN)

        self.Title = Label(self.CameraCanvas, text="Camera", font="Aerial 35")

        self.BackButton = Button(self.CameraCanvas, text="Back", font="Aerial 20", command=self.GoBack)

        self.TurnOnB = Button(self.CameraCanvas, text="Turn On", font="Aerial 20", command=self.TurnOnCamera)

        self.ImgLabel = Label(self.CameraCanvas, image=None, height=10, width=10)

    def PlaceWidget(self):
        self.CameraCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.Title.place(x=100, y=0)
        self.BackButton.place(x=5, y=340)

        self.TurnOnB.place(x=120, y=90)
        self.ImgLabel.place(x=100, y=150)

    def Update(self):
        self.MakeWidget()
        self.PlaceWidget()