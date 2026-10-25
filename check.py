import playsound3 as play
import os
import pyaudio
import speech_recognition as sr

"""
Will find all microphones and microphone index
"""


def fix(name):
    try:
        return name.encode("cp1251").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return name


p = pyaudio.PyAudio()

host_api_index = None
for i in range(p.get_host_api_count()):
    info = p.get_host_api_info_by_index(i)
    if info["name"] == "MME":
        host_api_index = i
        break

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if dev["hostApi"] == host_api_index and dev["maxInputChannels"] > 0:
        print(f"{i}: {fix(dev['name'])}")

p.terminate()

"""
Sound check
"""
play.playsound('tracks/Pud_spawn_06_ru.mp3')

"""
Opening file check
"""
os.system('"C:/Windows/System32/notepad.exe"')

print(sr.__version__)
print(sr.__file__)
print(hasattr(sr.Recognizer(), "recognize_google"))
