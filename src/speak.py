import imp
import re
from gtts import gTTS
from playsound import playsound
import os
def speak(dd):
    tts = gTTS(dd,lang='th')
    tts.save('./data/speech.mp3')
    playsound('./data/speech.mp3')
    os.remove('./data/speech.mp3')
    return 1