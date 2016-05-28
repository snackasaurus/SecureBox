from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import RPi.GPIO as GPIO

import time
import atexit

class BoxController:
    SENSOR_OUT_PIN = 18
    SENSOR_IN_PIN = 22
    NUM_MOTOR_STEPS = 50
    ####################################################################################################################
    #                                       HOUSE KEEPING
    ####################################################################################################################
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
        self.log('Openeing box')
        while not self.all_the_way_open():
            self.motor_open_box()

        self.log('Box Open')

    def close_box(self):
        """
        This will manange the closing of the secure box
        :return:
        """
        self.log('Closing box')
        while not self.all_the_way_closed():
            self.motor_close_box()

        self.log('Box closed')

    ####################################################################################################################
    #                                       MOTOR METHODS
    ####################################################################################################################
    def motor_open_box(self):
        """
        Turns the motor forward self.NUM_MOTOR_STEPS
        :return:
        """
        self.log('Turning motor forwarn ' + str(self.NUM_MOTOR_STEPS) + ' steps')
        self.stepper.step(self.NUM_MOTOR_STEPS, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)


    def motor_close_box(self):
        """
        Turns the motor backward self.NUM_MOTOR_STEPS
        :return:
        """
        self.log('Turning motor forwarn ' + str(self.NUM_MOTOR_STEPS) + ' steps')
        self.stepper.step(self.NUM_MOTOR_STEPS, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)



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

    def log(self, message):
        print(message)

def turnOffMotors():
    mh = Adafruit_MotorHAT(addr=0x60)
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
