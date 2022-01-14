from infi.systray import SysTrayIcon
import keyboard 
from src import speak,event



 
if __name__ == "__main__":
    menu_options = (("About", None,event.on_about),("How", None,event.on_how))
    systray = SysTrayIcon("./language.ico", "En_Th_OCR", menu_options,on_quit=event.on_end,)
    systray.start()
    speak.speak("เริ่มใช้programเเปลภาษา")
    keyboard.add_hotkey('ctrl + shift + z', event.run)
    
    
 
