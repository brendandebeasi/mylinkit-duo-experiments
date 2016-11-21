import mraa
import time
# Refer to the pin-out digram for the GPIO number to silk print mapping
# in this example the number 44 maps to Wi-Fi LED.
pin = mraa.Gpio(44)
pin.dir(mraa.DIR_OUT)
while True:
    pin.write(1)
    time.sleep(1)
    pin.write(0)
    time.sleep(1)
