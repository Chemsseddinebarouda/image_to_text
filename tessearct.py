
#!pip install pytesseract
from PIL import Image

import pytesseract

data = pytesseract.image_to_data(image,output_type=pytesseract.Output.DICT)


boxes = [] # to store boxes in a list 
text=[] # to store texts in a list 
for i in range(len(data['text'])):
    if data['text'][i].strip():
        text.append(data['text'][i])
        boxes.append((
            int(data['left'][i]),
            int(data['top'][i]),
            int(data['left'][i] + data['width'][i]),
            int(data['top'][i] + data['height'][i])
        ))
        
draw = ImageDraw.Draw(image, "RGBA")
font = ImageFont.load_default()
w,h=image.size
for box in boxes:
    draw.rectangle(box, outline='blue', width=1 )

image
