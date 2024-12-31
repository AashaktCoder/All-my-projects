import nltk
import json

class Chatbot:
    def __init__(self):
        print("\nThis is the PandaChess Chatbot, you can ask the bot about anything. To quit the program type quit\n")

        self.command = ""
        self.tokens = []
        
        self.run = True

    def TakeCommand(self):
        self.command = input("Type Something: ")
        self.tokens = nltk.word_tokenize(self.command)

        if self.command == "quit":
            self.run = False

    def GreetingCommands(self):
        GreetingComands = json.load(open("Command Files\\GreetingCommands.txt",))
        
        for words in GreetingComands:
            if words.lower() == self.command.lower():
                print("Hello, what can I do for you?")

    def Update(self):
        while self.run:
            self.TakeCommand()
            self.GreetingCommands()

chatbot = Chatbot()
chatbot.Update()