import cv2#นำเข้าmoduleชื่อว่าcv2มาเพื่อใช้ในการประมาลผลภาพ
from PIL import ImageGrab#นำเข้าmoduleเพื่อการเก็บรูปจากการcoppy

def image_cap():#เป็นfunctionที่ประกาศไว้เพื่อใช้ในการดึงรูปจากclipboard
    im = ImageGrab.grabclipboard()
    im.save('./data/1.png','PNG') #เซฟรูปชื่อ./data/1.png
    part = "./data/1.png"
    img = cv2. imread(part,2)#อ่านรูป ./data/1.pngขึ้นมา
    return img #ส่งออกรูปออกไป
def rgb_to_bin(img):#functionเพื่อทำimage R G B ให้เป็น ภาพขาวดำ #####ไม่ได้ใช้เเล้วเพราะocrมีการทำงานด้านนีี้อยู่เเล้ว#########
    ret, bw_img = cv2. threshold(img,200,255,cv2.THRESH_BINARY)
    return bw_img
