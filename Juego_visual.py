import keyboard
import time
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.base import runTouchApp
from kivy.factory import Factory



class MyGridLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.con = "\n."
        self.add = ""
        self.ids.dot_button.opacity = 0
        Clock.schedule_interval(self.constante, 0.015)
        Clock.schedule_interval(self.press,0.015)
    def constante(self,*args):
        self.ids.dot_label.text += self.con + self.add

    def press(self,*args):
        if self.ids.dot_button.state == "down":
            if len(self.add) < 82:
               self.add += "."
        else:
            self.add = self.add[:-1]








class MyApp(App):




    def build(self):
        return MyGridLayout()


if __name__=="__main__":
    MyApp().run()


