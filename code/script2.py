from gpiozero import LED
from time import sleep
import paho.mqtt.client as mqtt
import sys

# set broker address to the right ip
broker_address = "192.168.178.56"
status_topic = "/home/OG/Arbeitszimmer/LEDtest/status"
health_topic = "/home/OG/Arbeitszimmer/LEDtest/health"
cmnd_topic = "/home/OG/Arbeitszimmer/LEDtest/cmnd"

# This has to stay globally - otherwise it won't work
led1 = LED(14)

# determine what happens when message gets send to a subscribed channel
def on_message (client, userdata, message):
    load = str(message.payload.decode("utf-8"))
    print("message", load, "in", message.topic)
    if (load == "ON"):
        switchLED1(True)
    elif (load == "OFF"):
        switchLED1(False)


def switchLED1(status):
    if status:
        client.publish(status_topic, "ON")
        led1.on()
    else: 
        client.publish(status_topic, "OFF")
        led1.off()


# new instance of the paho-mqtt client
client = mqtt.Client("pi1")
# connect to the previous specified broker
client.connect(broker_address)

# start a loop
## The loop() function is a built in function that will read the receive and send buffers, and process any messages it finds
## On the receive side it looks at the messages, and depending on the message type, it will trigger the appropriate callback function
## The loop function will read the buffer of the client and send any messages it finds to the respective functions
### Source: http://www.steves-internet-guide.com/loop-python-mqtt-client/
client.loop_start()

# subscribe to a topic
client.subscribe(cmnd_topic)
# set the function that gets triggered when a message is received
client.on_message = function = on_message

# publish a message with payload to a topic
client.publish(health_topic, "Ready Booted up")

# Initial power-up
switchLED1(True)

# Sets an infinite loop to wait for incoming messages
while True:
    try:
        sleep
    except KeyboardInterrupt:
        print('You pressed "Ctrl + C" - exiting')
        sys.exit()
