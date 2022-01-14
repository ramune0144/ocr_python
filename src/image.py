import cv2
from PIL import ImageGrab

def image_cap():
    im = ImageGrab.grabclipboard()
    im.save('./data/1.png','PNG')
    part = "./data/1.png"
    img = cv2. imread(part,2)
    return img
def rgb_to_bin(img):
    ret, bw_img = cv2. threshold(img,200,255,cv2.THRESH_BINARY)
    return bw_img
