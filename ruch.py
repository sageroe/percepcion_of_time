import numpy as np
import math
import pandas as pd
#cm on flip

pos_x = [5]
pos_y = [-5]
speed = 10/60
def deg_to_rad(degrees = 0):
    angle = (math.pi/180)*degrees
    return angle

def move(angle):
    angle = deg_to_rad(angle)
    global speed  , pos_x, pos_y
    dx = speed *math.sin(angle)
    dy = speed *math.cos(angle)
    pos_x.append(pos_x[-1]+dx)
    pos_y.append(pos_y[-1]+dy)

#len in cm
def left():
    angle = deg_to_rad(180)
    global speed  , pos_x, pos_y
    dx = speed *math.cos(angle)
    dy = speed *math.sin(angle)
    pos_x.append(pos_x[-1]+dx)
    pos_y.append(pos_y[-1]+dy)


def right():
    angle = deg_to_rad(0)
    global speed  , pos_x, pos_y
    dx = speed *math.cos(angle)
    dy = speed *math.sin(angle)
    pos_x.append(pos_x[-1]+dx)
    pos_y.append(pos_y[-1]+dy)



def down():
    angle = deg_to_rad(270)
    global speed, pos_x, pos_y
    dx = speed *math.cos(angle)
    dy = speed *math.sin(angle)
    pos_x.append(pos_x[-1]+dx)
    pos_y.append(pos_y[-1]+dy)


def up():
    angle = deg_to_rad(90)
    global speed, pos_x, pos_y
    dx = speed *math.cos(angle)
    dy = speed *math.sin(angle)
    pos_x.append(pos_x[-1]+dx)
    pos_y.append(pos_y[-1]+dy)


for i in range(2*60):
    left()

for i in range(2*60):
    up()

for i in range(2*60):
    right()

for i in range(60):
    down()

for i in range(360):
    move(-i)
df = pd.DataFrame({"x":pos_x,"y":pos_y})
df.to_excel("how_to_move.xlsx")
