from ev3dev2.motor import MoveDifferential

import config

class DDrive:
    def __init__(self):
        self.mDiff = MoveDifferential(
            config.MOTOR_LEFT_PORT,
            config.MOTOR_RIGHT_PORT,
            config.TIRE,
            config.TIRE_DIST)

    # Move forward
    def moveForward(self):
        self.mDiff.on(config.MOVESPD, config.MOVESPD)
    
    # Turn a little left
    def turnLittleLeft(self):
        self.mDiff.turn_left(config.TURNLITTLESPD, config.TURNLITTLEANGLE)

    # Turn a little right
    def turnLittleRight(self):
        self.mDiff.turn_right(config.TURNLITTLESPD, config.TURNLITTLEANGLE)

    # Turn more left
    def turnMoreLeft(self):
        self.mDiff.turn_left(config.TURNMORESPD, config.TURNMOREANGLE)

    # Turn more right
    def turnMoreRight(self):
        self.mDiff.turn_right(config.TURNMORESPD, config.TURNMOREANGLE)
    
    # Move a bit forward
    def moveABitForward(self):
        self.mDiff.on_for_distance(config.MOVESLOWSPD, config.MOVESHORTDIST)

    # Stop
    def stop(self):
        self.mDiff.stop()