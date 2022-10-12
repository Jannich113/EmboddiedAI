from time import sleep
import config 
import src.sensor as sensor
import src.motor as motor
import math
import csv
import numpy as np


class objectDetection:
     
    def __init__(self, m: motor.Motor):
        self.mtr = m
        self.posCount = 0
        self.objLIst = []


    def turnSensor(self, angle: int): 
        self.mtr.mUltrasonic.run_to_abs_pos(position_sp = angle, speed_sp = config.TURN_SPEED_US, stop_action = "hold")        
        self.mtr.mUltrasonic.wait_until_not_moving()


    def detect(self, us: sensor.Sensor):
        objects = []
        positions = range(-config.MAX_DEGRESS, config.MAX_DEGRESS, config.DEGRESS_STEP)
        for turns in positions:
            self.turnSensor(turns)
            dist_val = us.sUltrasound.value()

            if dist_val < config.DIST_MAXED_OUT:
                # RETURNS the degress and distance to object
                val = [turns, dist_val]
                objects.append(val)
        
        self.objLIst = objects
        print(objects)

        with open('datafile.csv','w',newline='') as datadump:
            wr = csv.writer(datadump)
            wr.writerow(objects)

        return objects


    def convertToCoordinat(degrees, dist):
        sol = [dist * np.cos(np.radians(degrees)), dist *np.sin(np.radians(degrees))]
        return sol


        

    
                







