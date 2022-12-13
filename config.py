from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.wheel import EV3EducationSetTire
#-------------------------------------------------------------#
## configuration of parameter ##
#-------------------------------------------------------------#


#-------------------------------------------------------------#
# Lego specific parameters
#-------------------------------------------------------------#
STUD_MM = 8 #Distance between two lego studs

#-------------------------------------------------------------#
# Input ports    
#-------------------------------------------------------------#
SENSOR_LIGHT_LEFT_PORT = INPUT_1
SENSOR_LIGHT_RIGHT_PORT = INPUT_2
SENSOR_ULTRASOUND_PORT = INPUT_3
SENSOR_CAN_PORT = INPUT_4
#SENSOR_GYRO_PORT = INPUT_x

#-------------------------------------------------------------#
# Output ports
#-------------------------------------------------------------#
MOTOR_LEFT_PORT = OUTPUT_A
MOTOR_RIGHT_PORT = OUTPUT_B
MOTOR_ULTRASOUND_PORT = OUTPUT_C
MOTOR_GRIPPER_PORT = OUTPUT_D

#-------------------------------------------------------------#
# Motor / Diff drive: 
#-------------------------------------------------------------#
# negative value = forward drive
# positive value = backward drive
#-------------------------------------------------------------#

TURNLITTLESPD = SpeedPercent(10)    # speed for turning a little
TURNLITTLEANGLE = 15                # angle for turning a little
TURNMORESPD = SpeedPercent(10)      # speed for turning more
TURNMOREANGLE = 15                  # angle for turning more
MOVESPD = SpeedPercent(-30)          # speed for moving
MOVESLOWSPD = SpeedPercent(5)      # speed for moving slow
MOVESHORTDIST = 2                  # distance for moving a bit forward (mm)

#-------------------------------------------------------------#
# Ultrasonic sensor:
#-------------------------------------------------------------#
MODE_ULTRASOUND = 'US-DIST-CM'
DIST_IGNORE = 200
DIST_MAXED_OUT = 2550

MAX_DEGRESS = 65
DEGRESS_STEP = 1
TOLERATED_DIV = 10
NEEDED_POINTS = 6
TURN_SPEED_US = 40

#-------------------------------------------------------------#
# Color sensor:
#-------------------------------------------------------------#
MODE_COLOR = 'COL-REFLECT'
INTENSENTY_BLACK = 15

# USED FOR DETECTION OF CAN
RESCUE_INTENSETY = 15 


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
TIRE = EV3EducationSetTire
TIRE_DIST = 120 # Distance between center of the wheels in mm

#-------------------------------------------------------------#
# Gripper:
#-------------------------------------------------------------#
GRIPPER_ROTS = 6 # Number of rotations to open/close the gripper
GRIPPER_SPD_PERCENTAGE = 100 # Speed of the gripper motor in percentage

#-------------------------------------------------------------#
# RANSAC:
#-------------------------------------------------------------#

# the value choosen should consist with the SI unit of the Ultrasonic sensor
THRESHOLD_FOR_INLIERS = 20 # mm = 2 cm
MAX_ITERATIONS = 50 


#-------------------------------------------------------------#
# Orientation of robot:
#-------------------------------------------------------------#
ORIEN_COMPENSATION = 180 # degress


#-------------------------------------------------------------#
# Main loop parameters:
#-------------------------------------------------------------#
SLEEP_TIME = 0.01 # in seconds


#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#

