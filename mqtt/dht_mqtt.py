import time
import Adafruit_DHT
import paho.mqtt.client as mqtt


def get_dht():
    sensor = Adafruit_DHT.DHT22
    pin = 18

    h, t = Adafruit_DHT.read_retry(sensor, pin)
    if h is not None and t is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
        temp = str(t)
        humi = str(h)
        print(temp, humi)
        temp = temp[0:4]
        humi = humi[0:4]
        result = temp + humi
        return result

    else:
        print('Failed to get reading.')


dht_result = get_dht()
mqtt = mqtt.Client()

while True:
    test = get_dht()
    mqtt.connect("52.79.234.132", 1883)
    mqtt.publish("dht", get_dht())
    time.sleep(0.5)
