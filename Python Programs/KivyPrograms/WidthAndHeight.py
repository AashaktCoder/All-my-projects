from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2
        self.rows = 2

        self.WidthText = TextInput(multiline=False, font_size = 40, size_hint_y=None, height=100)
        self.add_widget(self.WidthText)

        self.HeightText = TextInput(multiline=False, font_size = 40, size_hint_y=None, height=100)
        self.add_widget(self.HeightText)

        self.MainB = Button(text="Change Size", size_hint_y=None, height=50, size_hint_x=None, width=150)
        self.MainB.bind(on_press=self.ChangeSize)
        self.add_widget(self.MainB)

        self.SecondB = Button(size_hint_y=None, height=50, size_hint_x=None, width=50, background_color=[0, 4, 0, 1])
        self.add_widget(self.SecondB) 

    def ChangeSize(self, instance):
        newWidth = int(self.WidthText.text)
        newHeight = int(self.HeightText.text)
        self.SecondB.height = newHeight
        self.SecondB.width = newWidth
  

class MyApp(App):
    def build(self):
        self.title = "Made By Aashakt"
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()        