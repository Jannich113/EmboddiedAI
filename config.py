from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.wheel import EV3EducationSetTire
#-------------------------------------------------------------#
## configuration of parameter ##
#-------------------------------------------------------------#

#-------------------------------------------------------------#
# Input ports    
#-------------------------------------------------------------#
SENSOR_LIGHT_RIGHT_PORT = INPUT_1
SENSOR_LIGHT_LEFT_PORT = INPUT_2
SENSOR_ULTRASOUND_PORT = INPUT_3
SENSOR_TOUCH_PORT = INPUT_4
#SENSOR_GYRO_PORT = INPUT_x

#-------------------------------------------------------------#
# Output ports
#-------------------------------------------------------------#
MOTOR_LEFT_PORT = OUTPUT_A
MOTOR_RIGHT_PORT = OUTPUT_B
MOTOR_GRIPPER_PORT = OUTPUT_C
MOTOR_ULTRASOUND_PORT = OUTPUT_D

#-------------------------------------------------------------#
# Motor: 
#-------------------------------------------------------------#

THRESHOLD_LEFT = 30
THRESHOLD_RIGHT = 350
BASE_SPEED = 255
ZERO_SPEED = 0
TURN_SPEED = 50

#-------------------------------------------------------------#
# Ultrasonic sensor:
#-------------------------------------------------------------#
MODE_ULTRASOUND = 'US-DIST-CM'
DIST_IGNORE = 50
FRACTION = 10

#-------------------------------------------------------------#
# Color sensor:
#-------------------------------------------------------------#
MODE_COLOR = 'COL-REFLECT'
THRESHOLD_BLACK = 200

#-------------------------------------------------------------#
# Gyro sensor:
#-------------------------------------------------------------#
MODE_GYRO = 'GYRO-ANG'
THRESHOLD_UP = 20
THRESHOLD_DOWN = -20

#-------------------------------------------------------------#
# Touch sensor:
#-------------------------------------------------------------#
MODE_TOUCH = 'TOUCH'

#-------------------------------------------------------------#
# Wheels:
#-------------------------------------------------------------#
tire = EV3EducationSetTire()

#-------------------------------------------------------------#
# Main loop parameters:
#-------------------------------------------------------------#
SLEEP_TIME = 0.01 # in seconds


#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#

