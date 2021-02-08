from typing import List

import serial

from threading import Thread
from queue import Queue

class Arduino:
    port = ''

    def __init__(self, queue: Queue):
        self.quit = False       # became True when closing the application
        self.queue = queue      # save given Queue

    from serial.tools.list_ports_common import ListPortInfo

    @staticmethod
    def getPorts() -> List[ListPortInfo]:
        import serial.tools.list_ports
        ports = list(serial.tools.list_ports.comports())
        return ports

