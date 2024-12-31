from tkinter import *
import pyttsx3
import speech_recognition as sr

WIN = Tk()
WIN.geometry("200x230")
WIN.minsize(200, 230)
WIN.maxsize(200, 230)

MicrophoneIcon = PhotoImage(file = "C:\\MyFolder\\PythonProgramming\\VoiceAssistant\\MicrophoneIcon.png")

r1 = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 100)

def SpeakNow():
    L1.configure(text="Speak Now: ")
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source,duration=1)

        audio = r1.listen(source)
        said = ""

        try:
            said = r1.recognize_google(audio)
            L1.configure(text=said)

        except Exception as e:
            print(e)
    L1.configure(text="")        

L1 = Label(WIN, text="")
L1.place(x=0, y=200)
B1 = Button(WIN, image = MicrophoneIcon, width=200, height=200, command = SpeakNow)
B1.place(x=0, y=0)

WIN.mainloop()