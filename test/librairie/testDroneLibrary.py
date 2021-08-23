import sys
from librairie.DroneController import DroneController

class testDroneLibrary:
    def __init__(self):
        pass

    def init_test(self):
        #self.DC = DroneController("test")
        self.DC = DroneController()

    def kill_test(self):
        self.make_the_drone_land()
        #ret = self.DC.destroy()

    def make_the_drone_take_off(self):
        ret = self.DC.takeOff()
        if (ret != "ok"):
            raise Exception("Fail")
    
    def make_the_drone_land(self):
        ret = self.DC.land()
        if (ret != "ok"):
            raise Exception("Fail")
    
    def make_the_drone_go_left(self):
        ret = self.DC.leftCm(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_right(self):
        ret = self.DC.rightCm(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_forward(self):
        ret = self.DC.forwardCm(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_backward(self):
        ret = self.DC.backwardCm(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_turn_right(self):
        ret = self.DC.rotateClockwise(90)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_turn_left(self):
        ret = self.DC.rotateCounterClockwise(90)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_left_sec(self):
        ret = self.DC.leftSec(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_right_sec(self):
        ret = self.DC.rightSec(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_forward_sec(self):
        ret = self.DC.forwardSec(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_go_backward_sec(self):
        ret = self.DC.backwardSec(25)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_take_pic(self):
        ret = self.DC.takePicture()
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_flip_Forward(self):
        ret = self.DC.flipForward(self)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_flip_backward(self):
        ret = self.DC.flipBack(self)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_flip_left(self):
        ret = self.DC.flipLeft(self)
        if (ret != "ok"):
            raise Exception("Fail")

    def make_the_drone_flip_right(self):
        ret = self.DC.flipRight()
        if (ret != "ok"):
            raise Exception("Fail")   