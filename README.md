# Docker433mhz

This project will try to form a bridge between MQTT and cheap 433mhz Antennas for RaspberryPi and Arduino. 

My current setup exists of Docker Containers running Homebridge and Portainer on one Pi. The second Pi is running FHEM with Homebridge and a Script called "GenShellScript". So you can send commands via HomeKit (iPhone, ...) to Homebridge which gives the commands to FHEM which triggers the respective script and the right flags and codes (homecode and so on). 

This has worked fine for about 2-3 years now but I always wanted to have a better solution than this. Also the fact that the status is not updated in HomeKit correctly when something gets sent or controlled with another remote is a bit annoying. 

So, the new plan is to send commands from the Homebridge instance of the first Pi over MQTT to a Python script that then somehow sends the commands to the sender antenna. 