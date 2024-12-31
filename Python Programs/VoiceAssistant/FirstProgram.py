import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

r1 = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 100)

with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source,duration=1)

    print("Speak Now: ")
    audio = r1.listen(source)
    said = ""

    try:
        said = r1.recognize_google(audio)
        print(said)

        if 'open' in said:
            engine.say(f"opening {said[5:len(said)]}")
            engine.runAndWait()
            webbrowser.open(f"https://{said[5:len(said)]}.com")
        else:
            searchResult = wikipedia.summary(said, sentences=2)    
            print(searchResult)

    except Exception as e:
        print(e)    