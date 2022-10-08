from time import sleep
import config 
import src.sensor as sensor
import src.motor as motor



#-------------------------------------------------------------#
# function: object avoidance
#-------------------------------------------------------------#
class objectAvoidance:
     
    def __init__(self, m: motor.Motor):
        self.mtr = m


    def turnSensor(self, angle: int): 

        self.mtr.mUltrasonic.run_to_abs_pos(config.TURN_SPEED_US, angle)        
        self.mtr.mUltrasonic.wait_until_not_moving()


    def detect(self, us: sensor.Sensor):

        for turns in config.POSITIONS:
            self.turnSensor(turns)
            dist = us.sUltrasound.value()
            print(f"{turns} deg: {dist}")
            

    def Avoidance(self, us_dist, mCenter_deg):

    








