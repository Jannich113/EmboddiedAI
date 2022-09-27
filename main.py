#!/usr/bin/env python3
from time import sleep

import config
import motor

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

from ev3dev2.sensor.lego import TouchSensor, ButtonBase, GyroSensor, LightSensor, UltrasonicSensor, ColorSensor 



#-------------------------------------------------------------#
# init I/O:
#-------------------------------------------------------------#

mLeft = LargeMotor(OUTPUT_A)
mRight = LargeMotor(OUTPUT_B)
mCenter = LargeMotor(OUTPUT_C)
mGrip = MediumMotor(OUTPUT_D)

us = UltrasonicSensor(INPUT_1)
gy = GyroSensor(INPUT_2)
lsr = LightSensor(INPUT_3)
#lsl = LightSensor(INPUT_4)
ts = TouchSensor(INPUT_4)


#-------------------------------------------------------------#
# define data-unit:
#-------------------------------------------------------------#

us.MODE_US_DIST_CM
gy.MODE_GYRO_ANG
#lsl.MODE_REFLECT
lsr.MODE_REFLECT
ts.MODE_TOUCH

#-------------------------------------------------------------#
# Check and validate sensor connection: (VIRKER IKKE I ev3dev2)
#-------------------------------------------------------------#

#assert us.connected, "Ultrasound sensor is not connected"
#assert lsr.connected, "Lightsensor RIGHT is npt connected" 
#assert lsl.connected, "LIghtsensor LEFT is not connected"
#assert ts.connected, "Touchsensor is not connected"
#assert mA.connected, "Motor A not connected"
#assert mB.connected, "Motor B not connected"
#assert gy.connected, "Gyrosensor is not connected"

#-------------------------------------------------------------#
# main program: Test program
#-------------------------------------------------------------#
#-------------------------------------------------------------#

while True:


    #mB.run_forever(speed_sp=config.BASE_SPEED)
    #mA.run_forever(speed_sp=config.BASE_SPEED)
    
    #ts_val = ts.value()
    #ev3.Sound.speak('Running')
    #sleep(5)
    #ev3.Sound.speak('Stopping')
    #mA.stop()
    #sleep(5)
    #m2.duty_cycle_sp = config.BASE_SPEED
    

    #if ts_val == 1:
        #ev3.Sound.beep().wait()
        #mA.duty_cycle_sp = config.ZERO_SPEED
        #mB.duty_cycle_sp = config.ZERO_SPEED
        #exit()
    #else:
        #dis = us.value()/config.FRACTION
        #print(str(dis)) 
    #ang = gy.value()/config.FRACTION
    #print(ang)
    #refl = lsr.value()
    #print(refl)

#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#

