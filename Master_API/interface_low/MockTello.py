from PIL import Image


class MockTello:

    def __init__(self):
        print('Mock object initiated')

    def connect(self):
        return 'ok'

    def end(self):
        return 'ok'
    
    def emergency(self):
        return 'ok'

    def connect_to_wifi(self):
        return 'ok'

    def takeoff(self):
        return 'ok'

    def land(self):
        return 'ok'

    def send_rc_control(self, *args):
        return 'ok'

    def move_up(self, distance):
        return 'ok'

    def move_down(self, distance):
        return 'ok'

    def move_left(self, distance):
        return 'ok'

    def move_right(self, distance):
        return 'ok'

    def move_forward(self, distance):
        return 'ok'

    def move_back(self, distance):
        return 'ok'

    def flip_forward(self):
        return 'ok'

    def flip_back(self):
        return 'ok'

    def flip_left(self):
        return 'ok'

    def flip_right(self):
        return 'ok'

    def rotate_clockwise(self, degrees):
        return 'ok'

    def rotate_counter_clockwise(self, degrees):
        return 'ok'

    def streamon(self):
        return 'ok'

    def streamoff(self):
        return 'ok'

    def get_frame_read(self):
        img = Image.new("RGB", (800, 1280), (255, 255, 255))
        return img

    def get_video_capture(self):
        return 'ok'

    def get_acceleration_x(self):
        return 'ok'

    def get_acceleration_y(self):
        return 'ok'

    def get_acceleration_z(self):
        return 'ok'

    def get_barometer(self):
        return 'ok'

    def get_battery(self):
        return 'ok'

    def get_current_state(self):
        return 'ok'

    def get_distance_tof(self):
        return 'ok'

    def get_flight_time(self):
        return 'ok'

    def get_height(self):
        return 'ok'

    def get_highest_temperature(self):
        return 'ok'

    def get_lowest_temperature(self):
        return 'ok'

    def get_mission_pad_distance_x(self):
        return 'ok'

    def get_mission_pad_distance_y(self):
        return 'ok'

    def get_mission_pad_distance_z(self):
        return 'ok'

    def get_mission_pad_id(self):
        return 'ok'

    def get_own_udp_object(self):
        return 'ok'

    def get_pitch(self):
        return 'ok'

    def get_roll(self):
        return 'ok'

    def get_speed_x(self):
        return 'ok'

    def get_speed_y(self):
        return 'ok'

    def get_speed_z(self):
        return 'ok'

    def get_state_field(self):
        return 'ok'

    def get_temperature(self):
        return 'ok'

    def get_udp_video_address(self):
        return 'ok'

    def get_yaw(self):
        return 'ok'

    def get_xyz_speed(self):
        return 'ok'

    def get_xyz_speed_mid(self):
        return 'ok'

    def get_xyz_speed_yaw_mid(self):
        return 'ok'

    def set_speed(self, value):
        return 'ok'

    def stop(self):
        return 'ok'
