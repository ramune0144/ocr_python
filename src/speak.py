from gtts import gTTS #นำเข้าgTTSเพื่อนำมาใช้เป็นตัวกำเนิดตัวพูด
from playsound import playsound#นำเข้าplaysoundเพื่อเป็นตัวเล่นเสียง
import os#นำเข้าโมดูล os
def speak(dd,lange):#สร้างfunctionเพื่อเป็นตัวพูดจากstring
    tts = gTTS(dd,lang=lange)#กำหนดให้สร้างตัวพูดภาษาไทย
    tts.save('./data/speech.mp3')#เซฟไฟล์ที่ตัวพูดสร้างขึ้น
    playsound('./data/speech.mp3')#อ่านไฟล์ที่ตัวพูดสร้างขึ้น
    os.remove('./data/speech.mp3')#ลบไฟล์ที่อ่านเเล้วออก
    try:
        os.remove('./data/1.png')#ลบรูปที่เเปลเสร็จเเล้วออก
    except:
        pass #หากผิดพลาดให้ผ่านการทำงานไปเลย
    return 1 #ส่งกลับ1หากทำงานสำเร็จ
