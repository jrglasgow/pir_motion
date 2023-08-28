# pir_motion
Motion detection for Raspberry Pi and PIR sensor

Modified code based on https://www.thedigitalpictureframe.com/pir-motion-sensor-raspberry-pi-digital-picture-frame/

Configure motionsensor.py by changing the pin numbers being used for the sensor(s)

copy motionsensor.service
```
sudo cp motionsensor.service /etc/systemd/system/
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
