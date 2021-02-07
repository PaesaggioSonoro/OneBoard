from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from sound import Sound
from random import choice
from config import Config

class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        playback : DropDown = self.ids['playback']
        devices : dict = Sound.getSpeakers()
        index: int
        device_name: str
        for index, device_name in devices.items():
            btn: Button = Button(text=device_name, size_hint = (0.5, None), height='48dp')
            btn.index = index
            btn.bind(on_release=lambda b: playback.select([b.text, b.index]))
            playback.add_widget(btn)

        toSelect = Config().getDevice()
        if (toSelect is None) or (devices.get(toSelect) is None):
            toSelect = choice(list(devices.keys()))
            Config().setDevice(toSelect)

        playback.select([devices[toSelect], toSelect])



class GUI(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = Sound()

    def build(self):
        Window.clearcolor = (204/255, 229/255, 255/255, 1)
        return MyLayout()

if __name__ == '__main__':
    GUI().run()