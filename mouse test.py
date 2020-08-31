debug = False
runonce = True
waitstart = False
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
        #print("new Screen saved")
        v = screen[500,500]
        if(v[0]!=255):
            h=False
        if(waitstart == False):
            h=False
    h=True
    positions = []
    valuen = 0
    #mouse.position = (1440,900)
    positions = np.where(screen == [249])
    listOfCoordinates = list(zip(positions[0], positions[1]))
    #print(listOfCoordinates)
    solutions = []
    for i in range(len(listOfCoordinates)):
        l = listOfCoordinates[i]
        p = screen[l[0],l[1]]
        if(p[0] == 249):
            if (p[1] == 220):
                #if (p[2] == 198):
                #if(p == [249,220,198,255]):
                #print(p)
                #screen[l[0], l[1]] = [0, 0, 0, 255]
                solutions.append(l)


    b = datetime.datetime.now()
    print(b-a)
    #for i in range(len(positions))
    if(debug):
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.waitKey(0)
