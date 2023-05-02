
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock




class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.con = "\n."
        self.add = ""

        Clock.schedule_interval(self.constante, 0.005)
        Clock.schedule_interval(self.press,0.005)
    def constante(self,*args):
        self.ids.dot_button.text += self.con + self.add

    def press(self,*args):
        if self.ids.dot_button.state == "down":
            if len(self.add) < 88:    #Longitud de los puntos, ajustar en función de pantalla
               self.add += "."
        else:
            self.add = self.add[:-1]








class MyApp(App):




    def build(self):
        return MyGridLayout()


if __name__=="__main__":
    MyApp().run()


