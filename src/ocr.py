import pytesseract #นำเข้าโมดูล pytesseract
from googletrans import Translator#นำเข้าโมดูลTranslator
from src import image,speak#นำเข้าโมดูลimage,speak
def ocr():#สร้างfunctionเพื่อทำocr
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'#เป็นการชี้ไปที่ที่อยู่ของtesseractที่ติดตั้งเอาไว้
    img = image.image_cap()#เก็บรูปที่capมาได้
    data = pytesseract.image_to_string(img)#ให้ocrทำimage to stringเพื่อเปลี่ยนภาพเป็นตัวอักษรภาษาอังกฤษ
    translator = Translator()#เป็นการสร้างตัวเเปลภาษาขึ้นมา
    data_text = translator.translate(data, dest='th')#เป็นการเเปลภาษาจากstringที่ได้จากภาพให้เป็นภาษาไทย
    dd = data_text.text
    speak.speak(dd)#พูดคำที่เเปลได้
