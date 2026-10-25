import speech_recognition as sr
from vosk import Model, KaldiRecognizer, SetLogLevel
import playsound3 as play
import random
import json
import pyaudio
from os import system
import commands as c


SetLogLevel(-1)  # убрать лишние логи

WAKE_WORDS = c.wake_words
MIC_INDEX = 1


model = Model("vosk-model-small-ru-0.22")
r = sr.Recognizer()
r.pause_threshold = 0.5


def start():
    """
    Запуск программы с крутым звуком из бравл старса
    """
    print("-- Слово-триггер распознано[start()]")
    random_start = f"tracks/{random.choice(c.start_tracks)}"
    play.playsound(random_start)
    return "-- Функция завершена[start()]\n"


def open_browser():
    """
    Запуск браузера
    """
    print("-- Слово-триггер распознано[open_browser()]")
    random_confirm = f"tracks/{random.choice(c.confirm_tracks)}"
    play.playsound(random_confirm)
    browser = r'"D:\opera\opera.exe"'
    system(browser)
    return "-- Функция завершена[open_browser()]\n"


def hi():
    """
    Приветствие
    """
    print("-- Слово-триггер распознано[hi_func()]")
    random_hi = f"tracks/{random.choice(c.hi_tracks)}"
    play.playsound(random_hi)
    return "-- Функция завершена[hi_func()]\n"


def bye():
    """
    Заканчивает разговор с ассистентом
    """
    print("-- Слово-триггер распознано[bye_func()]")
    random_bye = f"tracks/{random.choice(c.bye_tracks)}"
    play.playsound(random_bye)
    print("-- Разговор окончен")
    return "-- Функция завершена[bye_func()]\n"


def end():
    """
    играет звук выключения Windows XP и завершает программу
    """
    print("-- Слово-триггер распознано[end_func()]")
    play.playsound(f"tracks/windows-xp-shutdown.mp3")
    return "-- Успешное завершение"


def wait_for_wake_word():
    """
    Слушает микрофон постоянно и офлайн, возвращается, когда услышал триггер.
    """
    grammar = json.dumps(WAKE_WORDS + ["[unk]"], ensure_ascii=False)
    rec = KaldiRecognizer(model, 16000, grammar)

    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=16000,
                     input=True, input_device_index=MIC_INDEX,
                     frames_per_buffer=4000)
    try:
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result()).get("text", "")
                if any(w in text.split() for w in WAKE_WORDS):
                    return
    finally:
        # обязательно закрываем, иначе sr.Microphone не сможет открыть то же устройство
        stream.stop_stream()
        stream.close()
        pa.terminate()


def listen_command():
    """
    Одна команда через Google, после того как ассистент проснулся.
    """
    with sr.Microphone(device_index=MIC_INDEX) as mic:
        r.adjust_for_ambient_noise(mic, duration=0.3)
        try:
            audio = r.listen(mic, timeout=5, phrase_time_limit=5)
            return r.recognize_google(audio, language="ru-RU").lower()
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return None


def main():
    play.playsound("tracks/01_now_loading.mp3")
    while True:
        wait_for_wake_word()          # спим, пока не услышим триггер
        print(start())           # играем приветственный трек

        while True:                   # режим диалога
            query = listen_command()
            print(f"Распознано: {query!r}")
            if query is None:
                continue
            if query in c.end_command:
                print(end())
                return
            if query in c.end_talking_command:
                print(bye())
                break                 # назад к ожиданию триггера
            for func_name, phrases in c.commands_dict.items():
                if query in phrases:
                    print(globals()[func_name]())


if __name__ == "__main__":
    main()
