from email.mime import image
import cv2 as v
from cv2 import destroyAllWindows
from cv2 import bilateralFilter
import numpy as np

def size(image,scale):
    (h,w)=image.shape[:2]
    new=int(scale/h*w)
    return v.resize(image,(new,scale))    #so we cant store it back to the var where the img is store vvvvvvvv imp
   



logo=size(v.imread("small.png",v.IMREAD_UNCHANGED),150)
(logo_h,logo_w)=logo.shape[:2]   #here [:] means splicing or accessing only till their 
pic=size(v.imread("pur.png",v.IMREAD_UNCHANGED),300)
(pic_h,pic_w)=pic.shape[:2]
 #here we add another layer called Alpha
pic=v.cvtColor(pic,v.COLOR_BGR2BGRA)
logo=v.cvtColor(logo,v.COLOR_BGR2BGRA)
print(pic.shape)
print(logo.shape)

# print(logo)
overlay=np.zeros((pic_h,pic_w,4),dtype="uint8")
overlay[0:logo_h,0:logo_w]=logo
# print(overlay)
print(pic.shape)


v.addWeighted(overlay,1,pic,0.7,1,pic)












while True:
    # v.imshow("ov",overlay)
    # v.imshow("logo",logo)   #should not have same name "inside this"
    v.imshow("pic",pic)
    if v.waitKey(0):
        break
 

    