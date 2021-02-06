import time
from numpy import array_split
import soundcard as sc
from audio2numpy import open_audio
import pyaudio, ffmpeg, wave

if __name__ == '__main__':
    # GUI().run()

    p = pyaudio.PyAudio()
    # info = p.get_host_api_info_by_index(0)
    # numdevices = info.get('deviceCount')
    # # for each audio device, determine if is an input or an output and add it to the appropriate list and dictionary
    # for i in range(0, numdevices):
    #     if p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels') > 0:
    #         print("Output Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0,i).get('name'))

    # sp = sc.get_speaker('{0.0.0.00000000}.{7a17482b-40aa-497f-a8e2-f36a90a58861}')
    #
    # signal, sampling_rate = open_audio(r'C:\Users\Winblu\Desktop\ts sound\avemo capito non ce ne frega un cazzo cicciogamer89.mp3')
    #

    # devinfo = p.get_device_info_by_index(12)
    # print("\n\nSelected device is " + devinfo['name'])
    # if p.is_format_supported(48000.0,  # Sample rate
    #                          output_device=devinfo["index"],
    #                          output_channels=devinfo['maxOutputChannels'],
    #                          output_format=pyaudio.paInt16):
    #     print('Yay!')
    chunk = 1024
    
    wf = wave.open('audio.wav', 'rb')

    stream = p.open(format= p.get_format_from_width(wf.getsampwidth()),
           channels= wf.getnchannels(),
           rate = wf.getframerate(),
           output= True, output_device_index= 12)

    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()