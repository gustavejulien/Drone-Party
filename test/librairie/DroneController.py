from .DroneLibrary import DroneLibrary
from time import sleep


class DroneController(DroneLibrary):

    def rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity, duration=0):
        self.tello.send_rc_control(left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity)
        if duration > 0:
            sleep(duration)
            self.tello.send_rc_control(0, 0, 0, 0)
        return ("ok")

    def flipForward(self):
        self.tello.flip_forward()
        return ("ok")

    def flipBack(self):
        self.tello.flip_back()
        return ("ok")

    def flipLeft(self):
        self.tello.flip_left()
        return ("ok")

    def flipRight(self):
        self.tello.flip_right()
        return ("ok")

    def flip(self, direction):
        flipDict = {
            'f': self.flipForward(),
            'forward': self.flipForward(),
            'front': self.flipForward(),
            'b': self.flipBack(),
            'backward': self.flipBack(),
            'back': self.flipBack(),
            'l': self.flipLeft(),
            'left': self.flipLeft(),
            'r': self.flipRight(),
            'right': self.flipRight(),
        }
        result = flipDict.get(direction)
        if(result is None):
            return 'ko'
        return 'ok'

    def getOppositeDirection(self, direction):
        oppositeDirectionDict = {
            'f': 'b',
            'forward': 'b',
            'front': 'b',
            'b': 'f',
            'backward': 'f',
            'back': 'f',
            'l': 'r',
            'left': 'r',
            'r': 'l',
            'right': 'l',
        }
        result = oppositeDirectionDict(direction)
        if(result is None):
            return 'ko'
        return result

    def getNextMoveClockWise(self, direction):
        nextMove = {
            'f': 'r',
            'forward': 'r',
            'front': 'r',
            'b': 'l',
            'backward': 'l',
            'back': 'l',
            'l': 'f',
            'left': 'f',
            'r': 'b',
            'right': 'b',
        }
        result = nextMove.get(direction)
        if(result is None):
            return 'ko'
        return result

    def getNextMoveCounterClockWise(self, direction):
        nextMove = {
            'f': 'l',
            'forward': 'l',
            'front': 'l',
            'b': 'r',
            'backward': 'r',
            'back': 'r',
            'l': 'b',
            'left': 'b',
            'r': 'f',
            'right': 'f',
        }
        result = nextMove.get(direction)
        if(result is None):
            return 'ko'
        return result

    def flipDanceClockwise(self, direction):
        secondDirection = self.getNextMoveClockWise(direction)
        if(secondDirection is None):
            return 'ko'
        thirdDirection = self.getNextMoveClockWise(secondDirection)
        fourthDirection = self.getNextMoveClockWise(thirdDirection)

        self.flip(direction)
        sleep(1)
        self.flip(secondDirection)
        sleep(1)
        self.flip(thirdDirection)
        sleep(1)
        self.flip(fourthDirection)
        return 'ok'

    def flipDanceCounterClockwise(self, direction):
        secondDirection = self.getNextMoveCounterClockWise(direction)
        if(secondDirection is None):
            return 'ko'
        thirdDirection = self.getNextMoveCounterClockWise(secondDirection)
        fourthDirection = self.getNextMoveCounterClockWise(thirdDirection)

        self.flip(direction)
        sleep(1)
        self.flip(secondDirection)
        sleep(1)
        self.flip(thirdDirection)
        sleep(1)
        self.flip(fourthDirection)
        return 'ok'

    def rotateClockwise(self, degrees=360):
        self.tello.rotate_clockwise(degrees)
        return ("ok")

    def rotateCounterClockwise(self, degrees=360):
        self.tello.rotate_counter_clockwise(degrees)
        return ("ok")

    def takePicture(self, filename="picture"):
        filename = filename + ".png"
        self.tello.streamon()
        frame_read = self.tello.get_frame_read()
#        cv2.imwrite(filename, frame_read.frame)
        self.tello.streamoff()
        return ("ok")

    def getFrameRead(self):
        # return a BackgroundFrameRead object
        return self.tello.get_frame_read()

    def getVideoCapture(self):
        # return a VideoCapture object. According to the documentation, "Users usually want to use get_frame_read instead".
        return self.tello. get_video_capture()
