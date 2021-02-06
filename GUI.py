import PySimpleGUI as sg
from constants import constants

class GUI:
    def __init__(self):
        self.run = False
        self.reload = False
        # noinspection PyTypeChecker
        self.window : sg.Window = None

        self.layout = [
            [
                sg.Text('asjkmhgbwk'),
                sg.HorizontalSeparator(pad=(50,0)),
                sg.Button('Reload', key=constants.events.RELOAD)
            ],
            [sg.HorizontalSeparator(pad=(0,20))],
            [
                sg.Button('Ciaoo', size=constants.BUTTON_SIZE, auto_size_button=True),
                sg.Button('ooaiC', size=constants.BUTTON_SIZE, auto_size_button=True),
                sg.Button('ooaiC', size=constants.BUTTON_SIZE, auto_size_button=True)
            ],
            [
                sg.Button('Ciaoo', size=constants.BUTTON_SIZE, auto_size_button=True),
                sg.Button('ooaiC', size=constants.BUTTON_SIZE, auto_size_button=True),
                sg.Button('ooaiC', size=constants.BUTTON_SIZE, auto_size_button=True)
            ],
            [
                sg.Button('Ciaoo', size=constants.BUTTON_SIZE, auto_size_button=True),
                sg.Button('ooaiC', size=constants.BUTTON_SIZE, auto_size_button=True),
                sg.Button('ooaiC', size=constants.BUTTON_SIZE, auto_size_button=True)
            ]
        ]
        self.window = sg.Window("OneBoard soundboard", self.layout, size=(700, 700), auto_size_buttons=True)
        self.run = True


    # called by Main function
    def loop(self):
        event, values = self.window.read()
        if event == sg.WIN_CLOSED:
            self.close()

        elif event == constants.events.RELOAD:
            self.reload = True

    def close(self):
        self.run = False
        self.window.close()
