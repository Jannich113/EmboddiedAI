
from main import io
import config as c


#-------------------------------------------------------------#
# function: object avoidance
#-------------------------------------------------------------#

def drive_sharp_right():
    
    io.mRight.run_forever(speed_sp=55)
    io.mLeft.run_forever(speed_sp=255)

def drive_less_right():

    io.mRight.run_forever(speed_sp=200)
    io.mLeft.run_forever(speed_sp=255)

def drive_straight_back():

    io.mRight.run_forever(speed_sp=c.BASE_SPEED)
    io.mLeft.run_forever(speed_sp=c.BASE_SPEED)

def drive_less_left():

    io.mRight.run_forever(speed_sp=255)
    io.mLeft.run_forever(speed_sp=200)

def drive_sharp_left():

    io.mRight.run_forever(speed_sp=255)
    io.mLeft.run_forever(speed_sp=55)



def objectAvoidance(us_dist, mCenter_deg):

    if us_dist < c.DIST_IGNORE:
      
        if  mCenter_deg< c.FARRIGHT:
            drive_sharp_left()
            print('farright')
        elif (mCenter_deg >= c.LESSRIGHT[0]) & (mCenter_deg < c.LESSRIGHT[1]):
            drive_less_left()
            print('lessright')
        elif (mCenter_deg >= c.MIDDEL[0]) & (mCenter_deg < c.MIDDEL[1]):
            drive_straight_back()
            print('straight')
        elif (mCenter_deg >= c.LESSLEFT[0]) & (mCenter_deg < c.LESSLEFT[1]):
            drive_less_right
            print('lessleft')
        elif mCenter_deg > c.FARLEFT:
            drive_sharp_right()
            print('farleft')
    








