import keyboard 
from src import speak,ocr
import sys
speak.speak("เริ่มใช้programเเปลภาษา")
def _end():
    speak.speak("ปิดprogram")
    sys.exit()
def run():
    try:
        ocr.ocr()
    except:
        speak.speak("ผิดพลาดกรุณาลองใหม่")

 
if __name__ == "__main__":
    keyboard.add_hotkey('ctrl + shift + z', run)
    keyboard.add_hotkey('ctrl + shift + e', _end)  
    keyboard.wait('ctrl + shift + e') 
