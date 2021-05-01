from termcolor import colored
from pyHM import mouse
import random
import time

error = colored("Error:", color="red")
warn = colored("Warning:", color="yellow")
info = colored("Info:", color="blue")

def mouse_move(x,y,w,h, click="", movSpeed = 1, debug=False):
    x,y = random.randint(x,x+w), random.randint(y,y+h)
    if debug: print(info, "Mouse moving to:", ', '.join([str(x), str(y)]))
    mouse.move(x,y, multiplier=movSpeed)
    if click!="":
        time.sleep(random.uniform(0.2, 0.4))
        if click.upper()=="RIGHT": mouse.right_click()
        elif click.upper()=="DOUBLE": mouse.double_click()
        elif click.upper()=="LEFT": mouse.click()
        else: print(error, "Unknown click action:", click)

def mouse_position():
    return [x for x in mouse.get_current_position()]

