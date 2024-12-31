import pyttsx3
  
engine = pyttsx3.init()

run = True

def TakeInput():
    global run

    msg = input("Text To Speech: ")
    engine.say(msg)
    engine.runAndWait()

    if msg == "q":
        run = False

while run:
    TakeInput()
