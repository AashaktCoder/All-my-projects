from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.topGrid = GridLayout()
        self.topGrid.cols = 2
        self.cols = 1

        self.topGrid.add_widget(Label(text="Name:", font_size=36))
        self.NameText = TextInput(multiline=False, font_size=40)
        self.topGrid.add_widget(self.NameText)

        self.topGrid.add_widget(Label(text="Class:", font_size=36))
        self.ClassText = TextInput(multiline=False, font_size=40)
        self.topGrid.add_widget(self.ClassText)

        self.topGrid.add_widget(Label(text="Hobbies:", font_size=36))
        self.hobbieText = TextInput(multiline=False, font_size=40)
        self.topGrid.add_widget(self.hobbieText)

        self.add_widget(self.topGrid)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.SubmitInfo)
        self.add_widget(self.submit)

        self.ResultLabel = Label(text="", font_size=24)
        self.add_widget(self.ResultLabel)

    def SubmitInfo(self, instance):
        name = self.NameText.text
        grade = self.ClassText.text
        hobbie = self.hobbieText.text

        self.ResultLabel.text = f"My name is {name} and I study in class {grade} and I like {hobbie}"

class MyApp(App):
    def build(self):
        self.title = "Aashakt's first kivy app"
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()        