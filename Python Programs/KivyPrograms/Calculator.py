from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.size = (330, 600)
Window.minimum_width, Window.minimum_height = Window.size

class MyLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.oldVal = ""
        self.ResultVal = ""
        self.newVal = ""

        self.Operator = {"Add":False, "Sub":False, "Multi":False}

        self.NewLayout = FloatLayout()

        self.MainInput = TextInput(size_hint_x=None, width=330, size_hint_y=None, height=100, font_size=70, pos=(0,500))
        self.NewLayout.add_widget(self.MainInput)

        self.add_widget(self.NewLayout)

        # Making the Buttons
        B1 = Button(text="1", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(0, 400))
        B1.bind(on_press = self.TypeNumber)
        self.add_widget(B1)
        B2 = Button(text="2", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(110, 400))
        B2.bind(on_press = self.TypeNumber)
        self.add_widget(B2)
        B3 = Button(text="3", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(220, 400))
        B3.bind(on_press = self.TypeNumber)
        self.add_widget(B3)
        B4 = Button(text="4", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(0, 300))
        B4.bind(on_press = self.TypeNumber)
        self.add_widget(B4)
        B5 = Button(text="5", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(110, 300))
        B5.bind(on_press = self.TypeNumber)
        self.add_widget(B5)
        B6 = Button(text="6", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(220, 300))
        B6.bind(on_press = self.TypeNumber)
        self.add_widget(B6) 
        B7 = Button(text="7", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(0, 200))
        B7.bind(on_press = self.TypeNumber)
        self.add_widget(B7)
        B8 = Button(text="8", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(110, 200))
        B8.bind(on_press = self.TypeNumber)
        self.add_widget(B8)
        B9 = Button(text="9", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(220, 200))
        B9.bind(on_press = self.TypeNumber)
        self.add_widget(B9)               
        B0 = Button(text="0", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(220, 100))
        B0.bind(on_press = self.TypeNumber)
        self.add_widget(B0) 

        B11 = Button(text="+", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(0, 100))
        B11.bind(on_press=self.AddFunc)
        self.add_widget(B11) 
        B12 = Button(text="-", font_size=72, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(0, 0))
        B12.bind(on_press=self.SubFunc)
        self.add_widget(B12)
        B13 = Button(text="x", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(110, 0))
        B13.bind(on_press=self.MultiFunc)
        self.add_widget(B13)
        B14 = Button(text="=", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(110, 100))
        B14.bind(on_press=self.ResultFunc)
        self.add_widget(B14) 
        B15 = Button(text="C", font_size=48, size_hint_x=None, width=110, size_hint_y=None, height=100, pos=(220, 0))
        B15.bind(on_press=self.ClearFunc)
        self.add_widget(B15)

    def TypeNumber(self, instance):
        self.MainInput.text = self.MainInput.text + instance.text

    def AddFunc(self, instance):
        self.oldVal = self.MainInput.text
        if (self.MainInput.text == ""):
            self.oldVal = 0  
        self.MainInput.text = ""
        self.Operator["Add"] = True

    def SubFunc(self, instance):
        self.oldVal = self.MainInput.text
        if (self.MainInput.text == ""):
            self.oldVal = 0  
        self.MainInput.text = ""
        self.Operator["Sub"] = True    

    def MultiFunc(self, instance):
        self.oldVal = self.MainInput.text
        if (self.MainInput.text == ""):
            self.oldVal = 0  
        self.MainInput.text = ""
        self.Operator["Multi"] = True 

    def ResultFunc(self, instance):
        if (self.Operator["Add"] == True):
            self.newVal = self.MainInput.text
            self.ResultVal = str(int(self.oldVal) + int(self.newVal))
            self.MainInput.text = self.ResultVal
            self.Operator["Add"] = False
        if (self.Operator["Sub"] == True):
            self.newVal = self.MainInput.text
            self.ResultVal = str(int(self.oldVal) - int(self.newVal))
            self.MainInput.text = self.ResultVal
            self.Operator["Sub"] = False
        if (self.Operator["Multi"] == True):
            self.newVal = self.MainInput.text
            self.ResultVal = str(int(self.oldVal) * int(self.newVal))
            self.MainInput.text = self.ResultVal      
            self.Operator["Multi"] = False                      

    def ClearFunc(self, instance):
        self.MainInput.text = ""               

class MyApp(App):
    def build(self):
        self.title = "Calculator By Aashakt"
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()        