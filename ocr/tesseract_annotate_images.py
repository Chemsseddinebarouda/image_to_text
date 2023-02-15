####instalallation#####
# !python3 -m pip install paddlepaddle
# !pip install "paddleocr>=2.0.1"
import glob
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import cv2
from paddleocr import PaddleOCR
img_pth="/content/1.png"
image = cv2.imread(img_pth)
ocr = PaddleOCR()
result = ocr.ocr(image)
image = Image.open(img_pth)
draw = ImageDraw.Draw(image, "RGBA")
font = ImageFont.load_default()
w,h=image.size
boxes=[]
for line in result[0]:
    
    bbox = line[0]
    tr=int(bbox[0][0])
    tl=int(bbox[0][1])
    br=int(bbox[2][0])
    bl=int(bbox[2][1])
    box=[tr,tl,br,bl]
    boxes.append(box)       
           
for boxs in boxes:
      draw.rectangle(boxs, outline="blue", width=2)
image
