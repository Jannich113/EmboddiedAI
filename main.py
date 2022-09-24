#!/usr/bin/env python3

from multiprocessing.connection import wait
import ev3dev.ev3 as ev3
from time import sleep

import config
import signal
# not necesseary if using ev3dev

    #from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank 
    #from ev3dev2.sensor import INPUT_1

    #from ev3dev2.sensor.lego import TouchSensor 
    #from ev3dev2.sensor.lego import UltrasonicSensor

#-------------------------------------------------------------#
# init I/O:
#-------------------------------------------------------------#


btn = ev3.Button()

mA = ev3.LargeMotor(ev3.OUTPUT_A)
mB = ev3.LargeMotor(ev3.OUTPUT_B)

us = ev3.UltrasonicSensor(ev3.INPUT_1)

lsr = ev3.LightSensor(ev3.INPUT_3)
lsl = ev3.LightSensor('int2')

ts = ev3.TouchSensor('int1')

gy = ev3.GyroSensor(ev3.INPUT_2)


#-------------------------------------------------------------#
# define SI-unit:
#-------------------------------------------------------------#

us.MODE_US_DIST_CM 

gy.MODE_GYRO_ANG

lsr.MODE_REFLECT

#-------------------------------------------------------------#
# Check and validate sensor connection:
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

    #mA.run_forever(speed_sp=config.BASE_SPEED) 
    #mB.duty_cycle_sp = config.BASE_SPEED
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
    refl = lsr.value()
    print(refl)

#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#

