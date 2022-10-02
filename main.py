#!/usr/bin/env python3
from ast import main
from operator import truediv
from time import sleep

import config
import src.motor as motor
import src.sensor as sensor
import src.speaker as speaker

#-------------------------------------------------------------#
# main program: 
#-------------------------------------------------------------#

def main():
    
    #-------------------------------------------------------------#
    # init I/O
    #-------------------------------------------------------------#
    motors = motor.Motor()  # init motors with custom motor class
    sensors = sensor.Sensor()  # init sensors with custom sensor class
    sensors.initialize()  # initialize sensors with modes specified in config.py
    spkr = speaker.Speaker()  # init speaker with custom speaker class
    spkr.play_boot()  # play boot sound


    while True:
        1+1 # do nothing
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


if __name__ == "__main__":
    main()


#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#
