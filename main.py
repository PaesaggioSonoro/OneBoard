from GUI import GUI

class Main:
    gui = GUI()

    @staticmethod
    def run():
        while True:
            if Main.gui.run:
                Main.gui.loop()
            else:
                break

            if Main.gui.reload:
                Main.reload()

    @staticmethod
    def reload():
        Main.gui.close()
        del Main.gui
        Main.gui = GUI()

if __name__ == '__main__':
    Main.run()