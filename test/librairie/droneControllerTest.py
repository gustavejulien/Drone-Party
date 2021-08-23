from . import DroneController
import inspect
from itertools import ifilter

class droneControllerTest:
    def test_getAllowedData(self):
        print('test_getAllowedData')
        drone = DroneController('test')
        r = drone.getAllowedData()
        assertion = ['acceleration_x',
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
        'xyz_speed_yaw_mid']
        try:
            assert r == assertion
            print('correct return')
        except AssertionError:
            print('wrong return')

    def test_allMethods(self):
        drone = DroneController('test')
        attrs = (getattr(drone, name) for name in dir(drone))
        methods = ifilter(inspect.ismethod, attrs)
        for method in methods:
            try:
                method()
            except TypeError:
                # Can't handle methods with required arguments.
                print(method)
                pass
