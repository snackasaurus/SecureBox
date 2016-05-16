from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

class MotorController:
    def __init__(self):
        mh = Adafruit_MotorHAT(addr=0x60)
        self.motor = mh.getMotor(1)
        self.motor.setSpeed(150)
    
    
    def motor_test(self):
        while (True):
            print "Forward! "
            self.motor.run(Adafruit_MotorHAT.FORWARD)
         
            print "\tSpeed up..."
            for i in range(255):
                self.motor.setSpeed(i)
                time.sleep(0.01)
         
            print "\tSlow down..."
            for i in reversed(range(255)):
                self.motor.setSpeed(i)
                time.sleep(0.01)
         
            print "Backward! "
            self.motor.run(Adafruit_MotorHAT.BACKWARD)
         
            print "\tSpeed up..."
            for i in range(255):
                self.motor.setSpeed(i)
                time.sleep(0.01)
         
            print "\tSlow down..."
            for i in reversed(range(255)):
                self.motor.setSpeed(i)
                time.sleep(0.01)
         
            print "Release"
            self.motor.run(Adafruit_MotorHAT.RELEASE)
            time.sleep(1.0)

def turnOffMotors():
    mh = Adafruit_MotorHAT(addr=0x60)
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)