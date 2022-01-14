import pytesseract
from googletrans import Translator
from src import image,speak
def ocr():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    img = image.image_cap()
    data = pytesseract.image_to_string(img)
    translator = Translator()
    data_text = translator.translate(data, dest='th')
    dd = data_text.text
    speak.speak(dd)