#!/usr/bin/env python3
from time import sleep

import config, motor, sensor, speaker


from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

from ev3dev2.sensor.lego import TouchSensor, ButtonBase, GyroSensor, LightSensor, UltrasonicSensor, ColorSensor 




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
