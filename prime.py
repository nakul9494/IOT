from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def draw_prime(draw, prime):
    if prime:
        draw.text((0, 0), "P", fill="white")

# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

# Take user input number
number = int(input("Enter a number: "))

# Check if the number is prime
prime = is_prime(number)

# Display the result on LED matrix
with canvas(device) as draw:
    draw_prime(draw, prime)

# Wait for 5 seconds
sleep(5)

# Clear the LED matrix
device.clear()
