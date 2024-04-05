import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = [26, 16, 25, 24, 23, 17, 27, 22]  # GPIO Pin Numbers
for light in led:
    GPIO.setup(light, GPIO.OUT)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    sum_num = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_num}. Lighting up {sum_num} LEDs...")
    
    for i in range(sum_num):
        print(f"LED {led[i % len(led)]} ON")
        GPIO.output(led[i % len(led)], GPIO.HIGH)
        time.sleep(0.5)
        print(f"LED {led[i % len(led)]} OFF")
        GPIO.output(led[i % len(led)], GPIO.LOW)
except KeyboardInterrupt:
    pass
finally:
    for light in led:
        GPIO.output(light, GPIO.LOW)

GPIO.cleanup()