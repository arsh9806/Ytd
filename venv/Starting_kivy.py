from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.inside= GridLayout()
        self.inside.cols=2
        self.inside.add_widget(Label(text="User Name : "))
        self.username=TextInput(multiline=False)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text="PassWord : "))
        self.password= TextInput(password=True,multiline=False)
        self.inside.add_widget(self.password)
        self.add_widget(self.inside)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    def pressed(self,instance):
        print(self.username.text)
        print(self.password.text)


class MyApp(App):
    def build(self):
        return LoginScreen()


MyApp().run()