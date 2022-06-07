import copy

def overlay(background, foreground) :
    frames = []
    repeat = copy.deepcopy(background)
    for i in foreground:
        y, x, _ = i.shape
        break
    for j in background:
        h, w, _ = i.shape
    
    for f in foreground:
        try:
            frame = background.get_next_data()
        except:
            background = copy.deepcopy(repeat)
            frame = background.get_next_data()

        # adding foreground frame to center of background
        frame[(h-y)//2:-(h-y)//2, (w-x)//2:-(w-x)//2] = f
        # adding frame to list of frame
        frames.append(frame)
    return frames

    
    