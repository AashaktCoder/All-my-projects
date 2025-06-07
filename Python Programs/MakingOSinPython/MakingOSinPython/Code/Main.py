# This would be a single user single task operating system made using tkinter module of python and would have a gui interface and features such as file handling, image manipulation, video recording, camera etc. This program is made by Aashakt.

from tkinter import *
from Login import LoginSystem
from os import listdir

class MainWindow:
    def __init__(self):
        self.WIN = Tk()

        self.loginSystem = LoginSystem(self.WIN)

    def Booting(self):
        self.WIN.title("Panda OS")
        icon = PhotoImage(file="Images/Icons/PandaIcon.png")
        self.WIN.iconphoto(False, icon)
        self.WIN.geometry("400x400")
        self.WIN.maxsize(400, 400)
        self.WIN.minsize(400, 400)

    def Update(self):
        self.Booting()
        self.loginSystem.Update()
        self.WIN.mainloop()

newWindow = MainWindow()
newWindow.Update()