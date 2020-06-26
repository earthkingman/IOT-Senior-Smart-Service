import paho.mqtt.client as mqtt
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz=1000000

def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

def fire():
    reading = analog_read(0)
    if reading < 100:
        print(str(reading))
        return reading

mqtt = mqtt.Client()
while True:
    fire_detect = fire()
    #15.164.213.137
    mqtt.connect("52.79.234.132", 1883)
    mqtt.publish("fire", fire_detect)
    time.sleep(0.5)