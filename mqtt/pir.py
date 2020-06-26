import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 23

GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("PIR Module Test(CTRL + C to exit)")
    time.sleep(2)
    print("Ready")

    while True:
        if GPIO.input(PIR_PIN):
            t = time.localtime()

            t_hour = t.tm_hour
            t_min = t.tm_min
            t_sec = t.tm_sec

            print(" %d:%d:%d Motion Detected!" % (t_hour, t_min, t_sec))
        time.sleep(1)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()

