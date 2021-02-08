from queue import Queue

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from arduino import Arduino
from sections.body import Body
from sound import Sound
from sections.header import Header



class GUI(App, BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (204/255, 229/255, 255/255, 1)
        self.sound = Sound()
        self.header = Header()
        self.body = Body()
        self.arduino_queue = Queue(maxsize=10)
        Arduino.initialize(self.arduino_queue)
        Sound.header = self.header

        Clock.schedule_interval(self.getQueueUpdates, 0.1)

    def getQueueUpdates(self, *args):
        if not self.arduino_queue.empty():
            data = self.arduino_queue.get()
            if data is None: return

    def on_stop(self):
        Sound().status = 0
        Arduino.quit = True

    def build(self):
        box = BoxLayout(orientation = 'vertical')
        box.spacing = 10
        box.padding = 10
        box.add_widget(self.header)
        box.add_widget(self.body)

        return box

