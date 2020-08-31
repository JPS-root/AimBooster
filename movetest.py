debug = False
runonce = False
from pynput.mouse import Button, Controller
import time
import numpy as np
import cv2
from PIL import ImageGrab
import datetime
mouse = Controller()
time.sleep(3)
z = True
while(z):
    if(runonce):
        z = False
    h = True
    while(h):
        a = datetime.datetime.now()
        screen = np.array(ImageGrab.grab(bbox=(0,0,2560,1600)))
        screen = cv2.resize(screen,(1024,640))
        print("new Screen saved")
        v = screen[500,500]
        if(v[0]!=255):
            h=False
    h=True
    positions = []
    valuen = 0
    #mouse.position = (1440,900)
    for x in range(0, 640):
        #print(x)
        for y in range(0, 1024):
            value = screen[x, y]

            #time.sleep(0.000001)
            #print(value)
            if (value[0] == 249):
                #print(value[0])
                if (value[1] == 220):
                    #if(value[2]==198):
                    print(value)
                    #print(x, y)
                    positions.append((int(x),int(y)))
                    screen[x, y] = [0, 0, 0, 255]

    print(positions)
    b = datetime.datetime.now()
    print(b-a)
    #for i in range(len(positions)):
    if(len(positions)!=0):
        for f in range(len(positions)):
            c = positions[f]
            value = screen[c[0],c[1]]
            #mouse.position = positions[0]
            #time.sleep(0.5)
            #print(screen[c[0],c[1]])
            #print(c[0],c[1])
            mouse.position = (c[1]*2.232*0.5625,c[0]*2.232*0.5625)
            mp = mouse.position
            mouse.click(Button.left, 1)
            #print(mouse.position)
            #print(mp[0]/2.23*1.77777777778,mp[1]/2.23*1.77777777778)
            screen[c[0], c[1]] = [255, 255, 255, 255]
    if(debug):
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.waitKey(0)
