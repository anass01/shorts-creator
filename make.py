import glob
import sys
# To add path to python source files
sys.path.insert(0, "./src")

from gtts import gTTS
from animation import wrap, create
from PIL import Image, ImageFont
import imageio as iio
import ffmpeg
import os
import random
import numpy as np

f = open('text/dadjokes.txt', 'r')

# to choose a random background video
rnd = lambda : random.randint(0,len(glob.glob1("./backgrounds","*.mp4"))-1)
# setting the font
font = ImageFont.truetype("fonts/mangabey-font/MangabeyRegular-rgqVO.otf", size=80)

# to keep count of number of videos produced
count = 0
for line in f:
    count += 1

    # saving the audio
    obj = gTTS(text= line, lang = 'en', slow = False)
    obj.save('temp.mp3')
    del obj

    # finding the duration of audio that we got earlier
    duration = ffmpeg.probe('temp.mp3')['format']['duration']

    # wrapping the line
    text = wrap(line, 16)

    # initializing background
    background = iio.get_reader(f"backgrounds/{rnd()}.mp4")

    # initializing frames
    frames = []

    # finding the duration of autio to match with the video frames
    for i in range(len(text)):

        try:
            frame = background.get_next_data()
        except:
            background = iio.get_reader(f"backgrounds/{rnd()}.mp4")
            frame = background.get_next_data()
        h, w, _ = frame.shape
        img = Image.fromarray(np.zeros((h,w,4), dtype=np.uint8))
        # creating the frame that would be in the center
        mid = create(text[:i+1], img, font)

        PilFrame = Image.fromarray(frame)
        PilFrame.paste(mid,(0,0) ,mask=mid.convert("RGBA"))

        frame = np.array(PilFrame)
        frames.append(frame)
    
    # adding a little pause at the end
    frames += [frames[-1]]*10

    # saving the video
    iio.mimsave("temp.mp4", frames, fps = frames.__len__()/float(duration))

    # adding audio to the video
    video = ffmpeg.input('temp.mp4')
    audio = ffmpeg.input('temp.mp3')
    ffmpeg.concat(video, audio, v = 1, a = 1).output(f"output/{count}.mp4").run()

# removing the unecessary files
os.remove("temp.mp3")
os.remove("temp.mp4")




    

        




