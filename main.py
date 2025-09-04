#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
rMotor = Motor(Port.C, positive_direction=Direction.CLOCKWISE) # left colour sensor is the front
lMotor = Motor(Port.D, positive_direction=Direction.CLOCKWISE) # right

armMotor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
rotateMotor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)

# Initialize the color sensor.
rSensor = ColorSensor(Port.S3)
lSensor = ColorSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(lMotor, rMotor, wheel_diameter=88.0, axle_track=187)

armMotor.reset_angle(0)
armMotor.run_target(10, -90, then=Stop.HOLD, wait=True)


DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 2.3

robot.settings(250, 100, 30, 10)
# robot.straight(150)


for i in range(100):
    # Calculate the deviation from the threshold.
    deviation = rSensor.reflection() - lSensor.reflection()

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)