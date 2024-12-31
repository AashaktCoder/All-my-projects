from tkinter import *
from tkinter import filedialog
from pygame import mixer

mixer.init()

WIN = Tk()
WIN.geometry("300x300")
WIN.minsize(300, 300)
WIN.maxsize(300, 300)
WIN.title("Music Player By Aashakt")

def OpenFile():
    WIN.filename = filedialog.askopenfilename(initialdir="C:", title="Select File", filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav"), ("All files", "*.*")))
    mixer.music.load(WIN.filename)

def PlayMusic():
    mixer.music.play()

def ResumePauseMusic(PlayPause):
    if PlayPause:
        mixer.music.unpause()
    else:
        mixer.music.pause()   

B1 = Button(WIN, text="Play", command=PlayMusic)
B1.place(x=0, y=0)

B2 = Button(WIN, text="Open File", command=OpenFile)
B2.place(x=0, y=40)

B3 = Button(WIN, text="Pause", command=lambda: ResumePauseMusic(False))
B3.place(x=0, y=80)

B4 = Button(WIN, text="Resume", command=lambda: ResumePauseMusic(True))
B4.place(x=0, y=120)

WIN.mainloop()