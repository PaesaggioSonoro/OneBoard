from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from sound import Sound

Builder.load_file('sections/screens/body.kv')

class Body(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ciao: Button = self.ids['ciao']
        ciao.bind(on_touch_down=self.pressed)

    def pressed(self, instance: Button, touch: MouseMotionEvent):
        if not instance.collide_point(touch.x, touch.y): return
        Sound().play()