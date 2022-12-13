from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, TouchSensor, LightSensor
from config import *
import src.motor as motor

class Sensor:
    def __init__(self):
        #self.sColorLeft  = ColorSensor(SENSOR_LIGHT_LEFT_PORT)
        #self.sColorRight = ColorSensor(SENSOR_LIGHT_RIGHT_PORT)
        self.sUltrasound = UltrasonicSensor(SENSOR_ULTRASOUND_PORT)
        self.sColorCan = LightSensor(SENSOR_CAN_PORT)
        #self.sTouch = TouchSensor(SENSOR_TOUCH_PORT)
        #self.sGyro = GyroSensor(SENSOR_GYRO_PORT)
        self.uDist = 0 # distance in cm from ultrasonic sensor
        self.uAngle = 0 # angle in degrees from ultrasonic sensor
        self.gripperAngle = 0 # angle in degrees from gripper motor
        self.lRefLeft = 0 # reflected light from left color sensor
        self.lRefRight = 0 # reflected light from right color sensor
        self.tVal = 0 # value from touch sensor, 0 when not pressed, 1 when pressed
        #self.gAng = 0 # angle from gyro sensor
        self.rSeesBlack = False # right sensor sees black
        self.lSeesBlack = False # left sensor sees black
    
    def initialize(self):
        #self.sColorLeft.mode = MODE_COLOR
        #self.sColorRight.mode = MODE_COLOR
        self.sColorCan.mode = 'REFLECT'
        self.sUltrasound.mode = MODE_ULTRASOUND
        #self.sTouch.mode = MODE_TOUCH
        #self.sGyro.mode = MODE_GYRO
    
    def update_all(self, mtr: motor.Motor):
        self.uDist = self.sUltrasound.value()      # distance in cm from ultrasonic sensor
        self.uAngle = mtr.mUltrasonic.position      # angle in degrees from ultrasonic sensor
        self.gripperAngle = mtr.mGripper.position   # angle in degrees from gripper motor
        self.lRefLeft = self.sColorLeft.value()     # reflected light from left color sensor
        self.lRefRight = self.sColorRight.value()   # reflected light from right color sensor
        self.tVal = self.sTouch.value()             # value from touch sensor, 0 when not pressed, 1 when pressed
        #self.gAng = self.sGyro.value()             # angle from gyro sensor
        
        # Determine if left sensors see black
        if (self.lRefLeft < INTENSENTY_BLACK):
            self.lSeesBlack = True
        else:
            self.lSeesBlack = False
        
        # Determine if right sensors see black
        if (self.lRefRight < INTENSENTY_BLACK):
            self.rSeesBlack = True
        else:
            self.rSeesBlack = False

    def update_Color(self):
        self.lRefLeft = self.sColorLeft.value()     # reflected light from left color sensor
        self.lRefRight = self.sColorRight.value()   # reflected light from right color sensor

        # Determine if left sensors see black
        if (self.lRefLeft < INTENSENTY_BLACK):
            self.lSeesBlack = True
        else:
            self.lSeesBlack = False
        
        # Determine if right sensors see black
        if (self.lRefRight < INTENSENTY_BLACK):
            self.rSeesBlack = True
        else:
            self.rSeesBlack = False