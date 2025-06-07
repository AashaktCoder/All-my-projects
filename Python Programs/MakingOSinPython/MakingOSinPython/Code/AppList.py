from tkinter import *
from FileManager import FileManager
from Camera import Camera
from Gallery import Gallery

class AppList:
    def __init__(self, WIN):
        self.WIN = WIN
        self.AppCanvas = Canvas(self.WIN)

        self.fileManager = FileManager(self.WIN, self.AppCanvas)
        self.camera = Camera(self.WIN, self.AppCanvas)
        self.gallery = Gallery(self.WIN, self.AppCanvas)

    def OpenFileManager(self):
        self.AppCanvas.pack_forget()
        self.fileManager.Update()
    
    def OpenCamera(self):
        self.AppCanvas.pack_forget()
        self.camera.Update()

    def OpenGallery(self):
        self.AppCanvas.pack_forget()
        self.gallery.Update()

    def MakeWidgets(self):
        self.MainTitle = Label(self.AppCanvas, text="App List of Panda OS", font="Aerial 30")

        self.FileManagerBicon = PhotoImage(file="Images/Icons/FileManagerIcon.png")
        self.FileManagerB = Button(self.AppCanvas, image=self.FileManagerBicon, command=self.OpenFileManager)

        self.CameraBicon = PhotoImage(file="Images/Icons/CameraIcon.png")
        self.CameraB = Button(self.AppCanvas, image=self.CameraBicon, command=self.OpenCamera)

        self.GalleryBicon = PhotoImage(file="Images/Icons/GalleryIcon.png")
        self.GalleryB = Button(self.AppCanvas, image=self.GalleryBicon, command=self.OpenGallery)

    def PlaceWidgets(self):
        self.AppCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.MainTitle.place(x=10,y=0)

        self.FileManagerB.place(x=10, y=60)
        self.CameraB.place(x=100, y=60)
        self.GalleryB.place(x=190, y=60)
    
    def Update(self):
        self.MakeWidgets()
        self.PlaceWidgets()