from pynput.mouse import Button, Controller
import time
mouse = Controller()
i = 0
x = 100#mouse.position[0]
y = 1600#mouse.position[1]
while(True):
    print(mouse.position[0]*1.7777777777778,mouse.position[1]*1.7777777777778)

