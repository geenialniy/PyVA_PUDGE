import speech_recognition as sr
import playsound as play
import random
from os import system

"""
--- COMMANDS LIST
"""

start_commands = {
    "start_func": ["пудж", "путч", "porsche", "лучше", "луч", "пупс", "пульс", "падж"]
}
end_talking_commands = {
    "bye_func": ["пока", "бб", "до свидания"]
}
end_commands = {
    "end_func": ["заверши программу", "завершить программу"]
}
commands_dict = {
    "hi_func": ["привет", "здравствуй", "как дела"],
    "open_opera": ["открой браузер", "включи браузер", "запусти браузер", "открой оперу", "открой опера",
                   "включи опера", "запусти опера", "включи оперу", "запусти оперу"]
}

"""
--- TRACKS LIST
"""

start_tracks = [
    "Pud_spawn_06_ru.mp3",
    "Pud_spawn_08_ru.mp3"
]
hi_tracks = [
    "Pud_ability_devour_02_ru.mp3"
]
bye_tracks = [
    "Pud_death_01_ru.mp3",
    "Pud_death_02_ru.mp3",
    "Pud_death_03_ru.mp3",
    "Pud_death_04_ru.mp3",
    "Pud_death_06_ru.mp3"
]
confirm_tracks = [
    "Pud_move_15_ru.mp3",
    "Pud_move_03_ru.mp3",
    "Pud_move_04_ru.mp3",
    "Pud_move_05_ru.mp3",
    "Pud_move_06_ru.mp3",
    "Pud_move_09_ru.mp3",
    "Pud_move_10_ru.mp3",
    "Pud_move_13_ru.mp3",
    "Pud_move_16_ru.mp3",
    "Pud_move_17_ru.mp3"
]

"""
DEFINE SOME PARAMETERS
"""
r = sr.Recognizer()
r.pause_threshold = 0.5

"""
--- FUNCTIONS
"""


def recognize_func():
    """
    Simple recognize function based on google recognizer
    Parameter device_index is personal
    """
    with sr.Microphone(device_index=2) as mic:
        r.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = r.listen(source=mic, phrase_time_limit=2)
        try:
            query = r.recognize_google(audio_data=audio, language='ru-RU').lower()
            return query
        except sr.UnknownValueError:
            pass


def start_func():
    """
    Starting function that picks random start track and play it, will start dialogue
    """
    print("-- Слово-триггер распознано[start_func()]")
    random_start = f"tracks/{random.choice(start_tracks)}"
    play.playsound(random_start)
    return "-- Функция завершена[start_func()]\n"


def open_opera():
    """
    This function plays random confirm track and open Opera Gx browser
    """
    print("-- Слово-триггер распознано[open_dota()]")
    random_confirm = f"tracks/{random.choice(confirm_tracks)}"
    play.playsound(random_confirm)
    dota2 = r'"D:\opera\opera.exe"'
    system(dota2)


def hi_func():
    """
    Simple greeting function with random greeting track
    """
    print("-- Слово-триггер распознано[hi_func()]")
    random_hi = f"tracks/{random.choice(hi_tracks)}"
    play.playsound(random_hi)
    return "-- Функция завершена[hi_func()]\n"


def bye_func():
    """
    Bye function with random bye track, will close dialogue
    """
    print("-- Слово-триггер распознано[bye_func()]")
    random_bye = f"tracks/{random.choice(bye_tracks)}"
    play.playsound(random_bye)
    print("-- Разговор окончен")
    return "-- Функция завершена[bye_func()]\n"


def end_func():
    """
    playing Windows XP shutdown soundtrack and finish project
    """
    print("-- Слово-триггер распознано[end_func()]")
    play.playsound(f"tracks/windows-xp-shutdown.mp3")
    return "-- Успешное завершение"


def main():
    run2 = True
    play.playsound("tracks/01_now_loading.mp3")
    while run2:
        print("[Говори сейчас]")
        query = recognize_func()
        print(f"Распознанная строка: \"{query}\"")
        for k, v in start_commands.items():
            if query in v:
                print(globals()[k]())
                run1 = True
                while run1:
                    print("[Говори сейчас]")
                    query = recognize_func()
                    print(f"Распознанная строка: \"{query}\"")
                    for key, val in commands_dict.items():
                        if query in val:
                            print(globals()[key]())
                    for key, val in end_talking_commands.items():
                        if query in val:
                            print(globals()[key]())
                            run1 = False
        for k, v in end_commands.items():
            if query in v:
                print(globals()[k]())
                run2 = False


if __name__ == "__main__":
    main()
