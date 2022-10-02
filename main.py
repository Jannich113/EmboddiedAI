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



    #-------------------------------------------------------------#
    # Super loop
    #-------------------------------------------------------------#
    while True:
        sensors.update(motors)  # update sensor values at start of each loop
        
        #-------------------------------------------------------------#
        # Behavior selection
        #-------------------------------------------------------------#


        #-------------------------------------------------------------#
        # Behavior execution
        #-------------------------------------------------------------#

        #-------------------------------------------------------------#
        # Sleep
        #-------------------------------------------------------------#
        #sleep(config.SLEEP_TIME)  # sleep for sepcified time in config.py

        #-------------------------------------------------------------#
        # End of loop
        #-------------------------------------------------------------#


if __name__ == "__main__":
    main()


#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#
