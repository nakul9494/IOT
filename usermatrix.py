from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep

def draw_led(draw, x, y):
    draw.point((x, y), fill="white")

# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

# Prompt user for x and y coordinates
x = int(input("Enter x coordinate (0-7): "))
y = int(input("Enter y coordinate (0-7): "))

# Display the specified LED
with canvas(device) as draw:
    draw_led(draw, x, y)

# Wait for 5 seconds
sleep(5)

# Clear the LED matrix
device.clear()
