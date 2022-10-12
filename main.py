#!/usr/bin/env python3
from operator import truediv
from time import sleep

import config
import src.motor as motor
import src.sensor as sensor
import src.speaker as speaker
import src.dDrive as dDrive
import src.lineFollow as lineFollow
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
    #spkr.speaker.play_file('dtmf.wav')
    #spkr.speaker.play_file('crabRave.wav')
    spkr.beep()
    linFol = lineFollow.LnFwl(sensors, diffDrive, spkr) # init line following with sensor and differential drive objects
    linFol.initialize() # initialize line following


    #-------------------------------------------------------------#
    # Super loop
    #-------------------------------------------------------------#
    
    
    while True:
        sensors.update(motors)  # update sensor values at start of each loop

        #-------------------------------------------------------------#
        # Test of gripper close
        #-------------------------------------------------------------#
        if (sensors.tVal == 1):
            spkr.beep()
            motors.closeGripper()
            motors.openGripper()

        #-------------------------------------------------------------#
        # Behavior selection
        #-------------------------------------------------------------#
        

        #-------------------------------------------------------------#
        # Behavior execution
        #-------------------------------------------------------------#
        linFol.sm.nextState() # update state machine


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
