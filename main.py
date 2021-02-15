from GUI import GUI
from kivy.config import Config
from kivy.resources import resource_add_path
import os, sys

# basepath = os.path.dirname(os.path.abspath(__file__))
# resource_add_path(os.path.join(basepath, 'sections\\screens\\'))
# resource_find('header.kv')

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

    GUI().run()
