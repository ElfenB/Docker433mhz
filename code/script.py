from code.blink import switchLEDoff, switchLEDon, swithLEDoff
import paho.mqtt.client as mqtt
import time
import sys

# set broker address to the right ip
broker_address = "192.168.178.56"
topic1 = "/home/OG/Arbeitszimmer/LEDtest"

# determine what happens when message gets send to a subscribed channel
def on_message (client, userdata, message):
    load = str(message.payload.decode("utf-8"))
    print("message", load, "in", message.topic)
    if (load == "ON"):
        switchLEDon()
    elif (load == "OFF"):
        switchLEDoff()



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
client.subscribe(topic1)
# set the function that gets triggered when a message is received
client.on_message = function = on_message

# publish a message with payload to a topic
client.publish(topic1, "OFF")

# Sets an infinite loop that waits for incoming messages
while True:
    try:
        time.sleep
    except KeyboardInterrupt:
        print('You pressed "Ctrl + C" - exiting')
        sys.exit()

# time.sleep(4) # wait
# client.loop_stop() #stop the loop
