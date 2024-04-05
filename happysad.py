from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from time import sleep

# Define emojis
sad_smiley = [
    "00111100",
    "01000010",
    "10100101",
    "10000001",
    "10011001",
    "10100101",
    "01000010",
    "00111100"
    ]

happy_smiley = [
    "00111100",
    "01000010",
    "10100101",
    "10000001",
    "10000001",
    "10100101",
    "01000010",
    "00111100"
    ]

def draw_smiley(draw, emoji):
    for y in range(8):
        for x in range(8):
            if emoji[y][x] == "1":
                draw.point((x, y), fill="white")

# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

# Display the sad emoji
with canvas(device) as draw:
    draw_smiley(draw, sad_smiley)

# Wait for 2 seconds
sleep(2)

# Display the happy emoji
with canvas(device) as draw:
    draw_smiley(draw, happy_smiley)

# Wait for 2 seconds
sleep(2)

# Clear the LED matrix
device.clear()