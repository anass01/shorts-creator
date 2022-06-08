from PIL import ImageDraw
import textwrap

def wrap(caption, width):
    wrapper = textwrap.TextWrapper(width = width) 
    words = wrapper.wrap(text = caption) 
    caption = ""
    for text in words:
        caption += (text + '\n')
    return ''.join(caption[:-1]) # removes the last \n


def create(text, img, font):
    draw = ImageDraw.Draw(img)
    w,h = draw.textsize(text, font=font)
    W,H = img.size
    x,y = 0.5*(W-w),0.75*H-h
    draw.text((x,y), text, font = font, fill = "white", anchor='la')
    return img    