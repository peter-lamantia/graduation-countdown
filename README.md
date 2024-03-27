# Graduation Countdown Display
A simple e-ink based countdown timer built with a Raspberry Pi Zero 2 W and the Adafruit 2.13" e-ink bonnet.

## Pre-requisites
To get up and running, there are a few prerequisites you need to install first.

1. Enable SPI
   - Enter `sudo raspi-config`
   - Go to Interface options -> SPI and enable it.
2. Install Adafruit EPD Library
   - `sudo pip3 install adafruit-circuitpython-epd`
3. Install DejaVu TTF Font and Pillow
   - `sudo apt-get install fonts-dejavu python3-pil`

## Setup
We want this display to update once an hour, and at boot.

1. Save the `main.py` file to a memorable place. I saved mine in `/opt/graduation_countdown/main.py`.
2. Edit the crontab with `crontab -e`. Add the following lines:
   - `@reboot /opt/graduation_countdown/main.py`
   - `@hourly /opt/graduation_countdown/main.py`

That's it! Assuming you've already snapped on the bonnet, you should be good to go!
