# 🎙️ PyVA_PUDGE

**An offline-capable Russian voice assistant in Python that answers with Pudge's voice lines from Dota 2.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Hobby%20project-green)

## ✨ Features

- Voice commands in Russian
- Offline speech recognition with [Vosk](https://alphacephei.com/vosk/)
- Responses with Pudge voice lines from Dota 2
- [Add your main commands here, e.g. open websites, tell the time, launch apps]

Full command list: see [`commands.py`](commands.py).

## 🧰 Tech stack

| Library | Purpose |
|---|---|
| [Vosk](https://alphacephei.com/vosk/) | Local (offline) speech recognition |
| [SpeechRecognition](https://github.com/Uberi/speech_recognition) | Microphone input and recognition wrapper |
| [PyAudio](https://github.com/jleb/pyaudio) | Audio stream from the microphone |
| [playsound3](https://pypi.org/project/playsound3/) | Playing voice lines |

## 🚀 Installation

**1. Clone the repository**
```bash
git clone https://github.com/geenialniy/PyVA_PUDGE.git
cd PyVA_PUDGE
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install PyAudio SpeechRecognition vosk playsound
```

**3. Download a Vosk model**

Download a Russian model from the [Vosk models page](https://alphacephei.com/vosk/models) (e.g. `[model name]`), unzip it and place the folder in the project root as `[folder name]`.

**4. Find your microphone index**
```bash
python check.py
```
Copy the index of your microphone and paste it into `main.py`:
```python
with sr.Microphone(device_index=YOUR_INDEX) as mic:
```

## ▶️ Usage

```bash
python main.py
```
Say a command and wait for Pudge's reply. [Add a wake word or example phrase here.]

## 📁 Project structure

```
PyVA_PUDGE/
├── main.py          # Main assistant logic
├── check.py         # Helper: lists microphones and their indexes
├── commands.py      # Supported commands
├── tracks/          # Voice lines
├── requirements.txt # Dependencies
└── README.md
```

## ⚠️ Disclaimer

This is a non-commercial hobby project. Pudge and all related voice lines belong to Valve Corporation. The project is not affiliated with or endorsed by Valve.
