import paho.mqtt.client as mqtt
import serial
import time

port="/dev/ttyACM0"
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()

def heart_rate():
    input_s = serialFromArduino.readline()
    input = int(input_s)
    if input < 21:
        print(str(input) +"초 경과")
    elif input > 20:
        print("심박수 : " + str(input))
        return input

mqtt = mqtt.Client()

while True:
    get_heart_rate = heart_rate()
    #15.164.213.137
    mqtt.connect("52.79.234.132", 1883)
    mqtt.publish("heart_rate", get_heart_rate)
    time.sleep(1)
