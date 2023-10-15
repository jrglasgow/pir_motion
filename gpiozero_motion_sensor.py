#!/bin/env python

import time
import datetime
from gpiozero import MotionSensor
import subprocess

DARK_DELAY = 60 #this is where you define after how many seconds you want the display to go dark when there is no motion detected
THRESHOLD = .5
QUEUE_LEN = 10
AWAKE_RANGE = {
    "wake": 6, # wake time is 6am
    "sleep": 22, # sleeop time is 10pm
} # only awake the monitor between these hours
#pir1 = MotionSensor(17, threshold = THRESHOLD, queue_len = QUEUE_LEN) #GPIO number here
#pir2 = MotionSensor(4, threshold = THRESHOLD, queue_len = QUEUE_LEN) #GPIO number here
pins = [17, 4] # list the pins with PIR sensors here
pirs=[]
for pin in pins:
    pirs.append(MotionSensor(pin, threshold = THRESHOLD, queue_len = QUEUE_LEN))

def main():
    last_motion_time = time.time()
    monitor_on = False # assume the monitor is off
    while True:
        motion = False
        for pir in pirs:
            if pir.motion_detected:
                motion = True
                last_motion_time = time.time()
        if motion: # there is motion
            if not monitor_on and awake_time_frame():
                monitor_on = True
                turn_on()
                
        else: # we don't have motion
            if monitor_on and time.time() > (last_motion_time + DARK_DELAY):
                # turn the monitor off
                turn_off()
                monitor_on = False
                
        time.sleep(0.1)


# determine if the current time is in the time frame of the day when it should be awakened
def awake_time_frame():
    this_hour = datetime.datetime.now().hour
    if this_hour >= AWAKE_RANGE['wake'] and this_hour < AWAKE_RANGE['sleep']:
        #print('this_hour %s is between wake time of %s and sleep time of %s' % (this_hour, AWAKE_RANGE['wake'], AWAKE_RANGE['sleep']))
        return True
    return False

# turn the screen on
def turn_on():
    print("turn_on")
    print (datetime.datetime.now())
    CONTROL = "vcgencmd"
    CONTROL_UNBLANK = [CONTROL, "display_power", "1"]
    subprocess.call(CONTROL_UNBLANK)

# turn the screen off
def turn_off():
    print("turn_off")
    print (datetime.datetime.now())
    CONTROL = "vcgencmd"
    CONTROL_BLANK = [CONTROL, "display_power", "0"]
    subprocess.call(CONTROL_BLANK)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #io.cleanup()
        pass