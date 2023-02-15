#!pip install keras_ocr


import matplotlib.pyplot as plt

import keras_ocr

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# Get a set of example image
img_pth = "1.png"
prediction_groups = pipeline.recognize(img_pth)

# Plot the predictions
prediction_groups

boxes=[]
words=[]

for group in prediction_groups[0]:
  #print(f'box = {group[1]} word = {group[0]}')
  
  tr=int(group[1][0][0])
  tl=int(group[1][0][1])
  br=int(group[1][2][0])
  bl=int(group[1][2][1])
  box=[tr,tl,br,bl]
  # get the boxes 
  boxes.append(box)
  #get the words 
  words.append(group[0])
  

from PIL import Image,ImageDraw,ImageFont
import numpy as np
import cv2

image = Image.open(img_pth)
draw = ImageDraw.Draw(image, "RGBA")
font = ImageFont.load_default()
w,h=image.size
# let's draw boxes and words in image 
for boxs,word in zip(boxes,words):
      print(word)
      draw.text((boxs[0] + 10, boxs[1] - 10),word, fill='red', font=font)
      draw.rectangle(boxs, outline="blue", width=2)
#display the image 
image
