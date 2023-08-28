#!/usr/bin/python

import time
import datetime
from gpiozero import MotionSensor

pir1 = MotionSensor(17) #GPIO number here
pir2 = MotionSensor(4) #GPIO number here

while True:
    pir1.wait_for_motion()
    pir2.wait_for_motion()
    if pir1.motion_detected or pir2.motion_detected:
        print("Somebody is moving")
        print (datetime.datetime.now())
        time.sleep(0.1)
