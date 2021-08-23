import sys
import os
import numpy as np

from interface_low.DroneController import DroneController
from interface_low.FacialRecognition import FacialRecognition
from config import PICTURE_PATH, HOST_API_SONG, PORT_API_SONG, BASE_URL_API_SONG

DEFAULT_MOVE_SIZE = 40

class Toutou:
    def __init__(self):
        self.__running = False
        self.DC = DroneController("dev")
        self.FR = FacialRecognition()
        pass

    def __move(self, actionId):
        if actionId == 0:
            # self.DC.forwardCm(DEFAULT_MOVE_SIZE * 2)
            self.DC.rotateClockwise(90)
            self.DC.forwardCm(DEFAULT_MOVE_SIZE * 4)
        elif actionId == 1:
            self.DC.rotateClockwise(90)
            self.DC.forwardCm(DEFAULT_MOVE_SIZE * 4)
            #self.DC.leftCm(int(DEFAULT_MOVE_SIZE*1.5))
        elif actionId == 2: 
            self.DC.rotateClockwise(90)
            self.DC.forwardCm(DEFAULT_MOVE_SIZE * 4)
            #self.DC.backwardCm(int(DEFAULT_MOVE_SIZE*1.5))
        elif actionId == 3:
            self.DC.rotateClockwise(90)
            self.DC.forwardCm(DEFAULT_MOVE_SIZE * 4)
#            self.DC.rightCm(int(DEFAULT_MOVE_SIZE*1.5))

    def start(self):
        try:
            os.makedirs(PICTURE_PATH)
        except :
            pass
        self.DC.takeOff()
        pass

    def destroy(self):
        pass

    def featuresloop(self):
        index = 0
        while self.__running == True:
            index += 1
            print(f'{index = }', file=sys.stderr)

    def activate(self):
        self.__running = True

    def desactivate(self):
        self.__running = False
