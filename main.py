from GUI import GUI
from kivy.config import Config




if __name__ == '__main__':
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
    GUI().run()
