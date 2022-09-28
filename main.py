#!/usr/bin/env python3
from time import sleep
import config as c
import motor


from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MediumMotor, SpeedValue
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

from ev3dev2.sensor.lego import TouchSensor, GyroSensor, LightSensor, UltrasonicSensor, ColorSensor 



#-------------------------------------------------------------#
# init I/O:
#-------------------------------------------------------------#
class io:
    mLeft = LargeMotor(OUTPUT_A)
    mRight = LargeMotor(OUTPUT_B)
    mCenter = LargeMotor(OUTPUT_C)
    #mGrip = MediumMotor(OUTPUT_D)

    us = UltrasonicSensor(INPUT_3)
    #gy = GyroSensor(INPUT_)
    #lsr = LightSensor(INPUT_1)
    #lsl = LightSensor(INPUT_4)
    #ts = TouchSensor(INPUT_3)


#-------------------------------------------------------------#
# define data-unit:
#-------------------------------------------------------------#

io.us.MODE_US_DIST_CM
#gy.MODE_GYRO_ANG
#lsl.MODE_REFLECT
#lsr.MODE_REFLECT
#ts.MODE_TOUCH

#-------------------------------------------------------------#
# Check and validate sensor connection: (VIRKER IKKE I ev3dev2)
#-------------------------------------------------------------#

#assert us.connected, "Ultrasound sensor is not connected"
#assert lsr.connected, "Lightsensor RIGHT is npt connected" 
#assert lsl.connected, "LIghtsensor LEFT is not connected"
#assert ts.connected, "Touchsensor is not connected"        
#assert mA.connected, "Motor A not connected"
#assert mB.connected, "Motor B not connected"
#assert gy.connected, "Gyrosensor is not connected"

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
    




#-------------------------------------------------------------#
# main program: Test program
#-------------------------------------------------------------#
#io.mLeft.reset()
#io.mRight.reset()

io.mCenter.reset()


#objectAvoidance(io.us.value,io.mCenter.degrees)

while True:
    io.mCenter.on_for_degrees(5,-45)
    val = io.us.value()
    print(f"-45 deg: {val}")
    io.mCenter.on_for_degrees(5,-30) # left
    print(f"-75 deg: {io.us.value()}")
    io.mCenter.on_for_degrees(5,75) # center
    print(f"0 deg: {io.us.value()}")
    io.mCenter.on_for_degrees(5,45) # right
    print(f"45 deg: {io.us.value()}")
    io.mCenter.on_for_degrees(5,30)
    print(f"75 deg: {io.us.value()}")
    io.mCenter.on_for_degrees(5,-75) # center
    print(f"0 deg: {io.us.value()}")
    #mGrip.run_forever(speed_sp=40)
    #io.mRight.run_forever(speed_sp=-c.BASE_SPEED)
    #io.mLeft.run_forever(speed_sp=-c.BASE_SPEED)
    #print(io.mLeft.degrees)
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

#-------------------------------------------------------------#
# END OF DOCUMENT 
#-------------------------------------------------------------#