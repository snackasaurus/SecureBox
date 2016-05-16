from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperM$

import time
import atexit

class MotorController:
    def __init__(self):
        mh = Adafruit_MotorHAT(addr=0x60)
        self.stepper = mh.getStepper(200, 1)
        self.stepper.setSpeed(30)
    
    
    def motor_test(self):
        while (True):
            print("Single coil steps")
            self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
            self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
            print("Double coil steps")
            self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
            self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
            print("Interleaved coil steps")
            self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)
            self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
            print("Microsteps")
            self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
            self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)

def turnOffMotors():
    mh = Adafruit_MotorHAT(addr=0x60)
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)