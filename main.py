from infi.systray import SysTrayIcon #เป็นการนำเข้าmoduleเพื่อจะเอาไว้ทำTrayIconมุมล่างจอ
import keyboard #เป็นการนำเข้าmodule เพื่อใช้ keybrod เพื่อจะทำ hotkey
from src import speak,event #เป็นการนำเข้าโมดูลspeakกับevent speakคือโมดูลสำหรับพูด event คือโมดูลการทำงานเพื่อสร้างtrayIcon
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from threading import Thread

def show_splash():
    splash_root = tk.Tk()
    splash_root.overrideredirect(True)
    splash_root.geometry("400x300+500+250")
    
    img = Image.open("splash.png")  # ใส่รูป splash screen ที่ต้องการ
    img = img.resize((400, 300), Image.ANTIALIAS)
    splash_img = ImageTk.PhotoImage(img)
    
    label = tk.Label(splash_root, image=splash_img)
    label.pack()
    
    splash_root.after(3000, splash_root.destroy)  # แสดงเป็นเวลา 3 วินาที
    splash_root.mainloop()
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
def set_langcode_eng_japanese(systray):
    global _LANGCODE
    _LANGCODE = ["eng","ja"]
def set_langcode_eng_chinese(systray):
    global _LANGCODE
    _LANGCODE = ["eng","zh-cn"]
def set_langcode_eng_korean(systray):
    global _LANGCODE
    _LANGCODE = ["eng","ko"]
def set_langcode_eng_eng(systray):
    global _LANGCODE
    _LANGCODE = ["eng","en"]
def set_langcode_japanese_eng(systray):
    global _LANGCODE
    _LANGCODE = ["jpn","en"]
def set_langcode_korean_eng(systray):
    global _LANGCODE
    _LANGCODE = ["kor","en"]
def set_langcode_chinese_eng(systray):
    global _LANGCODE
    _LANGCODE = ["chi_sim", "en"]
    
def main_window():
    splash.destroy()
    start_tray()
    
def show_splash():
    global splash
    splash = tk.Tk()
    splash.title("Loading...")
    splash.geometry("300x200")
    splash.overrideredirect(True)
    
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width - 300) // 2
    y = (screen_height - 200) // 2
    splash.geometry(f"300x200+{x}+{y}")
    
    try:
        img = Image.open("loading.png")  # Replace with your image path
        img = img.resize((100,100),Image.LANCZOS)
        splash_img = ImageTk.PhotoImage(img)
        image_label = tk.Label(splash, image=splash_img)
        image_label.image = splash_img
        image_label.pack(pady=(10,0))
    except FileNotFoundError:
        print("Error: 'loading.png' not found.")
        label = tk.Label(splash, text="Image not found.", font=("Arial",12))
        label.pack(pady = (10,0))


    label = tk.Label(splash, text="ยินดีต้อนรับเข้าสู่โปรเเกรมเเปลภาษา v 1.0", font=("Arial", 12))
    label.pack(pady=(10,20))
  

    
    splash.after(3000, main_window)
    splash.mainloop()
def start_tray():
    menu_options = (("About", None, event.on_about),
                    ("How", None, event.on_how),
                    ('Language', "simon.ico", (
                        ('Eng-Thai', "simon.ico", set_langcode_eng_thai),
                        ('Thai-Eng', None, set_langcode_thai_eng),
                        ('Japanese-Thai', None, set_langcode_japanese_thai),
                        ('Thai-Japanese', None, set_langcode_thai_japanese),
                        ('Chinese-Thai', None, set_langcode_chinese_thai),
                        ('Thai-Chinese', None, set_langcode_thai_chinese),
                        ('Thai-Korean', None, set_langcode_thai_korean),
                        ('Korean-Thai', None, set_langcode_korean_thai),
                        ('Eng-Japanese', None, set_langcode_eng_japanese),
                        ('Eng-Chinese', None, set_langcode_eng_chinese),
                        ('Eng-Korean', None, set_langcode_eng_korean),
                        ('Eng-Eng', None, set_langcode_eng_eng),
                        ('Japanese-Eng', None, set_langcode_japanese_eng),
                        ('Korean-Eng', None, set_langcode_korean_eng),
                        ('Chinese-Eng', None, set_langcode_chinese_eng),
                    )))
    systray = SysTrayIcon("./language.ico", "En_Th_OCR", menu_options, on_quit=event.on_end)
    systray.start()
    try:
        speak.speak("เริ่มใช้โปรแกรมแปลภาษา", 'th')
    except:
        pass
    keyboard.add_hotkey('ctrl + shift + z', lambda: event.run(_LANGCODE))

if __name__ == "__main__":
    splash_thread = Thread(target=show_splash)
    splash_thread.start()

