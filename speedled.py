import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = [26, 16, 25, 24, 23, 17, 27, 22] # GPIO Pin Numbers
for light in led:
    GPIO.setup(light, GPIO.OUT)

try:
    speed = float(input("Enter the speed (in seconds) for glowing LED lights one by one: "))
    while True:
        for light in led:
            print(f"LED {light} ON")
            GPIO.output(light, GPIO.HIGH)
            time.sleep(speed)
            print(f"LED {light} OFF")
            GPIO.output(light, GPIO.LOW)
except KeyboardInterrupt:
    pass
finally:
    for light in led:
        GPIO.output(light, GPIO.LOW)
    GPIO.cleanup()
