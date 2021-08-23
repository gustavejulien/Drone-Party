from .MockTello import MockTello
from djitellopy import Tello


class DroneLibrary:

    def __init__(self, env = 'prod'):
        if(env == 'prod'):
            self.tello = Tello()
        else:
            self.tello = MockTello()
        self.tello.connect()

    def emergency(self):
        self.tello.emergency()

    def end(self):
        self.tello.end()

    def test(self):
        print('test')

    def takeOff(self):
        self.tello.takeoff()
        return "ok"

    def land(self):
        self.tello.land()
        return "ok"

    def move(self, direction, distance):
        moveDict = {
            'up': self.tello.move_up(distance),
            'down': self.tello.move_down(distance),
            'left': self.tello.move_left(distance),
            'right': self.tello.move_right(distance),
            'forward': self.tello.move_forward(distance),
            'back': self.tello.move_back(distance),
        }
        result = moveDict.get(direction)
        if(result is None):
            return 'ko'
        return 'ok'

    def getAllowedMoves(self):
        allowedMoves = ['up', 'down', 'left', 'right', 'forward', 'back']
        return allowedMoves

    def getData(self, data):
        allData = {
            'acceleration_x': self.tello.get_acceleration_x(),
            'acceleration_y': self.tello.get_acceleration_y(),
            'acceleration_z': self.tello.get_acceleration_z(),
            'barometer': self.tello.get_barometer(),
            'battery': self.tello.get_battery(),
            'current_state': self.tello.get_current_state(),
            'distance_tof': self.tello.get_distance_tof(),
            'flight_time': self.tello.get_flight_time(),
            'frame_read': self.tello.get_frame_read(),
            'height': self.tello.get_height(),
            'highest_temperature': self.tello.get_highest_temperature(),
            'lowest_temperature': self.tello.get_lowest_temperature(),
            'mission_pad_distance_x': self.tello.get_mission_pad_distance_x(),
            'mission_pad_distance_y': self.tello.get_mission_pad_distance_y(),
            'mission_pad_distance_z': self.tello.get_mission_pad_distance_z(),
            'mission_pad_id': self.tello.get_mission_pad_id(),
            'own_udp_object': self.tello.get_own_udp_object(),
            'pitch': self.tello.get_pitch(),
            'roll': self.tello.get_roll(),
            'speed_x': self.tello.get_speed_x(),
            'speed_y': self.tello.get_speed_y(),
            'speed_z': self.tello.get_speed_z(),
            'state_field': self.tello.get_state_field(),
            'temperature': self.tello.get_temperature(),
            'udp_video_address': self.tello.get_udp_video_address(),
            'video_capture': self.tello.get_video_capture(),
            'yaw': self.tello.get_yaw(),
            'xyz_speed': self.tello.get_xyz_speed(),
            'xyz_speed_mid': self.tello.get_xyz_speed_mid(),
            'xyz_speed_yaw_mid': self.tello.get_xyz_speed_yaw_mid()}
        if(data == 'all'):
            return allData
        result = allData.get(data)
        if(result is None):
            return 'Invalid data type, please use getAllowedData() to get the accepted data type.'
        return result

    def getAllowedData(self):
        allowedData = [
            'acceleration_x',
            'acceleration_y',
            'acceleration_z',
            'barometer',
            'battery',
            'current_state',
            'distance_tof',
            'flight_time',
            'frame_read',
            'height',
            'highest_temperature',
            'lowest_temperature',
            'mission_pad_distance_x',
            'mission_pad_distance_y',
            'mission_pad_distance_z',
            'mission_pad_id',
            'own_udp_object',
            'pitch',
            'roll',
            'speed_x',
            'speed_y',
            'speed_z',
            'state_field',
            'temperature',
            'udp_video_address',
            'video_capture',
            'yaw',
            'xyz_speed',
            'xyz_speed_mid',
            'xyz_speed_yaw_mid'
        ]
        return allowedData

    def forwardCm(self, value):
        self.tello.move_forward(value)
        return ("ok")

    def forwardSec(self, value):
        distance = value * self.tello.get_speed_x()
        self.tello.move_forward(distance)
        return ("ok")

    def backwardCm(self, value):
        self.tello.move_back(value)
        return ("ok")

    def backwardSec(self, value):
        distance = value * self.tello.get_speed_x()
        self.tello.move_back(distance)
        return ("ok")

    def leftCm(self, value):
        self.tello.move_left(value)
        return ("ok")

    def leftSec(self, value):
        distance = value * self.tello.get_speed_x()
        self.tello.move_left(distance)
        return ("ok")

    def rightCm(self, value):
        self.tello.move_right(value)
        return ("ok")

    def rightSec(self, value):
        distance = value * self.tello.get_speed_x()
        self.tello.move_right(distance)
        return ("ok")

    def upCm(self, value):
        self.tello.move_up(value)
        return ("ok")

    def upSec(self, value):
        distance = value * self.tello.get_speed_x()
        self.tello.move_up(distance)
        return ("ok")

    def downCm(self, value):
        self.tello.move_down(value)
        return ("ok")

    def downSec(self, value):
        distance = value * self.tello.get_speed_x()
        self.tello.move_down(distance)
        return ("ok")

    def setSpeed(self, value):
        if(value < 10 | value > 100):
            return ('ko, speed must me between 10 and 100.')
        self.tello.set_speed(value)
        return ("ok")
