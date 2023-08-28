#!/usr/bin/python3

import sys
import time
import datetime
import RPi.GPIO as io
import subprocess

io.setmode(io.BOARD)
DARK_DELAY = 10 #this is where you define after how many seconds you want the display to go dark when there is no motion detected
THRESHOLD = .5
PIR1_PIN=11 #if you connect to another pin, specify here
PIR2_PIN=7

def main():
    io.setup(PIR1_PIN, io.IN)
    io.setup(PIR2_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
    while True:
        #print("io.input(PIR1_PIN) = %s" % io.input(PIR1_PIN))
        #print("io.input(PIR2_PIN) = %s" % io.input(PIR2_PIN))
        if io.input(PIR1_PIN) or io.input(PIR2_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + DARK_DELAY):
                turned_off = True
                turn_off()
            if not turned_off and time.time() > (last_motion_time + 1):
                time.sleep(.1)
def turn_on():
    print("turn_on")
    print (datetime.datetime.now())
    CONTROL = "vcgencmd"
    CONTROL_UNBLANK = [CONTROL, "display_power", "1"]
    subprocess.call(CONTROL_UNBLANK)

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
        io.cleanup()
