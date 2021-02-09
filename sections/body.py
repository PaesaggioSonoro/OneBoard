from kivy.input.providers.mouse import MouseMotionEvent
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from config import Config
from sound import Sound

from easygui import fileopenbox

Builder.load_file('sections/screens/body.kv')

class Body(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = Config()
        for id, button in self.config.getButtons().items():
            Body.setup_button(self.ids[id], button['name'], button['file'])

    def pressed(self, instance: Button, touch: MouseMotionEvent = None):
        if touch is not None:
            if not instance.collide_point(touch.x, touch.y): return
            if touch.button == 'right':
                from os.path import basename, split, splitext, exists
                from os import remove
                import ffmpeg

                btn_id = self.get_id(instance)
                path: str = fileopenbox(msg='Choose audio', title='OneBoard file chooser',
                                        default=self.config.getLastPath() + '\\*.mp3',
                                        filetypes=[['*.mp3', '*.flac', '*.wav', '*.m4a', '*.aac', "Audio files"]])
                if path is not None:
                    self.config.setLastPath(split(path)[0])
                    file_name = basename(splitext(path)[0])  # only the name of the file
                    new_file_name = file_name + '.wav'  # name with extension
                    Body.setup_button(instance, file_name, new_file_name)
                    self.config.setButton(btn_id, file_name, new_file_name)
                    old_path = 'audio/' + self.config.getButtonFile(btn_id)  # old local file directory
                    if old_path:  # remove old file
                        if exists(old_path):
                            remove(old_path)
                    ffmpeg.input(path).output('audio/' + new_file_name).run()  # convert and copy the file
                return
        if instance.file != '':
            Sound().play(instance.file)





    @staticmethod
    def setup_button(button: Button, name, file):
        button.text = name
        button.file = file


    def get_id(self, instance):
        for id, widget in self.ids.items():
            if widget.__self__ == instance:
                return id