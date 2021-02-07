from random import choice

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.actionbar import ActionButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner

from config import Config
from sound import Sound

Builder.load_file('sections/screens/header.kv')

class Header(BoxLayout):
    player_disabled = True
    player_playing = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = Sound()
        self.playback : Spinner = self.ids['playback_device']

        devices : dict = Sound.getSpeakers()
        self.devices_indexes = list(devices.keys())
        self.devices_names = list(devices.values())

        self.playback.values = self.devices_names

        toSelectIndex = Config().getDevice()
        if (toSelectIndex is None) or (devices.get(toSelectIndex) is None):
            toSelectIndex = choice(self.devices_indexes)

        toSelect = self.devices_names[self.devices_indexes.index(toSelectIndex)]
        self.playback.text = toSelect

        self.update_player()

        # Clock.schedule_interval(self.update_player, 0.1)

    def _onSpinnerSelect(self, text):
        Config().setDevice(self.devices_indexes[self.devices_names.index(text)])

    def toggle_pause(self, btn: Button):
        if Header.player_playing:     # is playing
            self.sound.pause()
        else:                           # not playing
            self.sound.resume()
        Header.player_playing = not Header.player_playing

        self.update_player()

    def update_player(self, *args):
        btn : ActionButton = self.ids['player_button']
        btn.icon = 'icons/pause.png' if Header.player_playing else 'icons/play.png'
        btn.disabled = Header.player_disabled

    # def resume(self):
    #     self.sound.resume()

