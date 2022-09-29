from ev3dev2.motor import LargeMotor, MediumMotor

import config

class Motor:
    def __init__(self):
        self.mLeft = LargeMotor(config.MOTOR_LEFT_PORT)
        self.mRight = LargeMotor(config.MOTOR_RIGHT_PORT)
        self.mGripper = MediumMotor(config.MOTOR_GRIPPER_PORT)
        self.mUltrasonic = LargeMotor(config.MOTOR_ULTRASOUND_PORT)