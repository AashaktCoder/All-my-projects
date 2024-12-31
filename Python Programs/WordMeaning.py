import pyttsx3
import wikipedia

engine = pyttsx3.init()
engine.setProperty("rate", 180)

MainText = input("Enter a Word: ") 
print(wikipedia.summary(MainText, sentences=2))

engine.say(wikipedia.summary(MainText, sentences=2))
engine.runAndWait()