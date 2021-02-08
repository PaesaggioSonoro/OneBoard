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
from arduino import Arduino

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
        self._updatePorts()

        # Clock.schedule_interval(self.update_player, 0.1)

    def _onSpinnerSelect(self, text):
        index = self.devices_indexes[self.devices_names.index(text)]
        Config().setDevice(index)
        Sound.device_index = index

    def _updatePorts(self):
        dropdown: DropDown = self.ids['ports_dropdown']
        dropdown.clear_widgets()
        toSelect = ''
        for port in Arduino.getPorts():
            if 'Arduino' in port.description and not 'Leonardo' in port.description:
                toSelect = port.name
            btn: Button = Button(text=port.name + ' - ' + port.description)
            btn.size_hint_y = None
            btn.height = 40
            btn.font_size = 13

            btn.port_name = port.name
            btn.bind(on_release=lambda b: dropdown.select(b.port_name))
            dropdown.add_widget(btn)
        if toSelect:
            dropdown.select(toSelect)

    @staticmethod
    def _setSelectedPort(port_name: str):
        Arduino.port = port_name

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

