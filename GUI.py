from queue import Queue

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

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

        Clock.schedule_interval(self.getQueueUpdates, 0.05)

    def getQueueUpdates(self, *args):
        if not self.arduino_queue.empty():
            data = self.arduino_queue.get()
            if data is None: return
            if data[0] == 'button':
                # print('Pressed button: ' + data[1])
                btn : Button = self.body.ids[data[1]]
                self.body.pressed(btn)
                btn.state = 'down'
                def btn_normal(*args):
                    btn.state = 'normal'
                Clock.schedule_once(btn_normal,0.2)
            elif data == 'pause':
                if not Header.player_disabled:
                    self.header.toggle_pause()


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

