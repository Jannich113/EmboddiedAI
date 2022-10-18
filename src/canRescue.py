import config
import src.dDrive as dDrive
import src.objectAvoidance as objDet
import src.sensor as sensor
import src.motor as motor


class CanRescue():

    def __init__(self, ddr: dDrive.DDrive, objdet: objDet.objectDetection, snsr: sensor.Sensor, mt: motor.Motor):
        self.rescued_can = False            # boolean check for can grabbed 
        self.object = objdet                # objectDetection object
        self.drive = ddr                    # differential 
        self.sensor = snsr                  # ultrasound sensor object
        self.motor = mt                     # motor object


    def checkRescueStatus(self)-> bool:
        return self.rescued_can

    def updateRescueStatus(self)-> None:
        update = self.sensor.sColorCan.value()
        if update <= config.RESCUE_INTENSETY:
            self.rescued_can = True
        else:
            self.rescued_can = False


    def CompensateForOrientation(deg: int):
        return (config.ORIEN_COMPENSATION + deg)    


    def RescueOperation(self)-> bool:
        # update rescue status and check if rescued
        # could add functionality for after xx attempt abort rescue operation and return false
        self.updateRescueStatus()
        while True:

            if self.checkRescueStatus() == True:
                return True
            else:
                # scan for  objects and find middle of object
                self.object.detect(self.sensor.sUltrasound)
                self.object.findClosetsPoints()

                # use the fund point to angle the robot towards object 
                point = self.object.pt
                self.drive.MOVEANGLE = self.CompensateForOrientation(point[0])
                self.drive.turnForAngle()

                # use the fund point distance to drive the robot towards object
                self.drive.MOVEDIST = point[1]
                self.drive.moveForDist()

                # grab can 
                self.motor.closeGripper()

                # update rescue attempt 
                self.updateRescueStatus()
            
            # reset gripper if not rescued
            if self.checkRescueStatus() == False:
                self.motor.openGripper()
        
            
