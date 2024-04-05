from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep

def draw_number(draw, num_leds):
    for y in range(8):
        for x in range(8):
            if num_leds > 0:
                draw.point((x, y), fill="white")
                num_leds -= 1

# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

# Take two numbers as input and calculate their sum
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_num = num1 + num2

# Calculate the number of LEDs to light up based on the sum
num_leds = min(sum_num, 64)  # Limit to 64 LEDs (8x8 matrix)

# Display the sum on the LED matrix
with canvas(device) as draw:
    draw_number(draw, num_leds)

# Wait for 45 seconds
sleep(45)

# Clear the LED matrix
device.clear()