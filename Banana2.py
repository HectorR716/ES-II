import math
from microbit import *

def anglex_radians(x, y, z):
    xrad = math.atan2(x,(math.sqrt((y**2)+(z**2))))
    return xrad

def angley_radians(x, y, z):
    yrad = math.atan2(y,(math.sqrt((x**2)+(z**2))))
    return yrad

def anglex_degree (xrad):
    xdeg = (xrad/math.pi)*180
    return xdeg

def angley_degree (yrad):
    ydeg = (yrad/math.pi)*180
    return ydeg

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    ax = anglex_degree(anglex_radians(x, y, z))
    ay = angley_degree(angley_radians(x, y, z))

    if -50 <= ay < -10 and -90 <= ax < -10:
        display.show(Image.ARROW_SE)
    elif -90 <= ay < -10 and 10 <= ax < 90:
        display.show(Image.ARROW_SW)
    elif -90 <= ay < 0 and  -10 < ax < 10:
        display.show(Image.ARROW_S)
    elif -10 < ay < 10 and -10 < ax < 10:
        display.show(Image.HAPPY)
    elif 10 <= ay <= 90 and -90 <= ax <= -10:
        display.show(Image.ARROW_NE)
    elif 10 <= ay <= 90 and 10 < ax <= 90:
        display.show(Image.ARROW_NW)
    elif 10 <= ay < 90 and -10 <= ax <= 10:
        display.show(Image.ARROW_N)
    elif -50 <= ax < -10 and -90 <= ay <= 0:
        display.show(Image.ARROW_E)
    elif 20 <= ax < 90 and -15<= ay <= 15:
        display.show(Image.ARROW_W)

    print((ax, ay))

    sleep(500)

#I worked with Zosia and Gillian