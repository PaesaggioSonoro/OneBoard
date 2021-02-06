from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class MyLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        playback : DropDown = self.ids['playback']
        btn = Button(text='Ciao ciao', size_hint_y=None, height='48dp', on_release = playback.select)
        # Button:
        # text: 'Value A'
        # size_hint_y: None
        # height: '48dp'
        # on_release: playback.select('A')
        playback.add_widget(btn)



class GUI(App):
    def build(self):
        Window.clearcolor = (204/255, 229/255, 255/255, 1)
        return MyLayout()

if __name__ == '__main__':
    GUI().run()