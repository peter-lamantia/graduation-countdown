import time
import digitalio
import busio
import board
from adafruit_epd.ssd1675 import Adafruit_SSD1675
from adafruit_epd.ssd1680 import Adafruit_SSD1680
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from adafruit_epd.epd import Adafruit_EPD


def countdown(target_date):
    """
    Returns a string of the days and hours from a target date, separated by a newline character.
    """
    target_datetime = datetime.strptime(target_date, "%Y-%m-%d %H:%M:%S")
    current_datetime = datetime.now()
    time_difference = target_datetime - current_datetime

    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)

    return f"{days} days\n{hours} hours"


# setup pins for display
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)

# initialize display
display = Adafruit_SSD1680(
    122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=None, rst_pin=rst, busy_pin=busy,
)
display.rotation = 1

# set up fonts
small_font  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
large_font  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
mega_font   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# clear display
# display.fill(Adafruit_EPD.WHITE)
# display.display()
# time.sleep(2)

target_date = "2024-04-27 10:30:00"  # commencement date!

# update the display
image = Image.new("RGB", (250, 122), color=WHITE)
draw = ImageDraw.Draw(image)
draw.text((0, 0), "Time until graduation:", font=medium_font, fill=BLACK)
draw.multiline_text((0, 25), countdown(target_date), font=mega_font, fill=BLACK)
display.image(image)
display.display()
