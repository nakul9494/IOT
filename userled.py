import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = [26, 16, 25, 24, 23, 17, 27, 22] # GPIO Pin Numbers
for light in led:
    GPIO.setup(light, GPIO.OUT)

try:
    while True:
        user_input = int(input("Enter 1 to turn on all LEDs, or any other key to turn them off: "))
        if user_input == 1:
            print("Turning on all LEDs...")
            for light in led:
                GPIO.output(light, GPIO.HIGH)
        else:
            print("Turning off all LEDs...")
            for light in led:
                GPIO.output(light, GPIO.LOW)
except KeyboardInterrupt:
    pass
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
