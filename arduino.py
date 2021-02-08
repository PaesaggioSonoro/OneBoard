from typing import List

import serial

from threading import Thread
from queue import Queue

class Arduino:
    quit: bool = False
    connection: serial.Serial = None
    connection_status = 0           # 0 disconnected, 1 connecting, 2 connected

    queue: Queue = None
    port = ''


    @staticmethod
    def initialize(queue: Queue):
        Arduino.quit = False       # became True when closing the application
        Arduino.queue = queue      # save given Queue

    from serial.tools.list_ports_common import ListPortInfo

    @staticmethod
    def connect():
        if Queue is None:
            raise Exception('Queue not defined')
        if Arduino.port:
            Arduino.connection = serial.Serial(Arduino.port, timeout=1)
            Thread(target=Arduino.update).start()

    last_update = None

    @staticmethod
    def update():
        Arduino.connection_status = 1
        import time
        time.sleep(2)
        Arduino.last_update = time.time()
        while not Arduino.quit:
            if time.time() - Arduino.last_update > 3:
                print('Arduino disconnected')
                break
            try:
                if Arduino.connection.in_waiting:
                    message = Arduino.connection.read(8)
                    if len(message) != 8:
                        print('Error, message is incomplete')
                        # return
                    data = message[1:7]
                    if data == b'000000':
                        Arduino.last_update = time.time()       # still alive
                        Arduino.connection_status = 2

                    # ERRORS
                    elif data == b'err1':
                        print('arduino message error')

            except serial.serialutil.SerialException:
                print('Arduino disconnected')
                break
        Arduino.connection_status = 0

    @staticmethod
    def getPorts() -> List[ListPortInfo]:
        import serial.tools.list_ports
        ports = list(serial.tools.list_ports.comports())
        return ports

