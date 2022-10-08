# Code from https://python-course.eu/applications-python/finite-state-machine.php

class StateMachine:
    
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self.handler = None

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self):
        try:
            self.handler = self.handlers[self.startState]
        except:
            raise Exception("must call .set_start() before .run()")
        if not self.endStates:
            raise Exception("at least one state must be an end_state")
    
    def nextState(self):
        newState = self.handler()
        if newState.upper() in self.endStates:
            print("reached ", newState) 
        else:
            self.handler = self.handlers[newState.upper()]
