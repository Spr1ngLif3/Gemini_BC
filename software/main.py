""" 
This code is the basic usage of Gemini BC with
data logging and second stage ignition.

The code use _thread module for implementing
basic multithreading for IO operations on file.

The workflow is basic:
- At startup the led turns on
- Wait 40 seconds for finishing rocket setup
- After that the board starts logging altitude and time
- In the meantime the code wait for lift-off
- At lift-off the board counts the time for the first stage
to finish burning
- A the end of this time send the ignition signal to the second stage
- Continue logging until turn off

**************
* ATTENTION! *
**************
Before load this script on the board and launching the rocket
double check it and all the variables! If u edit it, something
can go wrong!
I'm not responsible for every missuse of this code.

Made with <3 by Spr1ngLif3
"""
from machine import Pin, I2C, SPI
from bmp085 import BMP180
import sdcard, os, time
import _thread

# Setup the BMP180 sensor
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 40000)
print(i2c.scan())
bmp = BMP180(i2c)
bmp.oversample = 2
bmp.sealevel = 1013

# Constant for SD card module
SPI_BUS = 0
SCK_PIN = 2
MOSI_PIN = 3
MISO_PIN = 4
CS_PIN = 5
SD_MOUNT_PATH = '/sd'
FILE_PATH = "sd/log.txt"

# Init SPI communication for SD card
spi = SPI(SPI_BUS, sck=Pin(SCK_PIN), mosi=Pin(MOSI_PIN), miso=Pin(MISO_PIN))
cs_pin = Pin(CS_PIN)

# Other variables
start_altitude = 0
OCTOCOUPLER_PIN = 14
led_pin = Pin(25, Pin.OUT)

# Mounting SD card
try:
    sd = sdcard.SDCard(spi, cs_pin)
    os.mount(sd, SD_MOUNT_PATH)
    print(os.listdir(SD_MOUNT_PATH))
except Exception as e:
    print('An error occurred mounting the SD card: ', e)

def start_SD_thread() -> None:
    """Start a new thread for the SD printing when is possible
    """
    try:
        _thread.start_new_thread(SD_print, [])
    except OSError:
        pass

def SD_print() -> None:
    """Print a string in the file defined in the FILE_PATH constant

        Parameters:
            - string (str): the string to print
    """
    global led_pin
    global log_string
    try:
        with open(FILE_PATH, 'a') as file:
            file.write(log_string)
        _thread.exit()
    except Exception as e:
        print('An error occoured accessinf the file or printing on it', e)
        led_pin.off()
        _thread.exit()

def log_data(altitude: int, time: int) -> str:
    """Make the log string to print

        Parameters:
            - altitude (int): altitude value to include
            - time (int): time value to include (in ms)
    """
    result = "Time instant: " + str(time) + " | Altitude: " + str(altitude) + "\n"
    return result

def setup_altitudes() -> None:
    """Setup the start altitude and initialize the log file
    """
    global start_altitude
    global bmp
    altitudes = [abs(bmp.altitude) for i in range(10)]
    start_altitude = sum(altitudes)/10
    try:
        file = open(FILE_PATH, 'w')
        file.close()
        print("Setup succesfully!")
    except Exception as e:
        print('An error occoured during the initial setup')
        led_pin.off()

if __name__=='__main__':
    """Main function with the basic workflow
    """
    global log_string
    led_pin.on()
    time.sleep(40)
    setup_altitudes()
    motor_fire = Pin(OCTOCOUPLER_PIN, Pin.OUT)
    motor_fire.off()
    distacco = False
    time_start = time.ticks_ms()
    while True:
        altitude = abs(abs(bmp.altitude) - start_altitude)
        log_string = log_data(altitude, time.ticks_diff(time.ticks_ms(), time_start)) 
        start_SD_thread()
        print(log_string)

        if altitude >= 3.0 and not distacco:       
            time_start = time.ticks_ms()
            log_string = log_data(altitude, time.ticks_diff(time.ticks_ms(), time_start))
            while time.ticks_diff(time.ticks_ms(), time_start) < 4500:
                altitude = abs(abs(bmp.altitude) - start_altitude)
                log_string = log_data(altitude, time.ticks_diff(time.ticks_ms(), time_start)) 
                start_SD_thread()
                print(log_string)
                print("42")
            
            motor_fire.on()
            led_pin.off()
            distacco = True
