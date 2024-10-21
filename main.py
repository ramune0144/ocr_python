from infi.systray import SysTrayIcon #เป็นการนำเข้าmoduleเพื่อจะเอาไว้ทำTrayIconมุมล่างจอ
import keyboard #เป็นการนำเข้าmodule เพื่อใช้ keybrod เพื่อจะทำ hotkey
from src import speak,event #เป็นการนำเข้าโมดูลspeakกับevent speakคือโมดูลสำหรับพูด event คือโมดูลการทำงานเพื่อสร้างtrayIcon
#!!!!!!!!!!!!!!!!!! This is a debugger !!!!!!!!!!!!!!!!!!
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \|     |// '.
#                  / \|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====

_LANGCODE = ["eng", "th"]

def set_langcode_eng_thai(systray):
    global _LANGCODE
    _LANGCODE = ["eng", "th"]

def set_langcode_thai_eng(systray):
    global _LANGCODE
    _LANGCODE = ["tha", "en"]

def set_langcode_japanese_thai(systray):
    global _LANGCODE
    _LANGCODE = ["jpn", "th"]

def set_langcode_thai_japanese(systray):
    global _LANGCODE
    _LANGCODE = ["tha", "ja"]

def set_langcode_chinese_thai(systray):
    global _LANGCODE
    _LANGCODE = ["chi_sim", "th"]

def set_langcode_thai_chinese(systray):
    global _LANGCODE
    _LANGCODE = ["tha", "zh-cn"]
def set_langcode_thai_korean(systray):
    global _LANGCODE
    _LANGCODE = ["tha","ko"]
def set_langcode_korean_thai(systray):
    global _LANGCODE
    _LANGCODE = ["kor","th"]
if __name__ == "__main__": #เป็นการประกาศให้pythonรู้ว่าตรงนี้คือส่วนการทำงานหลัก
    menu_options = (("About", None,event.on_about),("How", None,event.on_how),('Language', "simon.ico", (
                                                ('Eng-Thai', "simon.ico", set_langcode_eng_thai),
                                                ('Thai-Eng', None, set_langcode_thai_eng),
                                                ('japanese-Thai', None, set_langcode_japanese_thai),
                                                ('Thai-japanese', None, set_langcode_thai_japanese),
                                                ('Chinese-Thai', None, set_langcode_chinese_thai),
                                                ('Thai-Chinese', None, set_langcode_thai_chinese),
                                                ('Thai-Korean', None, set_langcode_thai_korean),
                                                ('Korean-Thai', None, set_langcode_korean_thai),
                                              ))) #เป็นการสร้างเมนูชื่อ Aboutกับ HowของSysTray
    systray = SysTrayIcon("./language.ico", "En_Th_OCR", menu_options,on_quit= event.on_end,) #เป็นการสร้างSysTrayขึ้นมาชื่อEn_Th_OCRโดยตั้งiconด้วยรูป./language.ico
    systray.start()#เริ่มการทำงานของTrayIcon
    speak.speak("เริ่มใช้programเเปลภาษา",'th')#ทำให้ระบบพูดว่า"เริ่มใช้programเเปลภาษา"
    keyboard.add_hotkey('ctrl + shift + z',lambda: event.run(_LANGCODE))#เริ่มใช้hotkey ctrl + shift + z เพื่อทำงานevent.run
    
    
 
