from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import RPi.GPIO as GPIO

import time
import atexit

class BoxController:
    ####################################################################################################################
    #                                       HOUSE KEEPING
    ####################################################################################################################
    SENSOR_OUT_PIN = 11
    SENSOR_IN_PIN = 13
    def __init__(self):
        """
        setup the GPIO and motor hat for the Pi
        :return: BoxController
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.SENSOR_OUT_PIN, GPIO.OUT)
        GPIO.setup(self.SENSOR_IN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        mh = Adafruit_MotorHAT(addr=0x60)
        self.stepper = mh.getStepper(200, 1)
        self.stepper.setSpeed(1000)

    def tear_down(self):
        """
        Cleans up the external resources for the box controller
        :return:
        """
        turnOffMotors()
        atexit.register(turnOffMotors)
        GPIO.cleanup()


    ####################################################################################################################
    #                                       ACTION METHODS
    ####################################################################################################################
    def open_box(self):
        """
        This will manage the opening of the secure box
        :return:
        """
        while not self.all_the_way_open():
            self.motor_open_box()

    def close_box(self):
        """
        This will manange the closing of the secure box
        :return:
        """
        while not self.all_the_way_closed():
            self.motor_close_box()


    ####################################################################################################################
    #                                       MOTOR METHODS
    ####################################################################################################################
    def motor_open_box(self):
        """
        Turns the motor in the appropriate direction such that the lid to box retracts exposing the payload chamber
        :return:
        """
        #TODO
        print('open box')

    def motor_close_box(self):
        """
        Turns the motor in the appropriate direction such that the lid to the box will extend covering the payload
         chamber
        :return:
        """
        #TODO
        print('close box')

    def motor_test(self):
        """
        Test the motor
        :return:
        """
        while (True):
            print("Single coil steps")
            self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
            self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
            print("Double coil steps")
            self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
            self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
            #print("Interleaved coil steps")
            #self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)
            #self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
            #print("Microsteps")
            #self.stepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
            #self.stepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)


    ####################################################################################################################
    #                                       SENSOR METHODS
    ####################################################################################################################
    def all_the_way_open(self):
        """
        Check if the box is all the way open
        :return: boolean
        """
        return self.check_sensor_connection()

    def all_the_way_closed(self):
        """
        Check if the box is all the way closed
        :return:
        """
        return self.check_sensor_connection()

    def check_sensor_connection(self):
        """
        This will see if SENSOR_OUT_PIN is connected to SENSOR_IN_PIN. This means that the box is either all the way
        open or all the way closed.
        :return: boolean
        """
        GPIO.output(self.SENSOR_OUT_PIN, 1)
        sensor_value = GPIO.input(self.SENSOR_IN_PIN)
        GPIO.output(self.SENSOR_OUT_PIN, 0)
        return sensor_value is 1

def turnOffMotors():
    mh = Adafruit_MotorHAT(addr=0x60)
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
