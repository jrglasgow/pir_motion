# pir_motion
Motion detection for Raspberry Pi and PIR sensor

Modified code based on https://www.thedigitalpictureframe.com/pir-motion-sensor-raspberry-pi-digital-picture-frame/

# motionsensor.py
Configure motionsensor.py by changing the pin numbers being used for the sensor(s)

# gpiozero_motion_sensor.py
This is a script built using the [testpir.py script using the giozero library](https://www.thedigitalpictureframe.com/pir-motion-sensor-raspberry-pi-digital-picture-frame/#:~:text=sudo%20nano%20testpir.py) which allows for also setting the THRESHOLD (minimum movement level) and QUEUE_LEN (averaging across readings to even out motion detection) variables. Note that the `pins` array is a list of the GPIO pin numbers, not the board pin numbers.

# Setting up the service for automatic start

copy motionsensor.service
```
sudo cp motionsensor.service /etc/systemd/system/
```
Change the path of the ExecStart variable in motionsensor.service to the script you want to run.
```
sudo nano -e /etc/systemd/system/motionsensor.service
```
```
ExecStart=/usr/bin/python3 /home/pi/bin/pir_motion/motionsensor.py
ExecStart=/usr/bin/python3 /home/pi/bin/pir_motion/gpiozero_motion_sensor.py
```
Set permissions of motionsensor.service
```
sudo chmod 744 /etc/systemd/system/motionsensor.service
```
add the service
```
sudo systemctl daemon-reload
sudo systemctl enable motionsensor.service
```
