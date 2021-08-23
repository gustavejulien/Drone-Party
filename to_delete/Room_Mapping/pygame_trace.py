from djitellopy import tello
import KeyboardModule as keyboard # Partie keyboard test pour implémenter un chemin grâce a pygame
import numpy as np

from time import sleep
import cv2
import math


fSpeed = 117 / 10  # Vitesse en cm/s  (15cm/s)
aSpeed = 360 / 10  # Vitesse en degrès/s (50d/s)
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval


x, y = 500, 500
a = 0
yaw = 0
keyboard.init()

myDrone = tello.Tello()
myDrone.connect()

print(myDrone.get_battery())
points = [(0,0), (0,0)]


# Partie test pour l'instant puisque la partie manuelle sera controlé par l'API
def getKeyboardInput():

    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global x, y, yaw, a
    d = 0

    if keyboard.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180

    elif keyboard.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if keyboard.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif keyboard.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if keyboard.getKey("w"):
        ud = speed

    elif keyboard.getKey("s"):
        ud = -speed

    if keyboard.getKey("a"):
        yv = -aspeed
        yaw -= aInterval

    elif keyboard.getKey("d"):
        yv = aspeed
        yaw += aInterval

    if keyboard.getKey("q"): myDrone.land(); sleep(3)
    if keyboard.getKey("e"): myDrone.takeoff()

    sleep(interval)
    a += yaw

    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))

    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):

    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)

    cv2.circle(img, points[-1], 8, (0, 255,0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500 )/ 100}, {(points[-1][1] - 500) / 100})m',

    (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)

while True:

    vals = getKeyboardInput()
    myDrone.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)

    if points[-1][0] != vals[4] or points[-1][1] != vals[5]:
        points.append((vals[4], vals[5]))

    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)