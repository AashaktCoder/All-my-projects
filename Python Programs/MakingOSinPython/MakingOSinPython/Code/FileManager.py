from tkinter import *
from os import listdir, remove, path
import glob

class FileManager:
    def __init__(self, WIN, AppListCanvas):
        self.WIN = WIN
        self.AppListCanvas = AppListCanvas

        self.DropDownVar = StringVar()
        self.DeleteFileVar = StringVar()

        self.DropDownVar.set("Choose File")
        self.DeleteFileVar.set("Choose File")
        self.DropDownList = listdir("Storage")
        self.DeleteFilelist = listdir("Storage")

        self.NewFileName = StringVar()

    def GoBack(self):
        self.FileManagerCanvas.pack_forget()
        self.AppListCanvas.pack(side=LEFT, fill=BOTH, expand=True)

    def ShowDropDown(self):
        self.DropDownList = listdir("Storage")
        png_files = [file for file in self.DropDownList if file.endswith(".png")]
        for png_file in png_files:
            self.DropDownList.remove(png_file)
        self.OpenFileMenu = OptionMenu(self.FileManagerCanvas, self.DropDownVar, *self.DropDownList)
        self.OpenFileMenu.place(x=220, y=130)
        self.OpenFileB.place(x=240, y=165)
    
    def OpenFileScreen(self):
        OpenFileCanvas = Canvas(self.WIN)

        def GoBack():
            OpenFileCanvas.pack_forget()
            self.FileManagerCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        def SaveChanges():
            with open(f"Storage/{self.DropDownVar.get()}", 'w') as f:
                f.write(DisplayText.get(1.0, 'end-1c'))

        DisplayText = Text(OpenFileCanvas, width=50, height=20)
        
        with open(f"Storage/{self.DropDownVar.get()}", 'r') as f:
            content = f.read()
            DisplayText.insert("end-1c", content)

        BackButton = Button(OpenFileCanvas, text="Back", font="Aerial 20", command=GoBack)

        SaveButton = Button(OpenFileCanvas, text="Save", font="Aerial 20", command=SaveChanges)

        OpenFileCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        BackButton.place(x=5, y=340)
        SaveButton.place(x=160, y=340)
        DisplayText.place(x=0,y=0)

    def OpenTheFile(self):
        self.OpenFileMenu.place_forget()
        self.OpenFileB.place_forget()
        self.FileManagerCanvas.pack_forget()
        self.OpenFileScreen()

    def ShowNewName(self):
        self.NewNameL.place(x=0, y=140)
        self.NewNameE.place(x=42, y=142)
        self.NewCreateB.place(x=40, y=165)

    def MakeNewFile(self):
        open(f"Storage/{self.NewFileName.get()}.txt", "x")
        self.DeleteFilelist = listdir("Storage")
        self.DeleteMenu = OptionMenu(self.FileManagerCanvas, self.DeleteFileVar, *self.DeleteFilelist)
        self.NewNameL.place_forget()
        self.NewNameE.place_forget()
        self.NewCreateB.place_forget()

    def ShowDeleteFiles(self):
        self.DeleteFilelist = listdir("Storage")
        self.DeleteMenu = OptionMenu(self.FileManagerCanvas, self.DeleteFileVar, *self.DeleteFilelist)
        self.DeleteMenu.place(x=150, y=290)

    def DeleteFile(self):
        self.DeleteMenu.place_forget()
        remove(f"Storage/{self.DeleteFileVar.get()}")
        self.DeleteFilelist = listdir("Storage")
        self.DeleteMenu = OptionMenu(self.FileManagerCanvas, self.DeleteFileVar, *self.DeleteFilelist)
        self.DropDownVar.set("Choose File")
        self.DeleteFileVar.set("Choose File")

    def MakeWidgets(self):
        self.FileManagerCanvas = Canvas(self.WIN)

        self.title = Label(self.FileManagerCanvas, text="File Manager", font="Aerial 30")
        self.NewFileB = Button(self.FileManagerCanvas, text="New File", font="Aerial 20", command=self.ShowNewName)
        self.NewNameL = Label(self.FileManagerCanvas, text="Name:", font="Aerial 10")
        self.NewNameE = Entry(self.FileManagerCanvas, textvariable=self.NewFileName, font="Aerial 10")
        self.NewCreateB = Button(self.FileManagerCanvas, text="Make", font="Aerial 15", command=self.MakeNewFile)

        self.OpenMenuB = Button(self.FileManagerCanvas, text="Show File", font="Aerial 20", command=self.ShowDropDown)
        self.OpenFileB = Button(self.FileManagerCanvas, text="Open File", font="Aerial 12", command=self.OpenTheFile)

        self.OpenFileMenu = OptionMenu(self.FileManagerCanvas, self.DropDownVar, *self.DropDownList)

        self.DeleteFileB = Button(self.FileManagerCanvas, text="Delete", font="Aerial 20", command=self.DeleteFile)
        self.DeleteMenu = OptionMenu(self.FileManagerCanvas, self.DeleteFileVar, *self.DeleteFilelist)
        self.ShowDelete = Button(self.FileManagerCanvas, text="Show", font="Aerial 12", command=self.ShowDeleteFiles)

        self.BackButton = Button(self.FileManagerCanvas, text="Back", font="Aerial 20", command=self.GoBack)

    def PlaceWidgets(self):
        self.FileManagerCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.title.place(x=20, y=0)
        self.NewFileB.place(x=10, y=60)

        self.OpenMenuB.place(x=220, y=60)
        self.OpenFileMenu.place_forget()

        self.DeleteFileB.place(x=150, y=230)
        self.ShowDelete.place(x=150, y=330)

        self.BackButton.place(x=5, y=340)

    def Update(self):
        self.MakeWidgets()
        self.PlaceWidgets()