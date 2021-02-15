# OneBoard
When you're on discord or with your friends in some voice chat, you would like to make some noises and funny sounds. All current existing soundboards are ugly and only available on the computer, it's all virtual. But if you have arduino and some time to spend, why not making a **physical** soundboard?
## Usage
With OneBoard you can easily connect your physical, arduino soundboard.
Go on the [latest release page][latest] and download the installer and the sketchs.
Choose the preferred sketch and upload it to arduino. The sketch I used is based on capacitive sensors, inspired by musical [launchpads][launchpad]' touch buttons.

The soundboard have only 9 buttons, more coming soon...

<img src="https://i.imgur.com/S7R8UYK.png" width="600px"/>

It works also standalone without arduino. 
Select the playback device on the top dropdown menu. Right click on buttons to load audio file, then simply click and the audio will reproduce on the selected device.
To connect arduino select the serial port with the second dropdown menu on the top (may require a refresh) and then with the top right button connect to arduino.



# Create your own arduino sketch

The arduino sketch works based on a constant communication every 200 ms to keep the connection alive with an empty message, so to create your own sketch, download the [blank example][blank] and modify only the main file, keep untouched the *CheckAlive.cpp*, *packets.cpp* and *packets.h* .
Pay attention to call at every loop (or in compex cycles, every 1000 ms) the *check* method.
```c++
CheckAlive::check();
```

Implement your own way to call events (buttons, capacitive sensor, photoresistor...), and when you are ready to touch the button call the method *Packets::sendPacket("data")* with your data basing on the table below.

## Data codes

The serial communication between OneBoard software and the arduino is based on some predefined messages, to activate buttons and other actions. The code messages **must** be of 6 characters, or both arduino and OneBoard will throw an error.

### Press buttons
The standard code to press buttons is *btn* followed by the id of the button in the header.kv file located in "*sections/screens/*". The buttons ids are from *b00* to *b08*, where b00 is at the top left corner, *b02* at the top right and *b08* at the bottom right.
##### Examples:
Press button 2 (top center)
```c++
Packets::sendPacket("btnb01");
```
Press button 06 (center right)
```c++
Packets::sendPacket("btnb05");
```
### Toggle pause
You can implement code to pause and with the same button resume the playback.
```c++
Packets::sendPacket("pause0");
```
### Errors
Since arduino has no exceptions, when debugging, errors are useful and the program will print an error if you send code *err000*

[latest]: <https://github.com/PaesaggioSonoro/OneBoard/releases/latest>
[launchpad]: <https://www.google.com/search?q=launchpad&tbm=isch>
[blank]: <https://minhaskamal.github.io/DownGit/#/home?url=https:%2F%2Fgithub.com%2FPaesaggioSonoro%2FOneBoard%2Fblob%2Fmaster%2Fsketchs%2FOneBoard_blank.zip>

# Modify source code

If you want to add your custom functions or create a better code you have to clone the repository and install all the depencencies, and you will be ready to make your changes.
After cloning/downloading/forking the repository, you have to install the dependencies with
```
pip install -r requirements.txt
```
This will install all the dependencies except Pyaudio, that is difficoult to compile with pip. It's preferred to download the pre-built binaries from [this](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) site. I used the version amd64 for python 3.8 ([PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl](https://download.lfd.uci.edu/pythonlibs/w4tscw6k/PyAudio-0.2.11-cp38-cp38-win_amd64.whl)).

If you want to compile Pyaudio yourself, you need to install PortAudio and Visual Studio compiler (for more info read [this](https://stackoverflow.com/a/54396790/14918902)).
