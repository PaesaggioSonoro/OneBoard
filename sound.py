import pyaudio

class Sound:
    p = pyaudio.PyAudio()

    def __init__(self):
        pass

    @staticmethod
    def getSpeakers() -> dict:
        result = {}
        info = Sound.p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range(0, numdevices):
            if Sound.p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels') > 0:
                result.update({i:Sound.p.get_device_info_by_host_api_device_index(0, i).get('name')})
        return result