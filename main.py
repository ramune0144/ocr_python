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
#                        `=---='

if __name__ == "__main__": #เป็นการประกาศให้pythonรู้ว่าตรงนี้คือส่วนการทำงานหลัก
    menu_options = (("About", None,event.on_about),("How", None,event.on_how)) #เป็นการสร้างเมนูชื่อ Aboutกับ HowของSysTray
    systray = SysTrayIcon("./language.ico", "En_Th_OCR", menu_options,on_quit=event.on_end,) #เป็นการสร้างSysTrayขึ้นมาชื่อEn_Th_OCRโดยตั้งiconด้วยรูป./language.ico
    systray.start()#เริ่มการทำงานของTrayIcon
    speak.speak("เริ่มใช้programเเปลภาษา")#ทำให้ระบบพูดว่า"เริ่มใช้programเเปลภาษา"
    keyboard.add_hotkey('ctrl + shift + z', event.run)#เริ่มใช้hotkey ctrl + shift + z เพื่อทำงานevent.run
    
    
 
