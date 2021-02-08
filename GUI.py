from kivy.app import App
from kivy.core.window import Window
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from sections.body import Body
from sound import Sound
from sections.header import Header



class GUI(App, BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (204/255, 229/255, 255/255, 1)
        self.sound = Sound()
        self.header = Header()
        Sound.header = self.header



    def build(self):
        box = BoxLayout(orientation = 'vertical')
        box.spacing = 10
        box.padding = 10
        box.add_widget(self.header)
        box.add_widget(Body())

        return box

