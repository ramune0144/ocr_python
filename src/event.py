
import ctypes
from src import speak,ocr
def on_end(systray):
    speak.speak("ปิดprogram")
def on_about(systray):
    ctypes.windll.user32.MessageBoxW(None, u"For Ocr EN to TH", u"About", 0)   
def on_how(systray):
    ctypes.windll.user32.MessageBoxW(None, u"กด prtscr โดยใช้โปรเเกรม Ligthshot เพื่อถ่ายหน้าจอในส่วนที่ต้องการเเปล\nจากนั้นกด 'ctrl + shift + z' เพื่อฟังเสียง", u"วิธีการใช้งาน", 0)  
def run():
    try:
        ocr.ocr()
    except:
        speak.speak("ผิดพลาดกรุณาลองใหม่")