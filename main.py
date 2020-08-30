# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pynput.mouse import Button, Controller

from pynput.mouse import Button, Controller
import time
import numpy as np
import cv2
from PIL import ImageGrab
import datetime

xSize = 1000 #X-Resolution that will be processed
ySize = 2560 #Y-Resolution that will be processed

lastY = 150
lastX = 150

mouse = Controller()
time.sleep(4)


# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (502, 276)
nix = mouse.position
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
#mouse.move(5, -5)
#time.sleep(1)

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
mouse.click(Button.left, 1)

# Scroll two steps down
#mouse.scroll(0, 2)
#836/688 2040/1532 = 1204/844
isrun = True
while(isrun):
    a = datetime.datetime.now()
    #screen = np.array(ImageGrab.grab(bbox=(836,688,2040,1532)))
    screen = np.array(ImageGrab.grab(bbox=(0,0,2560,1600)))
    #screen[100, 100] = [255, 255, 255, 255]
    #screen = cv2.resize(screen,(ySize,xSize))
    #if(screen[150,150] != [255,255,255]):
    for x in range(0, xSize):
        for y in range(0, ySize):
            value = screen[x,y]
            #print(value)
            if(value[0]==255):
                if(value[1]==255):
                    #if(value[2]==255):
                    print(x, y)
                    lastX = x#+688
                    lastY = y#+836

                    #screen[x,y] = [0,0,0,255]
                    #calc = value[0]*65536+256*value[1]+value[2]
                    #HEX = hex(calc)
                    #print(HEX)
                    #if(HEX == "0xf9dcc6"):
    #else:
        #isrun = False
    #mouse.position =
    mouse.position = (lastX * 0.5625),(lastY*0.5625)
    #mouse.position = (100,100)
    #mouse.po
    print(lastY*0.5625)
    print(lastX*0.5625)
    f = mouse.position
    print(mouse.position[0]*1.777777777777777,mouse.position[1]*1.777777777777777)
    print("/////////////")
    #mouse.position = (836+113, 688+215)
    #mouse.position = (1280,800)
    b = datetime.datetime.now()
    print(b-a)
    isrun = False
#cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#cv2.waitKey(0)