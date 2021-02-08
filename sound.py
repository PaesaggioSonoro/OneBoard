import pyaudio, wave
from threading import Thread
from queue import Queue
from time import sleep

class Sound:
    chunk = 100
    p = pyaudio.PyAudio()
    device_index = 0
    header = None

    # singleton definition
    _instance = None
    _toInitialize = True
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if Sound._toInitialize:
            Sound._toInitialize = False
            super().__init__()
            self.status = 0         # 0 stop; 1 pause; 2 playing
            self.playing_thread = Thread()
            self.thread_alive = False

    @staticmethod
    def getSpeakers() -> dict:
        result = {}
        info = Sound.p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if Sound.p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels') > 0:
                result.update({i:Sound.p.get_device_info_by_host_api_device_index(0, i).get('name')})
        return result

    def play(self, audio: str):
        if self.thread_alive:
            self.status = 0             # stop playing
            self.playing_thread.join()  # wait for thread die
        self.playing_thread = Thread(target=self.reproduce, args=(audio,))
        self.playing_thread.start()     # start new playback

    def pause(self):
        self.status = 1

    def resume(self):
        self.status = 2

    def stop(self):
        self.status = 0

    def reproduce(self, audio):
        from sections.header import Header
        Header.player_disabled = False
        Sound.header.update_player()
        self.thread_alive = True
        self.status = 2
        wf: wave = wave.open('audio/' + audio, 'rb')

        stream = Sound.p.open(format=Sound.p.get_format_from_width(wf.getsampwidth()),
                              channels=wf.getnchannels(),
                              rate=wf.getframerate(),
                              output=True, output_device_index=Sound.device_index)

        data = wf.readframes(Sound.chunk)

        while data != b'':
            if self.status == 0:
                break
            elif self.status == 1:
                sleep(0.1)
            else:
                stream.write(data)
                data = wf.readframes(Sound.chunk)

        self.status = 0
        stream.close()
        self.thread_alive = False
        Header.player_disabled = True
        Header.player_playing = True
        Sound.header.update_player()