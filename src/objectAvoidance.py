from copy import copy
from time import sleep
import config 
import src.sensor as sensor
import src.motor as motor
import csv
#import numpy as np


class objectDetection:
     
    def __init__(self, m: motor.Motor):
        self.mtr = m
        self.pt = 0
        self.objLIst = [None]*(2*config.MAX_DEGRESS)


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


    #def convertToCoordinat(degrees, dist):
        sol = [dist * np.cos(np.radians(degrees)), dist *np.sin(np.radians(degrees))]
        return sol

    def findClosetsPoints(self):
        pointList = copy(self.objLIst)
        Points_Fund = False

        # run until atleast a minimum of closets points are fund withing a STD from one another
        while not(Points_Fund):
            print('start')
            print(pointList)
            # add functionality to remove old estimate of corret point
            # for points in list find the closets point 
            point = [0, config.DIST_IGNORE]
            index_of_point = 0
            for p in pointList:
                if p[1] <= config.DIST_IGNORE:
                    if p[1] < point[1]:
                        point = p
                        index_of_point = pointList.index(p)
                        print('closets point')
                        print(point)

            # check left side for close pairs 
            leftList = []
            for p in pointList[:index_of_point]:
                if abs(p[1] - point[1]) <= config.TOLERATED_DIV:
                    leftList.append(p)
            
            # check right side for close pairs
            rightList = []
            for p in pointList[index_of_point:]:
                if abs(p[1] - point[1]) <= config.TOLERATED_DIV:
                    rightList.append(p)

            # Combine list of found pairs 
            c = []
            c.extend(leftList)
            c.append(point)
            c.extend(rightList)
            print('close pairs')
            print(c)

            if len(c) >= config.NEEDED_POINTS:
                Points_Fund = True
                middleIndex = int((len(c)-1)/2)
                self.pt = c[middleIndex]
            else:
                # remove noisy points thats not part of a line
                for noise in c:
                    pointList.remove(noise)


            


        

    
                







