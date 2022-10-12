#!/usr/bin/env python3
from operator import truediv
from time import sleep

import config
import src.motor as motor
import src.sensor as sensor
import src.speaker as speaker
import src.dDrive as dDrive
import src.objectAvoidance as ObjAvoid
from ev3dev2.motor import SpeedRPM


#-------------------------------------------------------------#
# main program: 
#-------------------------------------------------------------#

def main():
    
    #-------------------------------------------------------------#
    # init I/O
    #-------------------------------------------------------------#
    motors = motor.Motor()  # init motors with custom motor class
    diffDrive = dDrive.DDrive() # init differential dirve
    sensors = sensor.Sensor()  # init sensors with custom sensor class
    sensors.initialize()  # initialize sensors with modes specified in config.py
    spkr = speaker.Speaker()  # init speaker with custom speaker class
    #spkr.play_boot()  # play boot sound
    objAvoid = ObjAvoid.objectDetection(motors)

    coun =1

    #-------------------------------------------------------------#
    # Super loop
    #-------------------------------------------------------------#
    #diffDrive.mDiff.on_arc_left(SpeedRPM(40),200,1256)
    
    
    while True:
        #sensors.update(motors)  # update sensor values at start of each loop

        #-------------------------------------------------------------#
        # Test of US
        #-------------------------------------------------------------#
        #objAvoid.detect(sensors)

        if coun == 1:
            objAvoid.detect(sensors)
            spkr.speak("done printing")
            objAvoid.turnSensor(64)

        coun = 2
       
        #-------------------------------------------------------------#
        # Test of gripper close
        #-------------------------------------------------------------#
        if (sensors.tVal == 1):
            #spkr.beep()
            motors.closeGripper()
            motors.openGripper()

        #-------------------------------------------------------------#
        # Behavior selection
        #-------------------------------------------------------------#
        

        #-------------------------------------------------------------#
        # Behavior execution
        #-------------------------------------------------------------#

        #-------------------------------------------------------------#
        # Sleep
        #-------------------------------------------------------------#
        sleep(config.SLEEP_TIME)  # sleep for sepcified time in config.py
        
        #-------------------------------------------------------------#
        # End of loop
        #-------------------------------------------------------------#


if __name__ == "__main__":
    main()


#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#
