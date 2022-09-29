from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, ColorSensor, TouchSensor
from config import *

class Sensor:
    def __init__(self):
        self.sColorLeft  = ColorSensor(SENSOR_LIGHT_LEFT_PORT)
        self.sColorRight = ColorSensor(SENSOR_LIGHT_RIGHT_PORT)
        self.sUltrasound = UltrasonicSensor(SENSOR_ULTRASOUND_PORT)
        self.sTouch = TouchSensor(SENSOR_TOUCH_PORT)
        #self.sGyro = GyroSensor(SENSOR_GYRO_PORT)
    
    def initialize(self):
        self.sColorLeft.mode = MODE_COLOR
        self.sColorRight.mode = MODE_COLOR
        self.sUltrasound.mode = MODE_ULTRASOUND
        self.sTouch.mode = MODE_TOUCH
        #self.sGyro.mode = MODE_GYRO