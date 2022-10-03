from ev3dev2.motor import MoveDifferential

import config

class DDrive:
    def __init__(self):
        self.mDiff = MoveDifferential(
            config.MOTOR_LEFT_PORT,
            config.MOTOR_RIGHT_PORT,
            config.TIRE,
            config.TIRE_DIST)
    
    