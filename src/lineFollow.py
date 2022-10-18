from hashlib import new
from os import abort
import ev3dev2.button as button
from config import *
import src.dDrive as dDrive
import src.sensor as sensor
import src.stateMachine as stateMachine
import src.speaker as speaker
import sys

class LnFwl:
    def __init__(self, snsr: sensor.Sensor, dDr: dDrive.DDrive, spkr: speaker.Speaker):
        self.sm = stateMachine.StateMachine()   # state machine for line following
        self.dDrive = dDr                       # differential drive
        self.sensor = snsr                      # sensor object
        self.speaker = spkr                     # speaker object

    def start_transition(self):
        self.speaker.beep()
        #if(button.Button.any()):    # if any button is pressed
        if(True):
            newState = "FORWARD"
        else:
            newState = "START"
        return newState
    
    def forward_transition(self):
        # Both sensors see black
        if (self.sensor.lSeesBlack and self.sensor.rSeesBlack):
            newState = "STOP"
        
        # Right sensor sees black
        elif (self.sensor.rSeesBlack):
            newState = "TURN_RIGHT"

        # Left sensor sees black
        elif (self.sensor.lSeesBlack):
            newState = "TURN_LEFT"
        
        # Neither sensor sees black
        else:
            # Move forward
            self.dDrive.moveForward()
            newState = "FORWARD"
        
        return newState

    def turn_left_transition(self):
        # Both sensors see black
        if (self.sensor.lSeesBlack and self.sensor.rSeesBlack):
            newState = "TURN_MORE_LEFT"
        
        # Left sensor sees black
        elif (self.sensor.lSeesBlack):
            # Turn a little more right
            self.dDrive.turnLittleLeft()
            
            newState = "TURN_LEFT"
        
        # Right sensor sees black
        elif (self.sensor.rSeesBlack):
                        
            newState = "TURN_RIGHT"
        
        # Neither sensor sees 
        else:
            newState = "FORWARD"
        
        return newState

    def turn_right_transition(self):
        # Both sensors see black
        if (self.sensor.lSeesBlack and self.sensor.rSeesBlack):
            newState = "TURN_MORE_RIGHT"
        
        # Right sensor sees black
        elif(self.sensor.rSeesBlack):
            # Turn a little more left
            self.dDrive.turnLittleRight()

            newState = "TURN_RIGHT"

        # Left sensor sees black
        elif (self.sensor.lSeesBlack):
            newState = "TURN_LEFT"
        
        # Neither sensor sees 
        else:
            newState = "FORWARD"
        
        return newState
    
    def turn_more_left_transition(self):
        #Both sensors see black
        if (self.sensor.lSeesBlack and self.sensor.rSeesBlack):
            # Turn a little more left
            self.dDrive.turnMoreLeft()
            newState = "TURN_MORE_LEFT"
        
        # Right sensor sees black
        elif (self.sensor.rSeesBlack):
            self.dDrive.moveABitForward()
            newState = "TURN_MORE_LEFT"

        # Left sensor sees black
        elif (self.sensor.lSeesBlack):
            # Turn a little more left
            self.dDrive.turnMoreLeft()
            newState = "TURN_MORE_LEFT"
        
        # Neither sensor sees black
        else:
            newState = "FORWARD"
        
        return newState

    def turn_more_right_transition(self):
        #Both sensors see black
        if (self.sensor.lSeesBlack and self.sensor.rSeesBlack):
            # Turn a little more left
            self.dDrive.turnMoreRight()
            newState = "TURN_MORE_RIGHT"
        
        # Left sensor sees black
        elif (self.sensor.lSeesBlack):
            self.dDrive.moveABitForward()
            newState = "TURN_MORE_RIGHT"

        # RIGHT sensor sees black
        elif (self.sensor.lSeesBlack):
            # Turn a little more right
            self.dDrive.turnMoreRight()
            newState = "TURN_MORE_RIGHT"
        
        # Neither sensor sees black
        else:
            newState = "FORWARD"
        
        return newState

    def stop_transitions(self):
        newState = "STOP"
        self.dDrive.stop()
        while True:
            1+1
        return newState
    
    def initialize(self):
        self.sm.add_state("START", self.start_transition)
        self.sm.add_state("FORWARD", self.forward_transition)
        self.sm.add_state("TURN_LEFT", self.turn_left_transition)
        self.sm.add_state("TURN_RIGHT", self.turn_right_transition)
        self.sm.add_state("TURN_MORE_LEFT", self.turn_more_left_transition)
        self.sm.add_state("TURN_MORE_RIGHT", self.turn_more_right_transition)
        self.sm.add_state("STOP", None, end_state=1)
        self.sm.set_start("START")
        self.sm.run()

class LineFollow_Single:
    def __init__(self, snsr: sensor.Sensor, dDr: dDrive.DDrive, spkr: speaker.Speaker):
        self.sm = stateMachine.StateMachine()   # state machine for line following
        self.dDrive = dDr                       # differential drive
        self.sensor = snsr                      # sensor object
        self.speaker = spkr                     # speaker object
    
    def start(self):
        self.lnFwl.initialize()