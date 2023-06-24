import speech_recognition as sr
import playsound as play
import os

"""
Will find all microphones and microphone index
"""
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

"""
Sound check
"""
play.playsound('tracks/Pud_spawn_06_ru.mp3')

"""
Opening file check
"""
os.system('"C:/Windows/System32/notepad.exe"')
