import ctypes #นำเข้าmoduleเพื่อสร้างwindows text box
from . import speak,ocr #นำเข้าโมดูล speakเเละocrท
def on_end(systray):#เป็นการสร้างfunctionชื่อว่าon_endขึ้นมาเพื่อให้พูดว่าปิดโปรเเกรม
    try:
        speak.speak("ปิดprogram",'th')
    except:
        pass
    
def on_about(systray):#เป็นการสร้างfunctionชื่อว่าon_aboutขึ้นม่เพื่อสร้างtextboxที่ขึ้นว่าFor Ocr EN to TH
    ctypes.windll.user32.MessageBoxW(None, u"For Ocr EN to TH", u"About", 0)   
def on_how(systray):#เป็นการสร้างfunctionชื่อว่าon_howขึ้นม่เพื่อสร้างtextboxที่ขึ้นว่ากด prtscr โดยใช้โปรเเกรม Ligthshot เพื่อถ่ายหน้าจอในส่วนที่ต้องการเเปล\nจากนั้นกด 'ctrl + shift + z' เพื่อฟังเสียง
    ctypes.windll.user32.MessageBoxW(None, u"กด prtscr โดยใช้โปรเเกรม Ligthshot เพื่อถ่ายหน้าจอในส่วนที่ต้องการเเปล\nจากนั้นกด 'ctrl + shift + z' เพื่อฟังเสียง", u"วิธีการใช้งาน", 0)  
def run(lang):#เป็นการสร้างfunctionเพื่อการทำงานหลักของโปรเเกรม
    try: #เป็นการให้โปรเเกรมลองการทำงานocr.ocr()
        ocr.ocr(lang)
    except Exception as e :#เป็นการบอกโปรเเกรมว่าหากทำงานไม่สำเร็จให้พูดคำว่าผิดพลาดกรุณาลองใหม่ออกมา
        print (e)
        speak.speak("ผิดพลาดกรุณาลองใหม่",'th')
