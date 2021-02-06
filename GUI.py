from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class MyLayout(BoxLayout):
    pass
    # def cacca(self):
    #     self.ids

class GUI(App):
    def build(self):
        Window.clearcolor = (204/255, 229/255, 255/255, 1)
        return MyLayout()

if __name__ == '__main__':
    GUI().run()